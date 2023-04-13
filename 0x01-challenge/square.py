#!/usr/bin/python3
"""define Square class"""


class Square():
    """define Square instances"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        if not args:
            for key, value in kwargs.items():
                if type(value) == int:
                    if key in ['width', 'height']:
                        setattr(self, key, value)
        else:
            self.width = args[0]
            self.height = args[1]

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_Square(self):
        """ permiter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of the instances"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_Square())
