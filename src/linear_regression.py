import numpy as np

def build_design_matrix(x):
    """
    Constructs the design matrix X from the feature vector x.

    Parameters:
    -----------
    x : np.ndarray
        Column vector (n, 1) of the independent variable.

    Returns:
    --------
    X : np.ndarray
        Design matrix (n, 2) which includes a column of ones for the intercept.
    """
    n = x.shape[0]  # Number of samples
    ones_column = np.ones((n, 1))  # Column of ones for the intercept
    X = np.hstack((ones_column, x))
    return X

def fit_linear_regression(x, y):
    """
    Calculates the beta parameters for linear regression using matrix algebra.

    Parameters:
    -----------
    x : np.ndarray
        Column vector of the independent variable.
    y : np.ndarray
        Column vector of the observed values.

    Returns:
    --------
    beta : np.ndarray
        Column vector with the coefficients [intercept, slope].
    """
    # Build the design matrix
    X = build_design_matrix(x)

    # Calculate beta using the normal equation
    # beta = (X^T * X)^-1 * X^T * y
    X_T = X.T
    XTX = X_T @ X
    XTX_inv = np.linalg.inv(XTX)
    XTy = X_T @ y
    beta = XTX_inv @ XTy

    return beta
