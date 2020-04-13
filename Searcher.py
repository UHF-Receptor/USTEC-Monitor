import requests #per llegir web
import pandas as pd
import numpy as np
def  read_web1():
    link = "https://antiga.sindicat.net/nomenaments/avui/"
    f = requests.get(link)
    text_file = open("Index.txt", "w+")
    text_file.write(f.text)
    text_file.close()
    Llistat = []
    searchfile = open("Index.txt", "r")
    for line in searchfile:
        if 'http://www.sindicat.net/nomenaments/avui/' in line:
            Llistat.append(line.split('"')[1])
    searchfile.close()
    return Llistat

def read_list(List):
    Llistat = []
    #for dia in List: fer tabulat
    dia = List[3]
    f = requests.get(dia)
    text_file = open("IndexDia.txt", "w")
    text_file.write(f.text)
    text_file.close()
    searchfile = open("IndexDia.txt", "r")
    for line in searchfile:
        if '<td>' in line:
            Llistat.append((line.split("<td>")[1])[:-6])
    x = np.array(Llistat)
    columnes=int(len(Llistat)/9)
    df = pd.DataFrame(np.reshape(x, (columnes,9)),columns=['st','data','n','centre','jor','inici','fi','k','proc'])
    df = df.drop(0)
    print(df)


def main():
    while True:
        read_list(read_web1())
        restart = input('\nVoleu fer alguna gestió més?.\n').lower()
        if restart[0] != 's':
            break

if __name__ == "__main__":
	main()
