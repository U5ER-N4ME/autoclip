terminalLogLevel = 2
fileLogLevel = 5
logLevelList = ['TMP', 'DBG', 'INF', 'WRN', 'ERR']

def log(level, *content):
    # log output to terminal
    if level >= terminalLogLevel:
        print ('[' + logLevelList[level] + '] ', end = '')
        for item in content:
            print(item, end = '')
        print ()
    else:
        pass
    
    # log to file
    if level >= fileLogLevel:
        with open('log.txt', 'a', encoding='utf-8', errors='ignore') as logfile:
            logfile.write('[' + logLevelList[level] + '] ')
            for item in content:
                logfile.write(str(item))
            logfile.write('\n')


