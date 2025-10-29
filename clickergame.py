import pygame
import sqlite3
import tkinter as tk


screen_width = 715
screen_height = 700
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clicker")


con = sqlite3.connect("stats.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS scores(points REAL, perclick REAL, cps REAL, totalclicks REAL, totaltime REAL, upgrade1 REAL, upgrade2 REAL,upgrade3 REAL, bonus1 REAL, bonus2 REAL, bonus3, upgrade1_price REAL, upgrade2_price REAL, upgrade3_price, auto1_price REAL, auto2_price REAL, auto3_price REAL, bonus1_price REAL, bonus2_price REAL, bonus3_price REAL, resets REAL, reset_price REAL, spent REAL, auto1_bought REAL, auto2_bought REAL, auto3_bought REAL)")


cur.execute("SELECT points, perclick, cps, totalclicks, totaltime, upgrade1, upgrade2, upgrade3, bonus1, bonus2, bonus3, upgrade1_price, upgrade2_price, upgrade3_price, auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, bonus3_price, resets, reset_price, spent , auto1_bought, auto2_bought, auto3_bought FROM scores ORDER BY rowid DESC LIMIT 1")
row = cur.fetchone()


if row:
    points, increase_on_click, clicks_per_second, totalclicks, totaltime, isupgrade1, isupgrade2, isupgrade3, isbonus1, isbonus2, isbonus3, upgrade1_price, upgrade2_price, upgrade3_price, auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, bonus3_price, resets, reset_price, spent, auto1_bought, auto2_bought, auto3_bought = row
    isupgrade1 = bool(isupgrade1)
    isupgrade2 = bool(isupgrade2)
    isupgrade3 = bool(isupgrade3)
    isbonus1 = bool(isbonus1)
    isbonus2 = bool(isbonus2)
    isbonus3 = bool(isbonus3)
    upgrade1_price = int(upgrade1_price)
    upgrade2_price = int(upgrade2_price)
    auto1_price = int(auto1_price)
    auto2_price = int(auto2_price)
    auto3_price = int(auto3_price)
    bonus1_price = int(bonus1_price)
    bonus2_price = int(bonus2_price)
    bonus3_price = int(bonus3_price)
    auto1_bought = int(auto1_bought)
    auto2_bought = int(auto2_bought)
    auto3_bought = int(auto3_bought)

else:
    points = 100000
    increase_on_click = 1
    clicks_per_second = 0
    totalclicks = 0
    totaltime = 0
    isupgrade1 = False
    isupgrade2 = False
    isupgrade3 = False
    isbonus1 = False
    isbonus2=False
    isbonus3 = False
    upgrade1_price = 150
    upgrade2_price = 500
    upgrade3_price = 2000
    auto1_price = 50
    auto2_price = 175
    auto3_price = 350
    bonus1_price = 1000
    bonus2_price = 2000
    bonus3_price = 10000
    resets = 0
    reset_price = 100000
    spent = 0
    auto1_bought = 0
    auto2_bought = 0
    auto3_bought = 0




mainimg = "pixil-frame-0.png"
click_img = pygame.image.load(mainimg).convert_alpha()
upgrade1 = pygame.image.load("Wooden_Sword.png").convert_alpha()
upgrade2 = pygame.image.load("Copper_Broadsword.png").convert_alpha()
upgrade3 = pygame.image.load("Tin_Broadsword.png").convert_alpha()
click_per_sec1 = pygame.image.load("Finch_Staff.png").convert_alpha()
click_per_sec2 = pygame.image.load("Flinx_Staff.png").convert_alpha()
click_per_sec3 = pygame.image.load("Vampire_Frog_Staff.png").convert_alpha()
no = pygame.image.load("Red X.png").convert_alpha()
statimg = pygame.image.load("statsbtn.png").convert_alpha()
reset = pygame.image.load("reset.png").convert_alpha()
shackle = pygame.image.load("Shackle.png").convert_alpha()
feral = pygame.image.load("Feral_Claws.png").convert_alpha()
wrath = pygame.image.load("Wrath_Potion.png").convert_alpha()


pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
font2 = pygame.font.SysFont("Arial", 25)



def draw():

    text_surface = font2.render(str(points), True, (255, 255, 255))
    upgrades = font.render("Upgrades", True, (255, 255, 255))
    auto = font.render("CPS Upgrades", True, (255, 255, 255))
    bonuses = font.render("Bonuses", True, (255, 255, 255))
    upgrade1_cost = font2.render(f"{upgrade1_price}|+1", True, (255, 255, 255))
    upgrade2_cost = font2.render(f"{upgrade2_price}|+1", True, (255, 255, 255))
    upgrade3_cost = font2.render(f"{upgrade3_price}|+1", True, (255, 255, 255))
    auto1l = font2.render(f"{auto1_price} | +0.25 | {auto1_bought}", True, (255, 255, 255))
    auto2l = font2.render(f"{auto2_price} | +1 | {auto2_bought}", True, (255, 255, 255))
    auto3l = font2.render(f"{auto3_price} | +2.5 | {auto3_bought}", True, (255, 255, 255))
    bonus1price = font2.render(f"{bonus1_price}|+10% CPS", True, (255, 255, 255))
    bonus2price = font2.render(f"{bonus2_price / 1000}k| +25% P/C", True, (255, 255, 255))
    bonus3price = font2.render(f"{bonus3_price / 1000}k| x2 P/C", True, (255, 255, 255))
    total_resets = font2.render(f"Resets: {resets}", True, (255, 255, 255))

    screen.blit(text_surface, (10, 10))
    screen.blit(total_resets, (600, 10))
    screen.blit(upgrades, (615, 45))
    screen.blit(upgrade1_cost, (624, 142))
    screen.blit(upgrade2_cost, (624, 242))
    screen.blit(upgrade3_cost, (620, 342))
    screen.blit(auto, (413, 45))

    screen.blit(auto1l, (413, 142))
    screen.blit(auto2l, (413, 242))
    screen.blit(auto3l, (413, 342))
    screen.blit(bonuses, (160, 45))
    screen.blit(bonus1price, (160, 142))
    screen.blit(bonus2price, (160, 242))
    screen.blit(bonus3price, (160, 342))
draw()


class BUTTON:
    def __init__(self, x, y, image, scale, held):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)



    def clickbtn(self, events):

        for event in events:
            global points, increase_on_click, text_surface, totalclicks, pos
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(pos):
                    points += increase_on_click
                    totalclicks = int(totalclicks) + 1
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def upgrade1(self, events):
        global points, spent, increase_on_click, text_surface, mainimg, click_img, isupgrade1, upgrade1_price, pos

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= upgrade1_price and isupgrade1 == 0:
                    isupgrade1 = True
                    points = float(points) - upgrade1_price
                    increase_on_click = float(increase_on_click) + 1
                    spent = spent + upgrade1_price
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))


        screen.blit(self.image, (self.rect.x, self.rect.y))
    def upgrade2(self, events):
        global points, spent, increase_on_click, text_surface, mainimg, click_img, isupgrade2, upgrade2_price, pos

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type ==pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= upgrade2_price and isupgrade2 == False:
                    isupgrade2 =True
                    points = float(points) - upgrade2_price
                    increase_on_click = float(increase_on_click) + 1
                    spent = spent + upgrade2_price
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))

        screen.blit(self.image, (self.rect.x, self.rect.y))
    def upgrade3(self, events):
        global points, spent, increase_on_click, text_surface, mainimg, click_img, isupgrade3, upgrade3_price, pos

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and points >= upgrade3_price:
                    isupgrade3 = True
                    points = float(points) - upgrade3_price
                    increase_on_click = float(increase_on_click) + 1
                    spent = spent + upgrade3_price
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def per_second1(self, events):
        global points, spent, clicks_per_second, text_surface, auto1_price, pos, auto1_bought

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and points >= auto1_price:
                    points = float(points) - auto1_price
                    clicks_per_second = float(clicks_per_second) + 0.25
                    spent = spent + auto1_price
                    auto1_bought += 1
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
                    auto1l = font2.render(f"{auto1_price} | +0.25 | {auto1_bought}", True, (255, 255, 255))
                    screen.fill(pygame.Color("Black"), (413, 142, 140, 30))
                    screen.blit(auto1l, (413, 142))

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def per_second2(self, events):
        global points, spent, clicks_per_second, text_surface, auto2_price, pos, auto2_bought

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= auto2_price:
                    points = float(points) - auto2_price
                    clicks_per_second = float(clicks_per_second) + 1
                    spent = spent + auto2_price
                    auto2_bought += 1
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
                    screen.fill(pygame.Color("Black"), (413, 242, 140, 30))
                    auto2l = font2.render(f"{auto2_price} | +1 | {auto2_bought}", True, (255, 255, 255))
                    screen.blit(auto2l, (413, 242))
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def per_second3(self, events):
        global points, spent, clicks_per_second, text_surface, auto3_price, pos, auto3_bought

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and points >= auto3_price:
                    points = float(points) - auto3_price
                    clicks_per_second = float(clicks_per_second) + 2.5
                    spent = spent + auto3_price
                    auto3_bought += 1
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
                    screen.fill(pygame.Color("Black"), (413, 342, 140, 30))
                    auto3l = font2.render(f"{auto3_price} | +2.5 | {auto3_bought}", True, (255, 255, 255))
                    screen.blit(auto3l, (413, 342))
        screen.blit(self.image, (self.rect.x, self.rect.y))





    def bonus1(self, events):
        global points, spent, clicks_per_second, isbonus1, bonus1_price, pos

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= bonus1_price and isbonus1 == False:
                    points -= bonus1_price
                    isbonus1 = True
                    clicks_per_second = clicks_per_second + 10/100
                    spent = spent + bonus1_price
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def bonus2(self, events):
        global points, spent, increase_on_click, isbonus2, bonus2_price, pos
        if self.rect.collidepoint(pos):
            for event in events:
                if event.type ==pygame.MOUSEBUTTONDOWN and event.button == 1 and points >= bonus2_price and isbonus2 == False:
                    isbonus2 = True
                    points = float(points) - bonus2_price
                    increase_on_click = increase_on_click + (increase_on_click * 25/100)
                    spent = spent + bonus2_price
                    screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                    points = round(points, 1)
                    text_surface = font2.render(str(points), True, (255, 255, 255))
                    screen.blit(text_surface, (10, 10))
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def bonus3(self, events):
        global points, spent, increase_on_click, isbonus3, bonus3_price, pos
        if self.rect.collidepoint(pos):
            if event.type==pygame.MOUSEBUTTONDOWN and event.button ==1 and points >= bonus3_price and isbonus3 == False:
                isbonus3 = True
                points = float(points) - bonus3_price
                spent = spent + bonus3_price
                increase_on_click = increase_on_click * 2
                points = round(points, 1)
                screen.fill(pygame.Color("black"), (10, 10, 100, 25))
                text_surface = font2.render(str(points), True, (255, 255, 255))
                screen.blit(text_surface, (10, 10))


        screen.blit(self.image, (self.rect.x, self.rect.y))

    def statistics(self, events):
        global totalclicks, totaltime, time1, pos, spent

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type ==pygame.MOUSEBUTTONDOWN and event.button ==1:
                    stats_window = tk.Tk()
                    stats_window.geometry("500x500")
                    stats_window.title("Statistics")
                    stats_window.configure(background="Black")
                    label = tk.Label(stats_window, text="Statistics", font=("Arial", 24))
                    label.pack(padx=10, pady=10)
                    totalclk = tk.Label(stats_window, text = f"Total Clicks: {int(totalclicks)}", font = ("Arial", 20))
                    totalclk.pack(padx=10, pady=10)
                    totaltimel = tk.Label(stats_window, text = f"Total Time: {int(totaltime)} Seconds", font = ("Arial", 20))
                    totaltimel.pack(padx=10, pady=10)
                    total_spent = tk.Label(stats_window, text = f"Total Spent: {int(spent)}", font = ("Arial", 20))
                    total_spent.pack(padx=10, pady=10)
                    stats_window.mainloop()


    def reset(self, events):
        global pos, running, reset_price, points, close

        if self.rect.collidepoint(pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    close=False
                    reset_window = tk.Tk()
                    reset_window.geometry("500x400")
                    reset_window.title("Reset")
                    reset_window.configure(background="Black")
                    reset_label = tk.Label(text="Reset To Gain A Permanent Discount", font=("Arial", 20))
                    reset_label.pack(padx=10, pady=5)
                    info_label1 = tk.Label(text="This Will Reset Everything!", font=("Arial", 20))
                    info_label1.pack(padx=10, pady=20)
                    info_label2 = tk.Label(reset_window, text="You Will Now Have A", font=("Arial", 20))
                    info_label2.pack(padx=10)
                    info_label3 = tk.Label(text="10% Discount On All Upgrades", font=("Arial", 20))
                    info_label3.pack(padx=10)
                    cost_label = tk.Label(reset_window, text=f"Cost: {reset_price}", font=("Arial", 20))
                    cost_label.pack(padx=10, pady=10)
                    if points < reset_price:
                        not_enough = tk.Label(text="Not Enough Points", font = ("Arial", 16))
                        not_enough.pack(padx=10, pady=20)
                    def doreset():
                        global close, spent, points, increase_on_click, clicks_per_second, isbonus1, isbonus2, isbonus3, isupgrade1, isupgrade2, isupgrade3, upgrade1_price, upgrade2_price, upgrade3_price, auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, bonus3_price, resets, reset_price, reset_window, run, totaltime, time1
                        if points >= reset_price:
                            totaltime = time1 + totaltime
                            points = 0
                            increase_on_click = 1
                            clicks_per_second = 0
                            isupgrade1 = False
                            isupgrade2 = False
                            isupgrade3 = False
                            isbonus1 = False
                            isbonus2 = False
                            isbonus3 = False

                            upgrade1_price -= (upgrade1_price * 10/100)
                            upgrade2_price -= (upgrade2_price * 10/100)
                            upgrade3_price -= (upgrade3_price * 10/100)
                            auto1_price -= (auto1_price * 10/100)
                            auto2_price -= (auto2_price * 10/100)
                            auto3_price -= (auto3_price * 10/100)
                            bonus1_price -= (bonus1_price * 10/100)
                            bonus2_price -= (bonus2_price * 10/100)
                            bonus3_price -= (bonus3_price * 10/100)
                            resets += 1
                            reset_price += (reset_price * 50/100)
                            spent = spent + reset_price
                            screen.fill(pygame.Color("black"), (160, 45, 700, 700))

                            upgrade1_price = int(upgrade1_price)
                            upgrade2_price = int(upgrade2_price)
                            upgrade3_price = int(upgrade3_price)
                            auto1_price = int(auto1_price)
                            auto2_price = int(auto2_price)
                            auto3_price = int(auto3_price)
                            bonus1_price = int(bonus1_price)
                            bonus2_price = int(bonus2_price)
                            resets = int(resets)

                            draw()
                            cur.execute(
                                "INSERT INTO scores (points, perclick, cps, totalclicks, totaltime, upgrade1, upgrade2, upgrade3, bonus1, bonus2, upgrade1_price, upgrade2_price, upgrade3_price, auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, resets, reset_price, spent, auto1_bought, auto2_bought, auto3_bought) "
                                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (points, increase_on_click, clicks_per_second, totalclicks, totaltime, isupgrade1,
                                 isupgrade2, isupgrade3, isbonus1, isbonus2, upgrade1_price, upgrade2_price, upgrade3_price,
                                 auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, resets, reset_price, spent,
                                 auto1_bought, auto2_bought, auto3_bought))
                            con.commit()
                            close=True


                    reset_button = tk.Button(reset_window, text="Reset", font=("Arial", 20), command = doreset)
                    reset_button.pack(padx=10, pady=10, side="bottom", anchor="center")


                    reset_window.mainloop()
        screen.blit(self.image, (self.rect.x, self.rect.y))



        screen.blit(self.image, (self.rect.x, self.rect.y))

clickbtn = BUTTON(25, 80, click_img, 4, True)
upgrade1btn = BUTTON(624, 80, upgrade1, scale=1.9, held=True)
upgrade2btn = BUTTON(624, 175, upgrade2, scale=1.85, held=True)
upgrade3btn = BUTTON(624, 270, upgrade3, scale=1.9, held=True)
auto1 = BUTTON(413, 80, click_per_sec1, scale=1.6, held=True)
auto2 = BUTTON(413, 175, click_per_sec2, scale=1.6, held=True)
auto3 = BUTTON(413, 270, click_per_sec3, scale=1.6, held=True)
statsbtn = BUTTON(10,625, statimg, scale=1.5, held=True)
reset = BUTTON(597, 610, reset, scale=2, held=True)
bonus1 = BUTTON(190,80, shackle, scale=2.6, held=True)
bonus2 = BUTTON(190, 175, feral, scale=2.6, held=True)
bonus3 = BUTTON(190, 270, wrath, 2.6, True)

screen.blit(upgrade1btn.image, upgrade1btn.rect)
screen.blit(statsbtn.image, statsbtn.rect)
last_update_time = pygame.time.get_ticks()
#
running = True
while running:
    clock.tick(60)
    pos = pygame.mouse.get_pos()
    time1 = pygame.time.get_ticks() / 1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or running==False:
            totaltime = time1 + totaltime
            cur.execute(
                "INSERT INTO scores (points, perclick, cps, totalclicks, totaltime, upgrade1, upgrade2, upgrade3, bonus1, bonus2, bonus3, upgrade1_price, upgrade2_price, upgrade3_price, auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, bonus3_price, resets, reset_price, spent, auto1_bought, auto2_bought, auto3_bought) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (points, increase_on_click, clicks_per_second, totalclicks, totaltime, isupgrade1,
                 isupgrade2, isupgrade3, isbonus1, isbonus2, isbonus3, upgrade1_price, upgrade2_price, upgrade3_price,
                 auto1_price, auto2_price, auto3_price, bonus1_price, bonus2_price, bonus3_price, resets, reset_price, spent,
                 auto1_bought, auto2_bought, auto3_bought))
            con.commit()
            running = False

    screen.fill(pygame.Color("black"), (160, 0, 700, 34))
    resets = int(resets)
    total_resets = font2.render(f"Resets: {resets}", True, (255, 255, 255))
    screen.blit(total_resets, (600, 10))
    points = round(points, 1)
    per_click = font2.render(f"Per Click: {increase_on_click}", True, (255, 255, 255))
    clicks_per_second = round(clicks_per_second, 2)
    cps = font2.render(f"CPS: {str(clicks_per_second)}", True, (255, 255, 255))
    screen.blit(cps, (160, 10))
    screen.blit(per_click, (375, 10))
    screen.blit(statsbtn.image, statsbtn.rect)


    clickbtn.clickbtn(events)
    upgrade1btn.upgrade1(events)
    upgrade2btn.upgrade2(events)
    upgrade3btn.upgrade3(events)
    auto1.per_second1(events)
    auto2.per_second2(events)
    auto3.per_second3(events)
    bonus1.bonus1(events)
    bonus2.bonus2(events)
    bonus3.bonus3(events)
    statsbtn.statistics(events)
    reset.reset(events)


    if isupgrade1:
        screen.blit(no, (624, 80))
    if isupgrade2:
        screen.blit(no, (624, 175))
    if isupgrade3:
        screen.blit(no, (624, 270))
    if isbonus1:
        screen.blit(no, (190, 80))
    if isbonus2:
        screen.blit(no, (190, 175))
    if isbonus3:
        screen.blit(no, (188,280))

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