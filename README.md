# Pygame Resize Fix

Just a thing I threw together in 10 minutes after finding [this on StackOverflow]([url](https://stackoverflow.com/questions/64543449/update-during-resize-in-pygame))

# Useage

```python
from pygamefix import * # imports pygame

# this is your tick function, called every frame AND while the window is resizing
def f(screen:pygame.Surface):
    # basically just draws a red rectangle that's perfectly centered in the window
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "#ff0000", screen.get_rect().inflate(-100, -100))
    pygame.display.update()

# normal pygame setup
pygame.init()
pygame.display.set_caption("test") # you can still call regular pygame functions

# new and interesting thing
window = Window((1080, 720))
window.set_draw_func(f) # that's basically all you have to do to make sure thats the tick function

window.mainloop() # this is really just a library for my purposes, so that's why it has a mainloop function

# if you want a more extended library where you have more control lemme know and I'll see what I can do

```
