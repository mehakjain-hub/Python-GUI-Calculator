# Simple Multi-Function Tkinter Calculator

This project is a robust, multi-function calculator built using Python's Tkinter GUI library. It successfully implements seven core operations. The application features comprehensive error handling to catch invalid inputs. The user interface is deliberately designed with a single-column vertical layout, where all input labels, entry fields, and operation buttons are stacked sequentially, creating a long, straightforward user flow. The design is unified by a distinctive dark theme and bold typography.

# Features

1. **Seven Operations:** Supports Addition (`X+Y`), Subtraction (`X-Y`), Multiplication (`X*Y`), Division (`X/Y`), **Exponentiation** (`X^Y`), and **Averaging** (`(X+Y)/2`).
2. **GUI Layout:** The core operations are organized in a compact grid structure for efficiency, demonstrating strong command of the Tkinter `grid` layout manager.
3. **Robust Error Handling:** Includes `try-except` blocks to catch non-numeric input and specific logic to prevent **Division by Zero** errors.
4. **Dynamic State:** Uses `tk.StringVar` to instantly update the result display upon calculation.
5. **Aesthetics:** Features a dark theme (`#2e3440`) with high-contrast text and colorful buttons for a clean, modern look.

# Getting Started

This application requires only a standard Python installation, as Tkinter is included with Python's standard library.

# Prerequisites

**Python 3.x:** Ensure you have Python installed. (Check by running `python --version` or `python3 --version` in your terminal.)

# Installation and Running

1.  **Clone the Repository** (If you haven't already):
    ```bash
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    cd YourRepoName
    ```
2.  **Ensure the file is present:** Make sure `SimpleCalculator.py` is in the current directory.
3.  **Execute the script:** Run the file from your terminal.

    *On Mac/Linux:*
    ```bash
    python3 SimpleCalculator.py
    ```
    *On Windows:*
    ```bash
    python SimpleCalculator.py
    ```

## Usage

1.  **Input:** Enter the first number (X) and the second number (Y) into the respective input boxes.
2.  **Calculate:** Click any of the seven operation buttons to perform the desired function.
3.  **View:** The result will be displayed in the result area at the bottom.
4.  **Reset:** Click the **Clear All Inputs** button to clear the text boxes and reset the result display.
