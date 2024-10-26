# The Luau Updater for MacOS by SpinnySpiwal #
# Please don't remove the credits, thank you! #
# Do not steal the credit of the script, it is created by me! #

import requests, os, zipfile, sys
def hasSudo():
    if os.geteuid() == 0:
        return True
    else:
        return False

try:
    def request_root():
        if os.geteuid() != 0:
            print("\r",end="")
            os.execvp("sudo", ["sudo"] + ["python3"] + sys.argv + ["-hassudo"])
        else:
            return True


    def progress_bar(iteration, total, prefix="", suffix="", length=30, fill="█"):
        percent = "{:.1f}".format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + "-" * (length - filled_length)
        color_code = (
            "\033[31m"
            if filled_length < length * 0.5
            else "\033[33m" if filled_length < length * 0.9 else "\033[32m"
        )
        color_reset = "\033[0m"
        print(
            f"\r{prefix} {color_code}{bar}{color_reset} {percent}% {suffix}",
            end="",
            flush=True,
        )


    response = requests.get("https://api.github.com/repos/luau-lang/luau/releases/latest", headers={"X-GitHub-Api-Version": "2022-11-28"}).json()

    def luau_updater_handler(response, dupeRequest=False):
        choice = None
        if not(dupeRequest) and not len(sys.argv)==2:
            choice = input(f"Luau version {response['tag_name']} has been released! Update now? [Y/N/S/?]\n")
        elif (len(sys.argv)) == 2:
            print(f"Updating to Luau {response['tag_name']}")
            choice = "y"
        else:
            choice = input("Update now? [Y/N/S]")
        currentChoice = choice.lower()
        if currentChoice == "y" or  sys.argv[1]:
            if not(hasSudo()):
                print("Luau updater by SpinnySpiwal")
                print("Luau updater requires root to access /opt/local/bin to later write the new luau binary and give you, the user execution permissions on the user level. Without using su or sudo.")
                request_root()
        elif currentChoice == "n":
            print("Okay, no problem!")
            print("Make sure to update later!")
            print("Tip ~ use s (aka skip) to skip this version and update next time! You can run this script at any time.")
            exit()
        elif currentChoice == "s":
            print("Okay, no problem!")
            print(f"Skipping version {response['tag_name']}.")
            try:
                with open(os.path.expanduser("~/.luau_version"), "w") as file:
                    file.write(str(response["tag_name"]))
            except:
                pass
            exit()
        elif currentChoice == "?":
            print("Y = Yes")
            print("N = No")
            print("S = Skip This Version")
            luau_updater_handler(response, True)
        else:
            print("Invalid query! Use ? for help.")
            luau_updater_handler(response)
            exit()

    if os.path.isfile(os.path.expanduser("~/.luau_version")):
        with open(os.path.expanduser("~/.luau_version"), "r") as luau_version:
            if response["tag_name"] == luau_version.read() and os.path.isfile("/opt/local/bin/luau"):
                exit()
            else:
                luau_updater_handler(response)
    else:
        luau_updater_handler(response)

    def handle_file_download(progress_bar, file_size, downloaded_bytes, r):
        with open("luau-macos.zip", "wb") as f:
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
                    downloaded_bytes += len(chunk)
                    progress_bar(
                        downloaded_bytes,
                        file_size,
                        prefix="Progress:",
                        suffix="Complete",
                        length=100,
                    )


    for file in response["assets"]:
        if file["name"] != "luau-macos.zip":
            continue

        file_size = int(file["size"])

        downloaded_bytes = 0
        with requests.get(file["browser_download_url"], stream=True) as r:
            handle_file_download(progress_bar, file_size, downloaded_bytes, r)
            if os.path.isfile("luau-macos.zip"):
                zipfile.PyZipFile("./luau-macos.zip").extract("luau", "/opt/local/bin")
                os.remove("./luau-macos.zip")
                os.system("chmod +x /opt/local/bin/luau")

    print("\nUpdated! Thanks for using Luau Updater for MacOS by SpinnySpiwal")

    try:
        with open(os.path.expanduser("~/.luau_version"), "w") as file:
            file.write(str(response["tag_name"]))
    except:
        pass
except KeyboardInterrupt:
    print("\r", end="")
except:
    pass