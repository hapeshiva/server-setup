import requests
import os
import shutil

# Optimization chech
core = input("Do you want optimization? (y, n) ")
# Start setup
tuinity_url = "https://ci.codemc.io/job/Spottedleaf/job/Tuinity/lastSuccessfulBuild/artifact/tuinity-paperclip.jar"
tuinity_response = requests.get(tuinity_url)
print("Download completed")
open('tuinity_paperclip.jar', "wb").write(tuinity_response.content)
open('tuinity_paperclip.jar')
server_path = "server"
if os.path.exists(server_path) == False:
    os.mkdir("server")
server_core = "tuinity_paperclip.jar"
shutil.move(server_core, server_path)
print("Core is ready. ")
sh = open("start.sh", "w")
bat = open("start.bat", "w")
sh.write("java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
bat.write("java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
sh.close()
bat.close()
print("Start files is ready")
# View distance
config = open("server.properties", "a")
view_distance = input("Input your view_distance (in chunks, default 10): ")
if int(view_distance) < 65:
    config.write("view-distance=" + str(view_distance) + "\n")
    print("Succesfully")
else:
    config.write("view-distance=10")
    print("Something went wrong, view distance set to default")
config.close()
# Server port
server_port = input("Input your server_port (from 1000 to 99999, default 25565): ")
configport = open("server.properties", "a")
print(type(server_port).__name__)
if int(server_port) > 1000 and int(server_port) < 99999:
    configport.write("server-port=" + server_port + "\n")
    print("Succesfully")
else:
    configport.write("server-port=25565")
    print("Something went wrong, server port set to default")
configport.close()
shutil.move("server.properties", server_path)
# Optimization
if core.casefold().startswith("y"):
    shutil.move("bukkit.yml", server_path)
    shutil.move("spigot.yml", server_path)
    shutil.move("paper.yml", server_path)
    shutil.move("tuinity.yml", server_path)
    print("Server is ready! Move start.bat (Windows) or start.sh (Linux) to \"server\" directory. Go to server directory and test! Thanks for using hapeshiva server setup\n Optimization created with this guide: https://www.spigotmc.org/threads/guide-server-optimization%E2%9A%A1.283181/")
    print("Please configure mob-spawn-range in spigot.yml for your view distance (vd * 16)") 
if core.casefold().startswith("y") == False:
    print("Server is ready! Move start.bat (Windows) or start.sh (Linux) to \"server\" directory. Go to server directory and test! Thanks for using hapeshiva server setup\n ")
    print("Please configure mob-spawn-range in spigot.yml for your view distance (vd * 16)") 
input = input("Press any key to close")
if input != "dontclose":
    exit()
