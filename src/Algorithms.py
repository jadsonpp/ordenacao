from PersonHandler import *
import time

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
def insertionsort(lst: list):
    i: int = 2                                                                    #
    while(i < len(lst)):                                                             #
        #
        person = lst[i]
        j:  int = i-1                                                                #
        # search the true spot of person.
        #Person < lst[j]
        while(j >= 0 and (compareTo(person, lst[j]) == -1)):           #
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
        #lst[i]<= pivot
        if(compareTo(lst[i], pivot) == -1):
            lower += 1
            lst[lower], lst[i] = lst[i], lst[lower]
        # end if
    # end for
    lst[lower+1], lst[end] = lst[end], lst[lower+1]
    return lower+1


def quicksort(lst: list, start: int, end: int):
    if start < end:
        partition = Partition(lst, start, end)
        quicksort(lst, start, partition-1)
        quicksort(lst, partition+1, end)
    # end if


def heapsort(lst: list):
    buildMaxHeap(lst)
    i = len(lst)-1
    while (i >= 0 ):
        lst[0],lst[i] = lst[i],lst[0]
        i -= 1 
        heapify(lst,i,0)

def buildMaxHeap(lst:list):
    i = (len(lst)//2)
    while(i>=0):
        heapify(lst,len(lst),i)
        i-=1

def heapify(lst:list,tam:int,i:int):
    left = 2 * i 
    right = (2*i) + 1 
    #iMax is the index of the largest num.
    iMax:int = i
    #lst[left] > lst[i]) e esq <= tamanho da lista
    if ((left < tam) and (compareTo(lst[left],lst[iMax]) == 1)):
        iMax = left
    #lst[dir]>lst[max] e dir <= tamanho da lista
    if((right < tam) and (compareTo(lst[right],lst[iMax]) == 1)):
        iMax = right

    if(iMax != i):
        lst[i],lst[iMax] = lst[iMax],lst[i]
        heapify(lst,tam,iMax) 

def mergesort(lst:list):
    if(len(lst) <= 1):
        return lst

    mid = (len(lst))//2
    lstLeft = lst[:mid]
    lstRight = lst[mid:]
    lstLeft = mergesort(lstLeft)
    lstRight = mergesort(lstRight)

    return merge(lstLeft,lstRight)

def merge(lstLeft:list,lstRight:list):
    lstMerge = []
    while (lstLeft != [] and lstRight != []):
        #lstLeft <= lstRight
        if ((compareTo(lstLeft[0],lstRight[0]) != 1)):
            lstMerge.append(lstLeft.pop(0))
        else:
            lstMerge.append(lstRight.pop(0))

    if(lstLeft!=[]):
        while(lstLeft != []):
            lstMerge.append(lstLeft.pop(0))
    if(lstRight != []):
        while(lstRight != []):
            lstMerge.append(lstRight.pop(0)) 

    return lstMerge

# Timsort/Introsort/Smoothsort/Patiencesorting


def sortCollection(algorithm: str,lstData : list ):
    # "Switch case"
    if(algorithm == 'selectionsort'):
        lstData = selectionsort(lstData)
    elif (algorithm == 'insertionsort'):
        lstData = insertionsort(lstData)
    elif(algorithm == 'quicksort'):
        lstData = quicksort(lstData,0,len(lstData)-1)
    elif(algorithm == 'heapsort'):
        lstData = heapsort(lstData)

    elif(algorithm == 'mergesort'):
        lstData = mergesort(lstData)
    
    '''
    else:
        print('Algorithm not found')
        print('Nome de arquivo incorreto, tente: selectsort, insertsort, mergesort, quicksort, heapsort')
    '''
    #showUids(lstData)
    return lstData