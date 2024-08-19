#کتابخامه
import requests
from colorama import Fore,init


#متغیر
site = "https://www.digikala.com/"
respans = requests.get(site)


#دریافت به صورت متن کامل
lists = str(respans.headers)


#تبدیل به لیست
list = lists.split(',')


#زدن حلقه برای نمایش زیباتر
x = 0
for i in range(len(list)):
    if x %2 == 0:
        print(Fore.GREEN)
        print(list[x])
        print("\n")
        x += 1
    elif x %2 != 0:
        print(Fore.YELLOW)
        print(list[x])
        print("\n")
        x += 1


#سازنده
#  id = Ghasem_slp
#  github = ghasemslp