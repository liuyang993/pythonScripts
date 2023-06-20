
#https://www.analyticsvidhya.com/blog/2021/07/understanding-rnn-step-by-step-with-pytorch/


# Input To RNN
# Input data: RNN should have 3 dimensions. 
# (Batch Size, Sequence Length and Input Dimension)

# Batch Size is the number of samples 
# we send to the model at a time. 
# Batch Size是一次送几条数据
# In this example, we have batch size = 2 
# but you can take it 4, 8,16, 32, 64 etc 
# depends on the memory (basically in 2’s power)

# Sequence Length is the length of the sequence of input data 
# (time step:0,1,2…N), 
#Sequence是每一条数据包含多少时间跨度
#  the RNN learn the sequential pattern in the dataset. 
#  Here the grey colour part is sequence length 
#  so our sequence length = 3.

# Suppose you have share market data on a daily basis
# (frequency = 1day) and you want that the network to learn 
# the sequence of 30 days of data. 
# So your sequence length will be 30.

# Input Dimension or Input Size is the number of features 
# or dimensions you are using in your data set. 
# In this case, it is one (Columns/ Features). 
# Suppose you have share market data with the following features: 
# High, Low, Open and Close and you want to predict Close. 
# In this case, you have input dimension = 4: 
# High, Low, Open and Close.
# We will see the input dimension in more detail.
#Input Dimension是input数据包含多少features


import numpy as np

import torch

import torch.nn as nn
from torch.utils.data import Dataset, TensorDataset, DataLoader
from torch.utils.data.dataset import random_split

import matplotlib.pyplot as plt



class MyDaatset(Dataset):
    def __init__(self, input, seq_len):
        self.input = input
        self.seq_len = seq_len
    def __getitem__(self, item):
        return input[item:item + self.seq_len], input[item + self.seq_len]
    def __len__(self):
        return len(self.input) - self.seq_len
    

input = np.arange(1,8).reshape(-1,1)
input = torch.tensor(input, dtype=torch.float)

ds = MyDaatset(input, 3)

# print(ds.input.numpy())
# print(ds.seq_len)
# print(ds.__getitem__(0))
# print(ds.__getitem__(1))

dl = DataLoader(ds, batch_size=2)
for inp, label in dl:
    print(inp.numpy())
    print('############')



############################################################


class RNNModel(torch.nn.Module):
    def __init__(self, input_size, HL_size):
        super(RNNModel, self).__init__()
        self.rnn = torch.nn.RNN(input_size=input_size,
                                hidden_size=Hidden Size(HS),
                                num_layers=number of stacked RNN,
                                bidirectional=True/False,
                                batch_first=True default is False)
        # If you want to use output for next layer then
        self.linear2 = torch.nn.Linear(#Direction * HS , Output_size)
        # If you want to use hidden for next layer then
        self.linear2 = torch.nn.Linear(HS , Output_size)

        def forward(self, input):
            out, hidden_ = self.rnn(input)
            #out: Select which time step data you want for linear layer 
            out = self.linear2(out)