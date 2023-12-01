# whiteBoxTesting
# CalculatorApp

This repository contains a simple calculator application implemented in Python. It includes various arithmetic operations and tests to ensure its functionality.

## Overview

The application consists of three main files:

- **calculatorApp.py:** Defines arithmetic functions and error handling for the calculator.
- **test_calculatorApp.py:** Contains unit tests using Python's `unittest` framework to validate the functions in `calculatorApp.py`.
- **mainApp.py:** The main application file that interacts with users through the console, providing a basic user interface for performing calculations.

## Files Description

### `calculatorApp.py`

This file defines several functions and handles arithmetic operations and user input validation.

- **Functions:**
  - `check_user_input(input)`: Validates user input to ensure it's a numeric value.
  - Arithmetic functions: `add`, `subtract`, `multiply`, and `divide`.
  - `calculate(choice, num1, num2)`: Executes arithmetic operations based on user input.

### `test_calculatorApp.py`

This file contains unit tests using Python's `unittest` module to validate the functionality and error handling of functions in `calculatorApp.py`.

- **Unit Tests:**
  - Tests various scenarios for arithmetic functions and error cases in `calculatorApp.py`.
  - Ensures accurate functionality and proper error handling.

### `mainApp.py`

This file offers a command-line interface for users to interact with the calculator.

- **User Interaction:**
  - Prompts users to select an operation and input numbers to perform arithmetic operations.
  - Displays the calculated result in the console.

## Usage

1. **Running the Calculator:**
   - Execute `mainApp.py` to access the calculator interface in the console.
   - Choose an operation (addition, subtraction, multiplication, division) by entering the respective choice number.
   - Input two numbers as requested to perform the chosen operation.

2. **Testing the Calculator:**
   - Execute `test_calculatorApp.py` to run unit tests and validate the functionality of the calculator functions.
   - Tests cover various scenarios, including valid arithmetic operations, error cases, and input validation.
