# inside your_script.py
import sys

def calculate(a, b):
    try:
        print(f"Sum: {a + b}")
        print(f"Difference: {a - b}")
        print(f"Product: {a * b}")
    except Exception as e:
        print(f"Calculation Error: {e}")
        sys.exit(1)

# Example values
a = 10
b = 5

calculate(a, b)
