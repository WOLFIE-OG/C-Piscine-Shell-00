import random
import os
import pathlib
import uuid

def get():
    if bool(random.randint(0, 1)):
        front = "#"
        back = "#"
    else:
        front = random.choice(["#", ""])
        back = "~"
    
    return front, back

for i in range(0, 20):
    folder = f"test-{i}"
    dir_ = pathlib.Path(f"{os.getcwd()}/{folder}")
    if not os.path.exists(pathlib.Path(dir_)):
        os.mkdir(dir_)
        print(f"Made dummy dir {dir_}")
    
    for i in range(0, 20):
        os.system(f"truncate -s 10 {pathlib.Path(f'{dir_}/{get()[0]}{str(uuid.uuid4())}{get()[1]}')}")
        print("Created dummy file")
        