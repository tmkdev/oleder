from screens.oledmodule import OledModule
import datetime

class AnalogClock(OledModule):
    def __init__(self, width, height):
        super().__init__(width, height)


    def update(self, disp):
        now = datetime.datetime.now()
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        center_x = int(self.width/2) 
        center_y = int(self.height/2)

        y_radius = int(self.height/2) - 1
        x_radius = (int(self.height/2) - 1) * 2

        self.draw.point([center_x, center_y], fill=1)
        self.draw.ellipse([center_x - x_radius, center_y - y_radius, center_x + x_radius, center_y + y_radius], fill=0, outline=1)

        for x in range(12):
            ang = x * (360/12) - 90
            self.draw.pieslice([center_x - x_radius, center_y - y_radius, center_x + x_radius, center_y + y_radius], ang-2, ang+2, fill=1, outline=1)

        self.draw.ellipse([center_x - x_radius + 8 , center_y - y_radius + 4, center_x + x_radius - 8 , center_y + y_radius - 4], fill=0, outline=0)


        s = int((now.second / 60) * 360) - 90
        m = int((now.minute / 60) * 360) - 90 
        h = int((now.hour % 12 / 12) * 360) - 90 

        self.draw.pieslice([center_x - x_radius, center_y - y_radius, center_x + x_radius, center_y + y_radius], s-1, s+1, fill=1, outline=1)
        self.draw.pieslice([center_x - x_radius + 8, center_y - y_radius + 4, center_x + x_radius - 8, center_y + y_radius - 4 ], m-2, m+2, fill=1, outline=1)
        self.draw.pieslice([center_x - x_radius + 16, center_y - y_radius + 8, center_x + x_radius - 16, center_y + y_radius - 8], h-3, h+3, fill=0, outline=1)


        #self.draw.text((0,0), now, font=self.font_m, fill=255)
        #self.draw.text((0,16), time, font=self.font_m, fill=255)
        
        # Display image.
        disp.image(self.image)
        disp.show()

