import cv2

img_file = 'C:/Download/girl.jpg'
save_file = 'C:/Download/girl_grey.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file,img)
cv2.waitKey( )
cv2.destroyAllWindows()