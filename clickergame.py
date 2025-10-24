import pygame
import sqlite3

#pygame display settings
screen_width = 500
screen_height = 500
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("clicker")

# database create file and table
con = sqlite3.connect("stats.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS scores(points REAL, perclick REAL, cps REAL, upgrade1 REAL, upgrade2 REAL)")

# reads the data from database
cur.execute("SELECT points, perclick, cps, upgrade1, upgrade2 FROM scores ORDER BY rowid DESC LIMIT 1")
row = cur.fetchone()

#set the variables to the read data, if there is no data than set to default values
if row:
    points, increase_on_click, clicks_per_second, isupgrade1, isupgrade2 = row
    isupgrade1 = bool(isupgrade1)
    isupgrade2 = bool(isupgrade2)
else:
    points = 500
    increase_on_click = 1
    clicks_per_second = 0
    isupgrade1 = False
    isupgrade2 = False


#button images
mainimg = "pixil-frame-0.png"
click_img = pygame.image.load(mainimg).convert_alpha()
upgrade1 = pygame.image.load("Wooden_Sword.png").convert_alpha()
upgrade2 = pygame.image.load("Copper_Broadsword.png").convert_alpha()
click_per_sec1 = pygame.image.load("Finch_Staff.png").convert_alpha()
click_per_sec2 = pygame.image.load("Flinx_Staff.png").convert_alpha()
no = pygame.image.load("Red X.png").convert_alpha()



#fonts
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
font2 = pygame.font.SysFont("Arial", 25)


#all text surfaces
text_surface = font2.render(str(points), True, (255, 255, 255))
clkl = font.render("Click For Coins", True, (255, 255, 255))
upgrades = font.render("Upgrades", True, (255, 255, 255))
auto = font.render("CPS Upgrades", True, (255, 255, 255))
cps = font2.render(f"cps: {str(clicks_per_second)}", True, (255, 255, 255))
per_click = font2.render(f"Per Click: {increase_on_click}", True, (255, 255, 255))
upgrade1_cost = font2.render("150|+1", True, (255, 255, 255))
upgrade2_cost = font2.render("500|+2", True, (255, 255, 255))
auto1 = font2.render("50|+0.25", True, (255, 255, 255))
auto2 = font2.render("150|+1", True, (255, 255, 255))



#renders the text surfaces on screen
screen.blit(upgrade2_cost, (434, 207))
screen.blit(auto2, (333, 207))
screen.blit(auto1, (333, 107))
screen.blit(upgrade1_cost, (434, 107))
screen.blit(per_click, (10, 145))
screen.blit(cps, (10, 120))
screen.blit(auto, (290, 10))
screen.blit(upgrades, (425, 10))
screen.blit(click_img, (0, 0))
screen.blit(clkl, (10, 100))
screen.blit(text_surface, (10, 10))

#button class
class BUTTON:
    def __init__(self, x, y, image, scale, held):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)


    #code for the main button
    def clickbtn(self, events):
        pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(pos):
                    global points, increase_on_click, text_surface
                    points += increase_on_click
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    #code for the per click1 upgrade
    def upgrade1(self, events):
        global points, increase_on_click, text_surface, mainimg, click_img, isupgrade1
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and points >=150 and isupgrade1 == 0:
                    isupgrade1 = True
                    points = float(points) - 150
                    increase_on_click = float(increase_on_click) + 1
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))

        screen.blit(self.image, (self.rect.x, self.rect.y))
    def upgrade2(self, events):
        global points, increase_on_click, text_surface, mainimg, click_img, isupgrade2
        for event in events:
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= 500 and isupgrade2 == False:
                isupgrade2 =True
                points = float(points) - 500
                increase_on_click = float(increase_on_click) + 2
                screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                text_surface = font2.render(str(points), True, (255, 255, 255))
                screen.blit(text_surface, (10, 10))

        screen.blit(self.image, (self.rect.x, self.rect.y))
    #code for the cps upgrade1
    def per_second1(self, events):
        global points, clicks_per_second, text_surface
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and points >= 50:
                    points = float(points) -50
                    clicks_per_second = float(clicks_per_second) + 0.25
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def per_second2(self, events):
        global points, clicks_per_second, text_surface
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and points >=175:
                    points = float(points) - 175
                    clicks_per_second = float(clicks_per_second) + 1
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))

#the buttons
clickbtn = BUTTON(25, 50, click_img, 2.5, True)
upgrade1btn = BUTTON(434, 45, upgrade1, scale=1.9, held=True)
upgrade2btn = BUTTON(434, 140, upgrade2, scale=1.85, held=True)
auto1 = BUTTON(333, 45, click_per_sec1, scale=1.6, held=True)
auto2 = BUTTON(333, 140, click_per_sec2, scale=1.6, held=True)
screen.blit(upgrade1btn.image, upgrade1btn.rect)

last_update_time = pygame.time.get_ticks()

run = True
while run:
    clock.tick(60)  # frame rate

    # 1️⃣ Get all events once per frame
    events = pygame.event.get()

    # 2️⃣ Handle quitting the game
    for event in events:
        if event.type == pygame.QUIT:
            run = False

          # Save to database here if needed

    screen.fill(pygame.Color("black"), (10, 120, 150, 80))
    per_click = font2.render(f"Per Click: {increase_on_click}", True, (255, 255, 255))
    cps = font2.render(f"cps: {str(clicks_per_second)}", True, (255, 255, 255))
    screen.blit(cps, (10, 120))
    screen.blit(per_click, (10, 145))


    clickbtn.clickbtn(events)
    upgrade1btn.upgrade1(events)
    upgrade2btn.upgrade2(events)
    auto1.per_second1(events)
    auto2.per_second2(events)


    if isupgrade1:
        screen.blit(no, (434, 45))
    if isupgrade2:
        screen.blit(no, (434, 140))


    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= 1000:
        points += clicks_per_second
        last_update_time = current_time
        screen.fill(pygame.Color("black"), (10, 10, 100, 25))
        text_surface = font2.render(str(points), True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    pygame.display.update()
pygame.quit()