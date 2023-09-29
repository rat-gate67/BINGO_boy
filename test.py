import cv2

# マウスイベントを処理するコールバック関数
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"カーソルの座標: ({x}, {y})\r", end="")  # \rで同じ行に表示し続ける

# 画像ファイルのパス
image_path = "image/1.jpeg"

# 画像を読み込む
image = cv2.imread(image_path)

# ウィンドウを作成し、マウスイベントを登録
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF

    # ウィンドウを閉じるためのキー操作 (qキー)
    if key == ord("q"):
        break

# ウィンドウを閉じる
cv2.destroyAllWindows()
