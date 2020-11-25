#importing Libraries
import cv2
import pytesseract

#set the path of Tesseract-OCR file
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#read image
img = cv2.imread(r'C:\Users\user\Desktop\a.png')

# cv2.imshow("sample",img)
# cv2.waitKey(0)

#print the text on the console
print(pytesseract.image_to_string(img))

#detecting individual characters
h_img,w_img,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])               
    cv2.rectangle(img,(x,h),(x+w,y+h),(0,0,225),1)              #create boxes around the characters
    cv2.putText(img,b[0],(x,h_img-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)         #preview the characters on the image

cv2.imshow("RESULT",img)    #preview the image
cv2.waitKey(0)              #for holding the window for infinite time
