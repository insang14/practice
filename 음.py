from board import boards
#pygame 가져오기
import pygame

pygame.init()

#게임 메인화면 설정
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('FreeSansBold.ttf', 20)
level = boards
#보드의 흰색 점들.
def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i*num1 + (0.5*num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5*num2), i*num1 + (0.5*num1)), 10)            


run = True 
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()
    #창 종료전까지 실행시키기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()