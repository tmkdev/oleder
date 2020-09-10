from screens.oledmodule import OledModule
import subprocess

class Stats(OledModule):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self, disp):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        cmd = "hostname -I | cut -d' ' -f1"
        IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")


        self.draw.text((0, 0), "IP: " + IP, font=self.font, fill=255)
        self.draw.text((0, 8), CPU, font=self.font, fill=255)
        self.draw.text((0, 16), MemUsage, font=self.font, fill=255)
        self.draw.text((0, 24), Disk, font=self.font, fill=255)

        # Display image.
        disp.image(self.image)
        disp.show()

