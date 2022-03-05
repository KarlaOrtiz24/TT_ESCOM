import PIL
import os
from os import remove
from os import path
import pathlib
import cv2 as cv

def convertirPng():
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
    cant_img = []

    for img_dir in list_img_real_dir:
        print('Directorio:', img_dir)
        files = os.listdir(img_dir)
        cant_img_dir = 0
        for file in files:
            img = cv.imread(os.path.join(img_dir, file))
            res = cv.resize(img, dsize=(50, 50), interpolation=cv.INTER_CUBIC)
            print('Archivo:', file)
            filename_list = file.split('.')
            
            if len(filename_list) > 2:
                second_half = filename_list[0] + '.' + filename_list[1]
                final_path = os.path.join(img_dir, second_half) + '.png'
                cv.imwrite(final_path, res)
                if path.exists(os.path.join(img_dir, second_half) + '.jpg'):
                    remove(os.path.join(img_dir, second_half) + '.jpg')
                    print('Archivo jpg eliminado')
                    print(os.path.join(img_dir, second_half) + '.jpg')
                elif path.exists(os.path.join(img_dir, second_half) + '.jpeg'):
                    remove(os.path.join(img_dir, second_half) + '.jpeg')
                    print('Archivo jpeg eliminado')
                    print(os.path.join(img_dir, second_half) + '.jpeg')
            
            else:
                final_path = os.path.join(img_dir, filename_list[0]) + '.png'
                cv.imwrite(final_path, res)
                    
            print('Nuevo archivo escrito con exito!')
            files_cant += 1
            cant_img_dir += 1
            labels.append(files_cant)
        cant_img.append(cant_img_dir)

    print(cant_img)
convertirPng()