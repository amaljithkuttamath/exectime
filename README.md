# Install

```
pip install etime
```

Usage:-

# Execution Time

## check_time

#### timeit wrapper

```python
from et import check_time

@check_time(number=10000, debug = True)
def multiply(x=1000, y=0.828348):
    return x*y

print("Value: ",multiply())
```
### Output:
```
--------------------------------------------------------------------------
[ multiply -> 10000 iterations] [Elapsed time]: 0.003009455000000001 Sec
--------------------------------------------------------------------------

Value: 828.348
 ```

## ET
```python
from et import ET

execution_time = ET("info")
"""
    YOUR CODE HERE
"""
execution_time.stop()
```
### Output:
```
 self  | The execution time = 0:00:00.000158S  | 156000 NS
 ```

 ## Example 

 ```python
from et import ET

executiontime = ET("Calculate radians")

import math
input1 = 1234567
y = math.radians(input1)
print(f'\n The input = {input1}, output = {y}')

executiontime.stop()
 ````
###     Output
 ```sh

 The input = 1234567, output = 21547.258986468834
 Calculate radians  | The execution time = 0:00:00.000102S  | 105000 NS
 
 ```

## ETM [Execution Time Manager]
```python
from et import ETM

with ETM() as etm:
    """
    YOUR CODE HERE
    """
```
### Output:
```shell
[Started]: 2021-01-19 17:36:39.878058
[End]: 2021-01-19 17:36:39.878538 Sec
[Elapsed time]:  0:00:00.000466 Sec
```

example

```python
from et import ETM

with ETM() as em:
    import math
    input1 = 1234567
    y = math.radians(input1)
    print(f'\n The input = {input1}, output = {y}')
```

### Output
```
The input = 1234567, output = 21547.258986468834

[Started]: 2021-01-19 17:36:39.878058
[End]: 2021-01-19 17:36:39.878538 Sec
[Elapsed time]:  0:00:00.000466 Sec

```

