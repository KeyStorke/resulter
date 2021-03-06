# Resulter
[![Build Status](https://travis-ci.org/KeyStorke/resulter.svg?branch=master)](https://travis-ci.org/KeyStorke/resulter)


Resulter is library for make a code more clearly, more readable and more supportable.

It's simply and readable. Awesome replacement of return tuples or error codes. 
# Installation

``` bash
pip3 install resulter
```

# Example

``` python
from resulter import ok, error, resultify


def plus_two(x):
    try:
        return ok(float(x) + 2)
    except Exception as e:
        return error(e)


@resultify
def divide_by_two(x):
    _x = int(x)

    if not _x:
        raise ValueError(x)
    return _x / 2


for i in range(-5, 5):
    y = divide_by_two(i)
    x = plus_two(i)
    if y.is_ok() and x.is_ok():
        print('y = {}'.format(y.value))
        print('x = {}'.format(x.value))
        print()
    else:
        print('error')
        print()


# OUTPUT

# y = -2.5
# x = -3.0
#
# y = -2.0
# x = -2.0
#
# y = -1.5
# x = -1.0
#
# y = -1.0
# x = 0.0
#
# y = -0.5
# x = 1.0
#
# error
#
# y = 0.5
# x = 3.0
#
# y = 1.0
# x = 4.0
#
# y = 1.5
# x = 5.0
#
# y = 2.0
# x = 6.0


```
