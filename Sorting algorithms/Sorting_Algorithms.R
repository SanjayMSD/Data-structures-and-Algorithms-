# testing the selectionsort function
#x <-sample(1:100,10)
x=c(73,94,9,17,60,67,82,55,1,58)






# SELECTION SORTING :-

selection_sort <- function (x,ascending = TRUE) {
  max <- length(x)
  if (ascending) {
    for (j in 1:(max-1)){ # j = 1 to 9
      m=x[j]              # here m=73
      p=j
      for(k in (j+1):max) { # k = 2 to 10
        if(x[k] < m) {    # here 73<9 (wrong)
          m=x[k]          # no swap , m is changed to 9 
          p=k             # continue this for all k 
         # print(m)
         # print(x[k])
         #  print(x)
        }
        # print(x[j])
        # print(x[k])
        # print(x)## end if
      } ## end for k
      x[p]=x[j]           # value 1 index 9 p=9 x[9]=x[1].
      x[j]=m              # now m = x[9] ==> x[1]=x[9]==> 73 and 1 changed. 
      # print(x[j])
      # print(x[k])
      # print(x)
    } ## end for j
  }
  else {
    for (j in 1:(max-1)){ # j = 1 to 9
    m=x[j]              # here m=73
    p=j
    for(k in (j+1):max) { # k = 2 to 10
      if(x[k] < m) {    # here 73<9 (wrong)
        m=x[k]          # no swap , m is changed to 9 
        p=k             # continue this for all k 
        # print(m)
        # print(x[k])
        #  print(x)
      }
      # print(x[j])
      # print(x[k])
      # print(x)## end if
    } ## end for k
    x[p]=x[j]           # value 1 index 9 p=9 x[9]=x[1].
    x[j]=m              # now m = x[9] ==> x[1]=x[9]==> 73 and 1 changed. 
    # print(x[j])
    # print(x[k])
    # print(x)
  }}## end ascending if
  x
}

example <- selection_sort(x)
example




# BUBBLE SORTING :-

bubble_sort=function(x){
    for(i in 1:(length(x)-1)){
      for(j in 1:(length(x)-i)){
        if(x[j] > x[j+1]){
          temp = x[j]
          x[j] = x[j+1]
          x[j+1] = temp
        }
      }
    }
  x
}

x=c(73,94,9,17,60)  # ,67,82,55,1,58)
bubble_sort(x)



# INSERTION SORT :-

insertion_sort=function(x){
  for (j in 2:length(x)){
    key = x[j]
    i = j-1 
    while (i>0 && x[i] > key){
      x[(i+1)] = x[i]
      i = i-1
    }
    x[(i+1)] = key
  }
  x
}

insertion_sort(x)

# Quick sort :-
quicksort = function(arr){
  # Pick a number at random.
  mid <- sample(arr, 1)
  
  # Place-holders for left and right values.
  left <- c()
  right <- c()
  
  # Move all the smaller values to the left, bigger values to the right.
  lapply(arr[arr != mid], function(d){
    if (d < mid){
      left <<- c(left, d)
    }
    else{
      right <<- c(right, d)
      }})
  if (length(left) > 1){
    left <- quickSort(left)
    }
  if (length(right) > 1){
    right <- quickSort(right)
  }
  # Finally, return the sorted values.
  c(left, mid, right)
}

quicksort(x)
