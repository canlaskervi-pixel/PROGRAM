import pygame
import sys

# --- Game Constants ---
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAVITY = 1

# --- Player Class ---
class Stickman(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.width = 30
        self.height = 70
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = True
        self.health = 100

        # Draw the basic stickman figure on the surface
        self._draw_stickman()

    def _draw_stickman(self):
        # Clear the surface first (important if redrawing)
        self.image.fill((0, 0, 0, 0)) # Transparent background

        head_radius = 10
        body_length = 40
        limb_thickness = 3

        # 1. Head (Circle)
        pygame.draw.circle(self.image, self.color, (self.width // 2, head_radius), head_radius, 0)

        # 2. Body (Line)
        body_start = (self.width // 2, head_radius * 2)
        body_end = (self.width // 2, head_radius * 2 + body_length)
        pygame.draw.line(self.image, self.color, body_start, body_end, limb_thickness)

        # 3. Arms (simple V shape from top of body)
        arm_start = body_start
        arm_left_end = (body_start[0] - 15, body_start[1] + 10)
        arm_right_end = (body_start[0] + 15, body_start[1] + 10)
        pygame.draw.line(self.image, self.color, arm_start, arm_left_end, limb_thickness)
        pygame.draw.line(self.image, self.color, arm_start, arm_right_end, limb_thickness)

        # 4. Legs (simple V shape from bottom of body)
        leg_start = body_end
        leg_left_end = (body_end[0] - 10, body_end[1] + 20)
        leg_right_end = (body_end[0] + 10, body_end[1] + 20)
        pygame.draw.line(self.image, self.color, leg_start, leg_left_end, limb_thickness)
        pygame.draw.line(self.image, self.color, leg_start, leg_right_end, limb_thickness)


    def update(self):
        # --- Apply Gravity ---
        if not self.on_ground:
            self.vel_y += GRAVITY
        
        # --- Update position ---
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # --- Simple Boundary/Ground Check ---
        if self.rect.bottom >= HEIGHT - 50: # 50 is the ground level
            self.rect.bottom = HEIGHT - 50
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        # Ensure player stays within the screen width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def move(self, direction):
        # direction is -1 for left, 1 for right
        self.vel_x = direction * 5

    def jump(self):
        if self.on_ground:
            self.vel_y = -15  # Negative value moves up
            self.on_ground = False

    def stop(self):
        self.vel_x = 0

    # This is where you would add attack logic later!
    def attack(self):
        print(f"{self.color} Stickman attacks!")
        # Implement hitboxes, damage, and animations here

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickman Duel")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Create Players and Groups ---
player1 = Stickman(BLUE, 100, HEIGHT - 50 - 70) # x, y (starts above ground)
player2 = Stickman(RED, WIDTH - 100 - 30, HEIGHT - 50 - 70)

all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2)

# --- Game Loop ---
running = True
while running:
    # 1. Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Key down events
        if event.type == pygame.KEYDOWN:
            # Player 1 Controls (WASD)
            if event.key == pygame.K_a:
                player1.move(-1)
            elif event.key == pygame.K_d:
                player1.move(1)
            elif event.key == pygame.K_w:
                player1.jump()
            elif event.key == pygame.K_s: # Simple Attack key
                player1.attack()

            # Player 2 Controls (Arrow Keys & P)
            if event.key == pygame.K_LEFT:
                player2.move(-1)
            elif event.key == pygame.K_RIGHT:
                player2.move(1)
            elif event.key == pygame.K_UP:
                player2.jump()
            elif event.key == pygame.K_p: # Simple Attack key
                player2.attack()

        # Key up events (stop movement)
        if event.type == pygame.KEYUP:
            # Player 1 stops
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1.stop()
            
            # Player 2 stops
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player2.stop()

    # 2. Update
    all_sprites.update()

    # 3. Drawing
    screen.fill(WHITE)

    # Draw the ground
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 50, WIDTH, 50))

    # Draw all sprites
    all_sprites.draw(screen)

    # Draw Health Bars (Simple boxes)
    # Player 1 Health
    pygame.draw.rect(screen, RED, (20, 20, 200, 20)) # Background (Max Health)
    pygame.draw.rect(screen, BLUE, (20, 20, player1.health * 2, 20)) # Current Health
    
    # Player 2 Health
    pygame.draw.rect(screen, RED, (WIDTH - 220, 20, 200, 20))
    pygame.draw.rect(screen, RED, (WIDTH - 220 + (100-player2.health) * 2, 20, player2.health * 2, 20)) # Placeholder: use this logic to shrink from the right

    # 4. Refresh Display and Tick Clock
    pygame.display.flip()
    clock.tick(FPS)

# --- Game Exit ---
pygame.quit()
sys.exit()
