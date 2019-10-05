import PersonHandler

def menorNumIndex(start:int,lst:list):
    menorNum:int = lst[start]
    index:int = start
    pos:int = start+1
    #
    while(pos<len(lst)):
        if(lst[pos]<menorNum):
            menorNum =pos
            index = pos
        pos+=1
    #
    return index

def ordenaInsercao(lst:list):
    i:int = 0
    while(i<len(lst)):
        num:int = lst[i]
        index = menorNumIndex(i,lst)
        lst[i] = lst[index]
        lst[index] = num
        i+=1
    return lst


def selectionsort(a: list):
    i: int =0                                                                      #1  
    while (i<len(a)):                                                              #
        j:int = i                                                                  #
        min:int = a[i]                                                             #
        pos:int = 0                                                                #
        while (j<len(a)):                                                          #
            #a[j] <= min
            if(PersonHandler.compareTo(a[j],min) != 1):                            #
                min = a[j]                                                         #
                pos = j                                                            #
            j +=1                                                                  #
        a[i], a[pos] = a[pos],a[i]                                                 #
        i +=1                                                                      #
    #
    return a


def insertionsort(lst:list):
    i: int = 2                                                                     #
    while(i<len(lst)):                                                             #
        person = lst[i]                                                            #
        j:int = i-1                                                                #
        #search the true spot of person.
        while(j>0 and (PersonHandler.compareTo(person,lst[j-1]) == -1)):           #
            lst[j] = lst[j-1]                                                      #
            j = j - 1                                                              #
        #end while
        lst[j] = person                                                            #
        i = i+1                                                                    #
    #end while
    return lst 
   

#MergeSort
#QuickSort
#HeapSort
#Timsort/Introsort/Smoothsort/Patiencesorting
