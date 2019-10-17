from PersonHandler import Person,showUids
import csv
import os



#function that read a file and return a list with the data.
def readArq(arqName):
    lstData: list = []
    cwd = os.getcwd()+'/trab2-data'  # Get the current working directory (cwd)
    with open(os.path.join(cwd, arqName),'r') as arq:
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
    cwd = os.getcwd()+'/trab2-data'  # Get the current working directory (cwd)
    with open(os.path.join(cwd, arqName),'r') as arq:
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
    cwd = os.getcwd()+'/trab2-data'  # Get the current working directory (cwd)
    with open(os.path.join(cwd, arqName),'w',newline='') as arq:
        datawriter = csv.writer(arq, delimiter=',')
        for data in datas:
            datawriter.writerow([data.email,data.gender,data.uid,data.birthdate,data.height,data.weight])
    return 0

def testeArqCsv(tempo,algoritmo,tamanho,arqName):
    cwd = os.getcwd()+'/trab2-data-output'  # Get the current working directory (cwd)
    with open(os.path.join(cwd, arqName),'a',newline='') as arq:
        datawriter = csv.writer(arq, delimiter=',')
        datawriter.writerow([algoritmo,tempo,tamanho])
       
    return 0