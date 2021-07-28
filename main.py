import cv2
import pytesseract
import tweepy
import keys
from datetime import date
from scrshot import screenshot_data

# Twitter Authentication
auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
API = tweepy.API(auth)

# screenshot_data()
img = cv2.imread("name.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, img) = cv2.threshold(img, 210, 255, 1)

x=140
y=244
h=110
w=320

x1=697
y1=245
h1=95
w1=245
crop_img = img[y:y+h, x:x+w]
crop_img2 = img[y1:y1+h1, x1:x1+w1]

# crop_img = img[186:281, 120:365]
# crop_img2 = img[186:281, 510:755]

#Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
new = list(pytesseract.image_to_string(crop_img))
die = list(pytesseract.image_to_string(crop_img2))

# new.pop(2)
# b = int(''.join(new[:-2]))

# print("ติดเชื้อเพิ่มวันนี้ : " + ''.join(new[:-2]))
# print("เสียชีวิตวันนี้ : " + ''.join(die[:-2]))

today = date.today()
tm = today.strftime("%d/%m/%Y")

timeline = str("📅 วันที่ " + tm + " 📅\n \n" + "🚨🚨🚨 ยอดติดเชื้อเพิ่มวันนี้ : " + ''.join(new[:-2]) + " คน ❗❗\n" + "⚠⚠ เสียชีวิต : " + ''.join(die[:-2]) + " คน\n" + "#โควิดวันนี้ #โควิด19 #โควิด19วันนี้\n \n" + "ddc.moph.go.th/covid19-dashboard/")
API.update_status(timeline)
cv2.imshow('Result',crop_img)
cv2.imshow('Result2',crop_img2)
cv2.waitKey(0)

