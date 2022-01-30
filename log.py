logLevel = 2
logLevelList = ['TMP', 'DBG', 'INF', 'WRN', 'ERR']

def log(level, *content):
    if level >= logLevel:
        print ('[' + logLevelList[level] + '] ', end = '')
        for item in content:
            print(item, end = '')
        print ()
    else:
        pass

