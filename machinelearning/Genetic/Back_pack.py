#coding=utf-8

import random
#物品的重量价格
X = {1:[10,15],
     2:[15,25],
     3:[20,35],
     4:[25,45],
     5:[30,55],
     6:[35,70]}

#终止界限
FINISHED_LIMIT = 5
#重量界限
WEIGHT_LIMIT = 80
#染色体长度
CHROMOSOME_SIZE = 6
#筛选次数
SELECT_NUMBER = 4
max_last = 0
diff_last = 10000
#收敛条件，判断退出
def is_finish(fitnesses):
    global max_last
    global diff_last
    max_current = 0
    for v in fitnesses:
        if v[1] > max_current:
            max_current = v[1]
    diff = max_current - max_last
    if diff < FINISHED_LIMIT and diff_last < FINISHED_LIMIT:
        return True
    else:
        diff_last = diff
        max_last = max_current
        return False
#初始染色体状态
def init():
    chromosome_state1 = '100100'
    chromosome_state2 = '101010'
    chromosome_state3 = '010101'
    chromosome_state4 = '101011'
    chromosome_states = [chromosome_state1,
                         chromosome_state2,
                         chromosome_state3,
                         chromosome_state4]
    return chromosome_states
#计算适应度
def fitness(chromosome_states):
    fitnesses = []
    for chromosome_state in chromosome_states:
        value_sum = 0
        weight_sum = 0
        for i,v in enumerate(chromosome_state):
            if int(v) == 1:
                weight_sum += X[i+1][0]
                value_sum += X[i+1][1]
        fitnesses.append([value_sum,weight_sum])
    return fitnesses
#筛选
def filter(chromsome_states,fitnesses):
    #重量超标的直接删除
    index = len(fitnesses) - 1
    while index >= 0:
        index -= 1
        if fitnesses[index][1] > WEIGHT_LIMIT:
            chromsome_states.pop(index)
            fitnesses.pop(index)
    #筛选
    selected_index = [0] * len(chromsome_states)
    for i in range(SELECT_NUMBER):
        j = chromsome_states.index(random.choice(chromsome_states))
        selected_index[j] += 1
    return selected_index
#产生下一代
def crossover(chromsome_states,selected_index):
    chromsome_states_new = []
    index = len(chromsome_states) - 1
    while index >=0 :
        index -= 1
        chromsome_state = chromsome_states.pop(index)
        for i in range(selected_index[index]):
            chromsome_states_x = random.choice(chromsome_states)
            pos = random.choice(range(1,CHROMOSOME_SIZE - 1))
            chromsome_states_new.append(chromsome_state[:pos] + chromsome_states_x[pos:])
        chromsome_states.insert(index,chromsome_state)
    return chromsome_states_new


if __name__ == '__main__':
    chromosome_states = init()
    n = 100
    while n > 0:
        n -= 1
        fitnesses = fitness(chromosome_states)
        if is_finish(fitnesses):
            break
        selected_index = filter(chromosome_states,fitnesses)
        chromosome_states = crossover(chromosome_states,selected_index)
    #return chromosome_states
    print selected_index
    print fitnesses
    print chromosome_states