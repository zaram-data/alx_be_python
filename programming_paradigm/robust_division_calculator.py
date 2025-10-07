# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform a safe division between numerator and denominator.
    Handles ZeroDivisionError and ValueError (non-numeric input).
    """
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try dividing
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
