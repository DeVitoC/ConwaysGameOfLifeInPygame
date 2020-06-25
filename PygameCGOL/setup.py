import sys
import cx_Freeze

executables = [cx_Freeze.Executable("HomeScreen.py")]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

cx_Freeze.setup(
    name="Conway's Game of Life",
    version = "0.1",
    options={"build_exe": {"packages":["pygame", "tkinter"],
                           "include_files": ["AboutCGOL.py", "game_description.txt", "GameOfLife.py", "key_commands.txt", "KeyCommands.py"]}},
    executables = executables
    )