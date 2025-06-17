import pygame
 
class HorizontalScrollBar:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value, bg_color, thumb_color):
        """
        Создает горизонтальную полосу прокрутки.
            x: Координата x верхнего левого угла полосы прокрутки.
            y: Координата y верхнего левого угла полосы прокрутки.
            width: Ширина полосы прокрутки.
            height: Высота полосы прокрутки.
            min_value: Минимальное значение полосы прокрутки.
            max_value: Максимальное значение полосы прокрутки.
            initial_value: Начальное значение полосы прокрутки.
            bg_color: Цвет фона полосы прокрутки (RGB).
            thumb_color: Цвет бегунка (RGB).
        """
        self.rect = pygame.Rect(x, y, width, height)  # Прямоугольник для фона ScrollBar
        self.min_value = min_value
        self.max_value = max_value
        self.bg_color = bg_color
        self.thumb_color = thumb_color
        self.thumb_width = 12  # Ширина бегунка
        self.thumb_rect = pygame.Rect(x, y, self.thumb_width, height)  # Прямоугольник для бегунка
        self.dragging = False

        # Вычисляем начальное положение бегунка на основе initial_value
        self.set_value(initial_value)

    def update(self, mouse_pos, mouse_pressed):
        """
        Обновляет положение полосы прокрутки на основе действий мыши.
            mouse_pos: Положение мыши (x, y).
            mouse_pressed: Кортеж, указывающий, какие кнопки мыши нажаты.
        """
        if self.rect.collidepoint(mouse_pos): # Проверяем, находится ли курсор над полосой прокрутки
            if mouse_pressed[0] and not self.dragging:  # Левая кнопка мыши нажата и мы не перетаскиваем
                # Проверяем, находится ли курсор над бегунком
                if self.thumb_rect.collidepoint(mouse_pos):
                    self.dragging = True

        if not mouse_pressed[0]:  # Левая кнопка мыши отпущена
            self.dragging = False

        if self.dragging:
            # Перемещаем бегунок по горизонтали
            self.thumb_rect.x = mouse_pos[0] - self.thumb_rect.width // 2

            # Ограничиваем движение бегунка в пределах ScrollBar
            self.thumb_rect.x = max(self.rect.x, min(self.thumb_rect.x, self.rect.x + self.rect.width - self.thumb_rect.width))

            # Вычисляем значение ScrollBar
            self.value = self.min_value + (self.max_value - self.min_value) * ((self.thumb_rect.x - self.rect.x) / (self.rect.width - self.thumb_rect.width - self.thumb_width) if (self.rect.width - self.thumb_width) > 0 else 0)


    def draw(self, screen):
        # Отрисовываем фон ScrollBar
        pygame.draw.rect(screen, self.bg_color, self.rect)
        # Рисуем бегунок
        pygame.draw.rect(screen, self.thumb_color, self.thumb_rect)

    def get_value(self):
        """
        Возвращает текущее значение полосы прокрутки.
            float: Текущее значение полосы прокрутки.
        """
        return self.value

    def set_thumb_color(self, color):
        """
        Устанавливает цвет бегунка.
            color: Цвет бегунка (RGB).
        """
        self.thumb_color = color

    def set_value(self, value):
        """
        Устанавливает значение полосы прокрутки и перемещает бегунок.
            value: Новое значение полосы прокрутки.
        """
        self.value = value
        # Ограничиваем значение
        self.value = max(self.min_value, min(self.value, self.max_value))

        # Вычисляем положение бегунка на основе значения
        pos = (self.value - self.min_value) / (self.max_value - self.min_value) * (self.rect.width - self.thumb_width)
        self.thumb_rect.x = self.rect.x + pos
        self.thumb_rect.x = max(self.rect.x, min(self.thumb_rect.x, self.rect.x + self.rect.width - self.thumb_rect.width))



