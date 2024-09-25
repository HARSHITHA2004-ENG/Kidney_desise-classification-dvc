import os
from pathlib import Path
import logging
#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # it will provide message while creating folders
project_name = 'cnnClassifier'
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # it will work finr for linux os and even for max
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html" 
    # we are using flask
]
for filepath in list_of_files:
    filepath = Path(filepath) # as window os support only backwoed slash for filr path here we have used forward slash so to support the os path we have used path convertor to support id we didnt provide this we will get array error as path cant find it will make the code more robust
    filedir, filename = os.path.split(filepath)
    
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) # to create a  folder we have used mkdir exit_ok makes sure that if this folder is already exist it wont be created again
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  #  it just provide login inform messg as creating a directory followed bu file directory for the named file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if  the file is not present in that specified directoery and its size is zero then we are s=ceatibg the file
        with open(filepath, "w") as f: # file path will create the file
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists") # if already exist it will provide this message