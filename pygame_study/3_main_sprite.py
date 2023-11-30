import pygame

pygame.init()    # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Name")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size    # 이미지의 크기를 구해옴
character_width = character_size[0]    # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2    # 가로 위치
character__y_pos = screen_height - character_height    # 세로 위치

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 있는지 확인 (반드시 필요)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))    # 배경 그리기

    screen.blit(character, (character_x_pos, character__y_pos))

    pygame.display.update()    # 게임화면을 다시 그리기 (반드시 필요)
       
# pygame 종료
pygame.quit()