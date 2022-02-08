import os, sys
import xmlproc as xp
import vidproc as vp
from log import log

if __name__ == "__main__":
    '''
    main entry
    @param fileName recording file
    '''

    # input file
    fileName = sys.argv[1].rsplit('.', 1)
    log(2, 'input file: ', fileName[0] + '.' + fileName[1])
    log(2, 'input file ext: ', fileName[1])

    # statistics
    danmu = xp.getDanmu(fileName[0] + '.xml')
    timeStat = xp.getCallStat(danmu, 6)
    fragments = xp.getFragment(timeStat)

    # create a new directory
    try: 
        os.mkdir(fileName[0])
    except:
        log(3, 'Target directory already exists. Type y to continue, else exit')
        choice = input()
        if choice == 'Y' or choice == 'y':
            pass
        else:
            sys.exit(0)
    else:
        pass

    # clip
    index = 0
    indexLength = len(str(len(fragments)))
    for frag in fragments:
        index = index + 1
        startTime = str((frag[0] - 9) // 3600).zfill(1) + '.' + \
                    str(((frag[0] - 9) % 3600) // 60).zfill(2) + '.' + \
                    str((frag[0] - 9) % 60).zfill(2)
        endTime   = str(frag[1] // 3600).zfill(1) + '.' + \
                    str((frag[1] % 3600) // 60).zfill(2) + '.' + \
                    str(frag[1] % 60).zfill(2)

        vp.clip(fileName[0] + '.' + fileName[1], 
                frag[0] - 9, frag[1], 
                fileName[0] + '\\' + str(index).zfill(indexLength) + '_' + startTime + '-' + endTime + '.flv'
                )
    log(2, index, ' video(s) clipped')
