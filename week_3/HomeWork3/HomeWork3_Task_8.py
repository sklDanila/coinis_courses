# task_8


class Player:
    def __init__(self, x: int, y: int, width: int, height: int, health: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        if 0 <= height <= 100:
            self.height = height
        else:
            print("Enter available height value!")

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health


class Enemy:
    def __init__(self, x, y, width, height, damage: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        if 0 <= damage <= 100:
            self.damage = damage
        else:
            print("Enter available damage value!")


def check_collision(player: Player, enemy: Enemy):
    player_x_range = range(player.get_x(), player.get_x() + player.get_width())
    player_y_range = range(player.get_y(), player.get_y() + player.get_height())
    enemy_x_range = range(enemy.get_x(), enemy.get_x() + enemy.get_width())
    enemy_y_range = range(enemy.get_y(), enemy.get_y() + enemy.get_height())

    if (set(player_x_range) & set(enemy_x_range)) and (
        set(player_y_range) & set(enemy_y_range)
    ):
        return True
    else:
        return False


def decrease_health(player: Player, enemy: Enemy):
    if check_collision(player, enemy):
        player_health = player.get_health()
        enemy_damage = enemy.get_damage()
        player.set_health(player_health - enemy_damage)


player = Player(x=0, y=0, width=10, height=10, health=100)
enemy1 = Enemy(x=5, y=5, width=8, height=8, damage=20)
enemy2 = Enemy(x=20, y=20, width=5, height=5, damage=15)

print("Collision between player and enemy1:", check_collision(player, enemy1))
print("Collision between player and enemy2:", check_collision(player, enemy2))

print("Player health before collision:", player.get_health())
decrease_health(player, enemy1)
print("Player health after collision with enemy1:", player.get_health())
decrease_health(player, enemy2)
print("Player health after collision with enemy2:", player.get_health())
