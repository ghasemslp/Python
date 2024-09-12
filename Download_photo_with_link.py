#کتابخانه
from urllib.parse import urlparse
import requests
import os

#گرفتن ادرس
Addres_photo = str(input("Enter Photo Request Addres: "))

# پیدا کردن اسم فایل برای ذخیره
Name = urlparse(Addres_photo)
Photo_name = (os.path.basename(Name.path))

#تشخیص درست بودن لینک
Request = requests.get(Addres_photo)

#درخواست ذخیره
with open(Photo_name,"wb") as Photo:
    Photo.write(Request.content)


#         سازنده
#  instageram => Ghasem_slp
#  github => ghasemslp