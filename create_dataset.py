import cv2
from PIL import Image, ImageDraw
#global fileno = 1
camera = cv2.VideoCapture(0)
fileno =1 
gesture = '1'
minValue = 127
while(True):
    
    ret, img = camera.read()
    
    img = cv2.flip(img , 1)
    img2 = img
    cv2.rectangle(img2 , (400 , 100) , (600 , 300) , ( 0 , 0,255),5)
    cv2.putText(img2, 'ROI', (400, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.putText(img2, 'Step 1', (30 , 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('RGB', img2)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray2 = gray
    cv2.putText(gray2, 'Step 2', (30 , 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('Grayscale' , gray2)
    gray = cv2.GaussianBlur(gray ,(5,5),cv2.BORDER_DEFAULT)

    blur = cv2.GaussianBlur(gray,(5,5),2)
    th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(th2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    res2 = res
    cv2.putText(res2, 'Step 3.A', (30 , 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow("Canny Edge" , res2)
    #cv2.imshow("O1" ,th2)

    binary = img_binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
    binary2 = binary
    cv2.putText(binary2, 'Step 3.B', (30 , 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('binary' , binary2)

    binary_crop = binary[100:300 ,400:600]
    cv2.putText(binary_crop, 'Step 3.B.1', (30 , 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('Binary Crop' , binary_crop)

    crop = res[100:300 ,400:600]
    crop2 = crop
    cv2.putText(crop2, 'Step 3.A.1', (30 , 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('Outline crop' , crop2)

    height = 50
    width = 50
    dim = (width , height)
    resized = cv2.resize(crop, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("resize" , resized)
    #print("img")
    pil_image = Image.fromarray(resized) 
    final_img = pil_image.resize((128 , 128), Image.ANTIALIAS)
    
    path = "C:\\Users\\randa\\Desktop\\Btech project\\Code\\Data\\Test\\5\\"
    if cv2.waitKey(1) == 32:
        name = path+ str(fileno) +".jpg"
        #cv2.imwrite(name,resized)
        final_img.save(name)
        fileno = fileno+1
        print("saved" + str(fileno))
        continue
        
    if cv2.waitKey(1) == 27:
        break
 
camera.release()
cv2.destroyAllWindows()
