import cv2  
  
# 读取两张图像  
img1 = cv2.imread('./1jietupng.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('./2murphypng.png', cv2.IMREAD_UNCHANGED)
img3 = cv2.imread('./3paizhaojpg.jpg', cv2.IMREAD_UNCHANGED)

print(img1.shape)
print(img2.shape)
print(img3.shape)