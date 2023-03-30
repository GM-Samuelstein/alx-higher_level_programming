#!/usr/bin/python3
"""
Module 6-rectangle.py.

This module has only one class.

Classes:
    Rectangle:
        A class representing a Rectangle.

Functions:
    This module has no functions.
"""


class Rectangle:
    """
    A class representing a Rectangle.

    Attributes:
        width (int) : Private instance attribute.
            The width of a new rectangle object.

        height (int) : Private instance attribute.
            The height of a new rectangle object.

        number_of_instances (int) : Public class attribute.
            The number of instances that have been created.

    Methods:
        __init__(self, width=0, height=0) :
            Initializes a new rectangle object with the given attributes.

        width(self) : @property
            Gets the attribute `width`.

        width(self, value) : @width.setter
            Sets the attribute `width`

        height(self) : @property
            Gets the attribute `height`.

        height(self, value) : @height.setter
            Sets the attribute `height`

        area(self) :
            Computes the area of the rectangle object.

        perimeter(self) :
            Computes the perimeter of the rectangle object.

        __str__(self) :
            Returns a string representation of the rectangle object.

        __repr__(self) :
            Returns a string representation of the rectangle to be able to
            recreate a new instance by using `eval()`.

        __del__(self) :
            Prints a message when an instance of Rectangle is deleted.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object with the given attributes.

        Args:
            width (int) : Private instance attribute.
                The width of a new rectangle object. The default value = 0.

            height (int) : Private instance attribute.
                The height of a new rectangle object. The default value = 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        This method retrieves the width of the rectangle object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the width of the rectangle object.

        Args:
            value (int): Private instance attribute.
                The width of a new rectangle object.

        Raises:
            TypeError:
                If `value` is not an integer.

            ValueError:
                If `value` is less than zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This method retrieves the height of the rectangle object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the height of the rectangle object.

        Args:
            value (int): Private instance attribute.
                The height of a new rectangle object.

        Raises:
            TypeError:
                If `value` is not an integer.

            ValueError:
                If `value` is less than zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes the area of the rectangle object.

        Returns:
            rectangle_area (int) :
                The area of the rectangle object.
        """
        rectangle_area = self.__width * self.__height

        return rectangle_area

    def perimeter(self):
        """
        Computes the perimeter of the rectangle object.

        Returns:
            rectangle_perimeter (int) :
                The area of the rectangle object.
        """
        if self.__width == 0 or self.__height == 0:
            rectangle_peimeter = 0
        else:
            rectangle_peimeter = 2 * self.__width + 2 * self.__height

        return rectangle_peimeter

    def __str__(self):
        """
        Returns a string representation of the rectangle object.

        A string representation of the rectangle object is printed with the
        character `#`. The number of columns printed is equal to the width
        of the rectangle, while the number of rows printed is equal to the
        height of the rectangle.

        Returns:
            rectangle_string (str) :
                A string that draws a representation of the rectangle.
        """
        rectangle_string = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle_string
        else:
            for row in range(self.__height):
                for column in range(self.__width):
                    rectangle_string += "#"
                if row == self.__height - 1:
                    continue
                else:
                    rectangle_string += "\n"

        return rectangle_string

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able to
        recreate a new instance by using `eval()`.
        """
        rectangle_repr = f"Rectangle({self.__width:d}, {self.__height:d})"

        return rectangle_repr

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.

        The message printed is "Bye rectangle...". It also decrements
        `number_of_instances`.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
