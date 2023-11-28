import pygame
import win32gui
import win32con

def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
    if message == win32con.WM_SIZE:
        draw_callback()
        win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
    return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)

def _dummy_function_that_is_the_default_update_or_draw_or_tick_function_that_is_called_every_frame_by_the_window(screen):
    """deal with it"""
    screen.fill((48, 48, 48))
    pygame.display.flip()

class Window:
    def __init__(self, initsize):
        self.screen = pygame.display.set_mode(initsize, pygame.RESIZABLE | pygame.DOUBLEBUF)
        self.oldWndProc = win32gui.SetWindowLong(win32gui.GetForegroundWindow(), win32con.GWL_WNDPROC, lambda *args: wndProc(self.oldWndProc, self.draw_func, *args))
        self.clock = pygame.time.Clock()
        self.func = _dummy_function_that_is_the_default_update_or_draw_or_tick_function_that_is_called_every_frame_by_the_window

    def draw_func(self):
        self.func(self.screen)

    def set_draw_func(self, func):
        self.func = func

    def mainloop(self, fps:int=30):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.draw_func()
            self.clock.tick(fps)
