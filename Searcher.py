import requests #per llegir web
import pandas as pd
import numpy as np

#potenciar-ho
SSTT_DATA = { 'gir': 'girona.csv'}

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
                Linia = (line.split("<td>")[1])[:-6]
                if " (" in line: Linia=Linia.split(" (")[0]
                if " - " in line: Linia=Linia.split(" - ")[0]+str(" ")+Linia.split(" - ")[1]
                #Linia=Linia[1:]
                Llistat.append(Linia)
    x = np.array(Llistat)
    columnes=int(len(Llistat)/9)
    df = pd.DataFrame(np.reshape(x, (columnes,9)),columns=['st','data','n','centre','jor','inici','fi','k','proc'])
    df.index.names = ['num']
    df.to_csv(r'./web.csv', encoding='utf-8', header='true')
    return(df)

def nom_profe2():
    #Llegeix el document qeu ve de la generalitat i tradueix llibre
    f=open("Girona01.txt","r",encoding='utf-8')
    noms = []
    nums = []
    comencar = False
    Professorat=[]
    for line in f:
        if ' 1 ' in line and '*' not in line:
            #Extreure coma de noms i cognoms
            nom=(line.split(" 1 ")[0]).split(", ")[0]+" "+(line.split(" 1 ")[0]).split(", ")[1]
            num= line.split(" 1 ")[1]
            if "." in num: num=num.split(".")[0]+num.split(".")[1]
            a_num = int(num)
            noms.append(nom)
            nums.append(a_num)
            Professorat.append(nom+',1,'+num)
        if ' 2 ' in line and '*' not in line:
            #Extreure coma de noms i cognoms
            nom=(line.split(" 2 ")[0]).split(", ")[0]+" "+(line.split(" 2 ")[0]).split(", ")[1]
            num= line.split(" 2 ")[1]
            if "." in num: num=num.split(".")[0]+num.split(".")[1]
            a_num = int(num)
            noms.append(nom)
            nums.append(a_num)
            Professorat.append(nom+',1,'+num)
    df = pd.DataFrame(noms, nums)
    df.columns = ['noms']
    df.index.name = 'NumOrdre'
    return df

def sstt():
    #tradueix un SSTT segons el seu codi
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
    #tradueix el codi d'assignatura
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
        Noms=nom_profe2()
        Whatdo= input('\nVoleu actualitzar la base de dades?\n').lower()
        #Whatdo='n'
        if Whatdo[0] == 's':
            #prova=['https://antiga.sindicat.net/nomenaments/avui/?data=29/08/2019','https://antiga.sindicat.net/nomenaments/avui/?data=30/08/2019']
            #df = read_list(prova)
            df = read_list(read_web1())
            df = pd.read_csv('web.csv', index_col = 'num')
        else:
            df = pd.read_csv('web.csv', index_col = 'num')
        #Rename columns and types
        df = df.rename(columns = {'k': 'espc'})
        df = df.rename(columns = {'n': 'NumOr'})
        df['NumOr'] = df['NumOr'].astype(int)
        Whatdo= input('\nVoleu veure com estàn les llistes?\n').lower()
        #Whatdo ='n'
        if Whatdo[0] == 's':
            SSTT = sstt()
            ESPEC = assignat()
            print()
            print('Consultem el servei territorial número {} i busquem l especialitat{}'.format(ESPEC,SSTT))
            print(df[(df.espc == ESPEC) & (df.st == SSTT)])
            Whatdo= input('\nComprobar si hi ha probabilitat de nomanament tot l any?\n').lower()
            if Whatdo[0] == 's':
                NumOrdre= 1
                NumOrdre= int(input('\n Quin número de ordre tens?\n'))
                print(type(NumOrdre))
                print('**********')
                print(df[(df.st==SSTT)&(df.espc==ESPEC)&(df.fi=='31/08/2020')&(df.jor ==str(1))][df['NumOr']>30000].tail(40))
                print()
            Whatdo= input('\nVoleu veure llista amb noms?\n').lower()
            if Whatdo[0] == 's':
                Interir_noms = pd.merge(df[(df.st==SSTT)&(df.espc==ESPEC)&(df.fi=='31/08/2020')&(df.jor ==str(1))][df['NumOr']>30000].tail(40), Noms, left_on='NumOr', right_on='NumOrdre')
                print(Interir_noms.drop_duplicates())

        Whatdo= input('\nVoleu saber quins professors trobareu en un institut?\n').lower()
        if Whatdo[0] == 's':
            nom_institut=input('\nQuin institut?\n')
            #print(Noms['30820'])
            Centre_Noms = pd.merge(df[(df.centre==nom_institut)], Noms, left_on='NumOr', right_on='NumOrdre')
            Centre_Noms = Centre_Noms.drop_duplicates()
            print(Centre_Noms[['noms','espc' ,'inici','fi','jor']])

        restart = input('\nVoleu fer alguna gestió més?\n').lower()
        if restart[0] != 's':
            break

if __name__ == "__main__":
	main()
