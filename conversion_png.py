import PIL
import os
import pathlib

actual_path = pathlib.Path(__file__).parent.absolute()
print(actual_path)

# directories = os.listdir(actual_path)

list_dir = []

with os.scandir(actual_path) as directories:
    for directory in directories:
        if directory.is_dir():
            list_dir.append(directory)

image_dir = os.path.join(actual_path, list_dir[2])

list_img_dir = []

with os.scandir(image_dir) as img_directories:
    for img_dir in img_directories:
        list_img_dir.append(img_dir)

list_img_real_dir = []

for img_dir in list_img_dir:
    list_img_real_dir.append(os.path.join(image_dir, img_dir))

files_cant = 0
labels = []

for img_dir in list_img_real_dir:
    print('Directorio:', img_dir)
    files = os.listdir(img_dir)
    for file in files:
        print('Archivo:', file)
        files_cant += 1
        labels.append(files_cant)

for label in labels:
    print('Etiqueta:', label)