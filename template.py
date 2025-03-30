import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "AI_image_detection"

list_of_files = [
   
    f"src/{project_name}/preprocess.py",
    f"src/{project_name}/train.py",
    f"src/{project_name}/evaluate.py",
    f"src/{project_name}/detect.py",
    "app.py",
    "requirements.txt",
    "README.md",
    ]

for filepath in list_of_files:
    file = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
