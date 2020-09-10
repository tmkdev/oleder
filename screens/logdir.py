from screens.oledmodule import OledModule
import subprocess
import os

class LogDir(OledModule):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.logpath=os.getenv('OLED_LOGDIR', None)

    def update(self, disp):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        if self.logpath:
            cmd = f"ls {self.logpath}/*.log | wc -l"
            LogCount = subprocess.check_output(cmd, shell=True).decode("utf-8")
            lctext = f"Log files: {LogCount}"
            self.draw.text((0, 0), lctext, font=self.font, fill=255)

            cmd = f"ls -tr {self.logpath} | tail -n 1"
            LASTFILE = subprocess.check_output(cmd, shell=True).decode("utf-8")
            lf = f"Last Log: {LASTFILE}"
            self.draw.text((0, 8), lf, font=self.font, fill=255)
    
            cmd = f"du -h --max-depth=1 {self.logpath} | tail -n 1 | cut -f 1"
            PathDisk = subprocess.check_output(cmd, shell=True).decode("utf-8")
            lu = f"Last Log Size: {PathDisk}"
            self.draw.text((0, 16), lu, font=self.font, fill=255)
 
        cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")


        self.draw.text((0, 24), Disk, font=self.font, fill=255)

        # Display image.
        disp.image(self.image)
        disp.show()

