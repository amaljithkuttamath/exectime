import time
from datetime import datetime as dt
class ET():
    '''
    args:
    info = String [Information about the lines you are testing]
    
    method:
    stop() - marks the end of program time to be calculated
    '''
    def __init__(self, info=None):
        self.__start1 =time.time_ns()
        self.__start2 = dt.now()
        self.__info = info
    def stop(self):
        self.__stop1 = time.time_ns()
        self.__stop2 = dt.now()
        __dtx = self.__stop2 - self.__start2
        __dtz = self.__stop1 - self.__start1
        return print(f" {self.__info}  | The execution time = {__dtx}S  | {__dtz} NS" )

# execution_time = ET("info")
# ET("self").stop()