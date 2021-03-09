import random
import math
import time
pop_size = 30
count_of_iter = 100000
mutation_probability = 0.01
accuracy = 0.01

# Beale Function
def Beale(x):
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0]+x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2
#Ackley N. 2 Function
def Ackley(x):
    return -200*math.exp(-0.2*math.sqrt(x[0]**2 + x[1]**2))



def F1(x):
    result = 0
    for i in range(len(x)):
        result += x[i]**2
    return result


def F2(x):
    return max([abs(a) for a in x])


def F3(x):
    summa = 0
    multi = 1
    for a in x:
        summa += abs(a)
        multi *= abs(a)
    return summa + multi 


def F4(x):
    multi = 1
    summa = 0
    i = 1
    for a in x:
        summa += a**2
        multi *= math.cos(a/math.sqrt(i))
    return summa/4000 - multi + 1
    

def BBO(F, search_params):
    left_bound = search_params[0]
    right_bound = search_params[1]
    dimention = search_params[2]
    true_value = search_params[3]
    Population = [[random.uniform(left_bound, right_bound) for _ in range(dimention)] for _ in range(pop_size)]
    
    mu = [(pop_size + 1 - i)/(pop_size + 1)for i in range(pop_size)]  #иммиграция
    lambd = [1 - mu[i] for i in range(pop_size)]  #эммиграция
    
    Population.sort(key = F)
    values = [F(x) for x in Population]
    print(f'First Values {values[:5]}')
    generation = 0
    Island = [[0 for _ in range(dimention)] for _ in range(pop_size)]   #Временные острова
    #for k in range(count_of_iter):
    while abs(abs(values[0]) - abs(true_value)) > accuracy:

        #Операция миграции
        for i in range(pop_size):
            for j in range(dimention):
                if random.random() < lambd[i]:  #Migration
                    RandomNum = random.random()*sum(mu)
                    Select = mu[0]
                    SelectIndex = 0
                    while (RandomNum > Select) and (SelectIndex < pop_size - 1):
                        SelectIndex += 1
                        Select += mu[SelectIndex]
                    Island[i][j] = Population[SelectIndex][j]
                else:
                    Island[i][j] = Population[i][j]

        #Операция мутации
        for i in range(pop_size):
            for j in range(dimention):
                if mutation_probability > random.random():
                    Island[i][j] = random.uniform(left_bound, right_bound)

        # Замена старых островов на полученные
        for i in range(pop_size):
            for j in range(dimention):
                Population[i][j] = Island[i][j] 

        #Сортировка по возрастанию F(X)
        Population.sort(key = F)
        values = [F(x) for x in Population]                           
        generation += 1
        #print(f'Generation {generation} values {values[:5]}')
        #print(f' Generation {generation} answer params {Population[:5]}')
        if generation % 1000 == 0:
            print(f'generation {generation} value {values[0]}')
    # первые 5
    print(f'Total count of generations is {generation}' )
    print(f'Answer Values {values[0]}')
    print(f'Answer Params {Population[0]}')

if __name__ == '__main__':
    search_params = {'F1':[-100, 100, 30, 0], 'F2': [-100, 100, 30, 0],
                     'F3': [-10, 10, 30, 0], 'Ackley': [-100, 100, 2, -200],
                     'Beale': [-4.5, 4.5, 2, 0], 'F4': [-600, 600, 30, 0]}
    start_time = time.time()
    BBO(Beale, search_params['Beale'])
    print(time.time() - start_time)
