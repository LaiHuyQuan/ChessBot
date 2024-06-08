import pygame, sys, subprocess
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
SQUARE_SIZE = 90
BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(None, size)

def play_chess():
    options_menu_visible = True
    while options_menu_visible:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(100).render("OPTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(1280 // 2, 100))

        PLAYER_VS_PLAYER_BUTTON = Button(image=None, pos=(1280 // 2, 250),
                                        text_input="Player vs Player", font=get_font(75), base_color="White",
                                        hovering_color="Green")

        PLAYER_VS_AI_BUTTON = Button(image=None, pos=(1280 // 2, 400),
                                    text_input="Player vs AI", font=get_font(75), base_color="White",
                                    hovering_color="Green")

        BACK_BUTTON = Button(image=None, pos=(1280 // 2, 550),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        for button in [PLAYER_VS_PLAYER_BUTTON, PLAYER_VS_AI_BUTTON, BACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_VS_PLAYER_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    subprocess.run(["python", "ChessMain1.py"])  # Chế độ chơi với người
                    options_menu_visible = False
                elif PLAYER_VS_AI_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    subprocess.run(["python", "ChessMain.py"])  # Chế độ chơi với máy
                    options_menu_visible = False
                elif BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    options_menu_visible = False

        pygame.display.update()

def show_guide():

    guide_visible = True
    while guide_visible:
        GUIDE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        GUIDE_TEXT = get_font(100).render("GUIDE", True, "#b68f40")
        GUIDE_RECT = GUIDE_TEXT.get_rect(center=(1280 // 2, 100))

        SCREEN.blit(GUIDE_TEXT, GUIDE_RECT)

        # Hiển thị nội dung hướng dẫn
        instruction_text1 = get_font(40).render("Press 'z' or click", True, "White")
        icon1 = pygame.image.load('images/return2.png')  # Đường dẫn đến biểu tượng 1
        icon1 = pygame.transform.scale(icon1, (40, 40))  # Điều chỉnh kích thước hình ảnh
        instruction_text3 = get_font(40).render("to undo your move", True, "White")

        instruction_text2 = get_font(40).render("Press 'r' or click", True, "White")
        icon2 = pygame.image.load('images/reset.png')  # Đường dẫn đến biểu tượng 2
        icon2 = pygame.transform.scale(icon2, (40, 40))  # Điều chỉnh kích thước hình ảnh
        instruction_text4 = get_font(40).render("to reset the game", True, "White")



        instruction_rect1 = instruction_text1.get_rect(midright=(1280 // 2, 250))
        icon_rect1 = icon1.get_rect(midleft=(instruction_rect1.right + 10, instruction_rect1.centery))
        instruction_rect3 = instruction_text3.get_rect(midleft=(icon_rect1.right + 10, 250))
        instruction_rect2 = instruction_text2.get_rect(midright=(1280 // 2, 400))
        icon_rect2 = icon2.get_rect(midleft=(instruction_rect2.right + 10, instruction_rect2.centery))
        instruction_rect4 = instruction_text4.get_rect(midleft=(icon_rect2.right + 10, 400))

        SCREEN.blit(instruction_text1, instruction_rect1)
        SCREEN.blit(icon1, icon_rect1)
        SCREEN.blit(instruction_text3, instruction_rect3)
        SCREEN.blit(instruction_text2, instruction_rect2)
        SCREEN.blit(icon2, icon_rect2)
        SCREEN.blit(instruction_text4, instruction_rect4)

        # BACK
        BACK_BUTTON = Button(image=None, pos=(1280 // 2, 550),
                             text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        BACK_BUTTON.changeColor(GUIDE_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(GUIDE_MOUSE_POS):
                    guide_visible = False


        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        GUIDE_BUTTON = Button(image=pygame.image.load("assets/Guide.png"), pos=(640, 400),
                              text_input="GUIDE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_chess()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    show_guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()