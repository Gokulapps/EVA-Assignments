# -*- coding: utf-8 -*-
"""model_cifar10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oC4a7NZyfaKsMfBJSjc2yCRdZexEoEiS
"""

import torch 
import torchvision 
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim 
import torch.autograd as grad
import matplotlib.pyplot as plt
import numpy as np
import warnings
from torch.optim.lr_scheduler import StepLR
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader
from torchsummary import summary
warnings.filterwarnings("ignore")


class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        # Convolution Block 1
        self.convblock1 = nn.Sequential(
                       nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, padding=1), # 32*32 --> 32*32 || RF = 3 
                       nn.BatchNorm2d(8),
                       nn.ReLU(),
                       nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1), # 32*32 --> 32*32 || RF = 5
                       nn.BatchNorm2d(16),
                       nn.ReLU(),
                       nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1), # 32*32 --> 32*32 || RF = 7
                       nn.BatchNorm2d(32),
                       nn.ReLU(),
                       nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1), # 32*32 --> 32*32 || RF = 9
                       nn.BatchNorm2d(64),
                       nn.ReLU(),
                       nn.Dropout2d(0.1),
                       nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, dilation=2), # 32*32 --> 28*28 || RF = 13
                       nn.BatchNorm2d(64),
                       nn.ReLU(),
                       nn.Dropout2d(0.1),
        )

        # Convolution Block 2
        self.convblock2 = nn.Sequential(
                            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=5, groups=64), # Depthwise seperable conv
                            nn.Conv2d(in_channels=64, out_channels=8, kernel_size=1), # Pointwise Convolution 
                            nn.BatchNorm2d(8),
                            nn.ReLU()
        )                   # 28*28 --> 24*24 || RF = 15

        # Convolution Block 3 
        self.convblock3 = nn.Sequential(
                            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1), # 24*24 --> 24*24 || RF = 17
                            nn.BatchNorm2d(16),
                            nn.ReLU(),
                            nn.Conv2d(in_channels=16, out_channels=24, kernel_size=3, padding=1), # 24*24 --> 24*24 || RF = 19
                            nn.BatchNorm2d(24),
                            nn.ReLU(),
                            nn.Conv2d(in_channels=24, out_channels=32, kernel_size=3, padding=1), # 24*24 --> 24*24 || RF = 21
                            nn.BatchNorm2d(32),
                            nn.ReLU(),
                            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, dilation=2), # 24*24 --> 20*20 || RF = 25
                            nn.BatchNorm2d(64),
                            nn.ReLU(),
                            nn.Dropout2d(0.1)              
        )

        # Convolution Block 4
        self.convblock4 = nn.Sequential(
                              nn.Conv2d(in_channels=64, out_channels=64, kernel_size=5, stride=2, padding=1), # 20*20 --> 9*9 || RF = 29
                              nn.Conv2d(in_channels=64, out_channels=10, kernel_size=1) # 9*9*64 --> 9*9*10 || RF = 29
        )

        # Output Block 
        self.output_gap = nn.AvgPool2d(9) # 9*9 --> 1*1 || RF = 45
         
    def forward(self, tensor):
        x = tensor
        x = self.convblock1(x)
        x = self.convblock2(x)
        x = self.convblock3(x)
        x = self.convblock4(x)
        x = self.output_gap(x)
        x = x.view(-1, 10)
        
        return F.log_softmax(x, dim=1)
    
    def network_architecture(self):
      use_cuda = torch.cuda.is_available()
      device = torch.device('cuda' if use_cuda else 'cpu')
      sample = Network().to(device)
      return summary(sample, input_size = (3, 32, 32))