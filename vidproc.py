import os
# import subprocess
from log import log

# ffmpeg -loglevel warning -ss <start_time> -to <stop_time> -i <input_file> -c copy <output_file>
def clip(fin, start, end, fout):
    os.system('ffmpeg -loglevel warning -ss ' + str(start) + ' -to ' + str(end) + ' -i ' + fin + ' -c copy ' + fout)
    # p = subprocess.Popen('ffmpeg -loglevel warning -ss ' + str(start) + ' -to ' + str(end) + ' -i ' + fin + ' -c copy ' + fout)
    # while p.poll() == None:
    #     pass
    log(0, 'video clipped: ', start, '-', end, ' to file ', fout)
