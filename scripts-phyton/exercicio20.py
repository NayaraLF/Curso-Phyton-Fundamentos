from pygame import mixer
import time
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

mixer.init()
mixer.music.load("musica.mp3")
mixer.music.play()




