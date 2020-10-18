import hello_module
hello_module.SayHello("kim")
print(type(hello_module))
import time
time.sleep(2)

import Calc
print(Calc.add(10, 10))

import Calc as meme
print(meme.div(6,3))

from Calc import sub
print(Calc.sub(4,3))
