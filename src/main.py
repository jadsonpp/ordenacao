import sys
import FileHandler,Algoritms

def main():
    if(len(sys.argv) != 3):
        print("Erro na entrada de dados, entre com: ArqEntrada e ArqSaida")
    else:
        data = FileHandler.readArq(sys.argv[1])
        Algoritms.selectSort(data)
        print(data)

        #print(data[0].showData())

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