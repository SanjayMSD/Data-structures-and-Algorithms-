""" ROOT FINDING METHODS """

""" BISECTION METHOD """

def f(x):
    return(x**2 - 11)

def bisection_method(a, b, tol):
    if (f(a)*f(b) > 0):
        #end function, no root.
        print("No root found.")
    else:
        while ((b - a)/2.0 > tol):
            midpoint = (a + b)/2.0
            if (f(midpoint) == 0):
                return(midpoint) #The midpoint is the x-intercept/root.
            elif (f(a)*f(midpoint) < 0): # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint
        return(midpoint)

answer = bisection_method(-1, 5, 0.0001)
print("Answer:", answer)

""" FALSE POSITION [ REGULAR FALSI ] METHOD """

MAX_ITER = 1000000

def func( x ): 
    return (x * x * x - x * x + 2) 
  
# Prints root of func(x) in interval [a, b] 
def regulaFalsi( a , b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
    c = a # Initialize result 
      
    for i in range(MAX_ITER): 
          
        # Find the point that touches x axis 
        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 
          
        # Check if the above found point is root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 
    print("The value of root is : " , '%.4f' %c) 
    
# Initial values assumed 
a = -200
b = 300
regulaFalsi(a, b) 

""" NEWTON-RAPHSON METHOD """

def func( x ): 
    return x * x * x - x * x + 2
  
# Derivative of the above function  
# which is 3*x^x - 2*x 
def derivFunc( x ): 
    return 3 * x * x - 2 * x 
  
# Function to find the root 
def newtonRaphson( x ): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/derivFunc(x) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
      
    print("The value of the root is : ", 
                             "%.4f"% x) 
  
# Driver program to test above 
x0 = -20 # Initial values assumed 
newtonRaphson(x0) 