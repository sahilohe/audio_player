"""
Modules used :
    playsound - pip3 install playsound
    alsaaudio - sudo apt install python3-alsaaudio
    time (optional)
This only works on Linux

The path is for my system, change if you want to run on your machine
"""
import os, time
from playsound import playsound as play
import alsaaudio as audio

def audio_player():


    volume = audio.Mixer()
    default = '/home/fsociety/Music/' # that's mine default path for music

    path = input('\nEnter the path of the folder (default is /home/fsociety/Music/): \n') # enter the path of the songs folder


    if path == "":
        print('\nChoosen default folder - /home/fsociety/Music/')
        song = os.system(f'\n cd {default}\n')
        print(f'\nThe available files are: \n{os.listdir(default)}')
    else:
        song = os.system(f'\ncd {path}\n')
        print(f'\nThe available files are: \n{os.listdir(path)}')

    while True:

        ask = input('\nEnter the name of the song you want to play: \n')
        ask_volume = int(input('Enter the amount of volume: '))
        set_volume = volume.setvolume(ask_volume)

        if ask == 'quit' or ask == 'exit':
            break

        else:
            print(f'Okay, playing {ask}\n')
            time.sleep(1)
            if path == "":
                play(f'{default}/{ask}')
                set_volume = volume.setvolume(100)
            else:
                play(f'{path}/{ask}')
                set_volume = volume.setvolume(100)

audio_player()
