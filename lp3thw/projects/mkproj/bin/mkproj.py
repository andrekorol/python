#! python3
import os, sys

try:
    script, projectname = sys.argv
    # print(projectname)
except ValueError:
    print("Name of new project must be given as argument!\n"
          "Usage: mkproj.py projectname")
    exit(0)

top = os.getcwd()

if sys.platform == "win32":
    project_path = top + '\\' + projectname
else:
    project_path = top + '/' + projectname

try:
    os.makedirs(project_path)
except FileExistsError:
    print(
        "FileExistsError: Cannot create a file when that file already exists:")
    print(project_path + " already exists!")