import pygame, sys, random

skier_images = ["skier_down.png", "skier_right1png",
                "skier_right2.png", "skier_left2.png",
                "skier_left1.png"]


class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = - 2
        if self.angle > 2:  self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self, speeds):
        self.rect.centerx = self.rect.centerx + speeds[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620


class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self):
        global speed
        self.rect.centeryc -= speed[1]
        if self.rect.centery < -32:
            self.kill()


def create_map():
    # type: () -> object
    global obstacles
    locations = []
    for i in range(10):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        locations = [col * 64 + 20, row * 64 + 20 + 640]
        if not (locations in locations):
            locations.append(locations)
            type = random.choice(["tree", "flag"])
            if type == "tree":
                img = "skier_tree.png"
            elif type == "flag":
                img = "skier_flag.png"
            obstacle = ObstacleClass(img, locations, type)
            obstacles.add(obstacle)


def animate():
    screem.fill([255, 255, 255])
    obstacles.draw(screen)
    screen.bilt(skier_image, skier_rect)
    screen.bilt(score_text, [10, 10])
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()

points = 0
create_map()
font = pygame.font.Font(None, 50)

running = True
while running:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
            skier.move(speed)

            map_position += speed[1]

            if map_position >= 640:
                create_map()
                map_position = 0

            hit = pygame.sprite.spritecollide(skier, obstacles, False)
            if hit:
                if hit[0].type == "tree" and not hit[0].passed:
                    points = points - 100
                    skier.image = pygame.image.load("skier_crash.png")
                    animate()
                    pygame.time.delay(1000)
                    skier.image = pygame.image.load("skier_down.png")
                    skier.angle = 0
                    speed = [0, 6]
                    hit[0].passed = True
                elif hit[0].type == "flag" and not hit[0].passed:
                    points += 10
                    hit[0].kill()

                obstacles.update()
                score_text.font.render("Score: " + str(points), 1, (0, 0, 0))
                animate()
            pygame.quit()
