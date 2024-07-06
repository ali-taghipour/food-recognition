import os

def fix_redundancy(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            print(f"Processing files in folder: {folder_name}")
            for filename in os.listdir(folder_path):
                if not os.path.isdir(folder_path + "/" + filename) and filename != "bb_info.txt":
                    old_file = os.path.join(folder_path, filename)
                    new_file = os.path.join(folder_path, folder_name + "-" + filename)
                    os.rename(old_file, new_file)


if __name__ == "__main__":
    root_directory = "E:/Projects/food-recognition/UECFOOD256"  # Replace with the actual path
    fix_redundancy(root_directory)
