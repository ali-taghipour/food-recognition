import os
from PIL import Image

def read_files_in_folders(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            print(f"Processing files in folder: {folder_name}")
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    # print(f"Reading lines from file: {filename}")
                    if filename == "bb_info.txt":
                        bb_info = []
                        with open(file_path, 'r') as file:
                            for line in file:
                                # Process each line (e.g., print, analyze, etc.)
                                splitted_line = line.split()
                                if(splitted_line[0] != "img"):
                                    # get image 
                                    img_file_path = folder_path + "/" + folder_name + "-" + splitted_line[0] + ".jpg"
                                    img = Image.open(img_file_path) 
                                    
                                    # get width and height 
                                    width = img.width 
                                    height = img.height 
                                    
                                    bb_info.append({
                                        "file_path": folder_name + "-" + splitted_line[0] + ".txt",
                                        "class_id": folder_name,
                                        "x_center": ((int(splitted_line[1]) + int(splitted_line[3]))/2) / width,
                                        "y_center": ((int(splitted_line[2]) + int(splitted_line[4]))/2) / height,
                                        "width": (int(splitted_line[3]) - int(splitted_line[1])) / width,
                                        "height": (int(splitted_line[4]) - int(splitted_line[2])) / height
                                    })

                        for item in bb_info:
                            bb_txt_file = open(root_folder + '/' + folder_name + '/' + item['file_path'],"w")
                            bb_txt_file.write(f"{item['class_id']} {item['x_center']:.4f} {item['y_center']:.4f} {item['width']:.4f} {item['height']:.4f}")
                            bb_txt_file.close()


if __name__ == "__main__":
    root_directory = "E:/Projects/food-recognition/UECFOOD256"  # Replace with the actual path
    read_files_in_folders(root_directory)
