import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files =[
    ".github/workflows/.gitkeep", #for deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", #Model related parameters will be stored here.
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]


for file_path in list_of_files:
    filepath = Path(file_path) #Instead of using os.path.join() , we use Path fucntion, so that it will modify path directory based on Oprating System.
    filedir, filename = os.path.split(filepath)#  #Seperating files and folders , Split function seperates into head and tail, Returns array of [(head, tail)]
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)):
        with open(filepath, 'w') as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
