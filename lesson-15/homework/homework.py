import matplotlib.pyplot as plt
import numpy as np

# Task 1: Basic Plotting
x = np.linspace(-10, 10, 400)
y = x**2 - 4 * x + 4
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^2 - 4x + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2 - 4x + 4")
plt.legend()
plt.grid(True)
plt.show()

# Task 2: Sine and Cosine Plot
x = np.linspace(0, 2 * np.pi, 400)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y1, linestyle="-", color="blue", label="sin(x)")
plt.plot(x, y2, linestyle="--", color="red", marker="o", label="cos(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of sin(x) and cos(x)")
plt.legend()
plt.grid(True)
plt.show()

# Task 3: Subplots
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y1 = x**3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(x + 1)
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(x, y1, color="blue")
plt.title("f(x) = x^3")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.subplot(2, 2, 2)
plt.plot(x, y2, color="green")
plt.title("f(x) = sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.subplot(2, 2, 3)
plt.plot(x, y3, color="red")
plt.title("f(x) = e^x")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.subplot(2, 2, 4)
plt.plot(x[x > 0], y4[x > 0], color="purple")
plt.title("f(x) = log(x+1)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.tight_layout()
plt.show()

# Task 4: Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, alpha=0.8, cmap="viridis")
plt.colorbar(label="Color intensity")
plt.title("Scatter Plot of 100 Random Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Task 5: Histogram
data = np.random.normal(0, 1, 1000)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, alpha=0.7, color="blue", edgecolor="black")
plt.title("Histogram of 1000 Random Normal Distribution Samples")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Task 6: 3D Plotting
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(x, y, z, cmap="coolwarm")
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
ax.set_title("3D Surface Plot of cos(x^2 + y^2)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("f(x, y)")
plt.show()

# Task 7: Bar Chart
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [200, 150, 250, 175, 225]
plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=["blue", "green", "red", "purple", "orange"])
plt.title("Vertical Bar Chart of Sales Data")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Task 8: Stacked Bar Chart
categories = ["Category A", "Category B", "Category C"]
time_periods = ["T1", "T2", "T3", "T4"]
data = np.random.rand(len(categories), len(time_periods))

plt.figure(figsize=(10, 8))
bar_width = 0.35
for i, category in enumerate(categories):
    plt.bar(time_periods, data[i], label=category, width=bar_width)

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart of Categories Over Time Periods")
plt.legend()
plt.grid(True)
plt.show()
