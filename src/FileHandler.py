from PersonHandler import Person,showUids
import csv
import os



#function that read a file and return a list with the data.
def readArq(arqName):
    lstData: list = []
    currentDirectory = os.getcwd()+'/trab2-data'  
    with open(os.path.join(currentDirectory, arqName),'r') as arq:
        data = arq.readline() 
        while(data!= ''):
            data = arq.readline()
            if(data!= ''):
                #clean the \n
                data = data[:-1]
                #split the list 
                data = data.split(',')
                #Insert the data on person class.
                person = Person(data[0],data[1],data[2],data[3],data[4],data[5])
                lstData.append(person)
            #endif
        #end while
    return lstData 

#function that read a file and return a list with the data.
def readArqCsv(arqName):
    lstData: list = []
    currentDirectory = os.getcwd()+'/trab2-data'  
    with open(os.path.join(currentDirectory, arqName),'r') as arq:
        #Split the csv file
        datas = csv.reader(arq,delimiter=',')
        #jump the header
        next(datas)
        for data in datas:
            #Insert the data on person class.
            person = Person(data[0],data[1],data[2],data[3],data[4],data[5])        
            lstData.append(person)    
        #end for 
    #showUids(lstData)
    return lstData 

def writeArqCsv(datas,arqName):
    currentDirectory = os.getcwd()+'/trab2-data'  
    with open(os.path.join(currentDirectory, arqName),'w',newline='') as arq:
        datawriter = csv.writer(arq, delimiter=',')
        datawriter.writerow(['email','gender','uid','birthdate','height','weight'])
        for data in datas:
            datawriter.writerow([data.email,data.gender,data.uid,data.birthdate,data.height,data.weight])
    return 0

def testeArqCsv(tempo,algoritmo,tamanho,arqName):
    currentDirectory = os.getcwd()+'/trab2-data' 
    with open(os.path.join(currentDirectory, arqName),'a',newline='') as arq:
        datawriter = csv.writer(arq, delimiter=',')
        datawriter.writerow([algoritmo,tempo,tamanho])
       
    return 0

def readTimeQuant(arqName):
    listaData = []
    currentDirectory = os.getcwd()+'/trab2-data'  
    with open(os.path.join(currentDirectory, arqName),'r') as arq:
        data = arq.readline() 
        while(data!= ''):
            
            #clean the \n
            data = data[:-1]
            #split the list 
            data = data.split(',')
            print(data)
            lista = [data[2],data[1]]
            
            listaData.append(lista)
            try:
                data = arq.readline()
            except:
                break

            #endif
        #end while
    return listaData 


def calcMMM(data):
    lista = []
    listaaux = []
    potencia = int(data[0][0])
    i = 0
    j = 0
    minimo = 99999999999999
    maximo = -1
    media = 0
    soma = 0
    while(i<len(data)):
        if(potencia==int(data[i][0])):
            soma = soma + float(data[i][1])            
            potencia=int(data[i][0])
            if float(data[i][1])<=minimo:
                minimo = float(data[i][1])
            if float(data[i][1])>=maximo:
                maximo = float(data[i][1])
            j+=1
            i+=1
        else:
            media = soma/j
            listaaux = [potencia,media*1000,minimo*1000,maximo*1000]
            lista.append(listaaux)
            listaaux = []
            soma = 0
            potencia = int(data[i][0])
            j = 0
            minimo = 99999999999
            maximo = -1
            media = 0
    media = soma/j
    listaaux = [potencia,media*1000,minimo*1000,maximo*1000]
    lista.append(listaaux)
    return lista

def writeMMM(datas,arqName):
    currentDirectory = os.getcwd()+'/trab2-data'  
    with open(os.path.join(currentDirectory, arqName),'w',newline='') as arq:
        datawriter = csv.writer(arq, delimiter=',')
        datawriter.writerow(['num','med','min','max'])
        for data in datas:
            datawriter.writerow([data[0],data[1],data[2],data[3]])

    return 0



