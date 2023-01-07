import cv2

start_time = int(
    input("Enter the value(in seconds) to start getting frames: "))
end_time = int(input("Enter the value(in seconds) to end getting frames: "))


path_of_video = r"J:\My Drive\Research\Videos\Spinning autism sign.mp4"
destination_path = r"J:\My Drive\Research\Dataset 50-75\Spinning autism sign\Raw images\time frame 8-11s"

vidcap = cv2.VideoCapture(path_of_video)


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        # save frame as JPG file
        cv2.imwrite(destination_path+"\image"+str(count)+".jpg", image)
    return hasFrames


sec = start_time
frameRate = 0.1  # //it will capture image in each 0.1 second, basically 10 frames per second
count = 1
success = getFrame(sec)
while success and sec <= end_time:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
