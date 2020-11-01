import torch
import torch.nn as nn

a = torch.Tensor([[[[1,2],[3,4]]]])
conv = nn.Conv2d(1,1,1,1,padding=(1,0),bias=True)
print(conv(a))