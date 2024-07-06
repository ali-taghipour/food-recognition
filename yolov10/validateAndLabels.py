import os

dataset_base_path = 'E:/Projects/food-recognition/datasets'
train_label_path = os.path.join(dataset_base_path, 'custom_dataset/dataset/train/labels')
val_label_path = os.path.join(dataset_base_path, 'custom_dataset/dataset/val/labels')
test_label_path = os.path.join(dataset_base_path, 'custom_dataset/dataset/test/labels')

nc = 256

def check_labels(label_path):
    invalid_labels = []
    # Traverse through the label files
    for root, _, files in os.walk(label_path):
        for file in files:
            if file.endswith('.txt'):
                label_file_path = os.path.join(root, file)
                with open(label_file_path, 'r') as f:
                    for line in f:
                        class_id = int(line.split()[0])
                        if class_id >= nc:
                            invalid_labels.append((label_file_path, class_id))
    return invalid_labels

train_invalid_labels = check_labels(train_label_path)
val_invalid_labels = check_labels(val_label_path)
test_invalid_labels = check_labels(test_label_path)

if train_invalid_labels or val_invalid_labels or test_invalid_labels:
    print("Invalid labels found:")
    for label_file, class_id in train_invalid_labels:
        print(f"Train - {label_file}: {class_id}")
    for label_file, class_id in val_invalid_labels:
        print(f"Validation - {label_file}: {class_id}")
    for label_file, class_id in test_invalid_labels:
        print(f"Test - {label_file}: {class_id}")
else:
    print("All labels are valid.")