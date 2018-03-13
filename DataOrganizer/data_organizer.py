import os
import sys
import glob

attribute_path = os.path.join(os.path.dirname(__file__), '../../data_center/')

attribute_list = os.listdir(attribute_path)

Database = []

image_num = 0
for attribute in attribute_list:
    path = attribute_path + attribute
    images_path = os.path.join(os.path.dirname(__file__), path)

    image_list = os.listdir(images_path)
    image_num = image_num + len(image_list)

print(image_num)
Database.append(str(image_num))
Database.append(' '.join(attribute_list))

for attribute in attribute_list:
    path = attribute_path + attribute + '/'
    images_path = os.path.join(os.path.dirname(__file__), path)
    filename_list = os.listdir(images_path)
    filename_list.sort()

    for filename in filename_list:
        print(len(os.listdir(images_path)))
        image_name = '/' + attribute + '/' + filename
        image_label = None
        if(attribute == 'closed_eye'):
            image_label = '1 -1 -1'
        elif(attribute == 'open_eye'):
            image_label = '-1 1 -1'
        elif(attribute == 'yawn'):
            image_label = '-1 -1 1'

        line = image_name + ' ' + image_label
        Database.append(line)



with open("list_attr_data_center.txt", "w") as f:
    for line in Database:
        line = line + '\n'
        f.write(line)
