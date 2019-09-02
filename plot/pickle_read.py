# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:48:11 2019

@author: olive
"""

import pickle

with open('E:\\NUS\\Research\\skeleton-based-action-recognition\\AS-GCN\\data\\nturgb_d\\xsub\\val_label.pkl','rb') as f:
    y = pickle.load(f)
    z = y