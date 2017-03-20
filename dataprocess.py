def dataProcess(keyData):
    print(keyData)
    for index, data in enumerate(keyData):
        if data.split('-')[1] == 'Key.backspace':
            keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1)]
            #can use del keyData[index] and del keyData[index - 1] 
            keydata = dataProcess(keyData)
            return keydata
    return keyData

def calculateKeypressTimings(keyPressData, keyReleaseData):
    interkeyTime = []
    keyPressData = [int(data.split('-')[2]) for data in keyPressData]
    keyReleaseData = [int(data.split('-')[2]) for data in keyReleaseData]
    keyHoldTime = [t2 - t1 for (t1, t2) in zip(keyPressData, keyReleaseData)]
    latencyTime = [keyPressData(index + 1) - keyPressData(index) for index in range(len(keyPressData) - 1)]
