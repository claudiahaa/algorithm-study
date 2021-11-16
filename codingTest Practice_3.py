#!/usr/bin/env python
# coding: utf-8

# In[1]:


대기인원 = 14000605
#대기인원 = 1200202


# In[9]:


대기일 = 대기인원 // 1200
대기일


# In[8]:


일년일수 = 0
for i in range (10,0,-1):
    print(2**i)
    일년일수 += 2**i

일년일수        


# In[10]:


대기일 // 일년일수


# In[12]:


남은일수 = 대기일 % 일년일수
남은일수


# In[14]:


월별일수누적값 = 0
월 = 0
for i in range (10,0,-1):
    월별일수누적값 += 2**i
    월 += 1
    if 월별일수누적값 > 남은일수 :
        break
        
월


# In[15]:


월별일수누적값 = 0
월 = 0
for i in range (10,0,-1):
    차감일 = 월별일수누적값
    월별일수누적값 += 2**i
    월 += 1
    if 월별일수누적값 > 남은일수 :
        break
        
월
남은일수 - 차감일


# In[16]:


대기인원 % 1200


# In[17]:


최종남은인원 = 대기인원 % 1200
최종남은인원 // 100+9


# In[18]:


출발분 = [25, 40, 55, 70, 85, 100]
몇분에탈지계산 = 최종남은인원 % 100
for i in 출발분 :
    if i > 몇분에탈지계산 :
        당일출발_분 = 출발분.index(i) * 10
        break
        
당일출발_분        


# In[20]:


출발분 = [25, 40, 55, 70, 85, 100]
몇분에탈지계산 = 24 +1
for i in 출발분 :
    if i > 몇분에탈지계산 :
        당일출발_분 = 출발분.index(i) * 10
        break
        
당일출발_분    


# In[21]:


import datetime

오늘시간 = datetime.datetime.today()
오늘시간


# In[23]:


시간 = 1
분 = 1
f'{시간:0>2}:{분:0>2}'


# In[24]:


'hello world'.zfill(20)


# In[35]:


import datetime

오늘시간 = datetime.datetime.today()
대기인원 = 14000605

def solution(대기인원) :
    일년일수 = 0
    for i in range (10,0,-1):
        일년일수 += 2**i
    년 = (대기인원 // 1200) // 일년일수    
    남은일수 = (대기인원 // 1200)  % 일년일수
    
    월별일수누적값 = 0
    월 = 0
    for i in range (10,0,-1):
        차감일 = 월별일수누적값
        월별일수누적값 += 2**i
        월 += 1
        if 월별일수누적값 > 남은일수 :
            break 
            
    일 = 남은일수 - 차감일       
    
    최종남은인원 = 대기인원 % 1200
    시 = 최종남은인원 // 100+9
    
    출발분 = [25, 40, 55, 70, 85, 100]
    해당시간에남은인원 = 최종남은인원 % 100 + 1
    for i in 출발분 :
        if i > 해당시간에남은인원 :
            분 = 출발분.index(i) * 10
            break
            
    if 최종남은인원 % 100 == 99 :
        시 += 1
        분 = 0
            
    if (오늘시간.minute + 분 > 60):
        분 = (오늘시간.minute + 분)- 60
        시 += 1
            
    return f'{년+2020}년 {월}월 {일}일 {시}시 {분}분 출발 '

solution(대기인원)
