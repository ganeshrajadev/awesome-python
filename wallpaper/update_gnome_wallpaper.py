import os,random
import constants

WALLPAPER_DIR= constants.WALLPAPER_DIR # Wallpaper Location 

images=[item for item in os.listdir(WALLPAPER_DIR) if os.path.isfile(os.path.join(WALLPAPER_DIR,item)) and item.split(".")[-1].lower() in ["png",'jpg']]

if len(images) >0:
    wallpaper=random.choice(images)
    os.system("gsettings set org.gnome.desktop.background picture-uri file://"+os.path.join(WALLPAPER_DIR,wallpaper))