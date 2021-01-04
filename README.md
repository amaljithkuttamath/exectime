# exectime

Average time to execute these 2 commands is 100ms

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



