# task_10

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        
    def get_red(self):
        return self.red
    def set_red(self, red):
        if 0 <= self.red <= 255:
            self.red = red
        else:
            print("Enter available red value!")
    def get_green(self):
        return self.green
    def set_green(self, green):
        if 0 <= self.green <= 255:
            self.green = green
        else:
            print("Enter available green value!")
    def get_blue(self):
        return self.blue
    def set_blue(self, blue):
        if 0 <= self.blue <= 255:
            self.blue = blue
        else:
            print("Enter available blue value!")
    def add_red(self, change):
        new_red = self.red + change
        if 0 <= new_red <= 255:
            self.red = new_red
    def add_green(self, change):
        new_green = self.green + change
        if 0 <= new_green <= 255:
            self.green = new_green
    def add_blue(self, change):
        new_blue = self.blue + change
        if 0 <= new_blue <= 255:
            self.blue = new_blue
    def It(self, color2):
        if self.get_red() + self.get_green() + self.get_blue() < color2.get_green() + color2.get_blue() + color2.get_red():
            return True
    def eq(self, color2):
        if self.get_red() == color2.get_red() and self.get_green() == color2.get_green() and self.get_blue() == color2.get_blue():
            return True
        else:
            return False
    def str(self):
        return f'"red": {self.get_red}, "green": {self.get_green}, "blue": {self.get_blue}"'