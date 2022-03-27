#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from english_words import english_words_lower_alpha_set
five_digit_word=[]
for word in english_words_lower_alpha_set:
    if len(word)==5:
        five_digit_word.append(word)
#print(len(a))


# In[2]:


answer=random.sample(five_digit_word,1)
fanswer=answer[0]
#print(fanswer)


# In[4]:


n=0
while n<5:
    a=input("Enter a 5 letter word or q to quit:" )
    if a.lower()=='q':
        break
    elif a.lower()==fanswer:
        print("CORRECT!")
        break
    else:
        j=0
        b=[]
        c=[]
        for i in a.lower():
            if i==fanswer[j]:
                b.append(i)
            elif i in fanswer:
                c.append(i)
            j+=1
        print(b,"is in correct place")
        print(c,"should be rearranged")
        if len(a)!=5:
            n=n
            print("Input should be 5 letters")
            a=input("Enter a 5 letter word or q to quit:")
        n+=1

if a.lower()!=fanswer:
    print("Correct Answer is",fanswer.upper())


# In[ ]:





# In[ ]:




