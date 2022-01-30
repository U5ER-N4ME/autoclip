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
    fileName = sys.argv[1].split('.')
    log(2, 'input file: ', fileName[0] + '.' + fileName[1])
    log(2, 'input file ext: ', fileName[1])

    # statistics
    danmu = xp.getDanmu(fileName[0] + '.xml')
    timeStat = xp.getCallStat(danmu, 6)
    fragments = xp.getFragment(timeStat)

    # create a new directory
    os.mkdir(fileName[0])

    # clip
    index = 0
    for frag in fragments:
        index = index + 1
        vp.clip(fileName[0] + '.' + fileName[1], 
                frag[0] - 9, frag[1], 
                fileName[0] + '\\' + str(index) + '.mp4'
                )
    log(2, index, ' video(s) clipped')
