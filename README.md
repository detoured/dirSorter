# Dirso
Organizes a directory by sorting files into separate subdirectories based on their file extensions.


Installation:

```
pipx install git+https://github.com/detoured/Dirso.git
```


Usage format:

> Sort files using default extensions and directories:
```
dirso <path_to_dir>
```

> Map an extension to a directory
```
dirso <path_to_dir> --add/-a <ext1=dir> 
```

> Map multiple extensions to a directory
```
dirso <path_to_dir> --add/-a <ext1,ext2,ext3=dir> 
```

> Map extensions to multiple directories
```
dirso <path_to_dir> --add/-a <ext1,ext2,ext3=dir> --add/-a <ext4,ext5,ext6=dir2> 
```

* To alter the default settings to your liking, edit the default_values.txt file. Use this format: name:ext1,ext2,ext3

* If you want to add a custom extension to a default directory, you use the same command as you would for a custom directory.

* Extensions are case sensitive and should be provided without a leading dot.