import torch.nn as nn
import torch


class swish(nn.Module):
    def forward(self, x):
        return x * torch.sigmoid(x)
#
#
