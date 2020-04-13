import requests #per llegir web
def  read_web1():
    link = "https://antiga.sindicat.net/nomenaments/avui/"
    f = requests.get(link)
    text_file = open("Index.txt", "w")
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
    print(List[0])
    f = requests.get(link)
    text_file = open("IndexDia.txt", "w")
    text_file.write(f.text)
    text_file.close()
    Llistat = []
    searchfile = open("IndexDia.txt", "r")
    for line in searchfile:
        if 'http://www.sindicat.net/nomenaments/avui/' in line:
            Llistat.append(line.split('"')[1])
    searchfile.close()
    return Llistat






def main():
    read_list(read_web1())
    if




if __name__ == "__main__":
	main()
