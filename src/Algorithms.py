from PersonHandler import *
import time
import math

'''
    Worst case - n²
    medium case - n²
    Best case - n²
'''

def selectionsort(lst: list):
    i: int =0                                                                      #1  
    while (i<len(lst)-1):                                                              #
        j:int = i+1                                                                 #
        min:int = i                                                                #
        while (j<len(lst)):                                                          #
            #lst[j] <= min
            if(compareTo(lst[j],lst[min]) == -1):                            #
                min = j                                                            #
            j +=1
        #end while
        if(compareTo(lst[i],lst[min]) != 0):                                                                  #
            lst[i], lst[min] = lst[min],lst[i]                                                 #
        i +=1                                                                      #
    #end while
    return lst


'''
    Cormen - 2.1 Insertionsort
    Worst case - n²
    medium case - n² (worst as the worst case)
    Best case - n
'''
def insertionsort(lst: list,left:int,right:int):
    i: int = left + 1                                                                   #
    while(i < right+1):                                                             #
        #
        person = lst[i]
        j:  int = i-1                                                                #
        # search the true spot of person.
        #Person < lst[j]
        while(j >= left and (compareTo(person, lst[j]) == -1)):           #
            lst[j+1] = lst[j]
            j = j - 1                                                              #
        # end while
        #
        lst[j+1] = person
        i = i+1                                                                    #
    # end while
    
    return lst


'''
    7. quicksort - Cormen
    Worst case - theta(n²)
    Best Practical choice - theta(nlgn)
    based on the divide-and-conquer paradigm
'''

def Partition(lst: list, start: int, end: int):
    pivot: person = lst[end]
    lower: int = start - 1
    for i in range(start, end):
        if(compareTo(lst[i], pivot) == -1):
            lower += 1
            lst[lower], lst[i] = lst[i], lst[lower]
    lst[lower+1], lst[end] = lst[end], lst[lower+1]
    return lower+1


def quicksort(lst: list, start: int, end: int):
    if start < end:
        partition = Partition(lst, start, end)
        quicksort(lst, start, partition-1)
        quicksort(lst, partition+1, end)
    return lst


def heapsort(lst: list):
    buildMaxHeap(lst)
    i = len(lst)-1
    while (i >= 0 ):
        lst[0],lst[i] = lst[i],lst[0]
        i -= 1 
        heapify(lst,i,0)
    return lst

def buildMaxHeap(lst:list):
    i = (len(lst)//2)
    while(i>=0):
        heapify(lst,len(lst),i)
        i-=1
    return lst

def heapify(lst:list,tam:int,i:int):
    left = 2 * i 
    right = (2*i) + 1 
    iMax:int = i
    if ((left < tam) and (compareTo(lst[left],lst[iMax]) == 1)):
        iMax = left
    if((right < tam) and (compareTo(lst[right],lst[iMax]) == 1)):
        iMax = right

    if(iMax != i):
        lst[i],lst[iMax] = lst[iMax],lst[i]
        heapify(lst,tam,iMax) 
    return lst


def mergesort(lst:list,ini:int,meio:int,fim:int):
    
    if len(lst) > 1:

        meio = len(lst)//2

        lstLeft = lst[:meio]
        lstRight = lst[meio:]

        mergesort(lstLeft,0,len(lstLeft)//2,meio-1)
        mergesort(lstRight,meio,meio+(len(lstRight)//2),fim-1)

        i = 0
        j = 0
        k = 0

        while i < len(lstLeft) and j < len(lstRight):

            if ((compareTo(lstLeft[i],lstRight[j]) != 1)):
                lst[k]=lstLeft[i]
                i += 1
            else:
                lst[k]=lstRight[j]
                j += 1
            k += 1

        while i < len(lstLeft):

            lst[k]=lstLeft[i]
            i += 1
            k += 1

        while j < len(lstRight):
            lst[k]=lstRight[j]
            j += 1
            k += 1
    return lst

def introsort(lst:list):
    deepest = math.log2(len(lst))
    nElem = len(lst)
    if(nElem <= 1):
        return
    elif (nElem-1 > deepest):
        heapsort(lst)
    else:
        pivot = Partition(lst,0,nElem-1)
        introsort(lst[:pivot-1])
        introsort(lst[pivot+1:])
    return lst

def minValue(n1:int, n2:int):
    minValue = n1 if n1<n2 else n2         
    return minValue

def timsort(lst:list):  
    tam = len(lst)
    
    for i in range(0,tam,2048):
        insertionsort(lst,i,minValue((i+2047),(tam-1)))

    size:int = 2048    
    while size < tam:

        for left in range(0,tam,2*size):
            mid = left+size-1
            right = minValue((left+2*size-1),(tam-1))

            mergesort(lst,left,mid,right)
        
        size = 2*size
    return lst



# Executa o algoritmo e retorna o tempo gasto.
def sortCollection(algorithm: str,lstData : list ):
    # "Switch case"
    if(algorithm == 'selectionsort'):
        lstData = selectionsort(lstData)
    elif (algorithm == 'insertionsort'):
        lstData = insertionsort(lstData,0,len(lstData)-1)
    elif(algorithm == 'quicksort'):
        lstData = quicksort(lstData,0,len(lstData)-1)
    elif(algorithm == 'heapsort'):
        lstData = heapsort(lstData)
    elif(algorithm == 'introsort'):
        lstData = introsort(lstData)
    elif(algorithm == 'mergesort'):
        meio = len(lstData)//2
        lstData = mergesort(lstData,0,meio,len(lstData)-1)
    elif(algorithm == 'timsort'):
        lstData = timsort(lstData)
    else:
        print('Algorithm not found')
        print('Nome de arquivo incorreto, tente: selectsort, insertsort, mergesort, quicksort, heapsort')        

    return lstData
