from PIL import Image, ImageOps
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(HERE, "originales")
out = os.path.join(os.path.dirname(HERE), "assets")
os.makedirs(out, exist_ok=True)

for f in ["logo-original.jpg", "foto-original.jpg"]:
    p = os.path.join(ORIG, f)
    im = Image.open(p)
    print(f, im.size, os.path.getsize(p) // 1024, "KB")

# Logo: transparencia a partir de la luminancia (letras oscuras sobre fondo claro),
# recortado al contenido y en dos versiones: azul (fondo claro) y blanca (fondo oscuro).
lg = Image.open(os.path.join(ORIG, "logo-original.jpg")).convert("L")
alpha = ImageOps.invert(lg).point(lambda v: 0 if v < 28 else min(255, int((v - 28) * 1.25)))
bbox = alpha.getbbox()
print("bbox", bbox)
alpha = alpha.crop(bbox)
for name, rgb in [("logo-blanco", (255, 255, 255)), ("logo-azul", (11, 16, 34))]:
    im = Image.new("RGBA", alpha.size, rgb + (0,))
    im.putalpha(alpha)
    w = 900
    h = int(alpha.size[1] * w / alpha.size[0])
    im = im.resize((w, h), Image.LANCZOS)
    im.save(out + "/" + name + ".png", optimize=True)
    print(name, im.size)

# Foto: recorte inferior para el encuadre y reducción de peso.
ph = Image.open(os.path.join(ORIG, "foto-original.jpg")).convert("RGB")
W, H = ph.size
ph = ph.crop((0, 0, W, int(H * 0.86)))
ph.thumbnail((820, 820))
ph.save(out + "/foto-lic-mena.jpg", quality=84, optimize=True)
print("foto", ph.size)

for f in sorted(os.listdir(out)):
    print(f, os.path.getsize(out + "/" + f) // 1024, "KB")
