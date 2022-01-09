import threading

from modules import Alarm, clear, time_formatter
from simple_term_menu import TerminalMenu


if __name__ == '__main__':
    
    alarm = Alarm()
    
    alarm_thread = threading.Thread(target=alarm)
    alarm_thread.daemon = True
    alarm_thread.start()
    
    options = ["Adicionar Alarme", "Finalizar Programa"]

    while 1:
        clear()
        print('\n\n')
        
        # Set alarm display flag to True.
        alarm.dflag = 1
        
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            alarm.dflag = 0
            while 1:
                try:
                    name = input("Nome do alarme: ")
                    time_value = input("Hora [H:M:S]: ")
                    description = input("Descrição (opcional): ")
                    alarm.add({'tag': name, 'time': time_formatter(time_value), 'description': description})
                except ValueError as err:
                    continue
                else:
                    break
        else:
            clear()
            break