# from et.et import ET

from et import ET

executiontime = ET("Calculate radians")

import math
input1 = 1234567
y = math.radians(input1)
print(f'\n The input = {input1}, output = {y}')

executiontime.stop()


#######################################################

from et import ETM

with ETM() as em:
    import math
    input1 = 1234567
    y = math.radians(input1)
    print(f'\n The input = {input1}, output = {y}')