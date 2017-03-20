from pynput.keyboard import Key, Listener
from datetime import datetime
from dataprocess import dataProcess

keyPressData = []
keyReleaseData = []
dataset = []

def onPress(key):
    t = datetime.now()
    # print("p-{0}".format(key))
    if not key == Key.enter:
        time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
        keyPressData.append("p-{0}-{1}".format(key,time))
    # if key == Key.enter:
    #     return False

def onRelease(key):
    t = datetime.now()
    # print("r-{0}".format(key))
    if key == Key.enter:
        return False
    else:
        time = t.minute*60*(10**6) + t.second*(10**6) + t.microsecond
        keyReleaseData.append("r-{0}-{1}".format(key,time))

def dataCollect():
    global keyPressData
    global keyReleaseData
    # text = input("Enter training text: ")
    print("Enter name 10 times:")
    for entry in range(10):
        print("Dataset_{0}".format(entry + 1))
        # print('start')
        with Listener(on_press=onPress, on_release=onRelease) as listener:
            listener.join()
        # keyPressData = dataProcess(keyPressData) 
        # keyReleaseData = dataProcess(keyReleaseData)
        dataset.append((dataProcess(keyPressData), dataProcess(keyReleaseData)))
        keyPressData = []
        keyReleaseData = []

dataCollect()
for dataentry in dataset:
    print(dataentry)