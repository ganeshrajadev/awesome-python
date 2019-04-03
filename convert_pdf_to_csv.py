#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 11:20:13 2019

@author: Ganesh
"""

from tabula import read_pdf
import pandas as pd

FILE_NAME="" #Ppdf file as input
dest="" #destination csv file name

df= read_pdf(FILE_NAME)
x=df.values
data=pd.DataFrame(data=x[1:,1:],columns=x[0,1:])

data.to_csv(dest,sep=',',encoding="utf-8")