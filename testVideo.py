import time
import math
import RTCvideo


IP = '127.0.0.1'
RTP_RECV_PORT0 = 5000
RTCP_RECV_PORT0 = 5001
RTCP_SEND_PORT0 = 5005


video=RTCvideo.Video(IP, RTP_RECV_PORT0, RTCP_RECV_PORT0, RTCP_SEND_PORT0)
video.drawOverlay("ring.png", x = 0, y = 0, scaleX = 0.3, scaleY = 0.2, fullScreen = True)


print("I started")
video.start()

time.sleep(30)

video.paused()
print("I paused")

time.sleep(30)

video.stop()
print("I stopped")





