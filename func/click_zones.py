import math

# Функция для создания зоны, реагирующей на нажатие мыши
def create_click_zone(x, y, width, height):
    """
    Создает зону, которая реагирует на нажатие мыши.
    :param x: Координата X верхнего левого угла зоны.
    :param y: Координата Y верхнего левого угла зоны.
    :param width: Ширина зоны.
    :param height: Высота зоны.
    :return: Функция, которая проверяет, находится ли точка (mouse_x, mouse_y) внутри зоны.
    """
    def is_inside(mouse_x, mouse_y):
        return x <= mouse_x <= x + width and y <= mouse_y <= y + height
    return is_inside

def create_click_zone_is_inside(x, y, width, height,mouse_x, mouse_y):
    """
    Создает зону, которая реагирует на нажатие мыши.
    :param x: Координата X верхнего левого угла зоны.
    :param y: Координата Y верхнего левого угла зоны.
    :param width: Ширина зоны.
    :param height: Высота зоны.
    :return: Функция, которая проверяет, находится ли точка (mouse_x, mouse_y) внутри зоны.
    """
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height

# Функция для создания круглой зоны
def create_circle_zone(center_x, center_y, radius, mouse_x, mouse_y):
    """
    Создает круглую зону, которая реагирует на клик мыши.
    :param center_x: Координата X центра круга.
    :param center_y: Координата Y центра круга.
    :param radius: Радиус круга.
    :param mouse_x: Координата мыши по x.
    :param mouse_y: Координата мыши по y.
    :return: Функция, которая проверяет, находится ли точка (mouse_x, mouse_y) внутри круга.
    """
    distance = math.sqrt((mouse_x - center_x) ** 2 + (mouse_y - center_y) ** 2)
    return distance <= radius
