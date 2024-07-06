import os
import random
import shutil

def split_images(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            print(f"Processing files in folder: {folder_name}")
            # 1. Obtain the image data Retrieve all the images located in the designated folder

            # path to destination folders
            train_folder = os.path.join(folder_path, 'train')
            val_folder = os.path.join(folder_path, 'eval')
            test_folder = os.path.join(folder_path, 'test')

            # Define a list of image extensions
            image_extensions = ['.jpg']

            # Create a list of image filenames in 'data_path'
            imgs_list = [filename for filename in os.listdir(folder_path) if os.path.splitext(filename)[-1] in image_extensions]
                    
            # 2. Split the data Randomly separate the image data into three sets: 70% for training, 10% for validation, and 20% for testing.

            # Sets the random seed 
            random.seed(42)

            # Shuffle the list of image filenames
            random.shuffle(imgs_list)

            # determine the number of images for each set
            train_size = int(len(imgs_list) * 0.70)
            val_size = int(len(imgs_list) * 0.10)
            test_size = int(len(imgs_list) * 0.20)

            # 3. Copy the images into their respective folders Create separate folders for each set, including the training, evaluation,
            #  and testing sets. Copy the images into their respective folders based on the random split.

            # Create destination folders if they don't exist
            for tvt_folder_path in [train_folder, val_folder, test_folder]:
                if not os.path.exists(tvt_folder_path):
                    os.makedirs(tvt_folder_path)

            # Copy image files to destination folders
            for i, f in enumerate(imgs_list):
                txt_file = f[0:f.index(".")] + ".txt"
                if i < train_size:
                    dest_folder = train_folder
                elif i < train_size + val_size:
                    dest_folder = val_folder
                else:
                    dest_folder = test_folder
                shutil.copy(os.path.join(folder_path, f), os.path.join(dest_folder, f))
                shutil.copy(os.path.join(folder_path, txt_file), os.path.join(dest_folder, txt_file))

def move_splitted_images(root_folder,assembled_directory):
    # path to destination folders
    train_folder = os.path.join(assembled_directory, 'train')
    val_folder = os.path.join(assembled_directory, 'val')
    test_folder = os.path.join(assembled_directory, 'test')

    # Create destination folders if they don't exist
    for tvt_folder_path in [train_folder, val_folder, test_folder]:
                if not os.path.exists(tvt_folder_path):
                    os.makedirs(tvt_folder_path)

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            print(f"Processing files in folder: {folder_name}")
            
            # get into train folder
            for filename in os.listdir(folder_path + "/train"):
                shutil.copy(os.path.join(folder_path + "/train", filename), os.path.join(train_folder, filename))

            # get into eval folder
            for filename in os.listdir(folder_path + "/eval"):
                shutil.copy(os.path.join(folder_path + "/eval", filename), os.path.join(val_folder, filename))

            # get into test folder
            for filename in os.listdir(folder_path + "/test"):
                shutil.copy(os.path.join(folder_path + "/test", filename), os.path.join(test_folder, filename))


if __name__ == "__main__":
    root_directory = "E:/Projects/food-recognition/UECFOOD256"  # Replace with the actual path
    assembled_directory = "E:/Projects/food-recognition/UECFOOD256_assembled"
    split_images(root_directory)
    move_splitted_images(root_directory,assembled_directory)






