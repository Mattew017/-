import random
import math
import time


def BBO(F, count_of_iter, pop_size, mutation_probability, search_params):
    left_bound = search_params[0]
    right_bound = search_params[1]
    dimention = search_params[2]
    Population = [[random.uniform(left_bound, right_bound) for _ in range(dimention)] for _ in range(pop_size)]
    
    mu = [(pop_size + 1 - i)/(pop_size + 1)for i in range(pop_size)]  #иммиграция
    lambd = [1 - mu[i] for i in range(pop_size)]  #эммиграция

    Population.sort(key = F)
    values = [F(x) for x in Population]
    Island = [[0 for _ in range(dimention)] for _ in range(pop_size)]   #Временные острова
    for k in range(count_of_iter):

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

    # первые 3 лучших значения
    print(f'Total count of generations is {generation}' )
    print(f'Answer Values {values[0]}')
    print(f'Best Population params {Population[0]}')



if __name__ == '__main__':
    pass
