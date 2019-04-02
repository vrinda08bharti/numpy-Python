#!/usr/bin/env python
# coding: utf-8

# # Question 1:  List the top 10 quality ranked colleges

# In[21]:


#Question1
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
top10 = dataset.nlargest(10, "Quality Rank")
print(top10)


# # Question2 List all the colleges in California

# In[22]:


#Question2
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
colleges_california = dataset[dataset.State=='CA']
print(colleges_california)


# # Question3 Which college has lowest average debt?

# In[52]:


#Question3
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
dataset.sort_values("Average Debt", ascending = True, inplace = True)
minimum = dataset.head(n=1)
print (minimum)


# # Question 4 List bottom 10 cost rank colleges

# In[45]:


#Question4
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
dataset.sort_values("Cost Rank", ascending = True, inplace = True)
Lowest_CR = dataset.head(n=10)
print (Lowest_CR)


# # Question 5 Among colleges having more than 2000 undergraduates, which has highest faculty/student ratio.

# In[57]:


#Question5
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
dataset.columns = [c.replace(' ', '_') for c in dataset.columns]
#print(dataset)
#minimum = dataset.Cost_Rank.min()
#print(minimum)
selected_colleges = dataset[dataset['Undergrad._Enrollment']>=2000]
#print(selected_colleges)
selected_colleges.sort_values("Student/faculty_Ratio", ascending = False, inplace = True)
maximum = dataset.head(n=1)
print (maximum)


# # Question 6 Which college has aid in grant more than 80% and costliest in total cost?

# In[2]:


#Question6
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
dataset.columns = [c.replace(' ', '_') for c in dataset.columns]
answer = dataset[dataset['Aid_From_Grants']>'80%']
print(answer)
answer.sort_values("Total_Costs", ascending = True, inplace = True)
highest_TC = top50rank.head(n=1)
print(highest_TC)


# # Question7 Among top 50 quality rank colleges, which has lowest total cost

# In[66]:


#Question7
import numpy as np
import pandas as pd
filename = 'Top 100 Private Colleges.2003.csv'
dataset = pd.read_csv(filename)
dataset.columns = [c.replace(' ', '_') for c in dataset.columns]
dataset.sort_values("Quality_Rank", ascending = False, inplace = True)
top50rank = dataset.head(n=50)
print (top50rank)
top50rank.sort_values("Total_Costs", ascending = False, inplace = True)
lowest_TC = top50rank.head(n=1)
print(lowest_TC)


# In[ ]:




