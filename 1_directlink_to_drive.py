# -*- coding: utf-8 -*-
"""directlink.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eUaitPD44oWo9l4Uf2VfK5mN6BViSDOF
"""

import os
from google.colab import drive
drive.mount('/content/drive')
path = '/content/drive/My Drive/Download2'
if not os.path.exists(path):
  os.mkdir(path)
os.chdir(path)
linkz = input("paste your link here")
print(type(linkz))
!wget -c $linkz --no-check-certificate
