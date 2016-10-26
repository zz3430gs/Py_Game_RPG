import graphics. as C
import pygame

class TitlePage:
    def __init__(self, tm, gm):

        self.title_file = open('files\\title_page.txt', 'r')

        self.lines = []

        line = self.title_file.readline()
        line = line.rstrip()

        while line != 'FINAL_END':
            self.lines.append(line)

            line = self.title_file.readline()
            line = line.rstrip()

        self.title_file.close()

    def showPage(self):

        # show current page

        gm.main_surf.fill((0, 0, 0))

        y = 1
        for p in self.lines:
            if y < 6:
                self.add_text(p, C.YELLOW, 0, y)
            elif y > 23:
                self.add_text(p, YELLOW, 0, y)
            else:
                self.add_text(p, GRAPH_PAPER, 0, y)
            y += 1

        pygame.display.update()
        gc.clock.tick(gc.FPS)

    def add_text(self, t, color, cx, cy):

        n = tc.FONT.render(t, False, color)

        gc.mainSurface.blit(n, (cx * tc.FONT_WIDTH, cy * tc.FONT_HEIGHT))
