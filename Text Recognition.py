import cv2
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread(r'C:\Users\user\Desktop\a.png')
# cv2.imshow("sample",img)
# cv2.waitKey(0)

print(pytesseract.image_to_string(img))

h_img,w_img,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,h),(x+w,y+h),(0,0,225),1)
    cv2.putText(img,b[0],(x,h_img-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)

cv2.imshow("RESULT",img)
cv2.waitKey(0)








# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\Text recognition'
# img = cv2.imread('Data.png')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# x = cv2.imshow('Result', img)
# cv2.waitKey(0)