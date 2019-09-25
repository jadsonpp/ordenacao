import sys
import FileHandler

def main():
    if(len(sys.argv) != 3):
        print("Erro na entrada de dados, entre com: ArqEntrada e ArqSaida")
    else:
        print(FileHandler.readArq(sys.argv[1]))
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