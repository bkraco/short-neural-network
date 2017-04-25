import numpy as np
def nonlinear(x, deriv=False):
    if deriv==True:
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
data = np.array([ [0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1] ])
               
data1 = np.array([[0,0,1,1]]).T 

np.random.seed(1)

s=2*np.random.random((3,1)) - 1 

for iter in range(1000):
    i0=data
    i1=nonlinear(np.dot(i0,s))
    i1error=data1-i1
    delta=i1error*nonlinear(i1,True)
    s += np.dot(i0.T,delta)
    print (i1)
    
print (i1)


    
