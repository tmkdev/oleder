from PIL import Image, ImageDraw, ImageFont


class OledModule(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)

        # Load default font.
        self.font = ImageFont.truetype(font='slkscr.ttf', size=7)
        self.font_m = ImageFont.truetype(font='slkscr.ttf', size=16)
        self.font_l = ImageFont.truetype(font='slkscr.ttf', size=24)
        

    def clearscreen(self, disp):
        disp.fill(0)
        disp.show()

    def update(self, disp):
        raise NotImplementedError