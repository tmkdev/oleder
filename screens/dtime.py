from screens.oledmodule import OledModule
import datetime

class Dtime(OledModule):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self, disp):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        now = datetime.datetime.now().strftime('%b %d, %Y')
        time = datetime.datetime.now().strftime('%H:%M:%S %Z')

        self.draw.text((0,0), now, font=self.font_m, fill=255)
        self.draw.text((0,16), time, font=self.font_m, fill=255)
        
        # Display image.
        disp.image(self.image)
        disp.show()

