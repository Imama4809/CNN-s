import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
import math


# def attention(query, key, value):
#     d_k = query.size(-1)
#     kq_pair = torch.matmul(query, key.transpose(-2,-1)) / math.sqrt(d_k)

x = torch.randn(2, 4)
print(x)
x.transpose(-2,-1)
print(x)