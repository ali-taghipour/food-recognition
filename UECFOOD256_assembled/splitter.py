import os
import random
import shutil

def split_images(root_folder):
    # path from source folders
    train_folder = root_folder + '/train'
    val_folder = root_folder + '/val'
    test_folder = root_folder + '/test'

    # path to destination folders
    train_img_folder = root_folder + '/train/images'
    train_lab_folder = root_folder + '/train/labels'
    val_img_folder = root_folder + '/val/images'
    val_lab_folder = root_folder + '/val/labels'
    test_img_folder = root_folder + '/test/images'
    test_lab_folder = root_folder + '/test/labels'

    # Create destination folders if they don't exist
    for tvt_folder_path in [train_img_folder, train_lab_folder, val_img_folder,val_lab_folder,test_img_folder,test_lab_folder]:
        if not os.path.exists(tvt_folder_path):
            os.makedirs(tvt_folder_path)

    # move files
    for filename in os.listdir(train_folder):
        if ".txt" in filename:
            shutil.move(train_folder + "/" + filename, train_lab_folder + "/" + filename)
        else:
            shutil.move(train_folder + "/" + filename, train_img_folder + "/" + filename)
     
    for filename in os.listdir(val_folder):
        if ".txt" in filename:
            shutil.move(val_folder + "/" + filename, val_lab_folder + "/" + filename)
        else:
            shutil.move(val_folder + "/" + filename, val_img_folder + "/" + filename)

    for filename in os.listdir(test_folder):
        if ".txt" in filename:
            shutil.move(test_folder + "/" + filename, test_lab_folder + "/" + filename)
        else:
            shutil.move(test_folder + "/" + filename, test_img_folder + "/" + filename)
            



if __name__ == "__main__":
    root_directory = "E:/Projects/food-recognition/UECFOOD256_assembled"  # Replace with the actual path
    split_images(root_directory)






