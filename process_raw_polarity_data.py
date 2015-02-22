# -*- coding: utf-8 -*-

import os,sys,glob
import pandas as pd

POS_DIR = 'data/pos/*.txt'
NEG_DIR = 'data/neg/*.txt'


positive_files = glob.glob(POS_DIR)
negative_files = glob.glob(NEG_DIR)


results = []
index = 1
for f in positive_files:
	results.append({
		'label' : "P",
		'text' : open(f).read(),
	}) 
	
for f in negative_files:
	results.append({
		'label' : "N",
		'text' : open(f).read(),
	}) 
	
df = pd.DataFrame(results).head()
df.to_csv("data/data.csv")
print("Outputted file: data/data.csv ")