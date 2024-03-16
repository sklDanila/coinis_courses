from HomeWork3_Task_10 import Color

class AlphaColor(Color):
    def __init__(self, alpha: float):
        super().__init__()
        self.alpha = alpha
    
    def get_alpha(self):
        return self.alpha
        
    def set_alpha(self, value: float):
        if 0 <= float(value) <= 1:
            self.alpha = float(value)
    def update_color_by_alpha(self, alpha):
        self.get_red = self.get_red - self.get_red * alpha
        self.get_green = self.get_green - self.get_green * alpha
        self.get_blue = self.get_blue - self.get_blue * alpha
    def str(self):
        return f'"red: "{self.get_red},\n"green: "{self.get_green},\n"blue: "{self.get_blue},\n"alpha: "{self.get_alpha}\n'
    
    
color1 = AlphaColor(100, 150, 200, 0.8)
color2 = AlphaColor(200, 100, 50, 0.5)

print("Color 1:")
print(f"Red: {color1.red}")
print(f"Green: {color1.green}")
print(f"Blue: {color1.blue}")
print(f"Alpha: {color1.alpha}")

print("\nColor 2:")
print(f"Red: {color2.red}")
print(f"Green: {color2.green}")
print(f"Blue: {color2.blue}")
print(f"Alpha: {color2.alpha}")

color1.update_color_by_alpha(0.5)
color2.update_color_by_alpha(0.2)

print("\nUpdated Color 1:")
print(f"Red: {color1.red}")
print(f"Green: {color1.green}")
print(f"Blue: {color1.blue}")
print(f"Alpha: {color1.alpha}")

print("\nUpdated Color 2:")
print(f"Red: {color2.red}")
print(f"Green: {color2.green}")
print(f"Blue: {color2.blue}")
print(f"Alpha: {color2.alpha}")

# Тестируем метод __str__
print("\nString Representation:")
print(str(color1))
print(str(color2))