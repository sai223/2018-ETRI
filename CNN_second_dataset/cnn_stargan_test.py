import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
import torch.utils.data as data
import torchvision.datasets as dataset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable

from cnn_model import Discriminator

import os


img_size = 128
crop_size = 896
batch_size = 1

model = Discriminator(img_size, 64, 2, 6)
model.cuda()

model_path = '/home/khsunkh/kihong/CNN_second_dataset/models/100_170_model.pth'
img_dir = '/home/khsunkh/kihong/CNN_second_dataset/test_dataset'

model.load_state_dict(torch.load(model_path))
model.eval()

transform = transforms.Compose([
    #transforms.CenterCrop(crop_size),
    transforms.Scale(img_size),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

img_data = dataset.ImageFolder(img_dir, transform)
test_loader = data.DataLoader(img_data, batch_size=batch_size, shuffle=False)

correct = 0
total = 0
for i, (img, label) in enumerate(test_loader):
    
    img2 = img.squeeze()
    
    save_img = transforms.ToPILImage()(img2)    
    print(save_img)

    x = Variable(img, volatile=True).cuda()
    y = Variable(label).cuda()

    output = model(x)
    output = output.unsqueeze(0)
    
    print(output)
    _, output_index = torch.max(output, dim=1)

    img_name = str(i) + '.jpg'
    img_save_path = '/home/khsunkh/kihong/CNN_second_dataset/{}/{}'.format(output_index.data[0], img_name)

    save_img.save(img_save_path)

    #total += label.size(0)
    #corret += (output_index == y).sum().float()



#print("Accuracy of Test Data: {}".format(100*correct/total))
