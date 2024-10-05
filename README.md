# Variance Estimator Bias Demonstration

This project demonstrates that the variance estimator, calculated as:

```
σ^2_hat = (1/N) * Σ (X_i - X_bar)^2
```

is a **biased estimator** of the population variance. The unbiased estimator, calculated as:

```
s^2 = (1/(N-1)) * Σ (X_i - X_bar)^2
```

is compared to the biased estimator in this simulation to highlight the difference in their performance. The goal is to visualize and quantify the bias introduced by the biased estimator.

## Project Overview

The project involves:

1. **Generating Samples**: Random samples are drawn from a known distribution (e.g., normal distribution) to demonstrate the bias of the variance estimators.
2. **Calculating Variance**: The biased and unbiased variance estimators are computed for each sample.
3. **Measuring Success**: The **Mean Squared Error (MSE)** is used as a measure of success for each estimator, indicating how closely they estimate the true variance.
4. **Visualizing the Results**: Line charts are plotted to visualize the estimated distributions of both biased and unbiased variance estimates.

## Files

- **main.py**: Main script for running the simulation.
- **README.md**: Project overview and usage instructions (this file).

## Getting Started

### Prerequisites

- Python 3.7+
- `matplotlib` for plotting
- `numpy` for numerical calculations
- `scipy` for density estimation

You can install the required libraries using the following command:

```sh
pip install numpy matplotlib scipy
```

### Running the Project

To run the project, execute the `main.py` script:

```sh
python main.py
```

The script will:

1. Generate random samples from a normal distribution.
2. Calculate the biased and unbiased variance estimates.
3. Compute the Mean Squared Error for both estimators.
4. Plot line charts for visualizing the distribution of the variance estimates.
5. Print the MSE for both estimators to compare their accuracy.

## Results

- The **biased variance estimator** underestimates the population variance.
- The **unbiased variance estimator** provides a better estimate of the true variance.
- The **Mean Squared Error (MSE)** for the unbiased estimator is consistently lower, demonstrating its improved accuracy over the biased estimator.

## Example Output

- Line charts comparing the density of the biased vs. unbiased variance estimates.
- Mean Squared Error values printed to the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute by submitting issues or pull requests. Suggestions for improvements are always welcome!

## Contact

For questions or suggestions, please open an issue or contact the author through GitHub.
