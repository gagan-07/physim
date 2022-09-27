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
                self.x = 0
                self.radius =  19
                
            def create_particle(self):
                pygame.draw.circle(screen, (255,255,255),(self.ini_x_pos,self.ini_y_pos),self.radius,1)
            def update_position(self):
                vx_vector,vy_vector = self.ini_velocity
                self.ini_x_pos += vx_vector*time_step
                self.ini_y_pos += vy_vector*time_step
                pygame.draw.circle(screen, (255,255,255),(self.ini_x_pos,self.ini_y_pos),self.radius,1)

                
        #to store all the particle that are created during program execution
        particle_list = []
        button_up = False
        while running:
            # clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_up = False
                    x,y = pygame.mouse.get_pos()
                    if not button_up:
                        pygame.draw.circle(screen,(255,255,255),(x,y),10,6)
                        print("this ran!")
                    # particle = Particle(x,y,(-10,0))
                    # particle.create_particle()
                    # particle_list.append(particle)
                if event.type == pygame.MOUSEBUTTONUP:
                    button_up = True
                    x1,y1  = pygame.mouse.get_pos()
                    velocity = (x-x1,y-y1)
                    particle = Particle(x,y,velocity)
                    particle.create_particle()
                    particle_list.append(particle)

            if particle_list:
                for particle in particle_list:
                    x_constraint = particle.ini_x_pos - WIDTH
                    y_constraint = particle.ini_y_pos - HEIGHT
                    
                    if x_constraint < -(particle.radius+WIDTH) or x_constraint > (particle.radius) or y_constraint > (particle.radius) or y_constraint < -(particle.radius+HEIGHT):
                        particle_list.remove(particle)
                    else:
                        particle.update_position()
            print(particle_list)
            pygame.display.flip()
            # screen.fill((0,0,0))


if __name__ == '__main__':
    main()