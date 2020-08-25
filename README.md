# File name obfuscator

## Usage

```
usage: main.py [-h] [-a] [-r] [-d D]

File name obfuscator

optional arguments:
  -h, --help  show this help message and exit
  -a          include directories
  -r          recursive
  -d D        directory
```

## Demo

```
~/Desktop >>> tree test 
test
├── dir
│   └── image.jpg
└── file.txt

1 directory, 2 files

~/Documents/GitHub/file-name-obfuscator >>> python main.py -a -r -d ~/Desktop/test
file.txt -> mZY7YyWN3kGPWedux2WPD2BlRZz25aVx.txt
image.jpg -> 7IfVhOuLL0qCqArShPkdMgDciZLTWOZ8.jpg
dir -> z0ZLC6BZPEKmW9qpPqKqwfuvh2qGVuj1

~/Desktop >>> tree test
test
├── mZY7YyWN3kGPWedux2WPD2BlRZz25aVx.txt
└── z0ZLC6BZPEKmW9qpPqKqwfuvh2qGVuj1
    └── 7IfVhOuLL0qCqArShPkdMgDciZLTWOZ8.jpg

1 directory, 2 files
```

