import _thread
from time import sleep

def test_thread():
    print("test")
    sleep(1)


for i in range(10):
    _thread.start_new_thread(test_thread, ())
