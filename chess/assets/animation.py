import tkinter as tk
from time import time, sleep
from random import choice, uniform, randint
from math import sin, cos, radians


colors = ['red', 'blue', 'yellow', 'white', 'green', 'orange', 'purple', 'seagreen','indigo', 'cornflowerblue']

class FireWork:
    def __init__(self, root, frame, end) -> None:
        self.root = root
        self.frame = frame
        self.end = end
        self.time = time()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.after(100, self.simulate)

    def simulate(self):
        t = time()
        explode_points = []
        wait_time = randint(10,100)
        numb_explode = randint(10,15)
        for point in range(numb_explode):
            objects = []
            x_cordi = randint(0, int(self.frame['width']))
            y_cordi = randint(0, int(self.frame['height']))
            speed = uniform (0.5, 1.5)          
            size = uniform (2,7)
            color = choice(colors)
            explosion_speed = uniform(2, 3)
            total_particles = randint(10,50)
            for i in range(1,total_particles):
                r = self.Particle(self.frame, id_fire = i, total = total_particles, explosion_speed = explosion_speed, x = x_cordi, y = y_cordi, 
                    vx = speed, vy = speed, color=color, size = size, lifespan = uniform(0.6,1.75))

                objects.append(r)

            explode_points.append(objects)

        total_time = .0
        while total_time < 1.8:
            sleep(0.01)
            tnew = time()
            t, dt = tnew, tnew - t
            for point in explode_points:
                for item in point: item.update(dt)

            self.frame.update()
            total_time += dt
        

        if tnew - self.time >= self.end: 
            self.close()
            return

        self.root.after(wait_time, self.simulate)


    def close(self, *ignore):
        self.root.quit()


    class Particle:
        def __init__(self, canv, id_fire, total, explosion_speed, x=0., y=0., vx = 0., vy = 0., size=0., color = 'red', lifespan = 2, **_):
            self.id = id_fire
            self.x = x
            self.y = y
            self.initial_speed = explosion_speed
            self.vx = vx
            self.vy = vy
            self.total = total
            self.age = 0
            self.color = color
            self.cv = canv
            self.cid = self.cv.create_oval(x - size, y - size, x + size, y + size, fill=self.color)
            self.lifespan = lifespan

        def update(self, dt):
            self.age += dt

            if (self.age <= 5) and (self.age <= self.lifespan):
                move_x = cos(radians(self.id*360/self.total))*self.initial_speed
                move_y = sin(radians(self.id*360/self.total))*self.initial_speed
                self.cv.move(self.cid, move_x, move_y)
                self.vx = move_x/(float(dt)*1000)

            elif self.cid is not None:
                self.cv.delete(self.cid)
                self.cid = None
