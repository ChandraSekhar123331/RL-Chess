import pygame
from pygame.event import get

class Cell:
    def __init__(self,screen,pos,dim):
        ##pos is [x_top_left,y_top_left]
        ##dim is [cell_width,cell_height]
        self.surf = pygame.Surface(dim)
        self.pos = pos
        self.dim = dim
        self.image = None
        self.color = None
        self.screen = screen
        self.blit_cell()
    
    def fill_color(self,color):
        self.color = color
        self.surf.fill(self.color)
        self.blit_cell()

    def blit_cell(self):
        self.screen.blit(self.surf,self.pos)
    
    def render(self,image):
        self.image = image
        if image == "":
            self.blit_cell()
        else:
            img = pygame.image.load(image)
            img = pygame.transform.scale(img,self.dim)
            self.surf = img.convert_alpha()
            self.blit_cell()

            # self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    def highlight_free(self):
        self.surf.fill([117, 150, 240])
        self.blit_cell()
        # self.render(self.image)

    def highlight_enemy(self):
        self.surf.fill([255, 0, 0])
        self.blit_cell()
        self.render(self.image)
    def reset(self):
        self.surf.fill(self.color)
        self.blit_cell()
        self.render(self.image)
    def get_piece(self,get_cell):
        # self.color = get_cell.color
        self.image = get_cell.image
        get_cell.image= ""
        self.reset()
        get_cell.reset()
        
    
    