# Python GUI
Some practice about Python GUI practice
## Turn to Executables
`make_exe.sh` uses [pyinstaller](http://www.pyinstaller.org/) to turn `.py` file to `.exe` file.

To turn file.py to file.exe
```bash=
./make_exe.sh file.py
```
The executables are in `dist/`.

To remove all pyinstaller files(including the executables)
```bash=
./make_exe.sh clean
```
