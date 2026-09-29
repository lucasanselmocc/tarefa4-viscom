import cv2, numpy, sys

# Lê a imagem original e o número do ruído
imgOriginal = cv2.imread(sys.argv[1], 0)
k = int(sys.argv[2])

# Lê a imagem com ruído gerada pelo gerarRuido.py
img = cv2.imread("ruido" + str(k) + ".png", 0)

# Verifica se as imagens foram abertas corretamente
if imgOriginal is None:
    print("Erro ao abrir a imagem original.")
    sys.exit()

if img is None:
    print("Erro ao abrir a imagem com ruído.")
    sys.exit()

# Escolha do filtro de acordo com o tipo de ruído :P
# Para salt and pepper a mediana costuma remover os pixels
# extremos sem borrar tanto as bordas
if k == 0:              # sal e pimenta leve
    imgResultante = cv2.medianBlur(img, 3)

elif k == 1:            # gaussiano leve
    imgResultante = cv2.GaussianBlur(img, (3, 3), 0)

elif k == 2:            # sal moderado
    imgResultante = cv2.medianBlur(img, 5)

elif k == 3:            # pimenta moderado
    imgResultante = cv2.medianBlur(img, 5)

elif k == 4:            # gaussiano grave
    imgResultante = cv2.GaussianBlur(img, (5, 5), 0)

elif k == 5:            # sal e pimenta grave
    imgResultante = cv2.medianBlur(img, 7)

else:
    print("k deve estar entre 0 e 5.")
    sys.exit()

# Calcula o PSNR usando a imagem original como referência
psnr = cv2.PSNR(imgResultante, imgOriginal)

# Coloca o PSNR na legenda da imagem filtrada
cv2.putText(
    imgResultante,
    "PSNR = " + str("%.2f" % psnr) + " dB",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    255,
    2
)

# Exibe a imagem com ruído e a imagem filtrada lado a lado
comparacao = cv2.hconcat([img, imgResultante])

cv2.imshow("Tarefa 4", comparacao)
cv2.waitKey(0)
cv2.destroyAllWindows()