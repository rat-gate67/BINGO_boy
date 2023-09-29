import cv2

def onMouse(event,x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        print(points)
    if event == cv2.EVENT_RBUTTONDOWN:
        exit()


points = []  
img = cv2.imread("image/1.jpeg")
cv2.imshow("1",img)
cv2.setMouseCallback("1",onMouse,param=[img,points])
cv2.waitKey(0)

ex = 100

x1 = points[0][0]
x2 = points[1][0]
y1 = points[0][1]
y2 = points[2][1]

print(y1,y2, x1,x2)

cropped_image = img[y1:y2,x1:x2]
cv2.imshow("cropped image",cropped_image)
cv2.waitKey(0)