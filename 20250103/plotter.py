import matplotlib.pyplot as plt
import pandas as pd


# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)
pclass_values = titanic_data['Pclass'].unique()
average_fare_per_class = titanic_data.groupby('Pclass')['Fare'].mean().sort_index()
# Calculate the number of passengers for each class
passenger_count_per_class = titanic_data['Pclass'].value_counts().sort_index()
# Plot the number of passengers per class on the same bar graph
fig, ax1 = plt.subplots(figsize=(5, 2))

# Plot average fare per class
average_fare_per_class.plot(kind='bar', color=['red'], ax=ax1, position=0, width=0.4)
ax1.set_ylabel('Average Fare')
ax1.set_xlabel('Class')
ax1.set_title('Average Fare Price and Passenger Count per Class on the Titanic')
ax1.grid(axis='y')

# Adjust the figure size to accommodate all bars
ax2 = ax1.twinx()
passenger_count_per_class.plot(kind='bar', color=['blue'], ax=ax2, position=1, width=0.4, alpha=0.5)
plt.xticks(ticks=range(len(pclass_values) + 2))
ax2.set_ylabel('Passenger Count')

# Add legends
ax1.legend(['Average Fare'], loc='upper right', bbox_to_anchor=(1, .80))
ax2.legend(['Passenger Count'], loc='upper right', bbox_to_anchor=(1, 1))

plt.show()