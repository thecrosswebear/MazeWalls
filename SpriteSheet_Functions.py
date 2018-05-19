import pygame


pygame.init()

'''
Try to change the line

image = pygame.Surface([width, height]).convert_alpha()

to:

image = pygame.Surface([width, height], pygame.SRCALPHA)

'''

#transColor = (255,255,255,0)
#print "spritesheet"

def imgcolorkey(image, colorkey):
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image

class SpriteSheet(object):
    sprite_sheet = None
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

        #self.sprite_sheet = pygame.image.load(file_name, pygame.SRCALPHA)
    #self.sheet = load_image(filename)
    
    '''
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
        #image = pygame.Surface([width, height], pygame.SRCALPHA ).convert()
        #image = pygame.Surface([width, height], pygame.SRCALPHA)
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        #image.set_colorkey(constants.BLACK)
        image.set_colorkey(0,0,0)
        # Return the image
        return image
    '''

    def imgat(self, rect, colorkey = None):
        rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size).convert()
        #image = pygame.Surface(rect.size, pygame.SRCALPHA ).convert()
        #image = pygame.Surface(rect.size, pygame.SRCALPHA)
        #image.fill(transColor)
        image.blit(self.sprite_sheet, (0, 0), rect)
        return imgcolorkey(image, colorkey)

    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs

