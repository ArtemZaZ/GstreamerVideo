import time
import math
import RTCvideo

IP = '173.1.0.86'
RTP_RECV_PORT0 = 5000
RTCP_RECV_PORT0 = 5001
RTCP_SEND_PORT0 = 5005

video = RTCvideo.Video(IP, RTP_RECV_PORT0, RTCP_RECV_PORT0, RTCP_SEND_PORT0, codec="H264")
video.drawOverlay("ring.png", x=0, y=0, scaleX=0.3, scaleY=0.2, fullScreen=True)

print("I started")
video.start()

time.sleep(40)

video.paused()
print("I paused")

time.sleep(5)

video.stop()
print("I stopped")
