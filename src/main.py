import sys
import time
from Algorithms import *
import Algorithms,PersonHandler
from FileHandler import readArq,readArqCsv,writeArqCsv,testeArqCsv
def main():
    if(len(sys.argv) != 4):
        print("Erro na entrada de dados, entre com: algoritmo ArqEntrada e ArqSaida")
    else:
        algorithm:str = sys.argv[1]
        inputData:list = readArqCsv(sys.argv[2])
        outputData = sys.argv[3]
        ini = time.time()
        data = sortCollection(algorithm,inputData)
        fim = time.time()
        tempo = fim-ini
        print(algorithm,tempo,len(inputData))
        testeArqCsv(tempo,algorithm,len(inputData),sys.argv[3])
                       
        

    #inputName = parseInputFileName(args)
    #outputName = parseOutputFileName(args)
    #A =  readCSV(inputName)
    #initTime = GetCPUTime
    #xyzSort(A)
    #finishTime = GetCpuTime
    #writeCsv(A,outputName)
    #reportTime(A,initTIme,finishTime)
    #end procedure
    return 0

if __name__ == "__main__":
    main()