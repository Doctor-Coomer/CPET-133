# Truth Table Generator

## Files
``truthtable.py`` is the backend for the truth table generator.  
``main.py`` is the entry point, and is intended to be modified.

# Example Usage

## Modify

Define a function with the signature ``Callable[[bool, Optional[...:bool]], bool]`` (this will be our "circut", and or our Boolean Algebra function).

```python
import truthtable;

# This is an AND gate
def f(x:bool, y:bool) -> bool:
	return x and y;
```

Then pass the function to the truth table generator.

```python
truthtable.print_truth_table(f);
```

## Running

Run ``main.py`` like so: 
```sh
$ python main.py
```

And the truth table for our AND function will be:
```
_________
x | y | f
---------
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1
```


# Other examples

```python
def f(a:bool, b:bool, c:bool) -> bool:
    return (a and b) or (not c);
```

```
_____________
a | b | c | f
-------------
0 | 0 | 0 | 1
0 | 0 | 1 | 0
0 | 1 | 0 | 1
0 | 1 | 1 | 0
1 | 0 | 0 | 1
1 | 0 | 1 | 0
1 | 1 | 0 | 1
1 | 1 | 1 | 1
```
