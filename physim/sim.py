from turtle import width
import pygame
import math


def main():
        #basic initialisation
        WIDTH = 600
        HEIGHT = 600 
        FPS = 60
        running = True
        pygame.init()
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        clock = pygame.time.Clock()
        time_step = 1/FPS


        class Particle():
            def __init__(self,ini_x_pos,ini_y_pos,ini_velocity):
                self.ini_x_pos = ini_x_pos
                self.ini_y_pos = ini_y_pos
                self.x_pos = 0
                self.y_pos = 0
                self.ini_velocity = ini_velocity
                
            def create_particle(self):
                pygame.draw.circle(screen, (255,255,255),(self.ini_x_pos,self.ini_y_pos),15,1)
            def update_position(self):
                vx_vector,vy_vector = self.ini_velocity
                self.ini_x_pos += vx_vector*time_step
                self.ini_y_pos += vy_vector*time_step
                pygame.draw.circle(screen, (255,255,255),(self.ini_x_pos,self.ini_y_pos),15,1)
                
        #to store all the particle that are created during program execution
        particle_list = []
        while running:
            # clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    particle = Particle(x,y,(10,10))
                    particle.create_particle()
                    particle_list.append(particle)
            if particle_list:
                for particle in particle_list:
                    particle.update_position()
            pygame.display.flip()
            screen.fill((0,0,0))


if __name__ == '__main__':
    main()