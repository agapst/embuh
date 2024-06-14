import cv2
import subprocess
import os

# Set environment variable at the start
os.environ['OPENCV_VIDEOIO_DEBUG'] = '0'

def ping_ip(ip_address):
    response = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

def check_rtsp_stream(url):
    try:
        cap = cv2.VideoCapture(url)
        if cap.isOpened():
            cap.release()
            return True
    except:
        pass
    return False

nvr_ip = "192.168.1.30"
channels = ["c1", "c2", "c3", "c4"]
username = "admin"
password = "Admin123@"

if ping_ip(nvr_ip):
    active_channels = []
    for channel in channels:
        rtsp_url = f"rtsp://{username}:{password}@{nvr_ip}:554/unicast/{channel}/s0"
        if check_rtsp_stream(rtsp_url):
            active_channels.append(channel)

    if not active_channels:
        print(f"NVR {nvr_ip} AKTIF - all channel CCTV unplugged")
    else:
        active_channels_str = ", ".join(active_channels)
        print(f"NVR {nvr_ip} AKTIF - RTSP PORT {active_channels_str} AKTIF")
else:
    print("NVR UNPLUGGED / NOT DETECTED")

