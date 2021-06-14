#    server-setup, generates configs and fetches tuinity jar
#    Copyright (C) 2021  hapeshiva                      Author
#    Copyright (C) 2021  Ethan Hemingway (LethalEthan)  Co-Author
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from os.path import exists
import psutil
import requests
import shutil
import sys

# Detect python version, only runs on 3+
if (sys.version_info > (3, 0)):
    print("Python 3 has been detected you may continue\n")
else:
    exit("Python 2 has been detected please run in Python3!")
server_core = "tuinity-paperclip.jar"
server_path = "server"
maxmem = float(psutil.virtual_memory().total / 1000000000)
tuinity_url = "https://ci.codemc.io/job/Spottedleaf/job/Tuinity/lastSuccessfulBuild/artifact/tuinity-paperclip.jar"

print("hapeshiva server setup")
def UserInput():
    global memory
    global optimise
    while True:
        try:
            optimise = str(input("Do you want optimised server configs? (y, n) "))
        except ValueError:
            print("Please enter y/n")
        else:
            break

# Check if server Jar exists /
def CheckJar():
    if exists(server_core):
        rm = str(input("Tuinity jar already downloaded, do you want to re-download? (y, n) "))
        if rm.casefold().startswith("y"):
            os.remove(server_core)
            os.remove(server_path+"/"+server_core)
            Download()
    else:
        Download()

#Download Tuinity Jar /
def Download():
    print("Downloading Jar...")
    tuinity_response = requests.get(tuinity_url)
    if tuinity_response.ok:
        print("Download completed")
        open('tuinity_paperclip.jar', "wb").write(tuinity_response.content)
        open('tuinity_paperclip.jar')
        if exists("server") == False:
            os.mkdir("server")
        if exists(server_path+"/"+server_core) == False:
            shutil.move(server_core, server_path)
    else:
        print("Something went wrong trying to download tuinity!")
        exit()

#Create Start scripts
def CreateStartScripts():
    while True:
        try:
            memory = int(input("How much memory do you want to allocate in GB? "))
        except EOFError:
            memory = 4
            break
        except ValueError:
            print("Please enter a number")
        else:
            if memory > 0 and memory <= maxmem - 2:
                print("Memory value is within range of max available memory, continuing")
                break
            else:
                print("The memory value you defined is higher than the available system memory detected! This will cause a crash!")
                override = str(input("f you believe this is an error you can override this message, do you want to override? (y, n) "))
                if override.casefold().startswith("y"):
                    print("Overrided")
                    break
    mem = str(memory)
    if exists("start.sh"):
        os.remove("start.sh")
    if exists("start.bat"):
        os.remove("start.bat")
    if exists(server_path + "/start.sh"):
        os.remove(server_path + "/start.sh")
    if exists(server_path + "/start.bat"):
        os.remove(server_path + "/start.bat")

    sh = open("start.sh", "w")
    bat = open("start.bat", "w")
    sh.write("java -Xms"+mem+"G -Xmx"+mem+"G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
    bat.write("java -Xms"+mem+"G -Xmx"+mem+"G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
    sh.close()
    bat.close()
    shutil.move("start.sh", server_path)
    shutil.move("start.bat", server_path)

# View distance And Server Port
def SetViewDistanceAndPort():
    # Remove existing server.props in current dir
    if exists("server.properties"):
        os.remove("server.properties")
    # Check for server.props in server_path
    if exists(server_path + "/server.properties"):
        rm = input("Current server.properties found, would you like to remove it so the view distance and port can be set? (y, n) ")
        if rm.casefold().startswith("y"):
            os.remove(server_path + "/server.properties")
        else:
            return
    else:
        config = open("server.properties", "a")
        # View Distance
        while True:
            try:
                view_distance = int(input("Input your view_distance (in chunks, default 10): "))
            # Incorrect input e.g.nfi437y
            except ValueError:
                print("Please enter a number")
            # On correct input with validation
            else:
                if view_distance <= 32 and view_distance >= 3:
                    config.write("view-distance=" + str(view_distance) + "\n")
                    print("View Distance set Succesfully")
                    break
                else:
                    print("View distance must be between 3 - 32")
        # Server port
        while True:
            try:
                server_port = int(input("Input your server_port (from 1000 to 99999, default 25565): "))
            # Incorrect Input e.g. Ajibijbewia
            except ValueError:
                print("Please enter a valid port")
            # On correct input and validation
            else:
                if server_port > 1000 and server_port < 99999:
                    config.write("server-port=" + str(server_port) + "\n")
                    print("Server port set successfully")
                    break
                else:
                    print("Server port must be 1000 - 99999")
        config.close()
        shutil.move("server.properties", server_path)

#Move optimised configs and create startup scripts /
def MoveConfig():
    #Move optimised configs
    if optimise.casefold().startswith("y"):
        print("Server Jar is download. Moving optimized server configs")
        #CreateStartScripts()
        if exists("bukkit.yml"):
            print("bukkit.yml exists")
            shutil.copy("bukkit.yml", server_path)
        if exists("spigot.yml"):
            print("spigot.yml exists")
            shutil.copy("spigot.yml", server_path)
        if exists("paper.yml"):
            print("paper.yml exists")
            shutil.copy("paper.yml", server_path)
        if exists("tuinity.yml"):
            print("tuinity.yml exists")
            shutil.copy("tuinity.yml", server_path)
    print("Server Jar is ready")
    print("\nServer is ready! Use start.bat (Windows) or start.sh (Linux. Go to server directory and test! Thanks for using hapeshiva server setup")
#End
def End():
    end = input("Press any key to close...")
    if end != "dontclose":
        exit()

CheckJar()
UserInput()
CreateStartScripts()
SetViewDistanceAndPort()
MoveConfig()
End()
