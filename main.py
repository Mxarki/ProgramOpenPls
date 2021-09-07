import os
import time

from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")
if not os.path.exists('config.ini'):
    print("No config detected!\nPlease create a config named 'config.ini'")
    exit(1)

outDir = config['Directory']['outDir']
application = config['Directory']['appToOpen']
applicationClose = config['Directory']['appToClose']
timer = int(config['Function']['time'])

fullPath = os.path.join(outDir, application)
print(fullPath)

print("Welcome!\nMade by Markie ;)))\n")
print("Current executing path set: " + fullPath)
print("Current application to kill set: " + applicationClose)
print("Amount of time set: " + str(timer))
print("\n")
while True:
    print("---------------------------------------------")
    print("Executing file...\n")
    os.startfile(fullPath)
    print("Sleeping for " + str(timer) + " seconds...\n")
    time.sleep(timer)
    print("Killing process...\n")
    os.system(r"TASKKILL /F /T /IM " + applicationClose)
    print("Process killed! Restarting loop!")
    print("---------------------------------------------\n\n\n")

