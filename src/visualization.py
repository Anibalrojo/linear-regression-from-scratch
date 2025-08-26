import matplotlib.pyplot as plt
from src.linear_regression import build_design_matrix

def plot_regression_results(x, y, beta):
    """
    Plots the original data and the fitted regression line.

    Parameters:
    -----------
    x : np.ndarray
        Column vector of the independent variable.
    y : np.ndarray
        Column vector of the observed values.
    beta : np.ndarray
        Column vector with the coefficients [intercept, slope].
    """
    # Predict values: y_hat = X @ beta
    X = build_design_matrix(x)
    y_pred = X @ beta

    # Plot the original data points and the fitted line
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='steelblue', alpha=0.7, edgecolors='k', label='Actual Data')
    plt.plot(x, y_pred, color='crimson', linewidth=2, label='Fitted Regression Line')
    plt.title("Linear Regression - Model Fit")
    plt.xlabel("Independent Variable (x)")
    plt.ylabel("Dependent Variable (y)")
    plt.legend()
    plt.grid(True)
    plt.show()
