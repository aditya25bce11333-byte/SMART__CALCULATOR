import math
import tkinter as tk
from tkinter import simpledialog, messagebox

SMART_FUNCTIONS = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,
    'log10': math.log10,
    'radians': math.radians,
    'degrees': math.degrees,
    'pi': math.pi,
    'e': math.e,
}

def smart_calculate(expression):
    """
    Evaluates a mathematical expression using a limited and safe context.
    """
    safe_globals = {'__builtins__': None}

    safe_locals = SMART_FUNCTIONS.copy()
    
    expression = expression.lower().strip()
    
    try:
        result = eval(expression, safe_globals, safe_locals)
        return result
        
    except (NameError, TypeError, SyntaxError, ZeroDivisionError, ValueError) as e:
        if isinstance(e, NameError):
            return f"Error: Invalid function or variable used. Try: {', '.join(SMART_FUNCTIONS.keys())}"
        elif isinstance(e, ZeroDivisionError):
            return "Error: Cannot divide by zero."
        elif isinstance(e, ValueError):
            return "Error: Invalid input for a math function (e.g., negative sqrt or log)."
        else:
            return f"Error in expression: {e}"

def main_calculator():
    """
    Runs the interactive command-line calculator.
    """
    print(" Smart Calculator Initialized ")
    print("Enter 'quit' or 'exit' to end the program.")
    print("You can use: +, -, *, /, **, sin(), cos(), sqrt(), pi, e, etc.")
    
    while True:
        
        user_input = input("\nEnter calculation: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Calculator closed. Goodbye!")
            break
        
        if not user_input.strip():
            continue 
            
        output = smart_calculate(user_input)
        print(f"Result: {output}")

if __name__ == "__main__":

    main_calculator()
