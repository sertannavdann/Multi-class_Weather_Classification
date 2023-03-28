import os
import shutil

path = 'data_original'
classes = ['cloudy', 'rain', 'shine', 'sunrise']

def get_class_name(file_name, classes):
    name_without_extension = file_name.split('.')[0]
    for class_name in classes:
        if class_name in name_without_extension.lower():
            return class_name
    return None


def organize_files(path, classes):
    files = os.listdir(path)
    for file in files:
        class_name = get_class_name(file, classes)
        if class_name is not None:
            class_folder = os.path.join(path, class_name)
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)
            # move the file to the corresponding class folder
            source_path = os.path.join(path, file)
            destination_path = os.path.join(class_folder, file)
            shutil.move(source_path, destination_path)

organize_files(path=path, classes=classes)