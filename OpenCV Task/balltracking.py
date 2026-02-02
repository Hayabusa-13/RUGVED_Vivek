import cv2
import numpy as np

cap = cv2.VideoCapture("Ball_Tracking.mp4")

path = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lg= np.array([35, 70, 70])  # took data from google 
    ug = np.array([85, 255, 255]) # took data from google 

    mask = cv2.inRange(hsvimg, lg, ug)

    con,a = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(con) > 0:
        ball = max(con, key=cv2.contourArea)
        M = cv2.moments(ball)
        if M["m00"] != 0:
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            path.append((x, y))
            cv2.circle(frame, (x, y), 1, (0, 255, 0))

    for i in range(1, len(path)):
        cv2.line(frame, path[i-1], path[i], (0, 0, 255), 5)

    cv2.imshow("Green Ball Tracking", frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
New things i have learnt from gpt, not from video:

1)M = cv2.moments(ball)
 if M["m00"] != 0:
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            path.append((x, y))
            cv2.circle(frame, (x, y), 1, (0, 255, 0))

Here , M is a dictionary which contains the data of the ball like the area,sum of all the x-cordinates
y-cordinates and etc(x^2)sum all that stuff

So in that line of code , what we have done is we have taken the value of m10 and divide it with the area
like sum of all x--cordinates/area and then m01 is the same but with y cordinates 

and then that is going to get appended to the path variable , its going to iterrate through each frame 



2) for i in range(1, len(path)):
        cv2.line(frame, path[i-1], path[i], (0, 0, 255), 5)

here this code draws line a line from previous point to the next point that are stored in the path 
variable ,

inside the path variable  the coordinates are stored in tuples .

so the line traces along those tupled points in that variable from one point to another 

Mistake i have done:
first i have used 0 in the range , then while tracing , it finxed an endpoint and started tracing it

3)
  if there isnt avalability of google we can use trackbars as well by setting the hue min, hue max, 
  sat min , sat max , val min , val max and then we can adjust it to our wish and then we can set the
  values we get in the trackbars to the max and min vaues to get the image/video
  if it is an image we can use bitwise_and() and we can add the colour to the desired image 
'''