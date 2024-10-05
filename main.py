import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def generate_samples(n, size, true_mean=0, true_var=1):
    """Generates n samples, each of the given size from a normal distribution."""
    return np.random.normal(loc=true_mean, scale=np.sqrt(true_var), size=(n, size))

def biased_variance(samples):
    """Computes the biased variance of the sample."""
    return np.var(samples, ddof=0, axis=1)

def unbiased_variance(samples):
    """Computes the unbiased variance of the sample."""
    return np.var(samples, ddof=1, axis=1)

def mean_squared_error(estimates, true_value):
    """Computes the mean squared error of the estimates compared to the true value."""
    return np.mean((estimates - true_value) ** 2)

# Simulation parameters
n_samples = 1000  # Number of samples
sample_size = 10  # Sample size for each group of samples
true_variance = 1  # The true variance of the population

# Generate samples
samples = generate_samples(n_samples, sample_size, true_var=true_variance)

# Compute biased and unbiased variances
biased_var = biased_variance(samples)
unbiased_var = unbiased_variance(samples)

# Compute MSE for both estimators
mse_biased = mean_squared_error(biased_var, true_variance)
mse_unbiased = mean_squared_error(unbiased_var, true_variance)

# Print the MSE values
print(f"Mean Squared Error for Biased Variance Estimator: {mse_biased:.4f}")
print(f"Mean Squared Error for Unbiased Variance Estimator: {mse_unbiased:.4f}")

# Create density estimates for biased and unbiased variances
density_biased = gaussian_kde(biased_var)
density_unbiased = gaussian_kde(unbiased_var)

# Generate x values for plotting
x_vals = np.linspace(min(biased_var.min(), unbiased_var.min()), max(biased_var.max(), unbiased_var.max()), 1000)

# Plot the density lines for biased and unbiased variances
plt.plot(x_vals, density_biased(x_vals), label='Biased Variance', color='blue')
plt.plot(x_vals, density_unbiased(x_vals), label='Unbiased Variance', color='green')
plt.axvline(x=true_variance, color='red', linestyle='--', label='True Variance')
plt.legend()
plt.title('Biased vs. Unbiased Variance Estimators')
plt.xlabel('Variance Estimate')
plt.ylabel('Density')
plt.show()
