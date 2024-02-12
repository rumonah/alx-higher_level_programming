#!/usr/bin/python3

"""Defines a base model class."""


class Base:
    """Base model.

    This Represents the "base" for all other classes in the project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
	
if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)
	return to_json

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)


    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))


    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for p in list_dicts]
                return [cls.create(**p) for p in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for r in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for r in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
