import math, re, xml.dom.minidom
from log import log

def getDanmu(filePath):
    '''
    @param filePath recorded xml file path
    @return list of danmu
    '''

    # open file and read data
    # with open(filePath, 'r', encoding = 'utf-8') as xmlFile:
    #     xmlDoc = xml.dom.minidom.parse(xmlFile)
    #     xmlFile.close()
    xmlDoc = xml.dom.minidom.parse(filePath)
    danmuList = xmlDoc.getElementsByTagName('d')
    log(1, 'danmuList: ', danmuList)

    # extract danmu time and content
    danmuConverted = []
    for danmuItem in danmuList:
        danmuParam = danmuItem.getAttribute('p')
        danmuTime = danmuParam.split(',')[0]
        danmuContent = danmuItem.childNodes[0].data
        danmuConverted.append([danmuTime, danmuContent])
        log(0, danmuTime, ': ', danmuContent)
    log(0, danmuConverted)

    return danmuConverted

# ref: K-bai. https://github.com/K-bai/meumy-live-showcase/blob/master/server/danmu_analyse.py
def isCall(content):
    '''
    @param content danmu content
    @return one of: True, False
    '''

    callListRe = re.compile('\u10e6|\u2600|\u26c8|\u26c5|\\\\.+/') # re of call
    if callListRe.search(content):
        return True
    else: 
        return False

def getCallStat(danmuList, statPeriod = 3):
    '''
    @param danmuList list of danmu (generated by function getDanmu)
    @param statPeriod the period of statistics in unit second
    @return dictionary of time with frequency
    '''

    # get call danmu list
    timestamps = []
    for danmu in danmuList:
        if isCall(danmu[1]):
            timestamps.append(danmu[0])
            log(0, 'danmu ', danmu, ' is call')
        else:
            log(0, 'danmu ', danmu, ' is not call')
    log(1, 'timestamp: ', timestamps)
    log(2, len(timestamps), ' danmu(s) accepted')
    
    # get statistics of period
    # will be updated
    timeStat = {}
    for time in timestamps:
        timeSec = math.floor(float(time)/statPeriod)*statPeriod
        # timeMark = str(int(timeSec/60)) + ':' + str(timeSec%60)
        timeMark = timeSec
        timeStat[timeMark] = timeStat.get(timeMark, 0) + 1
        log(0, 'time ', timeMark)
    log(1, 'timeStat: ', timeStat)
    log(2, len(timeStat), ' timestamp(s) extracted')

    return timeStat

            
def getFragment(timeStat, minlen = 30, maxmerge = 9):
    '''
    @param timeStat call statictics (generated by function getCallStat)
    @param minlen minimal length of a period
    @param maxmerge maximum length of blank. Any blank longer than this leads to separated fragment
    @return 
    '''

    timeList = list(timeStat)
    # log(1, timeList)

    # variable init
    status = True # True: within a fragment, False: out of any fragment
    tmpTimeStart = timeList[0]
    tmpTimeStop = timeList[0]

    fragmentCollect = []

    for index in range(len(timeList) - 1): 
        if status == True:
            if timeList[index+1] - timeList[index] > maxmerge:
                # the blank exceeds maxmerge, fragment ends here
                status = False
                tmpTimeStop = timeList[index]
                if tmpTimeStop - tmpTimeStart > minlen:
                    fragmentCollect.append([tmpTimeStart, tmpTimeStop])
                else: 
                    # too short, abandoned
                    pass
        else:
            # try to start
            if timeList[index+1] - timeList[index] > maxmerge:
                pass # isolated call
            else:
                status = True
            tmpTimeStart = timeList[index]
    
    log(1, 'fragmentCollect: ', fragmentCollect)
    log(2, len(fragmentCollect), ' fragment(s) extracted')
    return fragmentCollect
