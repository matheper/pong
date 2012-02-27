import sys, pygame, os
pygame.init()

score = [0,0]
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
black = 0,0,0

class Ball(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [3,3]
        self.image, self.rect = load_image("images/ball.png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0:
            score[1] += 1
            self.speed[0] = -self.speed[0]
            self.rect.centerx = self.init_pos[0]
            self.rect.centery = self.init_pos[1]
        if self.rect.right > width:
            score[0] += 1
            self.speed[0] = -self.speed[0]
            self.rect.centerx = self.init_pos[0]
            self.rect.centery = self.init_pos[1]
       # if self.rect.left<0 or self.rect.right>width:
       #     self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

class Paddle(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.direction = 0
        self.image, self.rect = load_image("images/paddle.png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    def update(self):
        self.rect.move_ip((0,self.direction*4))

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

def load_image(name):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image: ", fullname
        raise SystemExit, message
    return image, image.get_rect()

def main():
    ball = Ball([width/2,height/2])
    paddle1 = Paddle([10,height/2])
    paddle2 = Paddle([width-15,height/2])
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    while 1:
        clock.tick(120)

        for event in pygame.event.get():
            pass
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            sys.exit()

        if key_pressed[pygame.K_UP]:
            paddle2.direction = -1
        elif key_pressed[pygame.K_DOWN]:
            paddle2.direction = 1
        else:
            paddle2.direction = 0

        if key_pressed[pygame.K_a]:
            paddle1.direction = -1
        elif key_pressed[pygame.K_z]:
            paddle1.direction = 1
        else:
            paddle1.direction = 0

        if ball.rect.colliderect(paddle1.rect) or \
           ball.rect.colliderect(paddle2.rect):
            ball.speed[0] = -ball.speed[0]

        stringScore = '%d   %d'%(score[0], score[1])
        font = pygame.font.Font(None, 28)
        text = font.render(stringScore, True, (255,255,255), (0,0,0))
        
        textRect = text.get_rect()

        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery/4
        

        ball.update()
        paddle1.update()
        paddle2.update()
        
        screen.fill(black)

        screen.blit(text,textRect)
        screen.blit(ball.image, ball.rect)
        screen.blit(paddle1.image, paddle1.rect)
        screen.blit(paddle2.image, paddle2.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
