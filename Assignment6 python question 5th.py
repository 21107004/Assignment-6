
# In[ ]:


input_string=str(input("enter a hyphen separated sentence: "))

li=list(input_string.split("-"))
li.sort()

print("-".join(li))


