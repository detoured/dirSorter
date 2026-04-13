import os 
import sys
from pathlib import Path
import shutil


def main():
    extentions = {
    "images" : ["jpg","jpeg","jpe","png"],
    "videos" : ["mp4","mov", "avi", "mkv", "wmv"],
    "documents" : ["txt","pdf"]
    }

    handle_argv(extentions)

    path = sys.argv[1]
    contents = os.listdir(f"{path}")

    files = assign_files(contents,extentions)

    creare_dirs(path,contents,extentions,files)

    move_files(path,files)

def handle_argv(extentions):
    if len(sys.argv) < 2:
        print("Please provide a path to a dir")
        sys.exit(1)
    
    for arg in range (0,len(sys.argv)):
        if sys.argv[arg] == "-ae":
            if sys.argv[arg+1] in extentions:
                    extentions[sys.argv[arg+1]] += (sys.argv[arg+2]).split(",")
            else:
                extentions[sys.argv[arg+1]] = sys.argv[arg+2]
    

def assign_files(contents, extentions):
    files = {}
    
    for file in contents:
        for ext in extentions:
            if file.rsplit(".",1)[1] in extentions[ext]:
                if ext not in files:
                    files[ext] = []
                files[ext].append(file)
    return files

def creare_dirs(path,contents,extentions,files):
    for ext in extentions:
        if ext not in contents and ext in files:
                Path(f"{path}/{ext}").mkdir()

def move_files(path, files):
    for file_type in files:
        for file in files[file_type]:
            shutil.move(f"{path}/{file}",f"{path}/{file_type}")
main()