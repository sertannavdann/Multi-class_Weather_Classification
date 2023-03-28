import os
import shutil
import random

directory = 'data'
balance_dir = 'balanced_data'
merged_dir = 'data/merged/'
classes = os.listdir(directory)

# Function to determine the class based on filename
def get_class(file_name, classes):
    for cls in classes:
        if cls in file_name:
            return cls
    return None

# Create a dictionary to store files for each class
class_files = {}
for cls in classes:
    class_files[cls] = []

# Collect files from the respective directories
for cls in classes:
    for data_type in ['train', 'test']:
        source_dirs = [directory, balance_dir]

        for source_dir in source_dirs:
            source_class_dir = os.path.join(source_dir, cls)
            if os.path.isdir(source_class_dir):
                for file in os.listdir(source_class_dir):
                    class_files[cls].append(os.path.join(source_class_dir, file))

# Shuffle and split the files for each class
train_ratio = 0.8
train_files = {}
test_files = {}
for cls in classes:
    random.shuffle(class_files[cls])
    train_size = int(len(class_files[cls]) * train_ratio)
    train_files[cls] = class_files[cls][:train_size]
    test_files[cls] = class_files[cls][train_size:]

# Create the necessary directories if they don't exist
for cls in classes:
    os.makedirs(os.path.join(merged_dir, 'train', cls), exist_ok=True)
    os.makedirs(os.path.join(merged_dir, 'test', cls), exist_ok=True)

# Move files into train and test directories with their respective class folders
for cls in classes:
    for file in train_files[cls]:
        shutil.copy(file, os.path.join(merged_dir, 'train', cls, os.path.basename(file)))

    for file in test_files[cls]:
        shutil.copy(file, os.path.join(merged_dir, 'test', cls, os.path.basename(file)))
