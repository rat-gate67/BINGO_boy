import cv2
import matplotlib.pyplot as plt

def cut(points,img,count):

    x1 = points[0][0]
    x2 = points[1][0]
    y1 = points[0][1]
    y2 = points[2][1]

    cropped_image = img[y1:y2,x1:x2]

    # 5x6にする
    rows, cols = 6, 5

    height, width, _ = cropped_image.shape
    dheight = height // 6
    dwidth = width  // 5

    margin = 0

    for i in range(rows):
        for j in range(cols):
        
            cell = cropped_image[i*dheight-margin:(i+1)*dheight+margin, j*dwidth-margin:(j+1)*dwidth+margin]
            # cv2.imshow("cell",cell)
            # cv2.waitKey(0)
            cv2.imwrite(f"source/{30*count + cols*i + j + 1}.png",cell)
            print(f"saved " + f"source/{30*count + cols*i + j + 1}.png")



def onMouse(event,x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        print(points)
    if event == cv2.EVENT_RBUTTONDOWN:
        points.pop()
        print(points)


for i in range(8):
    points = []  
    img = cv2.imread(f"image/{i+1}.jpeg")
    cv2.imshow("1",img)
    cv2.setMouseCallback("1",onMouse,param=[img,points])
    cv2.waitKey(0)
    print(f"points = {points}")
    cut(points,img,i)