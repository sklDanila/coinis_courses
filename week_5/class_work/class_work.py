# name = "Ivan"


# def a():
#     name = "Marko"

#     def b():
#         print("Zdravo", name)

#     b()


# a()


# OOP
"""

"""


# class Post:
#     def __init__(self, id, title, description="Default Description", author="Admin"):
#         self.__id = id
#         self.__title = title
#         self.description = description
#         self.author = author


# post_a = Post(1, "Clanak 1", "Neki opis")
# print(post_a.__dict__)
# print(post_a.author)
# print(type(post_a))


# class Circle:
#     pi = 3.14

#     def __init__(self, radius=1):
#         self.__radius = radius

#     def area(self):
#         return (self.__radius**2) * Circle.pi

#     def set_radius(self, new_radius):
#         self.__radius = new_radius

#     def get_radius(self):
#         return self.__radius


# c = Circle(10)
# print(c.area())


# class User:
#     def __init__(self):
#         print("User init")

#     def who_i_am(self):
#         print("Im user")

#     def login(self):
#         print("User login")


# class Admin(User):
#     def __init__(self):
#         User.__init__(self)
#         print("Admin")

#     def who_i_am(self):
#         print("Im admin")

#     def delete_user(self):
#         print("I cant delete User")


# user1 = User()
# admin1 = Admin()
# user1.who_i_am()
# admin1.who_i_am()


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width


# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"Title: {self.title}; Author: {self.author}; Pages: {self.pages}"

#     def __len__(self):
#         return self.pages

#     def __del__(self):
#         return "Book deleted"

#     def __gt__(self, book2):
#         return self.pages > book2.pages


# book1 = Book("War and peace", "Tolstoy", 54)
# book2 = Book("War and reconciliation", "Bernstein", 300)
# book3 = Book("cewcwecwe", "Tolstoy", 400)

# list_of_books = []
# list_of_books.append(book1)
# list_of_books.append(book2)
# list_of_books.append(book3)

# print(len(book1))
# print(list_of_books[1] > list_of_books[2])


# FILES

with open("week_4\\HomeWork4\\rectangles.txt") as f:
    content = f.read()
    lines = content.split("\n")
    max_area = 0
    # print(content)
    for line in lines:
        sides = line.split(",")
        # print(sides[0], sides[1])
        if sides[0] == sides[1]:
            area = int(sides[0]) * int(sides[0])
            if area > max_area:
                max_area = area
    print(max_area)
