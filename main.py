import pygame
import sys

from classes.scrollbar import HorizontalScrollBar
from func.click_zones import create_circle_zone, create_click_zone,create_click_zone_is_inside
from func.transitions import fade_transition, transition_with_animation,transition_with_animation_out,fade_transition_revers
from func.image_loader import load_image
from func.animations import play_animation
from func.play1 import play1
from func.text import draw_text

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Cat's Live")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (203, 172, 102)

# Шрифт
font = pygame.font.Font(None, 74)

def main_menu():
    # Координаты и размеры кнопок
    zone_x, zone_y = 0, 0
    zone_width, zone_height = 200, 150
        # кнопка настроек
    circle_center_x, circle_center_y = 64, 566  # центр кнопки
    circle_radius = 47  # радиус шестерёнки
        # кнопка выбора уровня (вход и выход)
    play_choice_x, play_choice_y,play_width, play_height=0,52,250,85
    play_out_x, play_out_y, play_out_width, play_out_height = 0, 16, 75, 64
        # кнопка информации по математике (вход и выход)
    infa_x, infa_y, infa_width, infa_height= 0,319,188,89
    infa_out_x, infa_out_y, infa_out_width, infa_out_height = 0, 10, 100, 64

    button_width, button_height = 220, 90
    button_x = 0  # середина меню WIDTH // 2 - button_width // 2
    button_radius = 20
    play_y = 200
    about_y = 300
    info_y = 400
    exit_x = 420
    exit_y = 525

    # x, y, width, height для кнопок не из меню
    buttons_choice_play = [
        200, 50, 263, 150

    ]
    buttons_infa = [
        200, 100, 255, 65
    ]

    # Информация для окон
    current_screen_infa = 1
    current_screen = "menu"
    language = "rus"  # на будущее

    # Для анимации
    image_rect = pygame.Rect(zone_x, zone_y, 0, 0)  # Инициализируем прямоугольник для blit
    animation_folder = "image/pink_cat"
    current_frame = 0
    animation_timer = 0
    animation_delay = 150  # милисекунд между кадрами
    animations = True

    # Загружаем изображение
    image = load_image("image/menu.png")
    image_bar = load_image("image/menu_bar.png")
    image_choice=load_image("image/choice.png")
    image_infa_1=load_image("image/infa01.png")
    image_infa_2 = load_image("image/infa02.png")

    buttons_settings = [load_image("image/settings/background_settings.png"),
                        load_image("image/settings/buttons_settings.png"),
                        load_image("image/settings/language_eng.png"),
                        load_image("image/settings/language_rus.png"),
                        load_image("image/settings/left_cross_language.png"),
                        load_image("image/settings/left_cross_animation.png"),
                        load_image("image/settings/right_cross_language.png"),
                        load_image("image/settings/right_cross_animation.png"),
                        load_image("image/settings/off.png"),
                        load_image("image/settings/on.png")]

    scrollbar_sound = HorizontalScrollBar(120, 85, 399, 20, 0, 100, 50, WHITE, (86, 153, 128))  # true_width 410, третий аргумент
    scrollbar_music = HorizontalScrollBar(120, 174, 399, 20, 0, 100, 50, WHITE, (86, 153, 128))  # true_width 410, третий аргумент

    # Время
    clock = pygame.time.Clock()
    frame_rate = 30
    # Потом переделать для вызовов ошибок
    if image:
        image_rect = image.get_rect(topleft=(zone_x, zone_y))
    #if buttons_settings:
    #    buttons_settings_rect = []
    #    for button in buttons_settings:
    #        buttons_settings_rect.append(button.get_rect(topleft=(zone_x, zone_y)))

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        # Отрисовка кнопок
        # draw_rounded_button(screen, GREEN, button_x, play_y, button_width, button_height, button_radius, "Играть", BLACK)
        # draw_rounded_button(screen, BLUE, button_x, about_y, button_width, button_height, button_radius, "Об игре", BLACK)
        # draw_rounded_button(screen, BLUE, button_x, info_y, button_width, button_height, button_radius, "Инфа", BLACK)
        # draw_rounded_button(screen, RED, button_x, exit_y, button_width, button_height, button_radius, "Выход", BLACK)
        if current_screen == "menu":

            current_frame = (current_frame + 1) % 14
            screen.blit(image, image_rect)
            play_animation(screen, current_frame,zone_x+50, zone_y+30,"image/pink_cat")
            screen.blit(image_bar, image_rect)

        if current_screen == "settings":
            screen.fill(BLACK)
            if buttons_settings:
                if not 'buttons_settings_rect' in locals():
                    buttons_settings_rect = []
                    for button in buttons_settings:
                        buttons_settings_rect.append(button.get_rect(topleft=(zone_x, zone_y)))
                screen.blit(buttons_settings[0], buttons_settings_rect[0])
                screen.blit(buttons_settings[1], buttons_settings_rect[1])
                screen.blit(buttons_settings[3], buttons_settings_rect[3])
                screen.blit(buttons_settings[4], buttons_settings_rect[4])
                screen.blit(buttons_settings[5], buttons_settings_rect[5])
                screen.blit(buttons_settings[6], buttons_settings_rect[6])
                screen.blit(buttons_settings[7], buttons_settings_rect[7])
                screen.blit(buttons_settings[9], buttons_settings_rect[9])
            scrollbar_sound.draw(screen)
            scrollbar_music.draw(screen)

            scrollbar_sound.update(mouse_pos, mouse_pressed)
            scrollbar_music.update(mouse_pos, mouse_pressed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Получение позиции мыши и состояния кнопок
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    # Обновление ScrollBar
                    scrollbar_sound.update(mouse_pos, mouse_pressed)
                    scrollbar_music.update(mouse_pos, mouse_pressed)
                    # Проверка нажатия на кнопки
                    if create_circle_zone(circle_center_x, circle_center_y, circle_radius, mouse_pos[0], mouse_pos[1]) and current_screen == "settings":
                        transition_with_animation_out(screen)  # Проигрываем анимацию
                        #fade_transition(screen, YELLOW, 750)  # Плавное затемнение
                        current_screen = "menu" if current_screen == "settings" else "settings"
        if current_screen == "choice level":
            #fade_transition_revers(screen, YELLOW, 4000)
            screen.blit(image_choice, image_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    if create_click_zone_is_inside(play_out_x, play_out_y, play_out_width,play_out_height,mouse_pos[0],mouse_pos[1]) and current_screen == "choice level":
                        fade_transition(screen, [230,120,170], 750)  # Плавное затемнение
                        current_screen = "menu" if current_screen == "choice level" else "choice level"
                    if create_click_zone_is_inside(buttons_choice_play[0], buttons_choice_play[1], buttons_choice_play[2], buttons_choice_play[3],mouse_pos[0], mouse_pos[1]) and current_screen == "choice level":
                        fade_transition(screen, [210,190,150], 750)  # Плавное затемнение
                        rating=play1()
                        screen.fill([90, 30, 20])
                        #fade_transition(screen, [90, 30, 20], 1050)
                        draw_text("Верных ответов: "+rating,font,[255,255,255],screen,WIDTH//2,HEIGHT//2)
                        fade_transition(screen, [230, 120, 170], 6000)

        if current_screen == "infa":
            if current_screen_infa==1:
                screen.blit(image_infa_1, image_rect)
            else:
                screen.blit(image_infa_2, image_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    if create_click_zone_is_inside(infa_out_x, infa_out_y, infa_out_width, infa_out_height,
                                                   mouse_pos[0], mouse_pos[1]) and current_screen == "infa":
                        current_screen_infa = 1
                        fade_transition(screen, [130, 110, 60], 750)  # Плавное затемнение
                        current_screen = "menu" if current_screen == "infa" else "infa"
                    if create_click_zone_is_inside(buttons_infa[0],buttons_infa[1],buttons_infa[2],buttons_infa[3],mouse_pos[0], mouse_pos[1]) and current_screen == "infa":
                        current_screen_infa=2

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                # Проверка нажатия на кнопки
                if create_circle_zone(circle_center_x, circle_center_y, circle_radius, mouse_pos[0], mouse_pos[1]) and current_screen == "menu":
                    fade_transition(screen, BLACK, 750)  # Плавное затемнение
                    transition_with_animation(screen)  # Проигрываем анимацию
                    current_screen = "settings" if current_screen == "menu" else "menu"

                if create_click_zone_is_inside(play_choice_x, play_choice_y, play_width,play_height,mouse_pos[0],mouse_pos[1]) and current_screen == "menu":
                    fade_transition(screen, YELLOW, 750)  # Плавное затемнение
                    current_screen = "choice level" if current_screen == "menu" else "menu"
                if create_click_zone_is_inside(infa_x, infa_y, infa_width, infa_height, mouse_pos[0],mouse_pos[1]) and current_screen == "menu":
                    fade_transition(screen, [130, 110, 60], 750)
                    current_screen = "infa" if current_screen == "menu" else "menu"
                # elif в зоне стрелки то switch_language
                elif exit_x <= mouse_pos[0] <= exit_x + button_width:
                    if exit_y <= mouse_pos[1] <= exit_y + button_height:
                        pygame.quit()
                        sys.exit()

        # Ограничение FPS
        clock.tick(frame_rate)
        # Обновление экрана
        pygame.display.flip()


# Запуск меню
if __name__ == '__main__':
    main_menu()

