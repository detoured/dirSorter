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

    creare_dirs(path,files)

    move_files(path,files)

def assign_defaults():
        with open("default_values.txt", "r") as file:
            extentions = {}
            content = file.readlines()

            for line in content:
                for ext in line.rstrip().split(":")[1].split(","):
                    extentions[ext] = line.split(":")[0] 

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
            for ext in sys.argv[arg+1].split(","):
                if ext not in extentions:
                    extentions[ext] = sys.argv[arg+2]
        except:
            print("Invalid [-ae] arguements.")

def assign_files(content, extentions):
    files = {}
    
    for file in content:
        try:
            file_ext = file.rsplit(".",1)[1]
            if file_ext in extentions:
                files[file] = extentions[file_ext]
            else:
                files[file] = "misq"
        except:
            continue
    return files

def creare_dirs(path,files):
        for file in files:
                Path(f"{path}/{files[file]}").mkdir(exist_ok=True)

def move_files(path, files):
    for file in files:
        shutil.move(f"{path}/{file}",f"{path}/{files[file]}")
            
     
main()