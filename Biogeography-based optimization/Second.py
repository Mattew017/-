import BBO as bbo
import BBO1 as bbo1
import benchmarks
import numpy
import math

#Sphere function
def F1(x):
    s=numpy.sum(x**2);
    return s

def F3(x):
    return max(x)
#Ackley Function
def F2(x):
    term1 = 0
    term2 = 0
    for i in range(10):
        #associated with ft1
        term1 = term1 + x[i]*x[i]
        #associated with ft2
        term2 = term2 + math.cos(2*3.14*x[i])


    ft1 = 20 * math.exp(-0.02 * math.sqrt(term1/10))
    ft2 = math.exp(term2/10)
    result = 20 + math.exp(1) - ft1 - ft2
    return round(result,2)

search_params = [F1, 3, -100, 100, 10, 3000]
function = F1
dimention = 30
left_bound = -100
right_bound = 100
pop_size = 100
cont_of_iter = 1000
bbo.BBO(function, left_bound, right_bound, dimention, pop_size, cont_of_iter)

