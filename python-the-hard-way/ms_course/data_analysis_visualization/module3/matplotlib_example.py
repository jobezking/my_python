import matplotlib.pyplot as plt
import numpy as np

# Create a figure with a specific size
fig = plt.figure(figsize=(10, 6))  # Width: 10 inches, Height: 6 inches

# Create a figure with 2 rows and 2 columns of subplots
fig, ax = plt.subplots(2, 2)

# Access individual subplots using indexing
ax[0, 0].plot([1, 2, 3], [4, 5, 6])  # Top-left subplot
ax[0, 1].bar(['A', 'B', 'C'], [7, 8, 9])  # Top-right subplot
ax[1, 0].scatter([10, 20, 30], [11, 12, 13])  # Bottom-left subplot
ax[1, 1].hist([1, 1, 2, 3, 3, 3])  # Bottom-right subplot

plt.show()

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot Title')
plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

# Set tick locations and labels for the x-axis
plt.xticks(np.arange(0, 11, 2), ['0', '2', '4', '6', '8', '10'])

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.show()

x = [1, 2, 3]
y1 = [4, 5, 6]
y2 = [7, 8, 9]

plt.plot(x, y1, label='Data Series 1')
plt.plot(x, y2, label='Data Series 2')

plt.legend()  # Automatically creates a legend based on labels
plt.show()

x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced points from 0 to 10
y = np.sin(x)  # Compute the sine of each x value

plt.plot(x, y)
plt.xlabel('Time (days)')  # Label the x-axis
plt.ylabel('Stock Price ($)')  # Label the y-axis
plt.title('Stock Price Trend')  # Add a title
plt.show()  # Display the plot

ages = np.linspace(20, 60, 100)  # Ages ranging from 20 to 60
income = ages * 500 + np.random.normal(0, 10000, 100)  # Simulating a positive correlation with some noise

plt.scatter(ages, income)
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs. Income')
plt.show()

categories = ['Product A', 'Product B', 'Product C', 'Product D']
values = [1500, 2300, 1200, 3000]

plt.bar(categories, values)
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales Comparison')
plt.show()

data = np.random.randn(1000)  # Generate 1000 random numbers from a standard normal distribution

plt.hist(data, bins=30)  # Create a histogram with 30 bins
plt.xlabel('Exam Score')
plt.ylabel('Number of Students')
plt.title('Distribution of Exam Scores')
plt.show()

labels = ['Windows', 'macOS', 'Linux', 'Other']
sizes = [70, 20, 5, 5]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # Display percentages on each slice
plt.title('Market Share of Operating Systems')
plt.show()