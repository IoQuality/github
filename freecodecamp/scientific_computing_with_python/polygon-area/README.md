# Polygon Area
Polygon Area project for PY4E.

# Rectangle and Square Classes

This module contains two classes: `Rectangle` and `Square`. The `Rectangle` class allows you to create and modify rectangle objects, while the `Square` class is a subclass of `Rectangle` that allows you to create and modify square objects.

## Rectangle Class

The `Rectangle` class has several methods that allow you to perform various operations on rectangle objects. Here's a brief overview of each method:

```python
__init__(self, width: int, height: int)
```
This method initializes a new `Rectangle` object with the specified width and height. It checks if both width and height are of type int. If True, the object is assigned the name "Rectangle". Otherwise, the method raises a TypeError.

```python
set_width(self, new_width: int)
```
This method changes the width of the rectangle to a new value.

```python
set_height(self, new_height: int)
```
This method changes the height of the rectangle to a new value.

```python
get_area(self)
```
This method calculates and returns the area of the rectangle.

```python
get_perimeter(self)
```
This method calculates and returns the perimeter of the rectangle.

```python
get_diagonal(self)
```
This method calculates and returns the length of the diagonal of the rectangle.

```python
get_picture(self, max_size=50)
```
This method returns a string representation of the rectangle using asterisks (`*`). If either the width or height of the rectangle is greater than `max_size`, it returns the string "Too big for picture."

```python
get_amount_inside(self, rectangle: 'Rectangle')
```
This method returns how many times a given rectangle fits inside this rectangle. The size of the given rectangle is assessed as is (meaning it is not rotated).

## Square Class

The `Square` class is a subclass of `Rectangle` that allows you to create and manipulate square objects. It has one additional method:

```python
set_side(self, new_side: int)
```
This method changes both the width and height of the square to a new value.

## Credits
test_module.py was provided with the project
