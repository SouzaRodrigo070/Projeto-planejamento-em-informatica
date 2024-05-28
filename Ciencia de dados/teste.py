import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#sample

data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [4, 7, 2, 5]
})

# Set Seaborn style
sns.set(style='whitegrid')

# Create a bar plot using seaborn
sns.barplot(x='Category', y='Value', data=data)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Sample Seaborn Bar Plot')

# show the plot
plt.show()