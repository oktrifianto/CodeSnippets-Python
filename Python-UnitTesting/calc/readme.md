# Calculator Testing

### Reference

https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

### How to Running Test?

Manual
```
python -m unittest test_calculator.py
```

if we run using 

```
python test_calculator.py 
```

result: <b>`nothing!`</b>

# But...

We can use this following syntax. 

```
if __name__ == '__main__':
  unittest.main()
```

So, we can ran this code:

```
python test_calculator.py
```

result:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```