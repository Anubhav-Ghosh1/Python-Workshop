# In[19]:


for i in range(1,15,2):
    
    print(sum)


# In[10]:


for i in range(15,0,-1):
    print(i)


# In[24]:


for i in range(15,0,-1):
    print(i,end = " ")


# How to find factorial a number

# In[37]:


fact = 1
n = int(input("Enter Number: "))
for i in range(1,n+1,1):
    fact = fact * i
    
print("Factorial of " , n ," is ", fact)


# How to find sum of n natural numbers

# In[23]:


sum = 0
n = int(input("Enter Number: "))
for i in range(1,n+1,1):
    sum = sum + i
    
print(sum)


# WAP to print sum of even number

# In[29]:


sum = 0
n = int(input("Enter Number: "))
for i in range(0,n+1,2):
    sum = sum + i
    
print("Sum of even number ",sum)


# WAP to print sum of odd number

# In[ ]:


sum = 1
n = int(input("Enter Number: "))
for i in range(0,n+1,2):
    sum = sum + i
    
print("Sum of even number ",sum)


# Prime number

# In[44]:


n = int(input("Enter Number: "))
count = 0
for i in range(2,n,1):
    if (n%i)==0:
            count = count + 1
if count == 0:
    print("Prime number")
else:
    print("Not a prime number")


# Factor of A number

# In[46]:


n = int(input("Enter Number: "))
count = 0
for i in range(1,n+1,1):
    if (n%i)==0:
            print(i,end = " ")


# Java highest interger save for factorial is a class
# 

# In[ ]:




