# ReLU(x)=max(0,x)
#


import numpy as np
import torch
import torch.nn as nn

m = nn.ReLU()
input = torch.randn(2).unsqueeze(0)
print(input)
output = torch.cat((m(input), m(-input)))

print(output)