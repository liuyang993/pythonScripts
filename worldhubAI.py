import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
X = np.array([  [80,60,30,19,1,60,80,40,19,1,20,100,30,19,1],
                [100,0,30,20,1,60,80,40,20,1,20,100,30,20,1],
                [40,80,30,2,1,50,50,40,2,1,20,100,30,2,1] ])

X = nonlin(X)
#print(X)          
    
# output dataset            
y = np.array([[-1000,500,600]]).T
y = nonlin(y)

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((15,1)) - 1
#print (syn0)
#syn0 =  np.array([0.1,0.2,0.3,0.4,0.1,0.1,0.2,0.3,0.4,0.1,0.1,0.2,0.3,0.4,0.1,0.1,0.2,0.3,0.4,0.1,0.1,0.2,0.3,0.4,0.1])

for iter in range(10000):

    # forward propagation
    l0 = X
    #print(np.dot(l0,syn0))
    l1 = nonlin(np.dot(l0,syn0))
    #l1 = np.dot(l0,syn0)

    # how much did we miss?
    l1_error = y - l1
    #print (l1)

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print ("Output After Training:")
print (l1)
print ("expected result:")
print (y)
print ("final quanzhong:")
print (syn0)


1# code sample from http://iamtrask.github.io/2015/07/12/basic-python-network/ 

