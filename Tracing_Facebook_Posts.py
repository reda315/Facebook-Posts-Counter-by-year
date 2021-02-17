"""
Created on Wed Feb 18 23:37:24 2021

@author:Ahmed Reda
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Reading the json file containing facebook information
df = pd.read_json('Facebook_Posts.json')

# Rename the timestamp Column
df = df.rename(columns = {'timestamp' : 'Date'})

# Removing unnecessary Columns
df = df.drop(['attachments', 'tags', 'title'], axis = 1)

# Setting the "Date" Column as the index for our Dataframe
df = df.set_index('Date')

# Resampling the data by month, counting how many posts occur in each month
Post_Counts = df['data'].resample('YS').size()
print(Post_Counts)

# Setting figure and font sizes
sns.set(rc={'figure.figsize':(60,40)})
sns.set(font_scale=5)

# Setting X-Label
x_labels = Post_Counts.index

# Creating bar plot
sns.barplot(x_labels, Post_Counts, color="red")

# Only show x-axis labels for Jan 1 of every year
tick_positions = np.arange(0, len(x_labels), step=1)

# Reformat date to display year onlyplt.ylabel("Post Counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"), rotation ='vertical')

# Display the plot
plt.show()

