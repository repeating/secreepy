import psutil
import os
from datetime import datetime


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    def __init__(self, debug=0):
        self.debug = debug

    def log(self, *argv, end='\n', error=False, debug=False):
        if debug and not self.debug:
            return
        process = psutil.Process(os.getpid())
        memory = str(process.memory_info().rss // 1024 // 1024) + ' MB'
        now = datetime.now().replace(microsecond=0)
        print(f'{Bcolors.BOLD}{Bcolors.OKBLUE}{memory} {Bcolors.OKGREEN}{now}:{Bcolors.ENDC}', end=' ')
        if error:
            print(f'{Bcolors.BOLD}{Bcolors.FAIL}WARNING:{Bcolors.ENDC}', end=' ')
            for arg in argv:
                print(f'{Bcolors.BOLD}{Bcolors.FAIL}{arg}{Bcolors.ENDC}', end=' ')
        else:
            for arg in argv:
                print(arg, end=' ')
        print('', end=end)
