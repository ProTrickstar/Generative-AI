# --------------------------------------------
# Topic 3: Matplotlib Visualization
# --------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------
# Line Plot
# --------------------------------------------
xpoint = np.array([1, 3])
ypoint = np.array([2, 4])

plt.plot(xpoint, ypoint)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# --------------------------------------------
# Line Plot: CGPA vs Package
# --------------------------------------------
cgpa = np.array([6, 6.8, 7, 7.5, 8, 8.4, 8.8, 9, 9.5, 10])
package = np.array([4, 5.2, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9])

font1 = {'family':'serif', 'color':'blue', 'size':18}
font2 = {'family':'serif', 'color':'black', 'size':12}

plt.plot(cgpa, package, "*-", markersize=10, markeredgecolor="orange", linewidth=2)
plt.xlabel("CGPA", fontdict=font2)
plt.ylabel("Package (LPA)", fontdict=font2)
plt.title("CGPA vs PACKAGE", fontdict=font1)
plt.grid(True)
plt.show()

# --------------------------------------------
# Bar Plot
# --------------------------------------------
fruit = np.array(["Apple", "Banana", "Orange", "Watermelon"])
fruit_number = np.array([100, 80, 120, 50])
color = ["red", "yellow", "orange", "green"]

plt.bar(fruit, fruit_number, color=color)
plt.title("Fruit Quantity Bar Chart")
plt.show()

# Horizontal Bar Plot
plt.barh(fruit, fruit_number, color=color)
plt.title("Fruit Quantity Horizontal Bar Chart")
plt.show()

# --------------------------------------------
# Pie Chart
# --------------------------------------------
x = np.array([25, 35, 20, 20])
my_labels = np.array(["Apple", "Banana", "Orange", "Watermelon"])
my_explode = [0.2, 0, 0, 0]

plt.pie(x, labels=my_labels, explode=my_explode, autopct='%1.1f%%')
plt.title("Fruit Distribution")
plt.legend(title="Fruits")
plt.show()

# --------------------------------------------
# Scatter Plot
# --------------------------------------------
x_scatter = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_scatter = np.array([200, 180, 160, 150, 130, 120, 110, 100])

plt.scatter(x_scatter, y_scatter)
plt.xlabel("Age of Car (Years)")
plt.ylabel("Speed (km/hr)")
plt.title("Car Age vs Speed Scatter Plot")
plt.grid(True)
plt.show()

# --------------------------------------------
# Histogram
# --------------------------------------------
marks = np.random.randint(40, 100, 200)
plt.hist(marks, bins=10)
plt.xlabel("Marks of Students")
plt.ylabel("Number of Students")
plt.title("Student Marks Distribution")
plt.grid(True)
plt.show()
