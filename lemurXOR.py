#see open cv lib documentation for beterr examples
#alse see geeksforkeeks.org 

import cv2 # pip upgrade then pip install opencv

#creating Image obj 1
flagImage = cv2.imread("/home/b00131083/college/Secure-Communications/CryptoHack/flag_7ae18c704272532658c10b5faad06d74.png")
#creating Image obj 2
lemurImage = cv2.imread("/home/b00131083/college/Secure-Communications/CryptoHack/lemur_ed66878c338e662d3473f0d98eedbd0d.png")

#apply bitwise xor using cv2 lib
outputImage = cv2.bitwise_xor(lemurImage, flagImage, mask = None)

#display the output image
cv2.imshow('Bitwise XOR', outputImage)

# deallocate memory
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
