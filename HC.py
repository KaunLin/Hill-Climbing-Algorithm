
# coding: utf-8

# <img src = 'https://image.slidesharecdn.com/2localsearch-171231213731/95/ai-local-search-13-638.jpg?cb=1562148628' >
# <img src = 'https://www.researchgate.net/profile/Burak_Eksioglu/publication/221787181/figure/fig1/AS:393982577266688@1470944174043/Hill-climbing-algorithm.png' >

# In[1]:


import sys
import time
import math
import random
import itertools


# In[2]:


#依照搜尋半徑,隨機產生 swap case
#Main idea:利用 shuffle 達到隨機與省略"重複判斷"
def random_swap_case(domain,neighbors_size):
    num = []
    #產生 1~domain 的 list
    temp = [n for n in range(1,domain+1)]
    #Shuffle the list
    random.shuffle(temp)
    
    for i in range(neighbors_size):
        num.append(temp.pop())
   
    return num

#產生隨機順序的初始 sequence
def initial_sequence(num):
    seq = [n for n in range(1,num + 1)]
    random.shuffle(seq)
    
    return seq

#依照該次的 case 交換
def swap_by_case(seq,case,position):
    temp = seq[:]
    
    for i in range(len(case)):
        temp[position[i]] = case[i]
        
    return temp

#因是Symmetic，所以先把各城鎮距離算出來，省下每次重新計算的時間
def calculate_distance_table(dic):
    dx = 0
    dy = 0
    distance_table = []
    for i in range(1,len(dic) + 1):
        temp = [0] * 51
        for j in range(i,len(dic)):
            dx = dic[i][0] - dic[j][0]
            dy = dic[i][1] - dic[j][1]
            temp[j - 1] = math.sqrt(dx**2 + dy**2)
            
        distance_table.append(temp)
        
    return distance_table
            

#計算該 seqence 總路徑長
def sequence_total_distance(seq,distance_table):
    dist = 0
    index1 = 0
    index2 = 0
    
    for i in range(len(seq)):
        if seq[i] > seq[(i + 1) % len(seq)]:
            index1 = seq[(i + 1) % len(seq)] - 1
            index2 = seq[i] - 1
        else:
            index1 = seq[i] - 1
            index2 = seq[(i + 1) % len(seq)] - 1
        
        dist += distance_table[index1][index2]
        #dist += distance_table[seq[i] - 1][seq[(i + 1) % len(seq)] - 1]
        
    return dist

#判斷誰大誰小
def determine(temp,min_seq,distance_table):
    if sequence_total_distance(temp,distance_table) < sequence_total_distance(min_seq,distance_table):
        min_seq = temp[:]
#         print(min_seq, evalu(min_seq,dic))
  
    return min_seq,sequence_total_distance(min_seq,distance_table)

#讀檔案
def readfile(dic):
    with open('eil51.txt') as f:
        r = f.read()
        read_line = r.split('\n')               
        for i in range(len(read_line)):         
            read_element = read_line[i].split()
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        f.close()


# In[3]:


# def Hill_Climming(iter_num,size_of_neighbors,temp_min_seq,temp_minVal,min_seq,minVal,distance_table):
#     global test_average
#     for i in range(iter_num): # iteration iter_num =10000次看看
#         case = random_swap_case(len(seq),size_of_neighbors)
    
#     position =[]
    
#     for j in range(len(case)):
#         position.append(seq.index(case[j]))

#     for permutation in itertools.permutations(case):
#         temp = swap_by_case(seq,permutation,position)
#         temp_min_seq,temp_minVal = determine(temp,temp_min_seq,distance_table)
        
#     min_seq, minVal= determine(temp_min_seq,min_seq,distance_table)
    
#     test_average += minVal


# # 變形:可抽 n 個 Node(n<= City數)
# ### 依序比較n個Node的排列中,是否存在更佳解

# In[4]:


def Hill_Climming(iter_num,size_of_neighbors,temp_min_seq,temp_minVal,min_seq,minVal,distance_table):
    global test_average
    for i in range(iter_num): # iteration iter_num =10000次看看
        case = random_swap_case(len(seq),size_of_neighbors)
    
    position =[]
    
    for j in range(len(case)):
        position.append(seq.index(case[j]))
        
    #依序比較n個Node的排列中,是否存在更佳解
    for permutation in itertools.permutations(case):
        temp = swap_by_case(seq,permutation,position)
        temp_min_seq,temp_minVal = determine(temp,temp_min_seq,distance_table)
        
    min_seq, minVal= determine(temp_min_seq,min_seq,distance_table)
    
    return minVal


# In[5]:


# def Simulated_Annealing(iter_num,size_of_neighbors,temp_min_seq,temp_minVal,min_seq,minVal,distance_table):
#     global test_average
#     for i in range(iter_num)


# In[6]:


global minVal
global min_seq

dic = {}
readfile(dic)

distance_table = []
distance_table = calculate_distance_table(dic)

num_cities = len(dic)

minVal=0
min_seq= initial_sequence(num_cities)
min_dist = 0

temp_min_seq = min_seq
temp_minVal = 0

seq = min_seq

temp = []

import pandas as pd

test_average = 0

iter_num = 1000
size_of_neighbors = 5

result = []

# for i in range(2,size_of_neighbors + 1):
# #     size_of_neighbors += 1
# #     print(size_of_neighbors)
#     #做十組 samples
#     test_average = 0
#     for j in range(10):
#         minVal=0
#         min_seq= initial_sequence(num_cities)
#         min_dist = 0
        
#         temp_min_seq = min_seq
#         temp_minVal = 0
        
#         seq = min_seq
        
#         Hill_Climming(iter_num,i,temp_min_seq,temp_minVal,min_seq,minVal,distance_table)
            
#     test_average /= 10
# #         print(test_average)
    
#     result.append(test_average)
    
for j in range(100):
    minVal=0
    min_seq= initial_sequence(num_cities)
    min_dist = 0
        
    temp_min_seq = min_seq
    temp_minVal = 0
        
    seq = min_seq
        
    temp = Hill_Climming(iter_num,6,temp_min_seq,temp_minVal,min_seq,minVal,distance_table)
            
    result.append(temp)


# In[8]:


pd.Series(result).plot(kind = 'kde')

