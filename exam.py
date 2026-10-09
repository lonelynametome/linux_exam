import torch
from torch.backends import cudnn # 若正常则静默

#能够正确返回一串数字，如：90100
b = cudnn.is_available() 
# 若正常返回True
a=torch.tensor(1.)
c = cudnn.is_acceptable(a.cuda()) 
# 若正常返回True
print(torch.backends.cudnn.version(),b,c)