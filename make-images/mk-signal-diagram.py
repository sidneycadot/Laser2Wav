#! /usr/bin/env python

import Image, ImageDraw

def plot(im, y, x, fillcolor):
    draw = ImageDraw.Draw(im)
    draw.rectangle(((17*x+0, 3*y+0), (17*x+17, 3*y+3)), outline = (100,100,100), fill = fillcolor)

def plot2(im, y, x, fillcolor):
    draw = ImageDraw.Draw(im)
    draw.rectangle(((17*x+0, 3*y+0), (17*x+17, 3*y+3)), outline = (0,0,0), fill = fillcolor)

def plot_q(im, y):
    q_delay = [107, 104, 99, 96, 91, 88, 83, 80, 75, 72, 67, 64, 59, 56, 51, 48, 43, 40, 35, 32, 27, 24, 19, 16, 11, 8, 3, 0]
    for x in range(28):
        plot2(im, y - q_delay[x], 1 + x, (0, 255, 0))

def plot_p(im, y):
    p_delay = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    for x in range(32):
        plot2(im, y - p_delay[x], 1 + x, (255, 255, 0))

def plot_sound(im, y):
    audio_bytes = [
        (105,  0), (102,  1),
        ( 97,  2), ( 94,  3),
        ( 89,  4), ( 86,  5),
        ( 81,  6), ( 78,  7),
        ( 73,  8), ( 70,  9),
        ( 65, 10), ( 62, 11),
        ( 43, 16), ( 40, 17),
        ( 35, 18), ( 32, 19),
        ( 27, 20), ( 24, 21),
        ( 19, 22), ( 16, 23),
        ( 11, 24), (  8, 25),
        (  3, 26), (  0, 27)
    ]

    for (oy, x) in audio_bytes:
        plot2(im, y - oy, 1 + x, (255, 0, 0))

im = Image.new('RGB', (562, 3 * 3 * 98 + 1))

for x in range(33):
    for y in range(3 * 98):

        if x in [0]:
            if y % 98 in [0, 1]:
                fillcolor = (204, 153, 204)
            else:
                fillcolor = (255, 204, 255)
        elif x in [1, 3, 5, 7,  9, 11, 17, 19, 21, 23, 25, 27]:
            fillcolor = (230, 230, 255)
        elif x in [2, 4, 6, 8, 10, 12, 18, 20, 22, 24, 26, 28]:
            fillcolor = (220, 220, 255)
        elif x in [13, 14, 15, 16]:
            fillcolor = (204, 255, 204)
        elif x in [29, 30, 31, 32]:
            fillcolor = (255, 255, 204)
        else:
            fillcolor = 'white'

        plot(im, y, x, fillcolor)

plot_p(im, 98 - 20)
plot_q(im, 205 - 10)
plot_sound(im, 203)

im.save('signal-diagram.png')
