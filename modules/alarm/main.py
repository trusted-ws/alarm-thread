import sys

from datetime import datetime
from gtts import gTTS
from playsound import playsound
from time import sleep

sys.path.insert(0, "../../audios")


class Alarm:    
    def __init__(self, *args, **kwargs):
        self.alarms = []
        self.alarms_beeped = 0
        self.dflag = True  # Display flag.
        self.__current_alarm_text = ""

    def __call__(self, *args, **kwargs):
        self.__main(args, kwargs)
    
    def add(self, obj: dict):
        self.alarms.append(obj)
    
    def show_status(self):
        if not self.dflag:
            return
        
        sys.stdout.write(f"\033[2F Alarmes ativos: {len(self.alarms)} | Alarmes tocados: {self.alarms_beeped}  {self.__current_alarm_text}\n\033[E")
        
        if len(self.__current_alarm_text) > 0:
            self.__current_alarm_text = ""
        
        sys.stdout.flush()
            
    def __start_alarm(self, details: dict):
        self.__current_alarm_text = f"[Alarme disparado: {details['tag']}]"
        self.alarms_beeped += 1
        self.show_status()
        
        if details['description']:
            audio = gTTS(details['description'], lang='pt-br')
            audio_name = "".join([str(hex(ord(x))).replace('0x', '') for x in details['tag']])
            audio_path = 'audios/' + audio_name + '.mp3'
            audio.save(audio_path)
            playsound(audio_path)        
        
    def __main(self, *args, **kwargs):

        while 1:
            sleep(1)

            for i, entry in enumerate(self.alarms):
                entry_dt = datetime.strptime(entry['time'], "%H:%M:%S")
                now_dt = datetime.now()
                
                if (entry_dt.hour, entry_dt.minute, entry_dt.second) == (now_dt.hour, entry_dt.minute, now_dt.second):
                    self.__start_alarm(entry)
                    self.alarms.pop(i)
                    
            if self.dflag:
                self.show_status()
