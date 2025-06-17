import pygame
import random as r
import sys
from func.animations import play_animation, fade_animation
from func.buttons import draw_button
from func.math import easiy
from func.buttons import draw_rounded_button
from func.text import draw_text
from func.image_loader import load_image
c = "1 "*30+"2 "*29+"3 "*16+"4 "*16+"5 "*9
k = c.split(" ")
k.pop()
while True:
    r.shuffle(k)
    if k[0] < "3" and k[1] < "3" and k[2] < "3" and k[9] > "4":
        break

t = easiy()
uroven=[]
for i in range(0,10):
    uroven.append(t.call(k[i]))
print(uroven)

pygame.init()

def play1():
    kol=0

    WIDTH, HEIGHT = 640, 640
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    font = pygame.font.SysFont('Chalkboard', 42)
    font_button = pygame.font.SysFont('Chalkboard', 40)
    zone_x, zone_y = 0, 0
    zone_width, zone_height = 200, 150
    button_width, button_height = 140, 50
    button_x = 0
    button_y=0
    button_radius = 20
    play_y = 200
    about_y = 300
    info_y = 400
    nomer=0
    max_uroven=10
    frame_rate=5
    text=""
    current_frame = 0
    schet = '/'+str(len(uroven))
    schet_dop=1
    image_button = pygame.image.load("image/play1/button.png")
    image_bar=pygame.image.load("image/play1/bar.png")
    image_fon = pygame.image.load("image/play1/play1_01.png")
    i1 = 0
    view_bar=False
    if image_fon:
        image_rect = image_fon.get_rect(topleft=(zone_x, zone_y))
        animation_frames = [load_image(f"image/play1/animation/1/{i}.png") for i in range(1, 35)]
        num_frames = len(animation_frames)
    clock = pygame.time.Clock()
    while True:
        if image_fon:
            screen.blit(image_fon, image_rect)
            current_frame = (current_frame + 1) % num_frames
            if 0 <= current_frame < num_frames:
                screen.blit(animation_frames[current_frame], (zone_x, zone_y+50))
            if view_bar==False:
                screen.blit(image_bar, (0,WIDTH//1.5))
            elif view_bar==True:
                screen.blit(image_bar, (0, WIDTH // 1.05))
            #image_rect_butt = image_button.get_rect(topleft=(button_x, button_y))
            #button = screen.blit(image_button, image_rect_butt)
            clock.tick(10)


            image_buttons=[]
            image_rect_butts=[]
            coords_clicer=[]
            text_mas=[]
            text_coords=[]

            if i1 < len(uroven):
                text = uroven[i1][0] + "=?"
                for i in range(len(uroven[i1][2])):
                    text_mas.append(str(uroven[i1][2][i]))  # Сохраняем текст для кнопки
                    image_buttons.append(pygame.image.load("image/play1/button.png"))

                    # Определяем координаты для отрисовки кнопок
                    if i * 170 > 440:
                        x = button_x + i * 170 - 510
                        y = button_y + 90
                    else:
                        x = button_x + i * 170
                        y = button_y

                    image_rect_butts.append(image_buttons[i].get_rect(topleft=(x, y)))
                    coords_clicer.append([x + button_width / 2-10, y + button_height / 2+440])  # Сохраняем координаты для кликов
                    text_coords.append([x + button_width / 2+50, y + button_height / 2+465])
                    if view_bar==False:
                        # Рисуем кнопку
                        screen.blit(image_buttons[i], image_rect_butts[i])
                        # Рисуем текст на кнопке
                        text_surface = font_button.render(text_mas[i], True, [0, 0, 0])
                        text_rect = text_surface.get_rect(center=text_coords[i])
                        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                # Проверка нажатия на кнопки
                if 600<=mouse_pos[1] <=640 and view_bar==True:
                    view_bar=False
                    print(view_bar)
                elif 430<=mouse_pos[1] <=455 and view_bar==False:
                    view_bar=True
                    print(view_bar)
                if view_bar==False:
                    for i in range(len(coords_clicer)):  # Проверка по всем кнопкам
                        if i>=len(coords_clicer):
                            x, y = 90,90
                        else:
                            x, y = coords_clicer[i]
                        if (
                                x <= mouse_pos[0] <= x + button_width
                                and y <= mouse_pos[1] <= y + button_height
                        ):
                            print(f"Нажата кнопка {i + 1} с ответом {text_mas[i]}")  # Debug output

                            # Обработка правильного ответа
                            if int(text_mas[i]) == uroven[i1][1]:
                                schet_dop+=1
                                print("Правильный ответ!")
                                kol+=1
                                if i1 < len(uroven) - 1:  # Увеличиваем только если не последний уровень
                                    i1 += 1
                                    nomer += 1
                                    text = uroven[i1][0] + "=?"  # Обновляем вопрос

                                    # Обновляем данные для кнопок
                                    text_mas = []
                                    image_buttons = []
                                    image_rect_butts = []
                                    coords_clicer = []
                                    text_coords = []
                                    for j in range(len(uroven[i1][2])):
                                        text_mas.append(str(uroven[i1][2][j]))
                                        image_buttons.append(pygame.image.load("image/play1/button.png"))
                                        if j * 170 > 440:
                                            x = button_x + j * 170 - 510
                                            y = button_y + 90
                                        else:
                                            x = button_x + j * 170
                                            y = button_y

                                        image_rect_butts.append(image_buttons[j].get_rect(topleft=(x, y)))
                                        coords_clicer.append([x, y])
                                        text_coords.append([x + button_width / 2, y + button_height / 2])
                                else:
                                    return str(kol)+" из "+str(len(uroven))
                            else:
                                schet_dop += 1
                                print("Неправильный ответ.")
                                if i1 < len(uroven) - 1:  # Увеличиваем только если не последний уровень
                                    i1 += 1
                                    nomer += 1
                                    text = uroven[i1][0] + "=?"  # Обновляем вопрос

                                    # Обновляем данные для кнопок
                                    text_mas = []
                                    image_buttons = []
                                    image_rect_butts = []
                                    coords_clicer = []
                                    text_coords = []
                                    for j in range(len(uroven[i1][2])):
                                        text_mas.append(str(uroven[i1][2][j]))
                                        image_buttons.append(pygame.image.load("image/play1/button.png"))
                                        if j * 170 > 440:
                                            x = button_x + j * 170 - 510
                                            y = button_y + 90
                                        else:
                                            x = button_x + j * 170
                                            y = button_y

                                        image_rect_butts.append(image_buttons[j].get_rect(topleft=(x, y)))
                                        coords_clicer.append([x, y])
                                        text_coords.append([x + button_width / 2, y + button_height / 2])
                                else:
                                    return str(kol)+" из "+str(len(uroven))
        schet_text=font.render(str(schet_dop)+schet, True, [240, 240, 220])
        rotate_schet_text=pygame.transform.rotate(schet_text, 15)
        text_urovnenia = font.render(text, True, [240, 240, 220])
        screen.blit(rotate_schet_text, [WIDTH // 2 - 20, HEIGHT // 2.2])
        screen.blit(text_urovnenia, [WIDTH//8, HEIGHT//8])
        pygame.display.flip()
