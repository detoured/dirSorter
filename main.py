import os 
import sys
from pathlib import Path
import shutil


def main():
    extentions = assign_defaults()
    
    handle_argv(extentions)

    path = sys.argv[1]
    content = os.listdir(f"{path}")

    files = assign_files(content,extentions)

    creare_dirs(path,content,extentions,files)

    move_files(path,files)

def assign_defaults():
        with open("default_values.txt", "r") as file:
            lines = {}
            current_line = -1
            extentions = {}
            content = file.read()
            for charI in range(0,len(content)):
                if charI == 0 or content[charI] == "\n":
                    current_line += 1
                    lines[current_line] = ""
                    if content[charI] == "\n":
                        continue
                lines[current_line] += content[charI]

            for ext in range(0,len(lines)):
                extentions[lines[ext].split(":")[0]] = lines[ext].split(":")[1].split(",")
            return extentions

def handle_argv(extentions):
    if len(sys.argv) < 2:
        print("Please provide a path to a directory")
        sys.exit(1)
    
    for arg in range (0,len(sys.argv)):
        if sys.argv[arg] == "-ae":
            add_ext(extentions, arg)

def add_ext(extentions, arg):
        try:
            if sys.argv[arg+1] in extentions:
                    extentions[sys.argv[arg+1]] += (sys.argv[arg+2]).split(",")
            else:
                extentions[sys.argv[arg+1]] = sys.argv[arg+2]
        except:
            print("Invalid [-ae] arguements.")

def assign_files(content, extentions):
    files = {}
    
    for file in content:
        for ext in extentions:
            if file.rsplit(".",1)[1] in extentions[ext]:
                if ext not in files:
                    files[ext] = []
                files[ext].append(file)
    return files

def creare_dirs(path,content,extentions,files):
    for ext in extentions:
        if ext not in content and ext in files:
                Path(f"{path}/{ext}").mkdir()

def move_files(path, files):
    for file_type in files:
        for file in files[file_type]:
            shutil.move(f"{path}/{file}",f"{path}/{file_type}")

main()