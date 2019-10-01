

#function that read a file and return a list with the data.
def readArq(arqName):
    lstData: list = []
    with open('./trab2-data/'+arqName,'r') as arq:
        data = arq.readline() 
        while(data!= ''):
            data = arq.readline()
            if(data!= ''):
                #clean the \n
                data = data[:-1] 
                lstData.append(data)
    return lstData 
