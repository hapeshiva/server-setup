import requests
import os
import shutil
tuinity_url = "https://ci.codemc.io/job/Spottedleaf/job/Tuinity/lastSuccessfulBuild/artifact/tuinity-paperclip.jar"
print("hapeshiva server setup")
core = input("Do you want optimization? (y, n) ")

if core.casefold().startswith("y"):
    tuinity_response = requests.get(tuinity_url)
    if tuinity_response.ok:
        print("Download completed")
        open('tuinity_paperclip.jar', "wb").write(tuinity_response.content)
        open('tuinity_paperclip.jar')
        os.mkdir("server")
        server_core = "tuinity_paperclip.jar"
        server_path = "server"
        shutil.move(server_core, server_path)
        print("Core is ready. Working for optimization")
        bukkit = "bukkit.yml"
        spigot = "spigot.yml"
        paper = "paper.yml"
        tuinity = "tuinity.yml"
        sh = open("start.sh", "w")
        bat = open("start.bat", "w")
        sh.write("java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
        bat.write("java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
        sh.close()
        bat.close()
        shutil.move(bukkit, server_path)
        shutil.move(spigot, server_path)
        shutil.move(paper, server_path)
        shutil.move(tuinity, server_path)
        shutil.move(sh, server_path)
        shutil.move(bat, server_path)
        print("Server is ready! Move start.bat (Windows) or start.sh (Linux) to \"server\" directory. Go to server directory and test! Thanks for using hapeshiva server setup")
    else:
        print("Something went wrong")
else:
    tuinity_response = requests.get(tuinity_url)
    if tuinity_response.ok:
        print("Download completed")
        open('tuinity_paperclip.jar', "wb").write(tuinity_response.content)
        open('tuinity_paperclip.jar')
        os.mkdir("server")
        server_core = "tuinity_paperclip.jar"
        server_path = "server"
        shutil.move(server_core, server_path)
        print("Core is ready. Working for start files")
        sh = open("start.sh", "w")
        bat = open("start.bat", "w")
        sh.write("java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
        bat.write("java -Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar tuinity-paperclip.jar nogui")
        sh.close()
        bat.close()
        print("Server is ready! Move start.bat (Windows) or start.sh (Linux) to \"server\" directory. Go to server directory and test! Thanks for using hapeshiva server setup")
input = input("Press any key to close")
if input != "dontclose":
    exit()
