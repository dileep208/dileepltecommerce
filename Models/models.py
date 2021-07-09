print('this is an excercise')

import os
def file_name(filename):
    return os.path.exists(filename) and os.path.isfile(filename)

    