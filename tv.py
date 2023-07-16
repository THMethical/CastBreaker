#/usr/bin/python3
import sys
import os
import pyfiglet
from rich import print 

ascii_banner = pyfiglet.figlet_format("CastBreaker")
print(ascii_banner)

def main():
   menu()


def menu():
    print()

    Frage = input("""
    1 =  TV Scan              
    2 =  TV Leise 0%
    3 =  TV Laut 100%
    4 =  Webseite Senden
    5 =  Aktuelle Info
    6 =  Play
    7 =  Pause
    8 =  Hacked Video
    """)
    
    

    if Frage == "1" or Frage =="1":
        tv_scan1()
        
    if Frage == "4":
        webseite_senden()
        
    if Frage == "2":
        volume_0()
        
    if Frage == "3":
        volume_100()
        
    if Frage == "5":
        aktuelle_informaton()
        
    if Frage == "6" or Frage == "play":
        play_whatever()
                
    if Frage == "7" or Frage == "stop":
        stop_whatever()
                
    if Frage == "8" or Frage == "Hacked":
        hacked_video()

    elif Frage=="Exit" or Frage=="exit":
        sys.exit
        
    else:
        print("Nochmal versuchen")
        menu()
        
        
def tv_scan1():
    scan1_tv = os.system("catt scan")


def webseite_senden():
    print("[red] Webseite Angeben: ")
    angegebene_webseite = input()
    sende_webseite = os.system(f"catt cast_site {angegebene_webseite} ")


def volume_100():
    lautstaerke_100 = os.system("catt volume 100")


def volume_0():
    lautstaerke_0 = os.system("catt volume 9")

def aktuelle_informaton():
    informationen_von_videoundgerat = os.system("catt info")
    
def play_whatever():
    spieleab = os.system("catt play")

def stop_whatever():
    stoppealles = os.system("catt stop")
    
    
def hacked_video():
    have_hacked_your_tv = os.system("catt cast -s ./script.srt ./video.mp4")



main()
