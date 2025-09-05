from tkinter import filedialog
import tkinter as tk
import rembg
import numpy as np
from PIL import Image

dosyaYolu =None
kaydetmeYolu=None


def dosyayı_sec():
    global dosyaYolu
    dosyaYolu=filedialog.askopenfilename(defaultextension=".png",filetypes=[("PNG dosyaları","*.png"),
                                                                            ("JPEG dosyaları","*.jpg"),
                                                                            ("tüm Dosyalar","*.*")])


def dosyayı_kaydet():
    global kaydetmeYolu
    kaydetmeYolu = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG dosyaları", "*.png"),
                                                                               ("JPEG dosyaları", "*.jpg"),
                                                                               ("tüm Dosyalar", "*.*")])

def arkaplan_sil(dosya,kaydet):
    try:
        input_image = Image.open(dosya)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)
        output_image.save(kaydet)
        print("İşlem tamamlandı. Resim başarıyla kaydedildi!")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def islemi_baslat():

    if(dosyaYolu!=None and kaydetmeYolu!=None):
        arkaplan_sil(dosyaYolu,kaydetmeYolu)
    else:
        print("Bir dosya yolu veya ikisi birden seçilemedi.")


##gui

ana_pencere=tk.Tk()
ana_pencere.title("Arka PLan Silici")
ana_pencere.geometry("500x300")

buton_resim_sec=tk.Button(ana_pencere,text="Resim Seç",command=dosyayı_sec)
buton_kaydet_sec=tk.Button(ana_pencere,text="Kaydedecek Yolu Seç",command=dosyayı_kaydet)
buton_islem_basla=tk.Button(ana_pencere,text="İşlemi Başlat",command=islemi_baslat)

buton_resim_sec.pack(pady=10)
buton_kaydet_sec.pack(pady=10)
buton_islem_basla.pack(pady=10)

ana_pencere.mainloop()