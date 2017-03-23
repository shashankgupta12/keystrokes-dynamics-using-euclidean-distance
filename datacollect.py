from pynput.keyboard import Key, Listener
from datetime import datetime
import json
from dataprocess import dataProcess, extractTimings

keyPressData = []
keyReleaseData = []
dataset = []

def processAndStore(keyPressData, keyReleaseData):
    keyPressData, keyReleaseData = extractTimings(dataProcess(keyPressData), dataProcess(keyReleaseData))
    data = dict(keyPressData=keyPressData, keyReleaseData=keyReleaseData)
    dataset.append(data)

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
    text = 'shashank'
    print("Enter {0} 10 times:".format(text))
    for entry in range(10):
        print("Dataset_{0}".format(entry + 1))
        
        with Listener(on_press=onPress, on_release=onRelease) as listener:
            listener.join()
        
        processAndStore(keyPressData, keyReleaseData)
        keyPressData = []
        keyReleaseData = []

    # create json file; since this a static model and text is always same
    # therefore it is not added to the json object
    with open('data.json', 'a') as f:
        json.dump(dataset, f) 

dataCollect()
for dataentry in dataset:
    print(dataentry)