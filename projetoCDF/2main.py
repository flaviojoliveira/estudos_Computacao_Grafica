import numpy as numpy
import cv2

img=cv2.imread('milhos.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

altura = img.shape [0]
largura = img.shape[1]

laplace = (1.0/16)* np.array([[0, 0, -1, 0,0], [0,-1, -2, -1, 0], [-1, -2, 16, -2, -1,], [0, -1, -2, -1, 0,], [0, 0, -1, 0, 0,]])

sum(sum(laplace))

for i in np.arange(2, altura - 2):
  for j in np.arange(2, largura-2):
    sum = 0
    for k in np.arange(-2,3):
      for l in np.arange(-2,3):
        a = img.item(i+k, j+l)
        w = laplace [2+k, 2+l]
         b = sum
         img_out.itemset ((i,j), b)

cv2.imwrite('laplace.jpg', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)




