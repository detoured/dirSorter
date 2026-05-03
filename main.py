import os 
import sys
from pathlib import Path
import shutil
import argparse

def main():
    extentions = assign_defaults()
    
    path = handle_argv(extentions).path

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
    parser = argparse.ArgumentParser(description="Directory Sorter")
    parser.add_argument("path",type=str,help="path to the directory to sort")
    parser.add_argument("-a","--add",action="append",type=str,help="add custom extensions and/or directories")
    args = parser.parse_args()

    if not args.path:
        print("Please provide a path to a directory")
        sys.exit(1)
        
    if args.add:
        add_ext(extentions, args.add)
    
    return args

def add_ext(extentions, arg):
        try:
            for addition in arg:
                exts = addition.rsplit("=")[0].split(",")
                for ext in exts:
                    if ext not in extentions:
                        extentions[ext] = addition.rsplit("=")[1]
                        continue
                    del extentions[ext]
                    extentions[ext] = addition.rsplit("=")[1]
        except:
            print("Invalid [--add] arguement/s.")
            sys.exit(1)

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