import sys
import time
import Algorithms,PersonHandler
from FileHandler import readArq,readArqCsv,writeArqCsv
def main():
    if(len(sys.argv) != 3):
        print("Erro na entrada de dados, entre com: ArqEntrada e ArqSaida")
    else:
        
        data = readArq(sys.argv[1])
        ini = time.time()
        Algorithms.quicksort(data,0,len(data))
        fim = time.time()
        tempo = fim-ini
        print('quicksort    ',len(data),'    ',tempo,'\n')
        writeArqCsv(sys.argv[2],'quicksort',len(data),tempo)
        

        if 'selectsort' in sys.argv[2]:
            ini = time.time()
            Algorithms.selectionsort(data)
            fim = time.time()
            tempo = fim-ini
            print('selectionsort    ',len(data),'    ',tempo,'\n')
            print("Criando arquivo de saída...\n")
            writeArqCsv(data,sys.argv[2])
            print("Arquivo de saída criado!\n")


        elif 'insertsort' in sys.argv[2]:
            ini = time.time()
            Algorithms.heapsort(data)
            fim = time.time()
            tempo = fim-ini
            print('insertsort    ',len(data),'    ',tempo,'\n')
            print("Criando arquivo de saída...\n")
            writeArqCsv(data,sys.argv[2])
            print("Arquivo de saída criado!\n")


        elif 'mergesort' in sys.argv[2]:
            ini = time.time()
            Algorithms.mergesort(data)
            fim = time.time()
            tempo = fim-ini
            print('mergesort    ',len(data),'    ',tempo,'\n')
            print("Criando arquivo de saída...\n")
            writeArqCsv(data,sys.argv[2])
            print("Arquivo de saída criado!\n")


        elif 'quicksort' in sys.argv[2]:
            ini = time.time()
            Algorithms.quicksort(data,0,len(data)-1)
            fim = time.time()
            tempo = fim-ini
            print('quicksort    ',len(data),'    ',tempo,'\n')
            print("Criando arquivo de saída...\n")
            writeArqCsv(data,sys.argv[2])
            print("Arquivo de saída criado!\n")


        elif 'heapsort' in sys.argv[2]:
            ini = time.time()
            Algorithms.heapsort(data)
            fim = time.time()
            tempo = fim-ini
            print('heapsort    ',len(data),'    ',tempo,'\n',data[0])
            print("Criando arquivo de saída...\n")
            writeArqCsv(data,sys.argv[2])
            print("Arquivo de saída criado!\n")

            
        else:
            print('Nome de arquivo incorreto, tente: selectsort, insertsort, mergesort, quicksort, heapsort')
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