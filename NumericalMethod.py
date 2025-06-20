import numpy as np

def midpoint_rule(f, a, b, n):
    """Approximates the integral using the Midpoint Rule."""
    h = (b - a) / n
    result = sum(f(a + h * (i + 0.5)) for i in range(n)) * h
    return result

def trapezoid_rule(f, a, b, n):
    """Approximates the integral using the Trapezoid Rule."""
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    result += sum(f(a + i * h) for i in range(1, n))
    result *= h
    return result

def compare_methods(f, a, b, true_value, tol):
    """
    Compares the Midpoint and Trapezoid rules to find which method converges quicker.
    Receives function, true value, and tolerance as input. Calculates and compares errors.
    """
    n = 1  # Start with 1 subinterval
    midpoint_error, trapezoid_error = float('inf'), float('inf')

    print("Iteration | n | Midpoint Error | Trapezoid Error")
    print("-" * 50)

    while midpoint_error > tol or trapezoid_error > tol:
        midpoint_result = midpoint_rule(f, a, b, n)
        trapezoid_result = trapezoid_rule(f, a, b, n)
        midpoint_error = abs(midpoint_result - true_value)
        trapezoid_error = abs(trapezoid_result - true_value)

        print("\n Midpoint result: " + str(midpoint_result))
        print(f"{n:9} | {n:1} | {midpoint_error:.6f}      | {trapezoid_error:.6f}")

        if midpoint_error <= tol and trapezoid_error <= tol:
            break

        n += 1

    # Determine which converges quicker
    if midpoint_error < trapezoid_error:
        faster_method = "Midpoint Rule"
    else:
        faster_method = "Trapezoid Rule"

    return faster_method, n

if __name__ == "__main__":
    # Input function
    user_function = input("Enter a function of x (e.g., np.sin(x), x**2 + 3): ")
    f = lambda x: eval(user_function)

    # Input integration bounds
    a = float(input("Enter the lower bound of integration (a): "))
    b = float(input("Enter the upper bound of integration (b): "))

    # Input true value
    true_value = float(input("Enter the true value of the integral (if known): "))

    # Input tolerance
    tol = float(input("Enter the tolerance for error (e.g., 1e-4): "))

    # Compare methods
    faster_method, iterations = compare_methods(f, a, b, true_value, tol)
    print(f"\nThe method that converges faster is: {faster_method}")
    print(f"Converged in {iterations} iterations.")
