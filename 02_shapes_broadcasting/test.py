import torch

x = torch.arange(12)            # shape [12]
print(x.view(3, 4).shape)       # [3, 4]
print(x.reshape(2, 6).shape)    # [2, 6]
print(x.view(3, -1).shape)      # [3, 4]  -1 means "figure it out"

img = torch.rand(3, 28, 28)              # one image: [channels, H, W]
print(img.unsqueeze(0).shape)            # [1, 3, 28, 28]  add a batch dim
print(img.unsqueeze(0).squeeze(0).shape) # [3, 28, 28]     remove it
print(img.permute(1, 2, 0).shape)        # [28, 28, 3]     reorder dims (for matplotlib)