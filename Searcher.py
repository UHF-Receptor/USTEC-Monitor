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
    for dia in List:
        #dia = List[3]
        f = requests.get(dia)
        text_file = open("IndexDia.txt", "w")
        text_file.write(f.text)
        text_file.close()
        searchfile = open("IndexDia.txt", "r")
        comencar = False
        for line in searchfile:
            if '</tr>' in line:
                comencar = True
            if '<td>' in line and comencar:
                Llistat.append((line.split("<td>")[1])[:-6])
    x = np.array(Llistat)
    columnes=int(len(Llistat)/9)
    df = pd.DataFrame(np.reshape(x, (columnes,9)),columns=['st','data','n','centre','jor','inici','fi','k','proc'])
    df.to_csv(r'./web.csv', encoding='utf-8', header='true')
    return df

def profe_llistat():
    profe = pd.read_csv("professors.csv")
    return(profe)

def sstt():
    print('Consorci Barcelona, Barcelona Comarques, Baix Llobregat, Vallès Occidental, Maresme Vallès Or., Catalunya Central, Girona, Lleida, Tarragona, Terres de lEbre')
    print()
    SSTTn= 0
    while SSTTn== 0:
        SSTT= input('\nQuin servei territorial?\n').lower()
        if SSTT[:3] == 'con': SSTTn = 1
        if SSTT[:3] == 'bar': SSTTn = 2
        if SSTT[:3] == 'bai': SSTTn = 3
        if SSTT[:3] == 'val': SSTTn = 4
        if SSTT[:3] == 'mar': SSTTn = 5
        if SSTT[:3] == 'cat': SSTTn = 6
        if SSTT[:3] == 'gir': SSTTn = 17
        if SSTT[:3] == 'lle': SSTTn = 25
        if SSTT[:3] == 'tar': SSTTn = 43
        if SSTT[:3] == 'ter': SSTTn = 44
    return SSTTn

def assignat():
    assign = "pastanaga"
    totes = ['133','134','135','136','137','138','190','192','193','195','198','501','502','503','504','505','506','507','508','509','510','511','512','513','514','515','516','517','518','519','520','521','522','523','524','525','601','602','603','604','605','606','607','608','609','610','611','612','613','614','615','616','617','618','619','620','621','622','623','624','625','626','627','628','629','701','702','703','704','705','706','707','708','709','710','711','712','713','714','715','716','717','718','719','720','721','722','723','725','801','802','803','804','806','807','808','809','810','811','812','813','814','815','816','817','818','819','820','821','AL','ALL','AN','AR','CLA','CN','DI','ECO','EES','EF','FI','FQ','FR','GE','INF','IT','LC','LE','MA','MU','PAN','PEF','PFR','PMU','PRI','PSI','SCO','TEC']
    while True:
        assign= input('\nQuina assignatura?\n').upper()
        if assign[:2] in totes:
            assign=assign[:2]
            break
            assign=assign[:2]
        if assign[:3] in totes:
            assign=assign[:3]
            break
    return assign

def main():
    while True:
        Whatdo= input('\nVoleu actualitzar la base de dades?\n').lower()
        if Whatdo[0] == 's':
            #prova=['https://antiga.sindicat.net/nomenaments/avui/?data=09/03/2020','https://antiga.sindicat.net/nomenaments/avui/?data=11/03/2020']
            #df = read_list(prova)
            df = read_list(read_web1())
        else:
            df = pd.read_csv('web.csv')
        #Filter by SSTT and Materia
        Whatdo= input('\nVoleu veure com estàn les llistes?\n').lower()
        if Whatdo[0] == 's':
            SSTT = sstt()
            ESPEC = assignat()
            print('**********')
            print(df.loc[(df.st==SSTT)&(df.k==ESPEC)])
            Whatdo= input('\nComprobar si hi ha probabilitat de nomanament tot l any?\n').lower()
            if Whatdo[0] == 's':
                print('**********')
                print(df.loc[(df.st==SSTT)&(df.k==ESPEC)&(df.fi=='31/08/2020')&(df.n>30820)].tail(40))
        Whatdo= input('\nNo sé què preguntar?\n').lower()
        if Whatdo[0] == 's':
            print('Jo tampoc')

        restart = input('\nVoleu fer alguna gestió més?\n').lower()
        if restart[0] != 's':
            break

if __name__ == "__main__":
	main()
