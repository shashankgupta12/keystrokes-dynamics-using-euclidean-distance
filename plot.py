# pip install pynput
# pip install python-xlib
from pynput.keyboard import Key, Listener
import time
import statistics

l = []
m = []

def on_press(key):
    t1 = "p-{0}-{1}".format(key,time.time())
    l.append(t1)
    # print('Pressed: {0}'.format(key))
    ## amazing discovery!!! because each thread required a key press
    ## to stop therefore the on_press function needed to return a 
    ## false value as well
    if key == Key.enter:
        # Stop listener
        return False

def on_release(key):
    t2 = 'r{0}'.format(time.time())
    l.append(t2)
    # print('Released: {0}'.format(key))
    # if key == Key.enter:
    #     # Stop listener
    #     return False

# Collect events until released
for _ in range(10):
    print ("start again")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    m.append(l[:-1])
    l = []

for i in m:
    print(i)