import os
import time


things = []
        
def delete_files():

    for i,j,k in os.walk(r'C:\Users\Erick and Holly\Pictures\4K Stogram'):
        if not i.endswith('.stogram'):
            things.append(i)

    for i in things[1:]:
        os.chdir(i)
        files = os.listdir(i)
        for j in files:
            if any('output.mp4' in s for s in files):
                if not j.endswith('.stogram'):
                    os.remove(j)

delete_files()
