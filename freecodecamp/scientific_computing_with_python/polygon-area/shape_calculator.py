class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        """
        Generates a rectangle with the specified width and height.

        :param width: width of the rectangle instance
        :param height: height of the rectangle instance

        The method checks if both width and height are of type int.
        If True, the object is assigned the name "Rectangle". Otherwise, the method raises a TypeError.
        """
        if self._check_value(width) and self._check_value(height):
            self.width, self.height = width, height
            self.name_of_shape = "Rectangle"
        else:
            raise TypeError(f"ERROR - inputted height and/or width must be integer\n "
                            f"width is {type(width)} height is {type(height)}")

    def __str__(self) -> str:
        return f"{self.name_of_shape}(width={self.width}, height={self.height})"

    def __repr__(self) -> str:
        return f"{self.name_of_shape}(width={self.width}, height={self.height})"

    @staticmethod
    def _check_value(value: int) -> bool:
        """
        The method displays an error if *value* is not of type *int*.
        :param value: Value of expected type int
        :return: True if the value is of type int or
                 error if the value is not of type int
        """
        if not isinstance(value, int):
            raise TypeError(f"ERROR| Invalid value. Expected an int.")
        else:
            return True

    def set_width(self, new_width: int) -> int:
        """
        Changes the width of the rectangle to a new one.
        :param new_width: new int value of width
        """
        if self._check_value(new_width):
            self.width = new_width
            return self.width

    def set_height(self, new_height: int) -> int:
        """
        Changes the height of the rectangle to a new one.
        :param new_height: new int value of height
        """
        if self._check_value(new_height):
            self.height = new_height
            return self.height

    def get_area(self) -> int:
        """
        Calculates the area of the rectangle.
        :return: width multiplied by height
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """
        Calculates the perimeter of the rectangle
        :return: takes width plus height and multiplies it by two
        """
        return (self.width + self.height) * 2

    def get_diagonal(self) -> float:
        """
        Calculates the diagonal of a rectangle.
        :return: square rooot of sum of squared values of width and height
        """
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self, max_size=50) -> str:
        """
        The checks if the height and width of the rectangle is greater than max_size.
        :returns: a string of * and \n or the string "Too big for picture."
        """
        if self.height > max_size or self.width > max_size:
            picture = "Too big for picture."
        else:
            picture = "\n".join("*" * self.width for _ in range(self.height)) + "\n"
        return picture

    def get_amount_inside(self, rectangle: 'Rectangle') -> int:
        """
        The method checks if the user passed a rectangle instance to the function.
        The method returns how many rectangles passed to the function as the argument fit inside the instance of the
        rectangle. The size of the given rectangle is assessed as is (meaning it is not rotated).
        :param rectangle: A rectangle to fit inside another rectangle
        :return: how many times a given rectangle fits in a specific rectangle instance
        """
        if not isinstance(rectangle, Rectangle):
            raise TypeError(f"Invalid object inputted. Type: {type(rectangle)}")
        else:
            return (self.height // rectangle.height) * (self.width // rectangle.width)


class Square(Rectangle):
    def __init__(self, width: int) -> None:
        """
        Generates a square with the specified width.

        :param width: The width of the rectangle.

        By using super(), the method calls on the parent function and performs the type verification check.
        If True the object is assigned name "Square". Otherwise, the method raises a TypeError.
        """
        super().__init__(width, width)
        self.name_of_shape = "Square"

    def __str__(self) -> str:
        return f"{self.name_of_shape}(side={self.width})"

    def set_side(self, new_side: int) -> int:
        """
        Changes the sides of the square to a new one value.
        :param new_side: new int value of side
        """
        if self._check_value(new_side):
            self.width = new_side
            self.height = new_side
            return self.width
