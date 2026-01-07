import os 
import shutil

public_path = "./public"
static_path = "./static"

def delete_from_public():
    # print('Removing all from public')
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)

def copy_to_public(path, public_dir):
    # print(" ")
    # print(os.listdir(path))

    completed = []
    dirs = os.listdir(path)
    for item in dirs:
        # print(f"\nIterating over {item}")
        joined_path = os.path.join(path, item)
        # print(f"\nThe file path is {joined_path}")
        if os.path.isfile(joined_path):
            shutil.copy(joined_path, public_dir)
            completed.append(joined_path)
        if os.path.isdir(joined_path):
            # print(f"\nRecursion will happen")
            public_dir = os.path.join(public_path, item)
            # print(f"\nPublic_dir is now {public_dir}")
            os.mkdir(public_dir)
            recursion_result = copy_to_public(joined_path, public_dir)
            completed.extend(recursion_result)
        # print(f"\nCompleted at the end of the iteration = {completed}")
    return completed

# delete_from_public()
# copy_to_public(static_path, public_path)