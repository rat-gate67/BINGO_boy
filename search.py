import cv2

while 1:
    num = input("num?")
    img = cv2.imread(f"source/{num}.png")
    cv2.imshow("image",img)
    cv2.waitKey(0)