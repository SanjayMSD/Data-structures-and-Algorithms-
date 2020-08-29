x=[73,94,9,17,60,67,82,55,1,58]

# SELECTION SORT 
def selection_sort(x):
    max = len(x)
    for j in range(0,max-1): 
        m=x[j]              
        p=j
        for k in range((j+1),max):
            if(x[k] < m):   
                m=x[k]         
                p=k             
        x[p]=x[j]          
        x[j]=m  
    x

selection_sort(x)
x

# BUBBLE SORT 
def bubble_sort(x):
    for i in range(1,(len(x)-1)):
        for j in range(1,(len(x)-i)):
            if(x[j] > x[j+1]):
              temp = x[j]
              x[j] = x[j+1]
              x[j+1] = temp
    x

bubble_sort(x)
x

# INSERTION SORT 
def insertion_sort(x):
    for j in range(2,len(x)):
        key = x[j]
        i = j-1 
        while i>0 and (x[i] > key):
                x[(i+1)] = x[i]
                i = i-1
                x[(i+1)] = key
    x


insertion_sort(x)
x


# QUICK SORT 
def quick_sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)  # Just use the + operator to join lists
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

quick_sort(x)
x
