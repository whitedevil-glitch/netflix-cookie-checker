import json
import os
import random
import shutil
import progressbar
import tkinter
from tkinter import filedialog

def maximum():
    count = 0
    for _, _, files in os.walk(folder_path):
        count += len(files)
    return count

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

def process_file(file_path, output_folder, progress):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    json_data = convert_netscape_cookie_to_json(content)

    with open(os.path.join(output_folder, os.path.basename(file_path)), "w", encoding="utf-8") as f:
        f.write(json_data)
        print(f"{os.path.basename(file_path)} - DONE!")
        progress += 1
        pbar.update(progress)

try:
    print("\n<<< Select Netflix cookies [Netscape] folder >>>\n\n")
    tkinter.Tk().withdraw()
    folder_path = filedialog.askdirectory()

    if not any(f.endswith(".txt") for f in os.listdir(folder_path)):
        raise ValueError("Error: The selected folder has no cookies. Please select another folder.")

    rand_number = random.randint(1, 99999)

    progress = 0
    pbar = progressbar.ProgressBar(maxval=maximum())

    path = "json_cookies"
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Folder {path} created!\n")
        try:
            pbar.start()  # Start the progress bar
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    process_file(filepath, path, progress)

        except FileNotFoundError:
            print("Error Occurred: Selected folder not found.")
            shutil.rmtree(path)

    except FileExistsError:
        shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)
        pbar.start()  # Start the progress bar
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath):
                process_file(filepath, path, progress)

    pbar.finish()

except ValueError as ve:
    print(str(ve))
except KeyboardInterrupt:
    print("\n\nProgram Interrupted by user")
    exit()
