class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        pass

    def draw(self):
        num_font = pygame.font.Font(None, 200)
        num_surf = num_font.render(self.value, 0, NUM_COLOR)

        num_rect = num_surf.get_rect()
        screen.blit(num_surf, num_rect)
