import os
import sys
import torch

people_path = os.path.join(os.path.dirname(__file__), '../../SavedData/')
attribute_path = os.path.join(os.path.dirname(__file__), '../../SavedData/hwang/day/RGB/')

people_list = os.listdir(people_path)
attribute_list = ['closed', 'front', 'yawn']

Database = []

image_num = 0
for people in people_list:
    for attribute in attribute_list:
        path = people_path + people + '/day/RGB/' + attribute
        images_path = os.path.join(os.path.dirname(__file__), path)

        image_list = os.listdir(images_path)
        image_num = image_num + len(image_list)

print(image_num)
Database.append(str(image_num))

Database.append('closed front yawn')


for people in people_list:
    for attribute in attribute_list:
        path = people_path + people + '/day/RGB/' + attribute
        images_path = os.path.join(os.path.dirname(__file__), path)

        image_list = os.listdir(images_path)
        for image in image_list:
            image_name = '/' + people + '/day/RGB/' + attribute + '/' + image
            image_label = None
            if(attribute == 'closed'):
                image_label = '1 -1 -1'
            elif(attribute == 'front'):
                image_label = '-1 1 -1'
            else:
                image_label = '-1 -1 1'

            line = image_name + ' ' + image_label
            Database.append(line)

with open("list_attr_etri.txt", "w") as f:
    for line in Database:
        line = line + '\n'
        f.write(line)

print(people_list)
print(attribute_list)

x = torch.ones(2,3)
y = x.clone()
print(y)


