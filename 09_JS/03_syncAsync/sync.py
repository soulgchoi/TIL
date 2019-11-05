# Python: Blocking
from time import sleep

print('hi')
sleep(3)
print('bye')

def sleep_3():
    sleep(3)
    print('Wake Up!')

print('start sleeping')
sleep_3()
print('End of program')