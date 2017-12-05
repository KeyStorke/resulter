#PyResult

Pyresult is library for make a code more clearly, more readable and more supportable.

It's simply and readable. Awesome replacement of return tuples or error codes. 
# Example

``` python
import os


def read_file(filename):
    str_filename = str(filename)

    if not os.path.isfile(str_filename):
        return error('not found')

    try:
        with open(str_filename, 'r') as file_handle:
            return ok(file_handle.read())
    except Exception as e:
        return error(str(e))


result = read_file('any_file')

if result.is_ok():
    ''' if no error '''
else:
    ''' if error '''

```