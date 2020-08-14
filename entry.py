# @Author: kolterdyx
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 14-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE.txt',\nwhich is part of this source code package.


import pygame as pg

letters = {
    pg.K_a: ['a', 'A'],
    pg.K_b: ['b', 'B'],
    pg.K_c: ['c', 'C'],
    pg.K_d: ['d', 'D'],
    pg.K_e: ['e', 'E'],
    pg.K_f: ['f', 'F'],
    pg.K_g: ['g', 'G'],
    pg.K_h: ['h', 'H'],
    pg.K_i: ['i', 'I'],
    pg.K_j: ['j', 'J'],
    pg.K_k: ['k', 'K'],
    pg.K_l: ['l', 'L'],
    pg.K_m: ['m', 'M'],
    pg.K_n: ['n', 'N'],
    pg.K_o: ['o', 'O'],
    pg.K_p: ['p', 'P'],
    pg.K_q: ['q', 'Q'],
    pg.K_r: ['r', 'R'],
    pg.K_s: ['s', 'S'],
    pg.K_t: ['t', 'T'],
    pg.K_u: ['u', 'U'],
    pg.K_v: ['v', 'V'],
    pg.K_w: ['w', 'W'],
    pg.K_x: ['x', 'X'],
    pg.K_y: ['y', 'Y'],
    pg.K_z: ['z', 'Z'],
}

characters = {
    pg.K_SPACE: ' ',
    pg.K_0: '0',
    pg.K_1: '1',
    pg.K_2: '2',
    pg.K_3: '3',
    pg.K_4: '4',
    pg.K_5: '5',
    pg.K_6: '6',
    pg.K_7: '7',
    pg.K_8: '8',
    pg.K_9: '9',
}


class Entry(pg.sprite.Sprite):
    def __init__(self, parent, *, x=0, y=0, w=100, size=20, font="Arial", border=0, func=None, max_length=0):
        self.parent = parent
        self.rect = pg.Rect((x, y), (w, size + size / 4))
        self.image = pg.Surface(self.rect.size).convert_alpha()
        self.image.fill((255, 255, 255))
        self.bg_color = (255, 255, 255)

        self.width = w

        self.border = pg.Rect((self.rect.x - border + 2, self.rect.y - border + 2),
                              (w + border, self.rect.height + border))
        self.border_width = border
        self.border_color = (0, 0, 0)

        self.cursor = pg.Surface((size / 10, size)).convert_alpha()
        self.cursor.fill((0, 0, 0))
        self.cursor_rect = self.cursor.get_rect()
        self.cursor_rect.x = self.rect.x + 20
        self.cursor_rect.y = self.rect.y + 1

        self.c = 0
        self.cc = 1
        self.type_cooldown = 0
        self.text = ''

        self.size = size
        self.screen = parent.screen
        self.func = func

        self.font = pg.font.SysFont(font, size)
        self.font_color = (0, 0, 0)
        self.font_name = font
        self.font_size = size

        self.label = self.font.render(self.text, 1, self.font_color)
        self.typing = False
        self.keypressed = False
        self.pressing = False

        self.max_length = max_length

    def add_char(self, char):
        self.keypressed = True
        if self.max_length:
            if len(self.text) < self.max_length:
                self.text += char
                self.label = self.font.render(self.text, 1, self.font_color)
        else:
            self.text += char
            self.label = self.font.render(self.text, 1, self.font_color)

    def remove_char(self):
        self.keypressed = True
        self.text = self.text[:-1]
        self.label = self.font.render(self.text, 1, self.font_color)

    def update(self):
        if self.c < 100 and self.cc == 1:
            self.c += self.cc
            self.cursor.fill(self.font_color)
        elif self.c > 0 and self.cc == -1:
            self.c += self.cc
            self.cursor.fill((0, 0, 0, 0))
        else:
            self.cc *= -1

        mousepos = pg.mouse.get_pos()
        p1, p2, p3 = pg.mouse.get_pressed()

        keys = pg.key.get_pressed()
        count = 0
        for i in keys:
            count += i
        if count >= 1:
            self.pressing = True
        else:
            self.pressing = False

        if self.typing and not self.keypressed:
            for a in characters:
                if keys[a]:
                    self.add_char(characters[a])
            for b in letters:
                if keys[b] and (keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                    self.add_char(letters[b][1])
                if keys[b] and not (keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]):
                    self.add_char(letters[b][0])
            if keys[pg.K_BACKSPACE]:
                self.keypressed = True
                self.remove_char()
            if keys[pg.K_RETURN]:
                self.keypressed = True
                if self.func:
                    self.func()
                else:
                    self.typing = False

        elif self.typing and self.keypressed:
            if self.type_cooldown >= 30 and self.pressing:
                self.keypressed = False
                self.type_cooldown = 0
            else:
                self.type_cooldown += 1
        if self.type_cooldown >= 60 and not self.pressing:
            self.keypressed = False
            self.type_cooldown = 0

        if p1:
            if self.rect.collidepoint(mousepos):
                self.typing = True
            else:
                self.typing = False

        self.label_rect = self.label.get_rect()
        self.label_rect.x = self.rect.height/20 + self.border_width
        self.label_rect.centery = self.rect.height / 2 + self.rect.height/20
        self.cursor_rect.x = self.label_rect.width + self.rect.height/20 + self.border_width
        self.cursor_rect.centery = self.rect.height / 2

        self.image.fill(self.bg_color)
        if self.typing:
            self.image.blit(self.cursor, self.cursor_rect)
        self.image.blit(self.label, self.label_rect)
        self.screen.blit(self.image, self.rect)

        if self.border_width > 0:
            pg.draw.rect(self.screen, self.border_color, self.border, self.border_width)

    def get_text(self):
        return self.text

    def set_font_color(self, color):
        self.font_color = color

    def set_font(self, font):
        self.font_name = font
        try:
            self.font = pg.font.Font(font, self.font_size)
        except:
            self.font = pg.font.SysFont(font, self.font_size)

    def set_font_size(self, size):
        self.font_size = size
        try:
            self.font = pg.font.SysFont(self.font_name, self.font_size)
        except:
            self.font = pg.font.Font(self.font_name, self.font_size)

        self.rect = pg.Rect(self.pos, (self.width, size + size / 4))
        self.image = pg.Surface(self.rect.size).convert_alpha()

        self.cursor = pg.Surface((size / 10, size)).convert_alpha()
        self.cursor_rect = self.cursor.get_rect()
        self.cursor_rect.x = 20
        self.cursor_rect.y = 1

    def set_bg_color(self, color):
        self.bg_color = color
        self.image.fill(color)

    def set_border_width(self, width):
        self.border_width = width

    def set_border_color(self, color):
        self.border_color = color

    def move(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.rect.topleft = self.pos
        self.border = pg.Rect((self.rect.x - self.border_width + self.border_width/2, self.rect.y - self.border_width + self.border_width/2),
                              (self.rect.width + self.border_width, self.rect.height + self.border_width))
