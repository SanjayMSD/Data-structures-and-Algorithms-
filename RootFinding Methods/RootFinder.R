# ROOT FINDING METHODS :- 

## BISECTION METHOD 

## WAY : 1

f = function(x){
  return (x**2 - 11)
}

bisection_method = function(a, b, tol){
  if (f(a)*f(b) > 0){
    #end function, no root.
    print("No root found.")
  }else{
    while (((b - a)/2) > tol){
      midpoint = (a + b)/2.0
      if (f(midpoint) == 0){
        return (midpoint)#The midpoint is the x-intercept/root.
      }else if (f(a)*f(midpoint) < 0){ # Increasing but below 0 case
        b = midpoint
      }else{
        a = midpoint
      }
      
    }
    return (midpoint)
  }
}


answer = bisection_method(-1, 5, 0.0001)
answer
print("Answer:", answer)

## WAY : 2

f = function(x){
  return (x*x*x - x*x + 2)
  }

# Prints root of func(x) 
# with error of EPSILON 
bisection_method = function(a,b){
  if ((f(a)*f(b)) >= 0){
    print("You have not assumed right a and b\n")
  }
  c = a 
  while ((b-a) >= 0.01){
    # Find middle point 
    c = (a+b)/2
    # Check if middle point is root 
    if (f(c) == 0.0){
      break
    } 
    # Decide the side to repeat the steps 
    if (f(c)*f(a) < 0){
      b = c 
    }
    else{
      a = c
    } 
  }
  print("The value of root is : ",c)
}


a =-200
b = 300

f(a)
f(b)

bisection(a, b) 






## false position [ Regular falsi method ]

MAX_ITER = 1000000

func = function(x){ 
  return ((x * x * x) - (x * x )+ 2)} 

# Prints root of func(x) in interval [a, b] 

regulaFalsi = function(a,b){
  if (func(a) * func(b) >= 0){
    print("You have not assumed right a and b") 
    return (-1)}

  c = a # Initialize result 

  for (i in (1:MAX_ITER)){
    
    # Find the point that touches x axis 
    c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 

    # Check if the above found point is root 
    if (func(c) == 0){ 
      break
      }

    # Decide the side to repeat the steps 
    else if (func(c)*func(a) < 0){ 
      b = c }
    else{ 
      a = c }
  
  }
  print(c) 
}

# Initial values assumed 
a = -200
b = 300
regulaFalsi(a, b) 

## NEWTON-RAPHSON METHOD :-

func = function(x){ 
  return ((x * x * x) - (x * x) + 2)}

# Derivative of the above function  
# which is 3*x^x - 2*x 
derivFunc = function(x){
  return ((3 * x * x)-(2 * x))} 

# Function to find the root 
newton_raphson = function(x){
  h = (func(x) / derivFunc(x))
  while (abs(h) >= 0.0001){
    h = (func(x)/derivFunc(x)) 
    # x(i+1) = x(i) - f(x) / f'(x) 
    x = (x - h)
  }
  print(x)
}

  
# Driver program to test above 
x0 = -20 # Initial values assumed 
newton_raphson(x0) 
