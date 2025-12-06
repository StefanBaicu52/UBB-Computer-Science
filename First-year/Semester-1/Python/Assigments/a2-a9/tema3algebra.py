import numpy as np

def gaussian_integral(a, n=10000):
    x = np.linspace(-a, a, n)
    y = np.exp(-x**2)
    return np.trapz(y, x)

# Test for increasing values of a
a_values = [1, 2, 5, 10, 20]
results = [gaussian_integral(a) for a in a_values]

# Print results
for a, res in zip(a_values, results):
    print(f"Integral from -{a} to {a}: {res:.6f}")

# Compare with sqrt(pi)
print(f"Exact value: {np.sqrt(np.pi):.6f}")