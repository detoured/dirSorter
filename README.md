# Directory Sorter
Organizes a directory by sorting files into separate subdirectories based on their file extensions.


Usage format:

> Sort files using default extensions and directories:
```
python3 main.py <path_to_dir>
```

> Add a custom extention to a custom directory
```
python3 main.py <path_to_dir> <-ae> <ext1> <dir> 
```

> Add custom extentions to a custom directory
```
python3 main.py <path_to_dir> <-ae> <ext1,ext2,ext3> <dir> 
```

> Add custom extentions to custom directories
```
python3 main.py <path_to_dir> <-ae> <ext1,ext2,ext3> <dir> <-ae> <ext4,ext5,ext6> <dir2> 
```

* To alter the default settings to your liking, edit the defualt_values.txt file. Use this format: name:ext1,ext2,ext3

* If you want to add a custom extension to a default directory, you use the same command as you would for a custom directory.
