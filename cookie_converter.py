import json
import os
import random
import shutil
import progressbar

try:
    if os.name == "posix":
        folder_path = "cookies"
    else:
        while True:
            import tkinter
            from tkinter import filedialog

            print("\n<<< Select Netscape cookies folder >>>\n\n")
            tkinter.Tk().withdraw()
            folder_path = filedialog.askdirectory()
            if folder_path == "":
                print("Trying to use default folder 'cookies'\n")
                folder_path = "cookies"
                break

            else:
                break

    def maximum():
        count = 0
        for _, _, files in os.walk(folder_path):
            count += len(files)
        return count

    rand_number = random.randint(1, 99999)

    progress = 0
    pbar = progressbar.ProgressBar(maxval=maximum())

    def convert_netscape_cookie_to_json(cookie_file_content):
        cookies = []
        for line in cookie_file_content.splitlines():
            fields = line.strip().split("\t")
            if len(fields) >= 7:
                cookie = {
                    "domain": fields[0].replace("www", ""),
                    "flag": fields[1],
                    "path": fields[2],
                    "secure": fields[3] == "TRUE",
                    "expiration": fields[4],
                    "name": fields[5],
                    "value": fields[6],
                }
                cookies.append(cookie)

        json_content = json.dumps(cookies, indent=4)
        return json_content

    json_folder_path = "json_cookies"
    try:
        os.makedirs(json_folder_path, exist_ok=True)
        print(f"Folder {json_folder_path} created!\n")
        try:
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    with open(filepath, "r", encoding="utf-8") as file:
                        content = file.read()

                    json_data = convert_netscape_cookie_to_json(content)

                    with open(os.path.join(json_folder_path, filename), "w", encoding="utf-8") as f:
                        f.write(json_data)
                        print(f"{filename} - DONE!")
                        if 0 <= progress <= maximum():
                            pbar.start()
                            pbar.update(progress)
                            progress += 1
                        else:
                            pass
        except FileNotFoundError:
            print(
                "Error Occurred: Default 'cookies' folder not found, please select a valid folder"
            )
            shutil.rmtree(json_folder_path)

    except FileExistsError:
        if (
            input(
                "Do you want to remove old json_cookies folder? (y/n)\n [y] Recommended \n > : "
            )
            == "y"
        ):
            shutil.rmtree(json_folder_path)
            os.makedirs(json_folder_path, exist_ok=True)
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    with open(filepath, "r", encoding="utf-8") as file:
                        content = file.read()

                    json_data = convert_netscape_cookie_to_json(content)

                    with open(os.path.join(json_folder_path, filename), "w", encoding="utf-8") as f:
                        f.write(json_data)
                        print(f"{filename} - DONE!")
                        if 0 <= progress <= maximum():
                            pbar.start()
                            pbar.update(progress)
                            progress += 1
                        else:
                            pass

        else:
            os.makedirs(f"temp {rand_number}", exist_ok=True)
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    with open(filepath, "r") as file:
                        content = file.read()

                    json_data = convert_netscape_cookie_to_json(content)

                    with open(
                        os.path.join(f"temp {rand_number}", filename), "w", encoding="utf-8"
                    ) as f:
                        f.write(json_data)
                        print(f"{filename} - DONE!")
                        if 0 <= progress <= maximum():
                            pbar.start()
                            pbar.update(progress)
                            progress += 1
                        else:
                            pass

            print(f"\n\nSaved cookies to the temp folder - temp {rand_number}")
    finally:
        pbar.finish()

except KeyboardInterrupt:
    print("\n\nProgram Interrupted by user")
    exit()
