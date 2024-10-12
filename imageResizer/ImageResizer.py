import cv2

source = "1.jpg"
dest= "new1.jpg"
scale = 1000

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

nwidth = int(src.shape[1] * scale / 100)
nhight = int(src.shape[0] * scale / 100)

output = cv2.resize(src , (nwidth, nhight))
cv2.imwrite(dest, output)