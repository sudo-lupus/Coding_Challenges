#!/usr/bin/env python3

import sys
import os
import subprocess
import re

def kyu_dir(kyu):
    dir = r"./{}".format(str(kyu)+"_kyu")
    if os.path.isdir(r"./{}".format(str(kyu)+"_kyu")):
        return dir
    else:
        print("There is no folder: " + dir)
        return None

def new_file(kyu_dir, ending = ".py"):
    files = " ".join(os.listdir(kyu_dir))
    file_numeration = [int(num) for num in re.findall(r"_(\d+)\.*", files)]
    new_file_num = max(file_numeration) + 1
    new_file_name = f"{kyu_dir}_{new_file_num}{ending}"
    new_file_loc = os.path.join(kyu_dir, new_file_name)
    with open(new_file_loc, "w+"):
        print("Successfully created {} in dir:\n{}".format(new_file_name, kyu_dir))

dir = sys.argv[1]
new_file(kyu_dir(dir))