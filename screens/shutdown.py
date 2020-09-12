import time
import subprocess
import logging

from screens.oledmodule import OledModule

class Shutdown(OledModule):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self, disp):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        
        self.draw.text((0,0), "Shutdown", font=self.font_m, fill=255)
        self.draw.text((0,16), "  Now!  ", font=self.font_m, fill=255)

        disp.image(self.image)
        disp.show()

        time.sleep(5)

        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        disp.image(self.image)
        disp.show()


        command = '/usr/bin/sudo poweroff'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        logging.critical(output)
