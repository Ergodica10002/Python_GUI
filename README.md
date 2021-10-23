# Python GUI
Some practice about Python GUI practice
## Turn to Executables
`make_exe.sh` uses [pyinstaller](http://www.pyinstaller.org/) to turn `.py` file to `.exe` file.

To turn prog.py to prog.exe
```bash=
./make_exe.sh prog.py
```

To turn programs to executables according to a spec file 
```bash=
./make_exe.sh file.spec
```

The executables will be in `dist/`.

To remove all pyinstaller files(including the executables)
```bash=
./make_exe.sh clean
```
