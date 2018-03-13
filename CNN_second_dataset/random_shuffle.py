import os
import random
import shutil

img_dir = '/home/khsunkh/kihong/CNN_second_dataset/second_dataset/train/'
new_dir = '/home/khsunkh/kihong/CNN_second_dataset/test_dataset/'
label_list = os.listdir(img_dir)

Database = []

image_num = 0
for label in label_list:
    label_path = os.path.join(img_dir, label)
    img_list = os.listdir(label_path)
    for img in img_list:
        img_path = os.path.join(label_path, img)
        Database.append(img_path)
        image_num = image_num + 1

random.shuffle(Database)

for i, line in enumerate(Database):
    if i < (image_num * 0.3):
        shutil.move(line, new_dir)
