import pygame
from SpriteSheet_Functions import SpriteSheet

pygame.init()

SIZE = [500,500]
BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]
RED = [255,0,0]
GREEN = [0, 255,0]
PLAYER_DIMENSION = 20


DEPLACEMENT = 5

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("mazeWalls")
SPRITE_SHEET_FILE = "Data/player.png"
SPRITE_SHEET = SpriteSheet(SPRITE_SHEET_FILE)
#sprite_tight = (4,0,54,64)
PLAYER_COORD = [(0,0,64,64), (64,0, 64,64), (0,64,64,64), (64,64,64,64),(0,128,64,64), (64,128,64,64), (0,192,64,64), (64,192,64,64)]


clock = pygame.time.Clock()

done = False

class Wall(pygame.sprite.Sprite):

	def __init__(self, x,y, width, height, color):
		super(Wall,self).__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = width
		self.height = height

	def __str__(self):
		return ("Wall(%d,%d,%d,%d)") %(self.rect.x, self.rect.y, self.width, self.height)

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super(Player, self).__init__()
		self.images = self.setImages()
		self.image = self.setImage()
		self.rect = self.image.get_rect()
		self.orient = 'up'
		self.rect.x = x
		self.rect.y = y
		self.direction = None

	def setImages(self):
		images = SPRITE_SHEET.imgsat(PLAYER_COORD)
		return images

	def setImage(self):
		return self.images[0]

	def update(self):
		pass

	def move(self, direction):

		self.direction = direction

		if direction == "LEFT":
			self.rect.x = self.rect.x - DEPLACEMENT
		elif direction == "RIGHT":
			self.rect.x = self.rect.x + DEPLACEMENT
		elif direction == "UP":
			self.rect.y = self.rect.y - DEPLACEMENT
		elif direction == "DOWN":
			self.rect.y = self.rect.y + DEPLACEMENT


class Room(object):

	def __init__(self):
		#self.wallsArray = wallsArray
		self.all_walls_in_room_list = pygame.sprite.Group()
		#self.createWalls()

	#def __init__(self, wallsArray):
	#	self.wallsArray = wallsArray
	#	self.all_walls_list = pygame.sprite.Group()
	#	self.createWalls()

	def addWall(self, wall):
		self.all_walls_in_room_list.add(wall)

	def createWalls(self):
		for wallCoord in self.wallsArray:
			wallSprite = Wall(wallCoord[0], wallCoord[1], wallCoord[2], wallCoord[3])
			all_walls_list.add(wallSprite)


class App (object):

	def __init__(self):
		self.all_sprite_list = pygame.sprite.Group()
		self.player = Player(200,200)
		#self.player2 = Player2((50,50), 'up')
		#self.player = Player((startCell.px, startCell.py), 
        #                     startCell['playerStart'], self.players)

		self.all_sprite_list.add(self.player)
		#self.all_sprite_list.add(self.player2)
		#self.all_wall_list = pygame.sprite.Group()
		self.roomArray = []
		self.currentRoom = 0
		#self.wall = Wall

	def setup(self):
		wall1Room1 = Wall(200, 4, 10,150, RED)
		wall2Room1 = Wall(4, 400, 200,10, RED)
		room1 = Room()
		room1.addWall(wall1Room1)
		room1.addWall(wall2Room1)

		
		wall1Room2 = Wall (300, 40, 10, 300, GREEN)
		wall2Room2 = Wall (40, 400, 300, 10, GREEN)
		room2 = Room()
		room2.addWall(wall1Room2)
		room2.addWall(wall2Room2)
		
		wall1Room3 = Wall (400, 0, 10, 100, BLUE)
		wall2Room3 = Wall (50, 400, 400, 10, BLUE)
		room3 = Room()
		room3.addWall(wall1Room3)
		room3.addWall(wall2Room3)

		self.roomArray.append(room1)
		self.roomArray.append(room2)
		self.roomArray.append(room3)

	def main(self):
		print "allo"
		#wall = Wall(10,10, 400,10)

		#print wall
		#player = Player(200,300,20,20)

		done = False
		self.setup()

		while not done:

			screen.fill(BLACK)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True

			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				done = True
			elif keys[pygame.K_LEFT]:
				self.player.move("LEFT")
			elif keys[pygame.K_RIGHT]:
				self.player.move("RIGHT")
			elif keys[pygame.K_UP]:
				self.player.move("UP")
			elif keys[pygame.K_DOWN]:
				self.player.move("DOWN")

			#player exits room from left
			if self.player.rect.x < 0:
				print "out of range"
				if self.currentRoom == 0:
					self.currentRoom = len(self.roomArray) -1
				else:
					self.currentRoom = self.currentRoom -1
				self.player.rect.x = SIZE[0] - 20

			#player exits room from right
			if self.player.rect.x > SIZE[0]:
				if self.currentRoom == len(self.roomArray) -1:
					self.currentRoom = 0 
				else:
					self.currentRoom = self.currentRoom + 1
				self.player.rect.x = 20

			
			block_hit_list = pygame.sprite.spritecollide (self.player, self.roomArray[self.currentRoom].all_walls_in_room_list, False)

			for block in block_hit_list:
				if self.player.direction == "LEFT":
					self.player.rect.left = block.rect.right
				elif self.player.direction == "RIGHT":
					self.player.rect.right = block.rect.left
				elif self.player.direction == "UP":
					self.player.rect.top = block.rect.bottom
				else:
					self.player.rect.bottom = block.rect.top
	

			self.all_sprite_list.draw(screen)

			self.roomArray[self.currentRoom].all_walls_in_room_list.draw(screen)
			pygame.display.update()
			clock.tick(60)


if __name__ == "__main__":
	
	app = App()
	app.main()
