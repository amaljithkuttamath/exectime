# Install

```
pip install etime
```

Usage:-

# Execution Time
```python
from et.et import ET

execution_time = ET("info")
"""
    YOUR CODE HERE
"""
execution_time.stop()
```
### Output:
```
 info  | The execution time = 0:00:00.000010ms  | 15000 NS
 ```

 ## Example 

 ```python
from et.et import ET

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

# ETM [Execution Time Manager]
```python
from et.et import ETM

with ETM() as etm:
    """
    YOUR CODE HERE
    """
```
### Output:
```
 | Started at | 2021-01-04 22:58:56.947392 |

 | End at | 2021-01-04 22:58:56.947535  |

  | Elapsed time | 0:00:00.000143 Sec | 
```

example

```python

from et.et import ETM

with ETM() as em:
    import math
    input1 = 1234567
    y = math.radians(input1)
    print(f'\n The input = {input1}, output = {y}')
```

### Output
```
 | Started at | 2021-01-05 14:14:25.392834 |

 The input = 1234567, output = 21547.258986468834
 | End at | 2021-01-05 14:14:25.392888  |

  | Elapsed time | 0:00:00.000054 Sec | 

```

