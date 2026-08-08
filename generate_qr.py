import os
import urllib.parse
import qrcode

ROOT = "D:/Undangan ABG"
os.chdir(ROOT)

url = "http://localhost:8000/index.html"
message = f"Undangan pernikahan Isa & Dea. Silakan buka: {url}"
wa_link = "https://wa.me/?text=" + urllib.parse.quote(message)

with open("wa_link.txt", "w", encoding="utf-8") as f:
    f.write(wa_link + "\n")
    f.write(url + "\n")

img = qrcode.make(wa_link)
img.save("qrcode_whatsapp.png")

print("Local URL:", url)
print("WhatsApp link:", wa_link)
print("QR saved to:", os.path.join(ROOT, "qrcode_whatsapp.png"))
