# food-recognition
Make the yolov10 architecture improve

# Dataset link
https://www.kaggle.com/datasets/rkuo2000/uecfood256/data

# Step 1
Download the dataset

# Step 2 - Preprocessing flow
0 - In UECFOOD256 folder, run pip install -r requirements.txt <br /> 
1 - In UECFOOD256 folder, run FixRedudancy.py to change the files name <br /> 
2 - In UECFOOD256 folder, run ConvertYoloFormat.py to apply the yolo format on the dataset <br />
3 - In UECFOOD256 folder, run splitter.py to split the dataset and move them to another directory located in root path of project <br />
4 - In UECFOOD256_assembeld folder, run splitter.py to split the images and labels <br />
5 - In yolov10 folder, run pip install -r requirements.txt <br />
6 - In yolov10 folder, check run_yolov10.ipynb file to download or run the requirements <br />
7 - If you had any problems, you can run validateAndLabels file in yolov10 folder <br />
