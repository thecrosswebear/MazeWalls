import pygame

pygame.init()

SIZE = [500,500]
BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]

pygame.display.set_mode(SIZE)
pygame.display.set_caption("mazeWalls")

done = False

class Wall(pygame.sprite.Sprite):

	def __init__(self, x,y, width, height):
		super(Wall,self).__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = width
		self.height = height

	def __str__(self):
		return ("Wall(%d,%d,%d,%d)") %(self.rect.x, self.rect.y, self.width, self.height)

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height):
		super(Player, self).__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = width
		self.height = height

class Room(object):

	def __init__(self):
		pass

class App (object):

	def __init__(self):
		self.player = Player(200,200, 20,20)
		#self.wall = Wall

	def main(self):
		print "allo"
		wall = Wall(10,10, 400,10)
		print wall
		#player = Player(200,300,20,20)



if __name__ == "__main__":
	
	app = App()
	app.main()
