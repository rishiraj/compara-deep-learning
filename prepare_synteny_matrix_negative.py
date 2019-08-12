import pandas as pd 
import numpy as np 
import os 
import sys
import progressbar
import json
from read_get_gene_seq import read_gene_sequences
from create_synteny_matrix import synteny_matrix

if not os.path.isdir("processed/synteny_matrices"):
    os.mkdir("processed/synteny_matrices")

df=pd.read_hdf("negative_dataset.h5",key="ndf")
for _,row in progressbar.progressbar(df.iterrows()):
    row["homology_species"]=row["homology_species"].lower()

with open("processed/neighbor_genes.json","r") as file:
    lsy=dict(json.load(file))
print(len(lsy))
print("Neighbor Genes Loaded")

a_h=[]
a_h.append(df)
gene_sequences=read_gene_sequences(a_h,lsy,"geneseq","gene_sequences")
print("Gene Sequences Loaded")

n=3
ndir="processed/synteny_matrices/"
nf1="synteny_matrices_global"
nf2="synteny_matrices_local"
nf3="indexes"
synteny_matrices_global,synteny_matrices_local,indexes=synteny_matrix(gene_sequences,df,lsy,n,0)
np.save(ndir+"negative_dataset"+"_"+nf1,synteny_matrices_global)
np.save(ndir+"negative_dataset"+"_"+nf2,synteny_matrices_local)
np.save(ndir+"negative_dataset"+"_"+nf3,indexes)
print("Synteny Matrices Created Successfully :)")