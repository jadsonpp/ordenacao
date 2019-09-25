

#function that read a file and return a list with the data.
def readArq(arqName):
    lstData: list = []
    with open('./trab2-data/'+arqName,'r') as arq:
        data = arq.readline() 
        while(data!= ''):
            data = arq.readline()
            if(data!= ''):
                lstData.append(data)
    return lstData 
