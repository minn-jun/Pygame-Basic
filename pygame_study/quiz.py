'''
Quiz) 하늘에서 떨어지는 물체 피하기

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 떨어지는 물체는 화면 가장 위에서 떨어짐. X 좌표는 매번 랜덤으로 설정
3. 캐릭터가 물체를 피하면 다음 물체가 다시 떨어짐
4. 캐릭터가 물체와 충돌하면 게임 종료
5. fps는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 물체 : 70 * 70 - enemy.png
'''

import pygame
from random import randint

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Avoid Object")

fps = pygame.time.Clock()

background = pygame.image.load("background.png")

char = pygame.image.load("character.png")
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x = (screen_width - char_width) / 2
char_y = screen_height - char_height
char_to_x = 0
char_speed = 0.5

obj = pygame.image.load("enemy.png")
obj_size = obj.get_rect().size
obj_width = obj_size[0]
obj_height = obj_size[1]
obj_x = randint(0, screen_width - obj_width)
obj_y = 0
obj_speed = 0.5

running = True
while running:
    dt = fps.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_to_x -= char_speed
            elif event.key == pygame.K_RIGHT:
                char_to_x += char_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char_to_x = 0

    char_x += char_to_x * dt
    if char_x < 0:
        char_x = 0
    elif char_x > screen_width - char_width:
        char_x = screen_width - char_width

    obj_y += obj_speed * dt
    if obj_y > screen_height:
        obj_x = randint(0, screen_width - obj_width)
        obj_y = 0
    
    char_rect = char.get_rect()
    char_rect.left = char_x
    char_rect.top = char_y
    
    obj_rect = obj.get_rect()
    obj_rect.left = obj_x
    obj_rect.top = obj_y

    if char_rect.colliderect(obj_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(char, (char_x, char_y))
    screen.blit(obj, (obj_x, obj_y))
    
    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()
