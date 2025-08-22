import pygame
import sys

pygame.init()

# --- Load your pet and set window size to match sprite ---
pet_image = pygame.image.load("pet.png").convert_alpha()
screen = pygame.display.set_mode(pet_image.get_size(), pygame.SRCALPHA)

pygame.display.set_caption("Virtual Pet")

# Clock for FPS
clock = pygame.time.Clock()

# --- Main Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0, 0))   # clear screen (transparent if supported)
    screen.blit(pet_image, (0, 0))  # draw pet at top-left

    pygame.display.flip()
    clock.tick(60)


class VirtualPet:
    def __init__(self, screen, sprite_folder, pos=(100, 100)):
        self.screen = screen
        self.sprite_folder = sprite_folder
        self.animations = {}  # store all animations
        self.load_all_animations()
        self.current_action = "idle"
        self.current_frames = self.animations[self.current_action]
        self.frame_index = 0
        self.image = self.current_frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_delay = 6
        self.counter = 0

    def load_all_animations(self):
        """Load all subfolders under sprites/ (idle, walk, run, jump)."""
        for action in os.listdir(self.sprite_folder):
            action_path = os.path.join(self.sprite_folder, action)
            if os.path.isdir(action_path):
                frames = []
                for filename in sorted(os.listdir(action_path)):
                    if filename.endswith(".png"):
                        frame = pygame.image.load(os.path.join(action_path, filename)).convert_alpha()
                        frames.append(frame)
                if frames:
                    self.animations[action] = frames

    def set_action(self, action):
        """Switch animations if different."""
        if action in self.animations and action != self.current_action:
            self.current_action = action
            self.current_frames = self.animations[action]
            self.frame_index = 0
            self.counter = 0

    def update(self):
        """Cycle through frames."""
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)
            self.image = self.current_frames[self.frame_index]

    def draw(self):
        self.screen.blit(self.image, self.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400), pygame.NOFRAME)  # frameless window
    pygame.display.set_caption("Virtual Pet")

    # Point to "sprites" folder that has idle/, walk/, run/, jump/
    sprite_folder = "sprites"
    pet = VirtualPet(screen, sprite_folder)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            pet.set_action("jump")
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            pet.set_action("run")
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            pet.set_action("walk")
        else:
            pet.set_action("idle")

        screen.fill((0, 0, 0, 0))  # transparent bg
        pet.update()
        pet.draw()
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
