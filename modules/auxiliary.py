from sys import stdout
from os import system, get_terminal_size, name as os_name


def clear():
    system('cls' if os_name == 'nt' else 'clear')


def time_formatter(tm):
    tm = str(tm).replace(':','')
    
    if len(tm) != 6 or not tm.isdigit():
        raise ValueError("Incorrect format for time. (H:M:S)")
    
    tm = [tm[i:i+2] for i in range(0, len(tm), 2)]
    return f'{str(int(tm[0]) % 24).zfill(2)}:{str(int(tm[1]) % 60).zfill(2)}:{str(int(tm[2]) % 60).zfill(2)}'