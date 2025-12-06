# Convex function: g(x) = x^2 and its derivative g'(x) = 2x
def convex_func(z):
    return z**2

def convex_func_derivative(z):
    return 2 * z

# Nonconvex function: h(x) = x^4 - x^2 and its derivative h'(x) = 4x^3 - 2x
def nonconvex_func(y):
    return y**4 - y**2

def nonconvex_func_derivative(y):
    return 4 * y**3 - 2 * y

# Gradient Descent Implementation
def gradient_descent_step(derivative_func, starting_point, step_size, max_iterations):
    points = [starting_point]
    for _ in range(max_iterations):
        next_point = points[-1] - step_size * derivative_func(points[-1])
        points.append(next_point)
    return points

# Part (a), (b), and (c): Gradient descent on a convex function
start = 10  # Starting point
max_steps = 10

# Test different learning rates for convex function
learning_rates = [0.1, 0.5, 1.5]  # Small, optimal, and too large step sizes
print("Convex Function: g(x) = x^2")
for rate in learning_rates:
    descent_results = gradient_descent_step(convex_func_derivative, start, rate, max_steps)
    print(f"\nLearning rate (η): {rate}")
    for step_index, val in enumerate(descent_results):
        print(f"Step {step_index}: z = {val}, g(z) = {convex_func(val)}")

# Part (d): Gradient descent on a nonconvex function
initial_values = [-1.5, -0.5, 0.5, 1.5]  # Different starting points
step_size = 0.1  # Moderate step size
print("\nNonconvex Function: h(x) = x^4 - x^2")
for start_value in initial_values:
    nonconvex_results = gradient_descent_step(nonconvex_func_derivative, start_value, step_size, max_steps)
    print(f"\nStarting point: y = {start_value}")
    for step_index, val in enumerate(nonconvex_results):
        print(f"Step {step_index}: y = {val}, h(y) = {nonconvex_func(val)}")
