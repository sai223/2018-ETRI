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

def compute_accuracy(x, y):
    _, predicted = torch.max(x, dim=1)
    correct = (predicted == y).float()
    accuracy = torch.mean(correct) * 100.0

    return accuracy

batch_size = 16
learning_rate = 0.0001
epoch = 100
img_size = 128

img_dir = "/home/khsunkh/kihong/second_dataset/train"
model_save_dir = "/home/khsunkh/kihong/CNN_second_dataset/models"

transform = transforms.Compose([transforms.Scale(img_size), transforms.RandomHorizontalFlip(), transforms.ToTensor(), transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))])

img_data = dataset.ImageFolder(img_dir, transform)
img_batch = data.DataLoader(img_data, batch_size=batch_size, shuffle=True)

model = Discriminator(img_size, 64, 2, 6)
model.cuda()

for i in model.named_children():
    print(i)

loss_func = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

for e in range(epoch):
    for i, (img, label) in enumerate(img_batch):
        
        img = Variable(img).cuda()
        label = Variable(label).cuda()

        
        output = model(img)

        
        #print(output)
        loss = loss_func(output, label)
        
        optimizer.zero_grad()
        loss.backward()

        optimizer.step()

        if (i+1) % 10 == 0:
            accuracies = compute_accuracy(output, label)
            log = ["{:.2f}".format(acc) for acc in accuracies.data.cpu().numpy()]

            print('{} / {}'.format(e+1, i+1))
            print('Classification Acc {}..!'.format(log))
            print('Loss {}..!'.format(loss))

        if (i+1) % 170 == 0:
            torch.save(model.state_dict(), os.path.join(model_save_dir, '{}_{}_model.pth'.format(e+1, i+1)))
        
