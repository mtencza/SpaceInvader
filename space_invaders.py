import tkinter as tk
import sys
import random

class SpaceInvaders:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders")

        # Set up the canvas
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(370, 580, 430, 590, fill="white")
        #print(self.canvas.coords(self.player)) 
        #self.bullet = self.canvas.create_rectangle(395, 565, 405, 575, fill="white")
        

        self.bullets = []


        self.enemies = []

        self.initialize_enemies()

        # Bind the keyboard events
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)
        
        self.play_game()


    def move_left(self, event):
        player_coords = self.canvas.coords(self.player)
        if((player_coords[0] - 20) > 0):
            self.canvas.move(self.player, -10, 0)

    def move_right(self, event):
        player_coords = self.canvas.coords(self.player)
        if((player_coords[2] + 20) < 800):
            self.canvas.move(self.player, 10, 0)
        

    def shoot(self, event):
        cur_player_coords = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(cur_player_coords[0] + 25, cur_player_coords[1] - 15, cur_player_coords[2] - 25, cur_player_coords[3] - 15, fill="white")
        self.bullets.append(bullet)
        self.move_bullet(bullet)

    def move_bullet(self, bullet):
        yValDiff = -5
        bullet_coords = self.canvas.coords(bullet)

        if not bullet_coords:
            test = 1
        elif bullet_coords[3] > 0:  # Continue moving the bullet until it reaches the top
            self.canvas.move(bullet, 0, yValDiff)
            self.is_collision_with_enemy(bullet)
            self.root.after(20, self.move_bullet, bullet) #this controls bullet speed
        else:
            self.canvas.delete(bullet)  # Remove the bullet when it reaches the top


    def is_collision_with_enemy(self, bullet):
        bullet_coords = self.canvas.coords(bullet)
        for enemy in self.enemies:
            enemy_coords = self.canvas.coords(enemy)
            if (self.is_y_collision(enemy_coords, bullet_coords)) and (self.is_x_collision(enemy_coords, bullet_coords)): 
                self.canvas.delete(bullet) #eventually will be destroying enemy and prob bullet, maybe with animation 
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)


    def is_x_collision(self, enemy_coords, bullet_coords):
        
        # bullet.x0 > enemy.x0 and bullet.x1 < enemy.x1
        # if (bullet_coords[0] > enemy_coords[0]) or (bullet_coords[2] < enemy_coords[2]):
        if (self.is_interval_overlap(bullet_coords[0], bullet_coords[2], enemy_coords[0], enemy_coords[2])):
            print('------------- x collision ----------------')
            self.coordify('Enemy', enemy_coords)
            self.coordify('Bullet', bullet_coords)

            #sys.exit()
            return True
        else:
            return False



    def is_y_collision(self, enemy_coords, bullet_coords):
        print(enemy_coords)
        if(enemy_coords[3] > bullet_coords[1]): #y1 is bottom, y0 is top
            # print('bullet y0 ', bullet_coords[1], ' enemy y0 ', enemy_coords[1], ' bullet y1 ', bullet_coords[3], ' enemy y1 ', enemy_coords[3])
            print('------------- y collision ----------------')
            self.coordify('Enemy', enemy_coords)
            self.coordify('Bullet', bullet_coords)
            return True
        else:
            return False

    # Determines if [aX0, aX1] is an overlapping interval with [bX0, bX1]
    def is_interval_overlap(self, aX0, aX1, bX0, bX1):
        return (self.is_in_range(aX0, bX0, bX1) or self.is_in_range(aX1, bX0, bX1))

    def is_in_range(self, x, rangeStart, rangeEnd):
        return (x > rangeStart and x < rangeEnd)

    def initialize_enemies(self):
        #enemy = self.canvas.create_rectangle(391, 20, 411, 40)
        enemy = self.canvas.create_rectangle(391, 40, 411, 60)
        self.enemies.append(enemy)

        enemy = self.canvas.create_rectangle(271, 60, 291, 80)
        self.enemies.append(enemy)
        
        enemy = self.canvas.create_rectangle(471, 30, 491, 50)
        self.enemies.append(enemy)

        enemy = self.canvas.create_rectangle(610, 70, 630, 90)
        self.enemies.append(enemy)

        enemy = self.canvas.create_rectangle(660, 40, 680, 60)
        self.enemies.append(enemy)


    def move_enemies(self):
        yValDiff = 8
        randomEnemyIndex = random.randint(0, len(self.enemies) - 1)
        self.canvas.move(self.enemies[randomEnemyIndex], random.randint(-15, 15), yValDiff)

    def coordify(self, title, coords):
        x0 = coords[0]
        y0 = coords[1]
        x1 = coords[2]
        y1 = coords[3]
        formattedStr = f"[{title}] 0: ({x0},{y0}), 1: ({x1},{y1})"
        print(formattedStr)


    def play_game(self):
        #do some state updating
        
        
        #print("test")
        #self.play_game()
        #game loop this bitch
        self.root.after(100, self.play_game)
        #self.root.after(50, self.move_enemies)
        
        self.move_enemies()
        


if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)
    root.mainloop()









