#کتابخانه
import sounddevice as sd
import pygame
from scipy.io.wavfile import write
pygame.init()
from colorama import Fore,init



#تنظمات ضبط
fs = 44100
seconds = 7


#شروع ضبط
print(Fore.YELLOW +"شروع ضبط")
myrecording = sd.rec(int(seconds * fs),samplerate=fs,channels=2,dtype='int16')
sd.wait()

#پایان ضبط
print("پایان ضبط")
write('ghasemslp.mkv',fs,myrecording)
pygame.mixer.music.load('ghasemslp.mkv')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
pygame.quit()


#لطفا از تولید کننده اصلی این کد حمایت کنید
# id : Ghasem_slp
# github : ghasemslp
