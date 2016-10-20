import os
import sys


def path_load(level=2):
    root_dir = os.path.abspath(__file__)
    for i in range(0, level):
        root_dir = os.path.dirname(root_dir)

    print root_dir
    return root_dir


sys.path.insert(0, path_load(2))
