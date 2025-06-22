from class_static_methods_demo import Calculator
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Test Calculator class methods
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

    # Existing polymorphism test (unchanged)
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

