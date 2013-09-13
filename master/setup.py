from cx_Freeze import setup, Executable

setup(
    name = "File Age",
    version = "0.1",
    description = "Shows the age of files",
    executables = [Executable("fileage.py", base="Win32GUI")])
