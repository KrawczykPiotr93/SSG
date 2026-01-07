import os 
import shutil

docs_path = "./docs"
static_path = "./static"

def delete_from_docs():
    # print('Removing all from public')
    if os.path.exists(docs_path):
        shutil.rmtree(docs_path)
    os.mkdir(docs_path)

def copy_to_docs(path, public_dir):
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
            public_dir = os.path.join(docs_path, item)
            # print(f"\nPublic_dir is now {public_dir}")
            os.mkdir(public_dir)
            recursion_result = copy_to_docs(joined_path, public_dir)
            completed.extend(recursion_result)
        # print(f"\nCompleted at the end of the iteration = {completed}")
    return completed

# delete_from_docs()
# copy_to_docs(static_path, docs_path)
