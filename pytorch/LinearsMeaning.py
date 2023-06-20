import numpy as np
import torch
import torch.nn as nn

m = nn.Linear(3, 4)
input = torch.randn(2, 3)
print(input)

output = m(input)
print(output)
