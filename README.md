# Directory Sorter
Organizes a directory by moving files into seperate sub directories that are sorted by file extention

Usage format:

> Sort files using default extensions and directories:
```
python3 main.py <path_to_dir>
```

> Add a custom extention to a custom directory
```
python3 main.py <path_to_dir> <-ae> <dir> <ext1>
```

> Add custom extentions to a custom directory
```
python3 main.py <path_to_dir> <-ae> <dir> <ext1,ext2,ext3>
```

> Add custom extentions to custom directories
```
python3 main.py <path_to_dir> <-ae> <dir> <ext1,ext2,ext3> <-ae> <dir2> <ext4,ext5,ext6> 
```

* To alter the default settings to your liking, edit the defualt_values.txt file. Use this format: name:ext1,ext2,ext3

* If you want to add a custom extension to a default directory, you use the same command as you would for a custom directory.
