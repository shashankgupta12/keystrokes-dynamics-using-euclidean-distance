from pynput.keyboard import Key, Listener
from datetime import datetime

dataentry = []
dataset = []

def on_press(key):
    t = datetime.now()
    time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
    dataentry.append("p-{0}-{1}".format(key,time))
    if key == Key.enter:
        return False

def on_release(key):
    t = datetime.now()
    time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
    dataentry.append("r-{0}-{1}".format(key,time))
    if key == Key.enter:
        return False

# text = str(input("Enter training text: "))
# print("Enter '{0}' 10 times:".format(text))
for entry in range(10):
    # print("Dataset_{0}".format(entry + 1), end='')
    print('start')
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    dataset.append(dataentry[:-1])
    dataentry = []

for dataentry in dataset:
    print(dataentry)