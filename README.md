# Auto-Wallpaper-Changer
A simple python script that changes the users wallpaper every time the pc is turned on.\
This script copies itself to windows startup, and changes your wallpaper to a random image from over 1000 images\
Runs Every time you start up your computer\
Simple Setup\

# How to setup
Prerequisites: \
\
An installation of python \
Pyinstaller \
A Code editor

Steps: \
\
Get the wallpaperchange.py script. Either download it or make a new file\
Then open up a new terminal, either in your IDE or as a windows CMD/Powershell\
Now run this command:
```
pyinstaller --noconfirm --onefile --windowed --ascii --clean  "C:/Path/To/wallpaperchanger.py"
```
Now your .exe file would have been created!\
Run the exe, ignore any errors, they wont hinder the process,\
Now, if you ran the .exe, the executable should now be copied into: 
```
C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
This means that whenever you turn on your computer, the executable will be ran, and thus, your wallpaper would have changed!\
\
If you dont want to do all of that, you can try downloading the exe from this repo for easy use\


```
Note: WallpaperChange.py is designed to work as an exe, therefore it will not work in your code editor as a .py
```
