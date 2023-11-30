import pygame

pygame.init()    # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Name")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size    # 이미지의 크기를 구해옴
character_width = character_size[0]    # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2    # 가로 위치
character_y_pos = screen_height - character_height    # 세로 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)    # 게임화면의 초당 프레임 수를 설정
    # print(f"FPS : {clock.get_fps()}")

    for event in pygame.event.get():    # 어떤 이벤트가 있는지 확인 (반드시 필요)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:    # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:    # 왼쪽 방향키
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:    # 오른쪽 방향키
                to_x += character_speed
            elif event.key == pygame.K_UP:    # 위쪽 방향키
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:    # 아래쪽 방향키
                to_y += character_speed

        if event.type == pygame.KEYUP:    # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # fps가 달라졌어도 게임속도는 동일해야 하기에 dt값을 곱함
    '''
    캐릭터가 1초 동안 100 만큼 이동을 해야 함.
    10 fps : 1초 동안 10번 동작 -> 1번에 10만큼 이동 10 * 10 = 100
    20 fps : 1초 동안 20번 동작 -> 1번에 5만큼 이동 5 * 20 = 100
    50 fps : 1초 동안 50번 동작 -> 1번에 2만큼 이동 2 * 50 = 100
    '''
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
            
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))    # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()    # 게임화면을 다시 그리기 (반드시 필요)
       
# pygame 종료
pygame.quit()