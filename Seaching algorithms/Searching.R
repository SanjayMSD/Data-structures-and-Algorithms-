# Searching algorithms :-

# Linear Search :-

x = c(23,34,53,657231,756,89,66,4,3,1)
y=readline("Enter any number : ")

linear_search = function (X,y){
  for(i in 1:length(x)){
    if (y==x[i]){
      print('Given')
      print(y)
      print('is at')
      print(i)
      print('th position')
    }
  }
  print('Given element is not in given list')
}

linear_search(x,y)


# BINARY SEARCH :-

binary_search = function(X,start,end,y){
  if (end >= start){ 
    mid = (end + start)/ 2
    
    if (mid == y){
      return (mid) 
    }
    # If element is smaller than mid, then it can only 
    # be present in left subarray 
    else if (mid > y){ 
      return (binary_search(X,start, mid - 1, y))
      }
    # Else the element can only be present in right subarray 
    else{ 
      return (binary_search(X, mid + 1, end, y))
    }
  }
  else{
    # Element is not present in the array 
    return (-1)
  
    }  
  }

X = c(111,222,333,444,555,666,777,888)

result = binary_search(X,0,max(X),y=21)

if (result != -1){ 
  print("Element is present at index", str(result)) 
}else 
  { 
  print("Element is not present in array") 
  }
