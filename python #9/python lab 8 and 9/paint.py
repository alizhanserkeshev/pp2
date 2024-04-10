import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 600))
surf = pg.Surface((700, 600))
buttons = pg.Surface((100, 240)) 
font = pg.font.SysFont("Verdana", 15)
cur_color = 'white' 
commands = {
    'right_triangle': [4, 4, 44, 44],
    'sqr': [52, 4, 44, 44],
    'triangle': [4, 50, 44, 44],
    'rhombus': [52, 50, 44, 44],
    'eraser' : [1000, 1000, 1, 1]
}

def setsurf():
    surf.fill('white')
    
    buttons.fill('white')
    pg.draw.rect(buttons, 'gray', (2, 2, 96, 236), 1)
    
    for i in commands:
        pg.draw.rect(buttons, 'black', commands[i], 1)
    tr1 = pg.image.load("right_triangle.png")
    buttons.blit(tr1, (8, 8))
    tr2 = pg.image.load("equilateral-triangle.png")
    buttons.blit(tr2, (8, 55))
    pg.draw.rect(buttons, 'black', (58, 10, 32, 32), 2)
    rh = pg.image.load("rhombus.png")
    buttons.blit(rh, (56, 58))
    screen.blit(surf, (0, 0))
    screen.blit(buttons, (700, 0))

def get_distance(a,b): 
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def right_triangle(screen, cur, end, d, color): 
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    difx = abs(x1-x2) 
    dify = abs(y1-y2) 
    if x1 <= x2: 
        if y1 < y2: 
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
        else: 
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    
             
    else: 
        if y1 < y2: 
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
        else: 
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    

def triangle(color, pos):
    pg.draw.polygon(surf, color, pos, 3)

def square(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    a = abs(x1-x2)
    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, a, a), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, a, a), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, a, a), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, a, a), d)

def rhombus(color, pos):
        pg.draw.polygon(surf, color, pos, 3)

last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

di = {
    'right_triangle' : True,
    'sqr': False,
    'triangle': False,
    'rhombus': False,
    'eraser' : False
}

setsurf()
running = True
while running:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False             
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                cur_color = 'red'
            if event.key == pg.K_2:
                cur_color = 'green'
            if event.key == pg.K_3:
                cur_color = 'blue'
            if event.key == pg.K_4:
                cur_color = 'white'
            if event.key == pg.K_5: 
                di['eraser'] = True 
                for k, v in di.items(): 
                    if k != 'eraser': 
                        di[k] = False              
        if event.type == pg.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0]-700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    di[k] = True
                    for i, j in di.items():
                        if i != k:
                            di[i] = False
                    break                 
        if di['right_triangle'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                right_triangle(surf, last_pos, pos, w, cur_color)
        elif di['sqr'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                square(surf, last_pos, pos, w, cur_color)
        elif di['triangle'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                triangle(cur_color,[last_pos, pos,((pos[0] - last_pos[0])*cos(pi/3) - (pos[1] - last_pos[1])*sin(pi/3) + last_pos[0], (pos[0] - last_pos[0])*sin(pi/3) + (pos[1] - last_pos[1])*cos(pi/3) + last_pos[1])])
        elif di['rhombus'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                rhombus(cur_color, [last_pos, (last_pos[0] + d, last_pos[1]), (pos[0] + d, pos[1]), pos])
        elif di['eraser'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pos
                pg.draw.rect(surf, 'black', (x, y, ed, ed))
                erase = True
            if event.type == pg.MOUSEMOTION:
                if erase:
                    pg.draw.rect(surf, 'black', (pos[0], pos[1], ed, ed))
            if event.type == pg.MOUSEBUTTONUP:
                erase = False
    for k, v in di.items():
        if v == True:
            pg.draw.rect(buttons, 'red', commands[k], 1)
        else:
            pg.draw.rect(buttons, 'black', commands[k], 1)
    
    screen.blit(buttons, (700, 0))
    screen.blit(surf, (0, 0))
    c = font.render('Press:', True, 'black')
    buttons.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons.blit(y, (5, 180))
    e = font.render('5 - Eraser', True, 'black')
    buttons.blit(e, (5, 200))

    pg.display.update()
pg.quit()