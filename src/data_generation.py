import numpy as np

def generate_data(n=100, seed=42):
    """
    Generates synthetic data for simple linear regression with a seed for reproducibility.

    Parameters:
    -----------
    n : int
        Number of samples to generate.
    seed : int
        Random seed for reproducibility.

    Returns:
    --------
    x : np.ndarray
        Column vector (n, 1) with the independent values.
    y : np.ndarray
        Column vector (n, 1) with the dependent values, following a linear relationship with noise.
    """
    np.random.seed(seed)
    x = np.random.rand(n, 1)  # Values between 0 and 1
    noise = np.random.randn(n, 1)  # Gaussian noise (mean 0, variance 1)
    y = 4 + 3 * x + noise  # Linear relationship: y = 4 + 3x + ε
    return x, y
