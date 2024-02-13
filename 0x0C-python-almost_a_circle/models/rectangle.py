#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base

class Rectangle(Base):
	"""Represents a rectangle."""

	def __init__(self, width, height, x=0, y=0, id=None):
	 """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
	self.width = width
	self.height = height
	self.x = x
	self.y = y
	super().__init__(id)

	@property
	def width(self):
		"""Setting/getting the width of the Rectangle."""
	return self.__width
	
	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@property
	def height(self):
		"""Setting/getting the height of the Rectangle."""
	return self.__height

	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
	self.__height = value

	@property
	def x(self):
		"""Setting/getting the x coordinate of the Rectangle."""
		return self.__x

	@x.setter
	def x(self, value):
		if type(value) != int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value
	
	@property
	def y(self):
		"""Setting/getting the y coordinate of the Rectangle."""
		return self.__y

	@y.setter
	def y(self, value):
		if type(value) != int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value

if __name__ == "__main__":

	r1 = Rectangle(10, 2)
	print(r1.id)

	r2 = Rectangle(2, 10)
	print(r2.id)

	r3 = Rectangle(10, 2, 0, 0, 12)
	print(r3.id)

if __name__ == "__main__":
	
	try:
		Rectangle(10, "2")
	except Exception as e:
		print("[{}] {}".format(e.__class__.__name__, e))

	try:
		r = Rectangle(10, 2)
		r.width = -10
	except Exception as e:
		print("[{}] {}".format(e.__class__.__name__, e))

	try:
		r = Rectangle(10, 2)
		r.x = {}
	except Exception as e:
		print("[{}] {}".format(e.__class__.__name__, e))

	try:
		Rectangle(10, 2, 3, -1)
	except Exception as e:
		print("[{}] {}".format(e.__class__.__name__, e))


	def area(self):
		"""Return the area of the Rectangle."""
		area = self.width * self.height
		return area

if __name__ == "__main__":

	r1 = Rectangle(3, 2)
	print(r1.area())

	r2 = Rectangle(2, 10)
	print(r2.area())

	r3 = Rectangle(8, 7, 0, 0, 12)
	print(r3.area())

	def display(self):
		"""Print the Rectangle using the `#` character."""
		for _ in range(self.y):
			print()
		for _ in range(Self.height):
			print(" " * self.x, "#" * self.width)

if __name__ == "__main__":
	r1 = Rectangle(4, 6)
	r1.display()

	print("---")

	r1 = Rectangle(2, 2)
	r1.display()

	def update(self, *args):
		"""Assigning attributes based on their positions."""
 if len(args):
		for count, arg in enumerate(args):
			if count == 0:
				self.id = arg
			elif count == 1:
				self.width = arg
			elif count == 2:
				self.height = arg
			elif count == 3:
				self.x = arg
			elif count  == 4:
				self.y = arg
			else:
				continue
			if len(kwargs) > 0:
				for key, value in kwargs.items():
					if key == "id":
						self.id = value
					elif key == "width":
						self.width = value
					elif key == "height":
						self.height = value
					elif key == "x":
						self.x = value
					elif key == "y":
						self.y = value
				else:
					break

	def update(self, *args, **kwargs):
		"""Updating the Rectangle.

		Args:
		*args (ints): New attribute values.
		- 1st argument represents id attribute
		- 2nd argument represents width attribute
		- 3rd argument represent height attribute
		- 4th argument represents x attribute
		- 5th argument represents y attribute
		**kwargs (dict): New key/value pairs of the attributes.
		"""

if args and len(args) != 0:
	r = 0
	for arg in args:
		if r == 0:
			if arg is None:
				self.__init__(self.width, self.height, self.x, self.y)
	else:
		self.id = arg
		if r == 1:
			self.width = arg
	if r == 2:
		self.height = arg if r == 3:
		self.x = arg
	if r == 4:
		self.y = arg
		r += 1
	if kwargs and len(kwargs) != 0:
		for m, j in kwargs.items():
			if m == "id":
		if j is None:
	self.__init__(self.width, self.height, self.x, self.y)
		else:
	self.id = j
	elif m == "width":
	self.width = j
	elif m == "height":
	self.height = j																				   elif m == "x":
	self.x = j
	elif m == "y":
	self.y = j

if __name__ == "__main__":

	r1 = Rectangle(4, 6, 2, 1, 12)
	print(r1)

	r2 = Rectangle(5, 5, 1)
	print(r2)

def to_dictionary(self):
	"""Return the dictionary representation of a Rectangle."""
	return {
	"id": self.id,
	"width": self.width,
	"height": self.height,
	"x": self.x,
	"y": self.y
	}

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

	def __str__(self):
	"""Return the print() and str() representation of the Rectangle."""
	return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
	self.x, self.y,
	self.width, self.height)

	def update(self. *args):
	""" Assign arguments to attributes based on their positions."""
	if args:
		for count, arg in enumerate(args):
			if count == 0:
	 			self.id = arg
		elif count == 1:
			self.width = arg
		elif count == 2:
			self.height = arg
		elif count == 3:
			self.x = arg
		elif count == 4:
			self.y = arg
		else:
			continue
	elif len(kwargs) > 0:
		for key, value in kwargs, items():
			if key == "id":
			self.id = value
		elif key == "width":
			self.width = value
		elif key == "height"
			self.height = value
		elif key == "x"
		 	self.x = value
		elif key == "y"
			self.y = value
		else:
			break:

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
