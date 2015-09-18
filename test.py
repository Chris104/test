def f(x):
    return(3*x*x)
    f()
    
def g(x):
    return (2*x*x*x)
    g()
    
def array (x):
    testarray = ["chris", "adam"]
    return testarray[x]
    array ()
def h(x):
    array=[]
    for n in range(100):
        if (n%2)==0:
            array.append(n+1) 
        else:
            array.append(n)
    return array[x]
    h()

def h1(x) :
    array1= []
    for n in range(100):
        if(n%2)==0:#if n is even 
            array1.append(f(n+1))#append to your array f(n+1) 
        else:
            array1.append(g(n))#if n is odd, append to your array g(n)
    return array1[x]
    h1()
def a():
    sum=0 #defining the sum as 0
    for n in range(100):
      sum=sum+h1(n)#adding the nth element of your array of the sum
    return sum#sum total of the array once the loop has finnished
    a()
def b():
    s="Wed, 29 July, 2015, 16:47:55."
    for n in range(len(s)):#looping across s
        if s[n]==":":#if :is found in the loop
            s=s.replace( ":", ",")#relace : with ,
            print #print the new sentence
    return s
    b()
