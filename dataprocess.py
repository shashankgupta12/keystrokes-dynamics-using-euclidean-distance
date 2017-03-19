# from pynput.keyboard import Key, Listener
# import time
# import statistics

# l = []
# m = []

# def on_press(key):
#     t1 = "p-{0}-{1}".format(key,time.time())
#     l.append(t1)
#     if key == Key.enter:
#         # Stop listener
#         return False

# def on_release(key):
#     t2 = 'r{0}'.format(time.time())
#     l.append(t2)
#     if key == Key.enter:
#         # Stop listener
#         return False

# # Collect events until released
# for _ in range(10):
#     print ("start again")
#     with Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()
#     m.append(l[:-1])
#     l = []

# for l in m:
#     for i in l:

# def dataprocess(dataList):
#     keyPressTime = []
#     keyReleaseTime = []
#     for eachDataset in dataList:
#         eachDataset = eachDataset[:-1]
#         for index, eachKeypressTime in enumerate(eachDataset):
#             values = eachKeypressTime.split('-')
#             if values[0] == 'p':
#                 keyPressTime.append(float(values[2]))
#             elif values[0] == 'r':
#                 keyReleaseTime.append(eachKeypressTime)
#         for index, eachKeypressTime in enumerate(keyPressTime):
#             values = eachKeypressTime.split('-')
#             if values[1] == 'key.backspace':


import datetime 
t1 = datetime.datetime.now()
t2 = datetime.datetime.now()
time1 = t1.minute*60*(10**6) + t1.second*(10**6) + t1.microsecond
time2 = t2.minute*60*(10**6) + t2.second*(10**6) + t2.microsecond
print t2 - t1
print time2 - time1