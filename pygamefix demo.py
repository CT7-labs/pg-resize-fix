from pygamefix import *

def f(screen:pygame.Surface):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "#ff0000", screen.get_rect().inflate(-100, -100))
    pygame.display.update()

pygame.init()
pygame.display.set_caption("test") # you can still call regular pygame functions

window = Window((1080, 720))
window.set_draw_func(f)

window.mainloop()
