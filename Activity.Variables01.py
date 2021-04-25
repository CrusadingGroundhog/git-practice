#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Variables


# In[3]:


subject = None


# In[4]:


subject = "Programmers"


# In[5]:


first_name = ""


# In[6]:


first_name = "Ada"


# In[7]:


last_name = "Lovelace"


# In[9]:


full_name = "f{first_name} {last_name}"


# In[35]:


profession = "Computer Programmer"


# In[12]:


known_for = "First Computer Programmer" 


# In[13]:


first_algorithm = "Analytical Engine"


# In[16]:


city_location = "London"


# In[17]:


country_location = "England"


# In[18]:


nationality = "British"


# In[ ]:





# In[19]:


birth_year = 1815


# In[21]:


death_year = 1852


# In[25]:


age_at_passing = (death_year - birth_year)


# In[26]:


age_at_passing


# In[27]:


year_of_publish = 1842


# In[32]:


print (f"First Name: {first_name}")


# In[33]:


print (f"Last Name: {last_name}")


# In[36]:


print (f"Profession: {profession}")


# In[39]:


print (f"Birth Year: {birth_year}")


# In[43]:


statement_one = f"{subject}: {first_name} {last_name} is a {nationality} {profession} born in {birth_year}."
print(statement_one)


# In[45]:


statement_two = f" She is commonly referred to as the {known_for}."
print(statement_two)


# In[46]:


statement_three = f" In {year_of_publish} she published the first algorithm, the {first_algorithm} at the age of 27"
print(statement_three)


# In[50]:


statement_four = f" She was a British Citizen who lived in {city_location}, {country_location} until her passing in {death_year} at the age of {age_at_passing}."
print(statement_four)


# In[ ]:




