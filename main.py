import os 
import sys
from pathlib import Path
import shutil


def main():
    path = sys.argv[1]
    contents = os.listdir(f"{path}")

    image_extentions = ["jpg","jpeg","jpe","png"]
    video_extentions = ["mp4","mov", "avi", "mkv", "wmv"]
    document_extentions = ["txt","pdf"]

    creare_dirs(path,contents)
    move_files(path,assign_files(contents,image_extentions,video_extentions,document_extentions))

def creare_dirs(path,contents):
    if "images" not in contents:
        Path(f"{path}/images").mkdir()

    if "videos" not in contents:
        Path(f"{path}/videos").mkdir()    
    
    if "documents" not in contents:
        Path(f"{path}/documents").mkdir()

def assign_files(contents, image_extentions,video_extentions, document_extentions):
    image_files = []
    video_files = []
    document_files = []

    for file in contents:
        if file.rsplit(".",1)[1] in image_extentions:
            image_files.append(file)
        elif file.rsplit(".",1)[1] in video_extentions:
            video_files.append(file)
        elif file.rsplit(".",1)[1] in document_extentions:
            document_files.append(file)  

    return image_files, video_files, document_files

def move_files(path, files):
    for file in files[0]:
        shutil.move(f"{path}/{file}",f"{path}/images")
    for file in files[1]:
        shutil.move(f"{path}/{file}",f"{path}/videos")
    for file in files[2]:
        shutil.move(f"{path}/{file}",f"{path}/documents")

main()