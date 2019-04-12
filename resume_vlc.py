import configparser
from constants import configFilePath #Vlc configuarion file path
import os, urllib.parse

configParser = configparser.RawConfigParser()   


configParser.read([configFilePath])
recent=configParser["RecentsMRL"]

last_watched=recent["list"].split(",")
time_list=recent["times"].split(",")

if len(last_watched) >0 and len(time_list):
    p=(urllib.parse.urlparse(last_watched[0]))
    finalPath = urllib.parse.unquote(p.path)
    last_stopped_seconds=int(time_list[0])/1000
    if last_stopped_seconds >5:
        last_stopped_seconds=last_stopped_seconds-5 # Go back 5 secs
    os.system("vlc --start-time="+str(last_stopped_seconds)+" '"+finalPath+"'")