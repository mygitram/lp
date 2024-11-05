import matplotlib.pyplot as plt
import numpy as np

# Define the function and its derivative
def function(x):
    return (x + 3) ** 2

def gradient(x):
    return 2 * (x + 3)

# Gradient Descent Implementation
def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    x_values = []
    y_values = []
    
    for i in range(num_iterations):
        x_values.append(x)  # Store the current x value
        y_values.append(function(x))  # Store the current function value
        grad = gradient(x)  # Compute the gradient
        x = x - learning_rate * grad  # Update x
        print(f"Iteration {i + 1}: x = {x}, f(x) = {function(x)}")
    
    return x, x_values, y_values

# Parameters
starting_point = 2  # Starting point
learning_rate = 0.1  # Learning rate
num_iterations = 10  # Number of iterations

# Run gradient descent
minima, x_values, y_values = gradient_descent(starting_point, learning_rate, num_iterations)
print(f"Local minima found at x = {minima}, f(x) = {function(minima)}")

# Visualization
plt.plot(x_values, y_values, 'ro-', label='Gradient Descent Path')
plt.title('Gradient Descent Visualization for y = (x + 3)^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.show()
