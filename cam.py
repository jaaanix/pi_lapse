from time import sleep
from picamera import PiCamera
import subprocess
import sys

print 'Start PiCam timelapse image capturing...'
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument list:', str(sys.argv)
print 'First argument: Capture interval in seconds =', str(int(sys.argv[1]))
print 'Second argument: Amount of picture taken =', str(int(sys.argv[2]))
print 'Third argument: FPS for rendering =', str(int(sys.argv[3]))

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()

sleep(2)

for x in range(int(sys.argv[2])):
    print 'Capturing picture %s' % (x)
    camera.capture('%s_img.jpg' % (x))
    sleep(int(sys.argv[1]))

subprocess.call(['ffmpeg', '-y',  '-r', '20', '-start_number', '0', '-i', '%d_img.jpg', '-s', '1280x720', '-vcodec', 'libx264', 'timelapse.mp4'])

