import os
import pathlib
import cv2 as cv

actual_path = os.path.join(os.path.dirname(__file__), 'Aprendizaje_Abecedario')
new_path = os.path.join(os.path.dirname(__file__), 'Aprendizaje_Abecedario_Puntos')

with os.scandir(actual_path) as directories:
    for directory in directories:
        letter_directory = os.path.join(actual_path, directory)
        new_letter_dir = new_path +  '\\' + str(directory).split("'")[1]
        # print(new_letter_dir)
        
        with os.scandir(letter_directory) as letters:
            for letter in letters:
                file = os.path.join(letter_directory, letter)
                letter_name = str(letter).split("'")[1].split('.png')[0]
                new_letter_name = letter_name + '_landmark'
                # print(letter_name)
                # print(new_letter_name)
                
                
                if os.path.exists(new_letter_dir) and os.path.isdir(new_letter_dir):
                    if not os.listdir(new_letter_dir):
                        # os.rmdir(new_letter_dir)
                        print('direcorio vacio')
                        
                        img = cv.imread(file)
                        
                        
                        
                    else:
                        with os.scandir(new_letter_dir) as new_letters:
                            for new_letter in new_letters:
                                existing_file = os.path.join(new_letter_dir, new_letter)
                                print(new_letter)
                                if existing_file == os.path.join(new_letter_dir, new_letter_name + '.png'):
                                    try:
                                        os.remove(existing_file)
                                    except:
                                        continue
                else:
                    os.mkdir(new_letter_dir)
                
                print(os.path.join(new_letter_dir, new_letter_name + '.png'))

                # cv.imshow(file, img)
                # cv.waitKey(0)
                # cv.destroyAllWindows()