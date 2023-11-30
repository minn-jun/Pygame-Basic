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

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 있는지 확인 (반드시 필요)
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((255, 255, 0))    # 색으로 배경 채우기
    screen.blit(background, (0, 0))    # 배경 그리기

    # 매 프레임 마다 게임 화면을 갱신해주어야 함
    pygame.display.update()    # 게임화면을 다시 그리기 (반드시 필요)
       
# pygame 종료
pygame.quit()