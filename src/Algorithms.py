from PersonHandler import compareTo


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


def quicksort(lista,ini,fim):
    if(ini<fim):
        p = particiona(lista,ini,fim)
        quicksort(lista,ini,p-1)
        quicksort(lista,p+1,fim)

def particiona(lista,ini,fim):
    pivot = lista[fim]
    i = ini-1
    for j in range(ini,fim):
        if (compareTo(lista[j],pivot)==-1):
            i = i + 1
            lista[i],lista[j] = lista[j],lista[i]
    if (compareTo(pivot,lista[i+1])==-1):
        lista[i+1],lista[fim] = lista[fim],lista[i+1]
    return i+1
    


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
    # iList = Tamanho da lista, i = index que o buildHeap manda.
    left = 2 * i 
    right = (2*i) + 1 
    iMax:int = i
    #lst[left] > lst[i]) e esq <= tamanho da lista
    #iMax is the index of the largest num.
    if ((left < tam) and (compareTo(lst[left],lst[iMax]) == 1)):
        iMax = left
    #lst[dir]>lst[max] e dir <= tamanho da lista
    if((right < tam) and (compareTo(lst[right],lst[iMax]) == 1)):
        iMax = right

    if(iMax != i):
        lst[i],lst[iMax] = lst[iMax],lst[i]
        heapify(lst,tam,iMax) 

# mergesort
# Timsort/Introsort/Smoothsort/Patiencesorting

# 
def sortCollection(algorithm: str,lstDatas : list ):
    ini = time.time()
    # "Switch case"
    if(algorithm == 'selectionsort'):
        lstDatas = selectionsort(lstDatas)
    elif (algorithm == 'insertionsort'):
        lstDatas = insertionsort(lstDatas)
    elif(algorithm == 'quicksort'):
        lstDatas = quicksort(lstDatas,0,len(lstDatas))
    elif(algorithm == 'heapsort'):
        lstDatas = quicksort(lstDatas)
    '''
        <A SER IMPLEMENTADO>
    elif(algorithm == 'mergesort'):
        lstDatas = mergesort(lstDatas)
    
    else:
        print('Algorithm not found')
        print('Nome de arquivo incorreto, tente: selectsort, insertsort, mergesort, quicksort, heapsort')
    '''
    fim = time.time()
    tempo = fim-ini

    return tempo
    
'''
def mergeSort(lst):

    tam = len(lst)

    if tam > 1:
        meio = tam//2
        lstEsq = lst[:meio]
        lstDir = lst[meio:]

        mergeSort(lstEsq)
        mergeSort(lstDir)

        i = 0
        j = 0
        k = 0
        tamEsq = len(lstEsq)
        tamDir = len(lstDir)
        while i < tamEsq and j < tamDir:
            if lstEsq[i] < lstDir[j]:
                lst[k] = lstEsq[i]
                i += 1
            else:
                lst[k] = lstDir[j]
                j += 1
            k += 1
        while i < tamEsq:
            lst[k] = lstEsq[i]
            i += 1
            k += 1
        while j < tamDir:
            lst[k] = lstDir[j]
            j += 1
            k += 1

def mergesort(lst:list,start:int,end:int):
    if(start < end):
        mid= (start+end)//2
        mergesort(lst,start,mid)
        mergesort(lst,mid+1,end)
        merge(lst,start,mid,end)
    #end mergesort

def merge(lst:list,start:int,mid:int,end:int):
    #separadores
    n = mid - start + 1 #primeira partição
    m = end - mid       #segunda partição
    #Listas
    A1 = lst[:n+1]
    A2 = lst[:m+1]
    #
    for i in range (n):
        A1 = lst[start+i-1]
    #end for
    for j in range (m):
        A2 = lst[mid + j]
    #end for
    i=0
    j=0

    for k in range(start,end):
        #A1[i] <= A2[j]
        if(compareTo(A1[i],A2[j])!= 1):
            lst[k] = A1[i]
            i= int(i) + 1
        #lst[k]==A2[j]
        if(compareTo(lst[k],A2[j])==0):
            j= int(j)+ 1
        #
    #end for


'''