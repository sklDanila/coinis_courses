# Kupili ste zavjesu pravouganog oblika. Provjerite da li će zavjesa prekriti prozor koji je
# takođe pravouganog oblika. Za zavjesu i prozor poznata je gornja lijeva i donja desna
# koordinata.


class calculation_area:
    def __init__(self, x_upperLeft, y_upperLeft, x_lowerRight, y_lowerRight):
        self.x_upperLeft = x_upperLeft
        self.y_upperLeft = y_upperLeft
        self.x_lowerRight = x_lowerRight
        self.y_lowerRight = y_lowerRight

    def area(self):
        side_a = self.x_lowerRight - self.x_upperLeft
        side_b = self.y_upperLeft - self.y_lowerRight
        return side_a * side_b


def curtains_window():
    curtains = calculation_area(20, 40, 40, 20)
    window = calculation_area(10, 30, 30, 10)
    area_curtains = curtains.area()
    area_window = window.area()
    if area_window == area_curtains:
        print("Curtain covers the window")
    else:
        print("Curtain doesnt cover the window")


curtains_window()
