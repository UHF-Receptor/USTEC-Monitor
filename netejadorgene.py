import pandas as pd
import numpy as np

def Professorat():
    f=open("Girona01.csv","r",encoding='utf-8')
    comencar = False
    Professorat=[]
    for line in f:
        if ' 1 ' in line:
            #Extreure coma de noms i cognoms
            nom=(line.split(" 1 ")[0]).split(", ")[0]+" "+(line.split(" 1 ")[0]).split(", ")[1]
            num= line.split(" 1 ")[1]
            if "." in num: num=num.split(".")[0]+num.split(".")[1]
            Professorat.append(nom+',1,'+num)
        if ' 2 ' in line:
            #Extreure coma de noms i cognoms
            nom=(line.split(" 2 ")[0]).split(", ")[0]+" "+(line.split(" 2 ")[0]).split(", ")[1]
            num= line.split(" 2 ")[1]
            if "." in num: num=num.split(".")[0]+num.split(".")[1]
            Professorat.append(nom+',1,'+num)
    for a in Professorat:
        print(a)
