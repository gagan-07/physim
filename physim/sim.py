from turtle import width
import pygame
import math


def main():
        #basic initialisation
        WIDTH = 600
        HEIGHT = 600
        FPS = 100
        running = True
        pygame.init()
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        clock = pygame.time.Clock()
        time_step = 1/(FPS)
        
        #gravitational constant
        G = 9.89

        class Particle():
            def __init__(self,ini_x_pos,ini_y_pos,ini_velocity):
                self.ini_x_pos = ini_x_pos
                self.ini_y_pos = ini_y_pos
                self.x_pos = 0
                self.y_pos = 0
                self.ini_velocity = ini_velocity
                self.x = 0
                self.radius =  15
                self.density = 0.78
                self.mass = self.density * (4/3)*math.pi*(self.radius**3)
                self.wall_pen= True
                self.gravity = True
            def create_particle(self):
                pygame.draw.circle(screen, (255,255,255),(self.ini_x_pos,self.ini_y_pos),self.radius,1)
            def update_position(self):
                if self.wall_pen:
                    width_value = self.ini_x_pos + self.radius
                    height_value = self.ini_y_pos + self.radius
                    if width_value >= WIDTH or self.ini_x_pos-self.radius <= 0:
                        self.ini_velocity[0] = -1*self.ini_velocity[0]
                    if height_value >= HEIGHT or self.ini_y_pos-self.radius <= 0:
                        self.ini_velocity[1] = -1*self.ini_velocity[1]
                        print("the velocity of particle in y direction is " + str(self.ini_velocity[1]))
                

                vx_vector,vy_vector = self.ini_velocity
                if self.gravity:
                    self.ini_velocity[1] += G*time_step
                self.ini_x_pos += vx_vector*time_step
                self.ini_y_pos += vy_vector*time_step
                pygame.draw.circle(screen, (255,255,255),(self.ini_x_pos,self.ini_y_pos),self.radius,1)

        def collision_detection(particle_list):
            for particle in particle_list:
                for particle2 in particle_list:
                    if particle != particle2:
                        if ((particle.ini_x_pos-particle2.ini_x_pos)**2 +  (particle.ini_y_pos-particle2.ini_y_pos)**2)**0.5  < (particle.radius + particle2.radius):
                            # particle.ini_x_pos -= particle.ini_velocity[0]*time_step
                            # particle.ini_y_pos -= particle.ini_velocity[1]*time_step
                            # particle2.ini_x_pos -= particle2.ini_velocity[0]*time_step
                            # particle2.ini_y_pos -= particle2.ini_velocity[1]*time_step
                            inter_radius_dist = math.sqrt((particle.ini_x_pos-particle2.ini_x_pos)**2 +  (particle.ini_y_pos-particle2.ini_y_pos)**2)
                            inter_dist = particle.radius + particle2.radius - inter_radius_dist
                            slope = (particle2.ini_y_pos-particle.ini_y_pos)/(particle2.ini_x_pos-particle.ini_x_pos)
                            inter_radius_angle = math.atan(slope)
                            particle1_adjusment =((particle.radius-inter_dist)/(particle.radius+particle2.radius))*inter_dist
                            particle2.adjustment = ((inter_dist+particle2.radius)/particle.radius+particle2.radius)*inter_dist
                            particle.ini_x_pos -= particle1_adjusment*math.cos(inter_radius_angle)
                            particle.ini_y_pos -= particle1_adjusment*math.sin(inter_radius_angle)
                            particle2.ini_x_pos += particle1_adjusment*math.cos(inter_radius_angle) 
                            particle2.ini_y_pos += particle1_adjusment*math.sin(inter_radius_angle)
                            vector1,vector2 = particle.ini_velocity,particle2.ini_velocity
                            dot_product = (vector1[0]*vector2[0]+vector1[1]*vector2[1])/(math.sqrt(vector1[0]**2+vector1[1]**2)*math.sqrt(vector2[0]**2+vector2[1]**2)+0.000001)
                            # print("the dot product is " + str(dot_product))
                            angle = 57.2958*math.acos(dot_product)
                            particle_angle = particle.ini_velocity[1]/(particle.ini_velocity[0]+0.00001)
                            particle2_angle = particle2.ini_velocity[1]/(particle2.ini_velocity[0]+0.0001)
                            vector1_angle = math.atan(particle_angle)*57.2958
                            vector2_angle = math.atan(particle2_angle)*57.2958
                            def unresolved_vel(vector):
                                return math.sqrt(vector[0]**2+vector[1]**2)
                            particle.ini_velocity[0] = (unresolved_vel(particle.ini_velocity)*math.cos(vector1_angle-angle)*(particle.mass-particle2.mass)*math.cos(angle)+2*particle2.mass*unresolved_vel(particle2.ini_velocity)*math.cos(vector2_angle-angle)*math.cos(angle))/(particle.mass+particle2.mass)+unresolved_vel(particle.ini_velocity)*math.sin(vector1_angle-angle)*math.cos(angle+90)
                            particle.ini_velocity[1] = (unresolved_vel(particle.ini_velocity)*math.cos(vector1_angle-angle)*(particle.mass-particle2.mass)*math.sin(angle)+2*particle2.mass*unresolved_vel(particle2.ini_velocity)*math.cos(vector2_angle-angle)*math.sin(angle))/(particle.mass+particle2.mass)+unresolved_vel(particle.ini_velocity)*math.sin(vector1_angle-angle)*math.sin(angle+90)
                            
                            particle2.ini_velocity[0] = (unresolved_vel(particle2.ini_velocity)*math.cos(vector2_angle-angle)*(particle.mass-particle.mass)*math.cos(angle)+2*particle.mass*unresolved_vel(particle.ini_velocity)*math.cos(vector1_angle-angle)*math.cos(angle))/(particle.mass+particle.mass)+unresolved_vel(particle2.ini_velocity)*math.sin(vector2_angle-angle)*math.cos(angle+90)
                            particle2.ini_velocity[1] = (unresolved_vel(particle2.ini_velocity)*math.cos(vector2_angle-angle)*(particle.mass-particle.mass)*math.sin(angle)+2*particle.mass*unresolved_vel(particle.ini_velocity)*math.cos(vector1_angle-angle)*math.sin(angle))/(particle.mass+particle.mass)+unresolved_vel(particle2.ini_velocity)*math.sin(vector2_angle-angle)*math.sin(angle+90)
                            
        #to store all the particle that are created during program execution
        particle_list = []
        button_up = False
        x,y=(None,None)
        while running:
            # clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_up = False
                    x,y = pygame.mouse.get_pos()
                    if not button_up:
                        pygame.draw.circle(screen,(255,255,255),(x,y),5,6)
                if event.type == pygame.MOUSEBUTTONUP:
                    button_up = True
                    x1,y1  = pygame.mouse.get_pos()
                    velocity = [(x-x1)*0.01*FPS,0.01*FPS*(y-y1)]
                    particle = Particle(x,y,velocity)
                    particle.create_particle()
                    particle_list.append(particle)
                    x=None

            if x!=None:
                mouse_pos = pygame.mouse.get_pos()
                distance = (((x-mouse_pos[0])**2+(y-mouse_pos[1])**2)**0.5)
                pygame.draw.circle(screen,(255,255,255),(x,y),15,1)
                
                pygame.draw.line(screen,(distance%255,0.2*distance%255,88),(x,y),(mouse_pos),5)

            if particle_list:
                collision_detection(particle_list)
                for particle in particle_list:
                    x_constraint = particle.ini_x_pos - WIDTH
                    y_constraint = particle.ini_y_pos - HEIGHT
                    
                    if x_constraint < -(particle.radius+WIDTH) or x_constraint > (particle.radius) or y_constraint > (particle.radius) or y_constraint < -(particle.radius+HEIGHT):
                        particle_list.remove(particle)
                    else:
                        particle.update_position()
            pygame.display.flip()
            screen.fill((0,0,0))


if __name__ == '__main__':
    main()