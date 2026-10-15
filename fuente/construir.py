# Genera la carpeta lista para GitHub Pages: index.html completo (SEO), assets, favicons,
# imagen para compartir (OG), CNAME, robots, sitemap y 404.
import os, sys, json, shutil
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # raíz del repositorio
DOM = "mgconsultorialegal.com.mx"
URL = f"https://{DOM}/"
sys.path.insert(0, HERE)
import contenido as B

TITLE = "M&G Consultoría Legal | Abogados en materia condominal, administrativa y civil en Edomex y CDMX"
DESC = ("Despacho de abogados especializado en materia condominal, administrativa y civil. "
        "Auditoría condominal, recuperación de cartera, asambleas, juicios y trámites en el Estado de México "
        "y la CDMX. Primera asesoría sin costo.")

# Las imágenes del sitio viven en assets/ (las genera preparar_imagenes.py).

# ---- Favicons e imagen para compartir ----------------------------------------
NAVY = (11, 21, 48)
GOLD = (246, 184, 29)
lg = Image.open(f"{OUT}/assets/logo-blanco.png").convert("RGBA")
mark = lg.crop((0, 0, lg.size[0], 335))  # solo las letras M&G, sin la leyenda


def icon(size):
    im = Image.new("RGBA", (size, size), NAVY + (255,))
    pad = int(size * 0.14)
    w = size - 2 * pad
    h = int(mark.size[1] * w / mark.size[0])
    m = mark.resize((w, h), Image.LANCZOS)
    im.alpha_composite(m, (pad, (size - h) // 2))
    d = ImageDraw.Draw(im)
    d.rectangle([0, size - max(3, size // 40), size, size], fill=GOLD)
    return im


icon(512).save(f"{OUT}/icon-512.png", optimize=True)
icon(192).save(f"{OUT}/icon-192.png", optimize=True)
icon(180).save(f"{OUT}/apple-touch-icon.png", optimize=True)
icon(256).save(f"{OUT}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

og = Image.new("RGBA", (1200, 630), NAVY + (255,))
w = 640
h = int(lg.size[1] * w / lg.size[0])
og.alpha_composite(lg.resize((w, h), Image.LANCZOS), ((1200 - w) // 2, (630 - h) // 2 - 10))
ImageDraw.Draw(og).rectangle([0, 622, 1200, 630], fill=GOLD)
og.convert("RGB").save(f"{OUT}/og-image.png", optimize=True)

# ---- index.html completo ----------------------------------------------------------
page = B.build()
cut = page.index('<header class="nav">')
head_part, body_part = page[:cut], page[cut:]
# El título viene como <title>…</title> al inicio: se reemplaza por el título SEO.
head_part = head_part.replace("<title>M&amp;G Consultoría Legal</title>", f"<title>{B.e(TITLE)}</title>")

ld = {
    "@context": "https://schema.org",
    "@type": "LegalService",
    "name": "M&G Consultoría Legal",
    "url": URL,
    "image": URL + "og-image.png",
    "logo": URL + "assets/logo-azul.png",
    "telephone": "+525633390183",
    "email": B.MAIL,
    "description": DESC,
    "address": {"@type": "PostalAddress", "addressLocality": "Cuautitlán Izcalli",
                "addressRegion": "Estado de México", "addressCountry": "MX"},
    "areaServed": ["Estado de México", "Ciudad de México"],
    "founder": {"@type": "Person", "name": "José Ángel Mena Galván", "jobTitle": "Licenciado en Derecho"},
    "knowsAbout": ["Derecho condominal", "Derecho administrativo", "Derecho civil", "Arrendamiento",
                   "Recuperación de cartera condominal"],
}

meta = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{B.e(DESC)}">
<meta name="theme-color" content="#0B1530">
<link rel="canonical" href="{URL}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/icon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:site_name" content="M&amp;G Consultoría Legal">
<meta property="og:title" content="{B.e(TITLE)}">
<meta property="og:description" content="{B.e(DESC)}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}og-image.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
"""
html_doc = meta + head_part + "</head>\n<body>\n" + body_part + "\n</body>\n</html>\n"
open(f"{OUT}/index.html", "w", encoding="utf-8").write(html_doc)

# ---- Archivos de soporte ----------------------------------------------------------
open(f"{OUT}/CNAME", "w", encoding="utf-8").write(DOM + "\n")
open(f"{OUT}/.nojekyll", "w").write("")
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {URL}sitemap.xml\n")
open(f"{OUT}/sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"  <url><loc>{URL}</loc></url>\n</urlset>\n")

nf = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1">'
      '<title>Página no encontrada | M&amp;G Consultoría Legal</title>'
      '<meta name="robots" content="noindex"></head>'
      '<body style="margin:0;min-height:100vh;display:grid;place-items:center;background:#0B1530;'
      'color:#f1f3fa;font-family:system-ui,sans-serif;text-align:center;padding:24px">'
      '<div><img src="/assets/logo-blanco.png" alt="M&amp;G Consultoría Legal" style="height:70px;margin:0 auto 24px">'
      '<h1 style="margin:0 0 10px">Esta página no existe</h1>'
      '<p style="color:#b3bbd6;margin:0 0 22px">Puede que el enlace haya cambiado.</p>'
      '<a href="/" style="background:#F6B81D;color:#0B1530;padding:12px 22px;border-radius:8px;'
      'font-weight:600;text-decoration:none">Ir al inicio</a></div></body></html>')
open(f"{OUT}/404.html", "w", encoding="utf-8").write(nf)

open(f"{OUT}/README.md", "w", encoding="utf-8").write(
    "# Sitio web de M&G Consultoría Legal\n\n"
    f"Sitio estático publicado con GitHub Pages en https://{DOM}/\n\n"
    "- `index.html`: la página completa (HTML y CSS en un solo archivo).\n"
    "- `assets/`: logo y foto.\n"
    "- `CNAME`: dominio personalizado. No borrar.\n"
    "- `fuente/contenido.py`: textos, servicios y precios. Después de editarlo, corre\n"
    "  `python fuente/construir.py` y sube los cambios.\n"
    "- `fuente/originales/`: logo y foto originales. `python fuente/preparar_imagenes.py`\n"
    "  regenera `assets/`.\n")

for root, _, files in os.walk(OUT):
    for f in files:
        p = os.path.join(root, f)
        print(os.path.relpath(p, OUT).replace("\\", "/"), os.path.getsize(p) // 1024, "KB")
