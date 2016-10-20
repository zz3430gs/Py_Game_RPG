import pygame



# THIS IS HOW I FOUND A FONT TO USE
fonts = pygame.font.get_fonts()
for font in fonts:
    if 'ber' in font:
        print(font)

print(pygame.font.match_font('berlinsansfbdemi'))
# TODO: 10/19/2016 "DO THE THING"