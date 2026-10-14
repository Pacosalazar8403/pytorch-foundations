import torch

m = torch.ones(3, 4)
row = torch.tensor([1., 2., 3., 4.])     
print((m + row)[0])                      

col = torch.tensor([[10.], [20.], [30.]])  
print((m + col)[:, 0])                     

m + torch.ones(3)
# RuntimeError: The size of tensor a (4) must match the size of tensor b (3)
# at non-singleton dimension 1