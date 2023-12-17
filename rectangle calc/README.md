# Rectangle Class

This Python exercise involves creating a `Rectangle` class with methods to calculate the area, perimeter, and diagonal length of a plot of land.
### Question

`Python exercise`
- a. Create a Rectangle class
- b. Write a constructor method in the Rectangle class, and assign the following 
attributes: length, width
- c. Create an area method that calculates the area of a plot of land
- d. Create a perimeter method that calculates the perimeter of a plot of land
- e. Create a diagonal_length method that calculates the length of the diagonal 
of a plot of land
- f. Create an object from the class and assign 40 and 30 for its length and 
width respectively
- `Hints.`
- All methods take self as its first and default parameter
- Import the sqrt method from the math module

## Class Definition

### Rectangle

The `Rectangle` class has the following attributes:
- `length`: Length of the rectangle.
- `width`: Width of the rectangle.

And the following methods:
- `__init__(self, length, width)`: Constructor method to initialize the `length` and `width` attributes.
- `area(self)`: Method to calculate the area of the plot of land.
- `perimeter(self)`: Method to calculate the perimeter of the plot of land.
- `diagonal_length(self)`: Method to calculate the length of the diagonal of the plot of land.

## Example Usage

```python
# Import the Rectangle class
from rectangle import Rectangle

# Create an object from the Rectangle class
plot = Rectangle(length=40, width=30)

# Calculate and print the area
print(f"Area of the plot: {plot.area()} square units")

# Calculate and print the perimeter
print(f"Perimeter of the plot: {plot.perimeter()} units")

# Calculate and print the diagonal length
print(f"Diagonal length of the plot: {plot.diagonal_length()} units")
```

## Notes

- Ensure that you have the `sqrt` method from the `math` module imported for the `diagonal_length` calculation.
- All methods in the `Rectangle` class take `self` as the first and default parameter.

Feel free to use this README as a starting point for your Python exercise solution. Update the class methods accordingly, and provide any additional instructions or examples as needed.
