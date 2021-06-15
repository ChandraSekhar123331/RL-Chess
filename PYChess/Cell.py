import pygame

class Cell:
    def __init__(self,screen,pos,dim):
        ##pos is [x_top_left,y_top_left]
        ##dim is [cell_width,cell_height]
        self.surf = pygame.Surface(dim)
        self.pos = pos
        self.dim = dim
        screen.blit(self.surf,pos)
    
    def fill_color(self,screen,color):
        self.surf.fill(color)
        screen.blit(self.surf,self.pos)
    
    def render(self,screen,image):
        if image == "":
            pass
        else:
            img = pygame.image.load(image)
            img = pygame.transform.scale(img,self.dim)
            self.surf = img.convert_alpha()
            screen.blit(self.surf,self.pos)
            # self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    
    