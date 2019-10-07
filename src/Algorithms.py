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
def insertionsort(lst:list):
    i: int = 2                                                                     #
    while(i<len(lst)):                                                             #
        person = lst[i]                                                            #
        j:int = i-1                                                                #
        #search the true spot of person.
        while(j>0 and (compareTo(person,lst[j-1]) == -1)):           #
            lst[j] = lst[j-1]                                                      #
            j = j - 1                                                              #
        #end while
        lst[j] = person                                                            #
        i = i+1                                                                    #
    #end while
    return lst 
   


'''
    7. quicksort - Cormen
    Worst case - theta(n²)
    Best Practical choice - theta(nlgn)
    based on the divide-and-conquer paradigm
'''

def Partition(lst:list,start:int,end:int):
    end = end-1
    x:int = lst[end]
    i:int = start -1
    for j in range(start,end):
        #lst[j]<= x
        if(compareTo(lst[j],x)!=1):
            i += 1
            lst[i],lst[j] = lst[j],lst[i]
        #end if
    #end for
    lst[i+1],lst[end]=lst[end],lst[i+1]
    return i+1
        

def quicksort(lst:list,start:int,end:int):
    if start < end:
        q = Partition(lst,start,end)
        quicksort(lst,start,end-1)
        quicksort(lst,start+1,end)
    #end if



#heapsort
#Timsort/Introsort/Smoothsort/Patiencesorting
