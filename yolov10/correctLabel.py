import os


dataset_base_path = 'E:/Projects/food-recognition/datasets'
train_label_path = os.path.join(dataset_base_path, 'custom_dataset/dataset/train/labels')
val_label_path = os.path.join(dataset_base_path, 'custom_dataset/dataset/val/labels')
test_label_path = os.path.join(dataset_base_path, 'custom_dataset/dataset/test/labels')


nc = 256

def correct_labels(label_path):
    for root, _, files in os.walk(label_path):
        for file in files:
            if file.endswith('.txt'):
                label_file_path = os.path.join(root, file)
                with open(label_file_path, 'r') as f:
                    lines = f.readlines()
                
                corrected_lines = []
                for line in lines:
                    parts = line.split()
                    class_id = int(parts[0])
                    if class_id >= nc:
                        print(f"Correcting {label_file_path}: {class_id}")
                        class_id = nc - 1  # Map to the maximum valid class index
                    parts[0] = str(class_id)
                    corrected_lines.append(" ".join(parts) + "\n")
                
                with open(label_file_path, 'w') as f:
                    f.writelines(corrected_lines)

correct_labels(train_label_path)
correct_labels(val_label_path)
correct_labels(test_label_path)

print("Label correction complete.")