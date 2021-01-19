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
        return print(f"\n\033[1;35m{self.__info}  | The execution time = \033[0m{__dtx}S  | {__dtz} NS" )
    
class ETM(object):
    """ ETM used with the statement 'with' to time some execution.
    Example:

    with ETM() as etm:
       # Code to time
    """
    def __enter__(self):
        """
        """
        self.start = dt.now()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        """
        self.endlog()
        return False

    def log(self, s, elapsed=None):
        """Log current time and elapsed time if present.
        :param s: Text to display, use '{}' to format the text with
            the current time.
        :param elapsed: Elapsed time to display. Dafault: None, no display.
        """
        # print(s.format(self._secondsToStr(self.clock())))
        print(s.format(dt.now()))
        if(elapsed is not None):
            print('\033[1;35m[Elapsed time]:\033[0m  {} Sec'.format(elapsed))

    def endlog(self):
        """Log time for the end of execution with elapsed time.
        """
        self.log(f'\n\033[1;33m[Started]:\033[0m {self.start}') 
        self.log('\033[1;33m[End]:\033[0m {} Sec', self.now())
        
        
    def now(self):
        """Return current elapsed time as hh:mm:ss string.
        :return: String.
        """
        self.seconds = dt.now() - self.start
        return self.seconds