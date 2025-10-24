import pygame
import sqlite3
import tkinter as tk
#pygame display settings
screen_width = 500
screen_height = 500
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("clicker")

# database create file and table
con = sqlite3.connect("stats.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS scores(points REAL, perclick REAL, cps REAL, totalclicks REAL, totaltime REAL, upgrade1 REAL, upgrade2 REAL, bonus1 REAL)")

# reads the data from database
cur.execute("SELECT points, perclick, cps, totalclicks, totaltime, upgrade1, upgrade2, bonus1 FROM scores ORDER BY rowid DESC LIMIT 1")
row = cur.fetchone()

#set the variables to the read data, if there is no data than set to default values
if row:
    points, increase_on_click, clicks_per_second, totalclicks, totaltime, isupgrade1, isupgrade2, isbonus1 = row
    isupgrade1 = bool(isupgrade1)
    isupgrade2 = bool(isupgrade2)
    isbonus1 = bool(isbonus1)
else:
    points = 10000
    increase_on_click = 1
    clicks_per_second = 0
    totalclicks = 0
    totaltime = 0
    isupgrade1 = False
    isupgrade2 = False
    isbonus1 = False


#button images
mainimg = "pixil-frame-0.png"
click_img = pygame.image.load(mainimg).convert_alpha()
upgrade1 = pygame.image.load("Wooden_Sword.png").convert_alpha()
upgrade2 = pygame.image.load("Copper_Broadsword.png").convert_alpha()
click_per_sec1 = pygame.image.load("Finch_Staff.png").convert_alpha()
click_per_sec2 = pygame.image.load("Flinx_Staff.png").convert_alpha()
no = pygame.image.load("Red X.png").convert_alpha()
statimg = pygame.image.load("statsbtn.png").convert_alpha()
shackle = pygame.image.load("Shackle.png").convert_alpha()


#fonts
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
font2 = pygame.font.SysFont("Arial", 25)


#all text surfaces
text_surface = font2.render(str(points), True, (255, 255, 255))
clkl = font.render("Click For Coins", True, (255, 255, 255))
upgrades = font.render("Upgrades", True, (255, 255, 255))
auto = font.render("CPS Upgrades", True, (255, 255, 255))
bonuses = font.render("Bonuses", True, (255, 255, 255))
upgrade1_cost = font2.render("150|+1", True, (255, 255, 255))
upgrade2_cost = font2.render("500|+2", True, (255, 255, 255))
auto1 = font2.render("50|+0.25", True, (255, 255, 255))
auto2 = font2.render("150|+1", True, (255, 255, 255))
bonus1price = font2.render("1000|+10%", True, (255, 255, 255))
cps = font2.render(f"cps: {str(clicks_per_second)}", True, (255, 255, 255))
per_click = font2.render(f"Per Click: {increase_on_click}", True, (255, 255, 255))


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
screen.blit(bonuses, (220, 10))
screen.blit(bonus1price, (220,107))

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
                    global points, increase_on_click, text_surface, totalclicks
                    points += increase_on_click
                    totalclicks = int(totalclicks) + 1
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
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
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
    def bonus(self, events):
        global points, clicks_per_second, isbonus1
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= 1000 and isbonus1 == False:
                    points -= 1000
                    isbonus1 = True
                    clicks_per_second = clicks_per_second * 1.10
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def statistics(self, events):
        global totalclicks, totaltime, time1
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for event in events:
                if event.type ==pygame.MOUSEBUTTONDOWN and event.button ==1:
                    totalclicks = int(totalclicks)
                    stats_window = tk.Tk()
                    stats_window.geometry("500x500")
                    stats_window.title("statistics")
                    stats_window.configure(background="Black")
                    label = tk.Label(stats_window, text="statistics", font=("Arial", 24))
                    label.pack(padx=10, pady=10)
                    totalclk = tk.Label(stats_window, text = f"Total Clicks: {totalclicks}", font = ("Arial", 20))
                    totalclk.pack(padx=10, pady=10)
                    totaltime = int(totaltime)
                    totaltimel = tk.Label(stats_window, text = f"Total Time: {totaltime}", font = ("Arial", 20))
                    totaltimel.pack(padx=10, pady=10)
                    stats_window.mainloop()


        screen.blit(self.image, (self.rect.x, self.rect.y))
#the buttons
clickbtn = BUTTON(25, 50, click_img, 2.5, True)
upgrade1btn = BUTTON(434, 45, upgrade1, scale=1.9, held=True)
upgrade2btn = BUTTON(434, 140, upgrade2, scale=1.85, held=True)
auto1 = BUTTON(333, 45, click_per_sec1, scale=1.6, held=True)
auto2 = BUTTON(333, 140, click_per_sec2, scale=1.6, held=True)
statsbtn = BUTTON(10,368, statimg, scale=1.6, held=True)
bonus1 = BUTTON(220,45, shackle, scale=2.6, held=True)

screen.blit(upgrade1btn.image, upgrade1btn.rect)
screen.blit(statsbtn.image, statsbtn.rect)
last_update_time = pygame.time.get_ticks()

run = True
while run:
    clock.tick(60)# frame rate
    time1 = pygame.time.get_ticks() / 1000




    events = pygame.event.get()


    for event in events:
        if event.type == pygame.QUIT:
            totaltime = time1 + totaltime
            cur.execute("INSERT INTO scores (points, perclick, cps, totalclicks,totaltime, upgrade1, upgrade2, bonus1) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (points, increase_on_click, clicks_per_second, totalclicks, totaltime, isupgrade1, isupgrade2, isbonus1))
            con.commit()
            run = False

    screen.fill(pygame.Color("black"), (10, 120, 150, 80))
    per_click = font2.render(f"Per Click: {increase_on_click}", True, (255, 255, 255))
    clicks_per_second = round(clicks_per_second, 2)
    cps = font2.render(f"cps: {str(clicks_per_second)}", True, (255, 255, 255))
    screen.blit(cps, (10, 120))
    screen.blit(per_click, (10, 145))
    screen.blit(statsbtn.image, statsbtn.rect)


    clickbtn.clickbtn(events)
    upgrade1btn.upgrade1(events)
    upgrade2btn.upgrade2(events)
    auto1.per_second1(events)
    auto2.per_second2(events)
    bonus1.bonus(events)
    statsbtn.statistics(events)


    if isupgrade1:
        screen.blit(no, (434, 45))
    if isupgrade2:
        screen.blit(no, (434, 140))
    if isbonus1:
        screen.blit(no, (220, 45))

    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= 1000:
        points += clicks_per_second
        last_update_time = current_time
        screen.fill(pygame.Color("black"), (10, 10, 100, 25))
        points = round(points, 2)
        text_surface = font2.render(str(points), True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    pygame.display.update()
pygame.quit()