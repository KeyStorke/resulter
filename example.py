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
