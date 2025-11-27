import cv2

#open default Webcam (0)
cap = cv2.VideoCapture(0)

#Check if open was a success
if not cap.isOpened():
    print("Error: Could not open Camera")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc('M','J','P','G'),
    20, #FPS
    (frame_width, frame_height)
)

print("recording press q to stop...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame")
        break

    #Write frame to file
    out.write(frame)

    #Show Preview
    cv2.imshow('Webcam', frame)

    #Stop on q press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
print("Recording stopped and saved as output.avi")


