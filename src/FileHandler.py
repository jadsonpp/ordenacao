import PersonHandler
import csv

#function that read a file and return a list with the data.
def readArq(arqName):
    lstData: list = []
    with open('src/trab2-data/'+arqName,'r') as arq:
        data = arq.readline() 
        while(data!= ''):
            data = arq.readline()
            if(data!= ''):
                #clean the \n
                data = data[:-1]
                #split the list 
                data = data.split(',')
                #Insert the data on person class.
                person = PersonHandler.Person(data[0],data[1],data[2],data[3],data[4],data[5])
                lstData.append(person)
    return lstData 

#function that read a file and return a list with the data.
def readArqCsv(arqName):
    lstData: list = []
    with open('./trab2-data/'+arqName,newline='') as csvFile:
        #Split the csv file
        data = csv.reader(csvFile,delimiter=',')
        #jump the header
        next(data)
        #Transform csv in list.
        data = list(data)
        for row in data:
            #Insert the data on person class.
            person = PersonHandler.Person(data[0],data[1],data[2],data[3],data[4],data[5])
        
            lstData.append(person)    
        #end for
        #print(lstData) 
    
    return lstData 



