import os
import time


things = []
                    
def combine_files():        

    for i,j,k in os.walk(r'C:\Users\Erick and Holly\Pictures\4K Stogram'):
        if not i.endswith('.stogram'):
            things.append(i)

    for i in things[1:]:
        os.chdir(i)
        files = os.listdir(i)
        saveFile = open('mylist.txt', 'w')
        for j in files:
            if j.endswith('.mp4'):
                saveFile.write('file '"'"+ j +"'"'\n')
        saveFile.close()
        if any('.mp4' in s for s in files):
            if not any('output.mp4' in s for s in files):
                os.system('ffmpeg -f concat -safe 0 -i mylist.txt -vcodec copy -acodec copy output.mp4')
        else:
            continue
        if float(os.popen('ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 output.mp4').read()) < 60:
            os.remove('output.mp4')

combine_files()
