from windows_capture_devices import get_capture_devices
import av
from PIL import Image


if __name__ == "__main__":
    # get list of device names
    device_list = get_capture_devices()

    # initialize a webcam handle using PyAV and the DirectShow backend
    cam_device = av.open(format="dshow", file=f"video={device_list[0]}")
    video_stream = cam_device.streams.video[0]

    # grab one frame from the video stream and save it
    for frame in cam_device.decode(video_stream):
        img = frame.to_image()
        break

    assert isinstance(img, Image.Image)
    img.save(f"test_{device_list[0]}.jpg")
    print(f"Success! An image from the {device_list[0]} webcam was stored.")

    # clean up
    cam_device.close()
