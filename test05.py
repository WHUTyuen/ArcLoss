import torch.nn as nn
import torch.nn.functional as F
import torch

class ArcLoss(nn.Module):

    def __init__(self,feature_dim,cls_dim):
        super().__init__()
        self.W = nn.Parameter(feature_dim,cls_dim)

    def forward(self, feature):
        _W = torch.norm(self.W,dim=0)
        _X = torch.norm(feature,dim=1)
        out = torch.matmul(feature,self.W)
        cosa = out/(_W*_X)
        a = torch.acos(cosa)

        top = torch.exp(_W*_X*torch.cos(a+0.1))
        _top = torch.exp(_W*_X*torch.cos(a))
        bottom = torch.sum(torch.exp(out),dim=1)

        return top/(bottom-_top+top)