import cv2

image = cv2.imread("WhatsApp Image 2026-09-08 at 7.49.33 AM.jpeg")
imgtype = image.dtype
(h, w, c) = image.shape

for i in range(w):
    for j in range(h):
        image[j, i, 1] = 0
        image[j, i, 0] = 0

cv2.imshow("foto", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w, c = frame.shape

    for i in range(w):
        for j in range(h):
            frame[j, i, 1] = 0
            frame[j, i, 0] = 0

    cv2.imshow("video", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
