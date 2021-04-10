"""
noto_fonts Writes the names of three Noto font using the font
    converted from True Type fonts using the font2bitmap utility
    centered on the display.
"""

from pyb import SPI, Pin
import st7789

import NotoSans_32 as noto_sans
import NotoSerif_32 as noto_serif
import NotoSansMono_32 as noto_mono


def main():

    def center(font, s, row, color=st7789.WHITE):
        screen = tft.width()                     # get screen width
        width = tft.write_len(font, s)           # get the width of the string
        if width and width < screen:             # if the string < display
            col = tft.width() // 2 - width // 2  # find the column to center
        else:                                    # otherwise
            col = 0                              # left justify

        tft.write(font, s, col, row, color)      # and write the string

    try:
        tft = st7789.ST7789(
            SPI(1, SPI.MASTER, baudrate=42000000, prescaler=2),
            240,
            320,
            reset=Pin('X3', Pin.OUT),
            cs=Pin('X5', Pin.OUT),
            dc=Pin('X4', Pin.OUT),
            backlight=Pin('X2', Pin.OUT),
            rotation=3)

        tft.init()

        # enable display and clear screen
        tft.init()
        tft.fill(st7789.BLACK)

        # center the name of the first font, using the font
        row = 16
        center(noto_sans, "NotoSans", row, st7789.RED)
        row += noto_sans.HEIGHT

        # center the name of the second font, using the font
        center(noto_serif, "NotoSerif", row, st7789.GREEN)
        row += noto_serif.HEIGHT

        # center the name of the third font, using the font
        center(noto_mono, "NotoSansMono", row, st7789.BLUE)
        row += noto_mono.HEIGHT

    finally:
        # shutdown spi
        if 'spi' in locals():
            spi.deinit()


main()