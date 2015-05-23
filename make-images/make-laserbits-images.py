#! /usr/bin/env python

import Image

with open("laserbits.txt") as f:
    raw_signal = f.read()

# The raw_signal contains 288121 bits == 490 frames of 588 bits each, plus a single extra bit so we can see the changes.

raw_signal = map(int, raw_signal)

# The 'delta' signal has one less entry:

delta_signal = [raw_signal[i] ^ raw_signal[i - 1] for i in range(1, len(raw_signal))]

if True:

    im = Image.new('1', (588, 490), 'red')

    for y in range(490):
        for x in range(588):
            if raw_signal[588 * y + x +1]:
                im.putpixel((x, y), 1)
            else:
                im.putpixel((x, y), 0)

    im.save("raw-signal.png")

if True:

    im = Image.new('1', (588, 490))

    for y in range(490):
        for x in range(588):
            if raw_signal[588 * y + x + 1]:
                im.putpixel((x, y), 0)
            else:
                im.putpixel((x, y), 1)

    im.save("raw-signal-inverted.png")

if True:

    im = Image.new('1', (588, 490))

    for y in range(490):
        for x in range(588):
            if delta_signal[588 * y + x]:
                im.putpixel((x, y), 0)
            else:
                im.putpixel((x, y), 1)

    im.save("delta-signal.png")

if True:

    im = Image.new('RGB', (588, 490))

    colormap = {
        0 : (255, 204, 255), # subchannel byte
        1 : (204, 255, 255), # AUDIO byte (MSB) LEFT
        2 : (204, 204, 255), # AUDIO byte (LSB) LEFT
        3 : (204, 255, 255), # AUDIO byte (MSB) LEFT
        4 : (204, 204, 255), # AUDIO byte (LSB) LEFT
        5 : (204, 255, 255), # AUDIO byte (MSB) LEFT
        6 : (204, 204, 255), # AUDIO byte (LSB) LEFT
        7 : (204, 255, 255), # AUDIO byte (MSB) RIGHT
        8 : (204, 204, 255), # AUDIO byte (LSB) RIGHT
        9 : (204, 255, 255), # AUDIO byte (MSB) RIGHT
        10: (204, 204, 255), # AUDIO byte (LSB) RIGHT
        11: (204, 255, 255), # AUDIO byte (MSB) RIGHT
        12: (204, 204, 255), # AUDIO byte (LSB) RIGHT
        13: (204, 255, 204), # error correction (C2 a.k.a. Q)
        14: (204, 255, 204), # error correction (C2 a.k.a. Q)
        15: (204, 255, 204), # error correction (C2 a.k.a. Q)
        16: (204, 255, 204), # error correction (C2 a.k.a. Q)
        17: (204, 255, 255), # AUDIO byte (MSB) LEFT
        18: (204, 204, 255), # AUDIO byte (LSB) LEFT
        19: (204, 255, 255), # AUDIO byte (MSB) LEFT
        20: (204, 204, 255), # AUDIO byte (LSB) LEFT
        21: (204, 255, 255), # AUDIO byte (MSB) LEFT
        22: (204, 204, 255), # AUDIO byte (LSB) LEFT
        23: (204, 255, 255), # AUDIO byte (MSB) RIGHT
        24: (204, 204, 255), # AUDIO byte (LSB) RIGHT
        25: (204, 255, 255), # AUDIO byte (MSB) RIGHT
        26: (204, 204, 255), # AUDIO byte (LSB) RIGHT
        27: (204, 255, 255), # AUDIO byte (MSB) RIGHT
        28: (204, 204, 255), # AUDIO byte (LSB) RIGHT
        29: (255, 255, 204), # error correction (C1 a.k.a. P)
        30: (255, 255, 204), # error correction (C1 a.k.a. P)
        31: (255, 255, 204), # error correction (C1 a.k.a. P)
        32: (255, 255, 204)  # error correction (C1 a.k.a. P)
    }

    for y in range(490):
        for x in range(588):
            if delta_signal[588 * y + x]:
                im.putpixel((x, y), (0, 0, 0))
            else:
                if x < 24:
                    im.putpixel((x, y), (255, 204, 204)) # sync pattern
                elif (x - 24) % 17 < 3:
                    im.putpixel((x, y), (204, 204, 204)) # merge bits
                else:
                    im.putpixel((x, y), colormap[(x - 24) // 17])

    im.save("delta-signal-colored.png")
