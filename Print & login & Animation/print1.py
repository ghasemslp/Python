import time , sys
from colorama import Fore,init
init()

target = "Id Github ==> G h a s e m S l p"
guess = ""

for index, charcter in enumerate(target):
    j = ord(' ')
    while True:
        sys.stdout.write(f'\r{guess}{chr(j)}')
        sys.stdout.flush()
        time.sleep(0.001)
        if chr (j) == charcter:
            guess += charcter
            break
        j += 1

#سازنده
#  id = Ghasem_slp
#  github = ghasemslp