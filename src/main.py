import sys
import Algorithms,PersonHandler
from FileHandler import readArq,readArqCsv
def main():
    if(len(sys.argv) != 3):
        print("Erro na entrada de dados, entre com: ArqEntrada e ArqSaida")
    else:
        data = readArqCsv(sys.argv[1])
        #Algorithms.heapsort(data)
        #print('x')
        

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