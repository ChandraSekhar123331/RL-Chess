import pygame

class Cell:
    def __init__(self,screen,pos,dim):
        ##pos is [x_top_left,y_top_left]
        ##dim is [cell_width,cell_height]
        self.surf = pygame.Surface(dim)
        self.pos = pos
        self.dim = dim
        self.screen = screen
        self.screen.blit(self.surf,self.pos)
    
    def fill_color(self,color):
        self.color = color
        self.surf.fill(self.color)
        self.screen.blit(self.surf,self.pos)
    
    def render(self,image):
        if image == "":
            pass
        else:
            img = pygame.image.load(image)
            img = pygame.transform.scale(img,self.dim)
            self.surf = img.convert_alpha()
            self.screen.blit(self.surf,self.pos)
            # self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    
    