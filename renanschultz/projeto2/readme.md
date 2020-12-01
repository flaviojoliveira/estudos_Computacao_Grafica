### PROJETO 2 ###

## REALIZAMOS A IMPORTAÇÃO DE IMAGENS E DEFINIMOS ALTURA E LARGURA ##





import cv2
import numpy as np

imagem = cv2.imread('imagem.png')

altura= imagem.shape[0]
largura = imagem.shape[1]

q_altura, q_largura = altura / 2, largura / 2

T = np.float32([[1, 0, q_largura,][0, 1, q_altura]])

img_translation = cv2.warpffline(imagem, T,(largura,altura))

cv2.imfitel('traslacao.png', img_translation)
