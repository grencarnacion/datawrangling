# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:50:40 2019

@author: 2ecea-16
"""

import pandas as pd

data1 = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 'Math':[80, 95, 79]}
Math = pd.DataFrame(data1, columns=['Student', 'Math'])

data2 = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics':[85, 81, 83]}
Elecs = pd.DataFrame(data2, columns=['Student', 'Electronics'])

data3 = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS':[90, 79, 93]}
Geas = pd.DataFrame(data3, columns=['Student', 'GEAS'])

data4 = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT':[93, 89, 88]}
Esat = pd.DataFrame(data4, columns=['Student', 'ESAT'])


data0 = pd.merge(Math, Elecs, how='right', on='Student')
data00 = pd.merge(data0, Geas, how='right', on='Student')
data000 = pd.merge(data00, Esat, how='right', on='Student')



