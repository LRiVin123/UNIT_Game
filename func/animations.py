import pygame
import os
from func.image_loader import load_image
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 640, 640


def fade_animation(screen, color, duration):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)
    for alpha in range(0, 255, 5):  # Увеличиваем прозрачность
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration // 50)

# Отображение кадра анимации
def play_animation(screen, current_frame, zone_x, zone_y, animation_folder):

    image_files = sorted([f for f in os.listdir(animation_folder) if f.endswith((".png", ".jpg", ".jpeg", ".gif"))])
    num_frames = len(image_files)

    # Для указания папки с кадрами, но криво работает сама анимация
    #animation_frames = []
    #for i in range(num_frames):
    #    image_path = os.path.join(animation_folder, image_files[i])
    #    animation_frames.append(load_image(image_path))

    # Версия с указанной папкой, временное решение
    animation_frames = [load_image(f"image/pink_cat/pink_cat{i}.png") for i in range(num_frames)]

    if 0 <= current_frame < len(animation_frames):
        screen.blit(animation_frames[current_frame], (zone_x, zone_y))

    # старая версия на всякий случай
    #animation_frames = [load_image(f"image/pink_cat/pink_cat{i}.png") for i in range(14)]
    #if 0 <= current_frame < len(animation_frames):
    #    screen.blit(animation_frames[current_frame], (zone_x, zone_y))


