from colorama import Fore, Back, Style
import sys
from pathlib import Path

def recursive_directory_mapping(directory_path, space_num = 0):
    for path in directory_path.iterdir():
        if path.is_file:
            print(Fore.BLUE, " " * space_num, path)
        else:
            print(Fore.GREEN, " " * space_num, path)
            recursive_directory_mapping(path, space_num + 4)
    return

print(Style.RESET_ALL)
directory = Path(input("Введіть шлях до директорії: "))
if not directory.exists():
    print("Вказазаний вами шлях не існує")
elif not directory.is_dir():
    print("Вказаний вами шлях не є директорією")
else:
    recursive_directory_mapping(directory)





# D:\BARDACHOCK\NOW