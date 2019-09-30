from mutagen.mp3 import MP3 as mp3
from time import sleep
import pygame
import sys

args = sys.argv
 
target_time = int(float(args[1]))
 
def up_timer(secs):
    for i in range(0,secs):
        print(i)
        sleep(1)
    filename = './one05.mp3' #再生したいmp3ファイル
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length
    pygame.mixer.music.play(1)
    sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()
 
 
up_timer(target_time)