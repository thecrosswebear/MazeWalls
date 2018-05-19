import pygame
from SpriteSheet_Functions import SpriteSheet

pygame.init()

SIZE = [500,500]
BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]
RED = [255,0,0]
GREEN = [0, 255,0]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("mazeWalls")
SPRITE_SHEET_FILE = "Data/player.png"
#SPRITE_SHEET_FILE = "Data/donkey-kong-sprite-sheet-2.png"
SPRITE_SHEET = SpriteSheet(SPRITE_SHEET_FILE)
#PLAYER_COORD = [(0,0,64,64), (64,0, 64,64), (0,64,64,64), (64,64,64,64),(0,128,64,64), (64,128,64.64), (0,192,64,64), (64,192,64,64)]
PLAYER_COORD = [(0,0,64,64), (64,0, 64,64)]
#MARIO_COORD =  [(14,200,18,20),(31,200,18,20), (51,200,18,20)]

clock = pygame.time.Clock()

done = False

class Player(pygame.sprite.Sprite):

	def __init__(self):
		super(Player, self).__init__()
		self.images = self.setImages()
		self.image = self.setImage()
		self.rect = self.image.get_rect()
		self.rect.x = 14
		self.rect.y = 470
		self.currentImage = 0
		self.direction = "Left"

	def setImages(self):

		images = SPRITE_SHEET.imgsat(PLAYER_COORD,-1)
		#images = SPRITE_SHEET.imgsat(MARIO_COORD,-1)
		return images

	def setImage(self):
		return self.images[0]


print "allo"

player = Player()