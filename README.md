# Linear Regression From Scratch

This project provides a detailed implementation of a simple linear regression model built from the ground up using Python and NumPy. The goal is to demonstrate the fundamental mechanics of linear regression by leveraging matrix algebra (the Normal Equation), without relying on high-level machine learning libraries like scikit-learn for the core modeling process.

The project is structured as a tutorial-style Jupyter Notebook that walks through the theory, implementation, and visualization of the model.

---

## Key Features

- **From-Scratch Implementation**: The core linear regression model is built using only NumPy to perform the necessary matrix calculations.
- **Modular Code Structure**: The Python code is refactored into separate modules for data generation, model fitting, and visualization, promoting clean and reusable code.
- **Scikit-learn Comparison**: The notebook includes a validation step that compares the results of our from-scratch model with the industry-standard implementation from scikit-learn, confirming its correctness.
- **Detailed Explanations**: The Jupyter Notebook contains clear, step-by-step explanations of the theory behind linear regression and the Normal Equation.

---

## Project Structure
```
linear-regression-from-scratch/
├── notebooks/
│   └── 01-linear-regression-from-scratch.ipynb
├── src/
│   ├── data_generation.py
│   ├── linear_regression.py
│   └── visualization.py
├── .gitignore
├── README.md
└── requirements.txt
```
---

## Technologies Used

- Python 3.8+
- NumPy
- Matplotlib
- Scikit-learn
- JupyterLab / Jupyter Notebook

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<YOUR_USERNAME>/linear-regression-from-scratch.git
    cd linear-regression-from-scratch
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

1.  **Start JupyterLab:**
    ```bash
    jupyter lab
    ```

2.  **Open and run the notebook:**
    Navigate to `notebooks/` and open the `01-linear-regression-from-scratch.ipynb` file. You can then run the cells sequentially to see the analysis.
