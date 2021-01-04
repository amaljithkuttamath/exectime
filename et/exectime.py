import time
from datetime import datetime as dt
class ET():
    def __init__(self, info=None):
        self.start1 =time.time_ns()
        self.start2 = dt.now()
        self.info = info
    def stop(self):
        self.stop1 = time.time_ns()
        self.stop2 = dt.now()
        dtx = self.stop2 - self.start2
        dtz = self.stop1 - self.start1
        return print(f" {self.info}  | The execution time = {dtx}ms  | {dtz} NS" )