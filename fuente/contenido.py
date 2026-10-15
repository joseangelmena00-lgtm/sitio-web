# Genera mg-sitio.html (landing de M&G Consultoría Legal).
# Todo el contenido editable vive en los datos de abajo; el CSS y el HTML son plantillas.
from urllib.parse import quote
import html

WA = "525633390183"
TEL2 = "55 7829 5140"
MAIL = "lic.angelmena@mgconsultorialegal.com.mx"
FACEBOOK = "https://www.facebook.com/profile.php?id=61579069425314"
TIKTOK = "https://www.tiktok.com/@myg.consultorialegal"
FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21z"/></svg>'
TT_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.6 3c.3 2.2 1.6 3.6 3.9 3.8v2.6c-1.4.1-2.6-.3-3.9-1.1v5.3c0 6.6-7.2 8.6-10.1 3.9-1.9-3-.7-8.3 5.3-8.5v2.8c-.5.1-.9.2-1.4.3-1.4.5-2.2 1.4-2 3 .4 3 6 3.9 5.5-2V3z"/></svg>'

DOMINIO = "mgconsultorialegal.com.mx"


def wa(texto):
    return f"https://wa.me/{WA}?text={quote(texto)}"


def e(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
#  CATÁLOGO DE SERVICIOS POR TIPO DE CLIENTE
#  precio: None -> "Cotización sin costo"; texto -> se muestra tal cual.
#  tipo:   "exito" (honorario por resultado) | "desde" (precio de referencia)
# ---------------------------------------------------------------------------
PANELES = [
    {
        "id": "condominio",
        "tab": "Administradores y comités",
        "lead": "Para quienes administran o dirigen un condominio y necesitan que todo esté en regla.",
        "cards": [
            {
                "nombre": "Auditoría de cumplimiento legal y financiero",
                "badge": "Nuevo",
                "destacada": True,
                "desc": "Revisamos tu condominio de punta a punta y te entregamos un informe claro: qué está en regla y qué hay que corregir antes de la próxima asamblea.",
                "incluye": [
                    "Personalidad jurídica y antecedentes registrales",
                    "Cuentas, cuotas y fondo de reserva",
                    "Actas, convocatorias y asambleas",
                    "Reglamento interior y plan de acción",
                ],
                "precio": None,
            },
            {
                "nombre": "Asambleas en regla",
                "desc": "Documentación y acompañamiento para celebrar asambleas generales o extraordinarias sin que nadie las pueda impugnar.",
                "incluye": [
                    "Convocatoria conforme a la ley",
                    "Orden del día y acta de asamblea",
                    "Asesoría durante la asamblea",
                ],
                "precio": None,
            },
            {
                "nombre": "Reglamento interior al día",
                "desc": "Elaboración, revisión o actualización del reglamento de tu condominio.",
                "incluye": [
                    "Revisión del reglamento vigente",
                    "Redacción o actualización",
                    "Adecuación a la legislación aplicable",
                ],
                "precio": None,
            },
            {
                "nombre": "Recuperación de cartera vencida",
                "desc": "Estrategia y representación para recuperar cuotas adeudadas, con convenios de pago, arbitraje o juicio según convenga.",
                "incluye": [
                    "Análisis de la cartera de morosos",
                    "Convenios de pago con seguimiento",
                    "Arbitraje o juicio cuando hace falta",
                ],
                "precio": "15% sobre lo recuperado",
                "tipo": "exito",
            },
            {
                "nombre": "Asesoría legal y contable continua",
                "desc": "Un despacho de cabecera para tu condominio, mes con mes.",
                "incluye": [
                    "Asesoría legal y contable condominal",
                    "Seguimiento mensual de tus asuntos",
                    "Un solo contacto para todo",
                ],
                "precio": "Desde $5,000 al mes",
                "tipo": "desde",
            },
            {
                "nombre": "Conflictos y juicios condominales",
                "desc": "Representación cuando el diálogo ya no alcanza.",
                "incluye": [
                    "Arbitraje condominal",
                    "Juicios civiles y ejecutivos",
                    "Defensa ante impugnaciones",
                ],
                "precio": None,
            },
        ],
    },
    {
        "id": "propietarios",
        "tab": "Civil y propietarios",
        "lead": "Para quien tiene una propiedad, la renta o vive en un condominio y necesita respaldo legal en materia civil.",
        "cards": [
            {
                "nombre": "Asesoría jurídica por hora",
                "desc": "Una hora con el abogado para resolver tu duda o revisar un documento antes de firmar.",
                "incluye": [
                    "Revisión de contratos y documentos",
                    "Orientación clara sobre tus opciones",
                    "Primera asesoría sin costo",
                ],
                "precio": "Desde $800 por hora",
                "tipo": "desde",
            },
            {
                "nombre": "Póliza jurídica de arrendamiento",
                "desc": "El respaldo legal para rentar tu propiedad con tranquilidad.",
                "incluye": [
                    "Póliza jurídica para tu contrato de renta",
                    "Revisión de las condiciones pactadas",
                    "Orientación si el inquilino incumple",
                ],
                "precio": "$4,500",
                "tipo": "desde",
            },
            {
                "nombre": "Juicios civiles",
                "desc": "Preparamos y presentamos tu demanda cuando hubo un daño patrimonial o un incumplimiento, y la llevamos hasta su resolución.",
                "incluye": [
                    "Análisis del caso y de las pruebas",
                    "Elaboración y presentación de la demanda",
                    "Juicio ordinario civil y ejecutivo civil",
                ],
                "precio": None,
            },
            {
                "nombre": "Antecedentes registrales y condominales",
                "desc": "Búsqueda y revisión de la historia legal de un inmueble o de un condominio.",
                "incluye": [
                    "Gestoría de búsqueda ante el IFREM",
                    "Revisión documental y de antecedentes",
                    "Resumen claro de lo encontrado",
                ],
                "precio": "Búsqueda ante el IFREM desde $1,000",
                "tipo": "desde",
            },
        ],
    },
    {
        "id": "empresas",
        "tab": "Empresas y negocios",
        "lead": "Para negocios que necesitan operar en regla y resolver conflictos sin perder tiempo.",
        "cards": [
            {
                "nombre": "Gestoría de trámites y permisos",
                "desc": "Trámites, permisos y servicios públicos ante el gobierno municipal y estatal.",
                "incluye": [
                    "Licencias y permisos de operación",
                    "Trámites de protección civil",
                    "Seguimiento hasta su resolución",
                ],
                "precio": None,
            },
            {
                "nombre": "Defensa ante multas y clausuras",
                "desc": "Si la autoridad te sancionó o clausuró, revisamos si procede y te defendemos.",
                "incluye": [
                    "Análisis del acto de autoridad",
                    "Recursos y promociones administrativas",
                    "Juicio de nulidad cuando corresponde",
                ],
                "precio": None,
            },
            {
                "nombre": "Asesoría laboral y conciliación",
                "desc": "Conciliación por rescisión laboral y asesoría en seguridad social.",
                "incluye": [
                    "Conciliación por rescisión laboral",
                    "Revisión de expediente de seguridad social",
                    "Acompañamiento en diligencias",
                ],
                "precio": None,
            },
            {
                "nombre": "Convenios y poderes",
                "desc": "Documentos claros que te protegen desde la firma.",
                "incluye": [
                    "Proyecto de convenio",
                    "Proyecto de poder notarial",
                    "Revisión antes de firmar",
                ],
                "precio": None,
            },
        ],
    },
    {
        "id": "gobierno",
        "tab": "Administrativo y autoridades",
        "lead": "Para cuando el conflicto es con una autoridad o necesitas gestionar ante el gobierno.",
        "cards": [
            {
                "nombre": "Procedimiento administrativo y recursos",
                "desc": "Procedimiento administrativo común y recursos de inconformidad.",
                "incluye": [
                    "Escritos y promociones",
                    "Desahogo de garantía de audiencia",
                    "Recursos de inconformidad",
                ],
                "precio": None,
            },
            {
                "nombre": "Juicio de nulidad",
                "desc": "Juicio contencioso administrativo para anular un acto de autoridad.",
                "incluye": [
                    "Demanda de nulidad",
                    "Seguimiento ante el tribunal",
                    "Alegatos",
                ],
                "precio": None,
            },
            {
                "nombre": "Créditos fiscales",
                "desc": "Defensa frente a créditos fiscales determinados por la autoridad.",
                "incluye": [
                    "Revisión del crédito y su origen",
                    "Medios de defensa procedentes",
                    "Seguimiento del asunto",
                ],
                "precio": None,
            },
            {
                "nombre": "Responsabilidades administrativas y denuncias",
                "desc": "Defensa en procedimientos de responsabilidad y denuncias ante Contraloría y fiscalía.",
                "incluye": [
                    "Defensa en procedimientos de responsabilidad",
                    "Denuncias ante Contraloría y fiscalía",
                    "Alegatos y promociones",
                ],
                "precio": None,
            },
            {
                "nombre": "Juicio de amparo",
                "desc": "Protección constitucional frente a actos y resoluciones de autoridad.",
                "incluye": [
                    "Análisis de procedencia",
                    "Demanda de amparo",
                    "Seguimiento hasta la sentencia",
                ],
                "precio": None,
            },
        ],
    },
]


def card_html(c):
    cls = "card feat" if c.get("destacada") else "card"
    badge = f'<span class="tag">{e(c["badge"])}</span>' if c.get("badge") else ""
    lis = "".join(f"<li>{e(x)}</li>" for x in c["incluye"])
    if c["precio"]:
        k = c.get("tipo", "desde")
        precio = f'<span class="price {k}">{e(c["precio"])}</span>'
    else:
        precio = '<span class="price">Cotización sin costo</span>'
    href = wa(f"Hola, me interesa el servicio: {c['nombre']}. Quisiera una cotización.")
    return (
        f'<article class="{cls}">{badge}'
        f'<h3>{e(c["nombre"])}</h3><p class="d">{e(c["desc"])}</p>'
        f'<ul>{lis}</ul>'
        f'<div class="foot">{precio}'
        f'<a class="cta" href="{href}" target="_blank" rel="noopener">Cotizar por WhatsApp →</a></div>'
        f"</article>"
    )


def paneles_html():
    tabs, panels = [], []
    for i, p in enumerate(PANELES):
        on = i == 0
        tabs.append(
            f'<button class="tabbtn" role="tab" id="tab-{p["id"]}" aria-controls="panel-{p["id"]}" '
            f'aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}">{e(p["tab"])}</button>'
        )
        cards = "".join(card_html(c) for c in p["cards"])
        panels.append(
            f'<div class="panel" role="tabpanel" id="panel-{p["id"]}" aria-labelledby="tab-{p["id"]}"'
            f'{"" if on else " hidden"}><p class="plead">{e(p["lead"])}</p><div class="cards">{cards}</div></div>'
        )
    return f'<div class="tabs" role="tablist" aria-label="Tipo de cliente">{"".join(tabs)}</div>' + "".join(panels)


CSS = """
  /* Layout: nav fija, hero azul con foto, catálogo por tipo de cliente (pestañas), proceso, despacho, contacto. Marca: azul del logo, amarillo de la publicidad, Poppins como en los flyers. */
  :root{
    --bg:#ffffff; --surface:#f3f5f9; --ink:#141a2e; --muted:#55607a; --line:#e0e4ee;
    --navy:#0B1530; --navy-2:#13204a; --on-navy:#f1f3fa; --on-navy-dim:#b3bbd6;
    --gold:#F6B81D; --gold-text:#7a5400; --on-gold:#0B1530;
    --logo-light:block; --logo-dark:none;
    --maxw:1140px;
    --f:"Poppins",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  }
  @media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
    --bg:#0d1019; --surface:#131827; --ink:#eceef7; --muted:#a4acc4; --line:#252b3e; --gold-text:#F6B81D;
    --logo-light:none; --logo-dark:block; color-scheme:dark;
  }}
  :root[data-theme="dark"]{
    --bg:#0d1019; --surface:#131827; --ink:#eceef7; --muted:#a4acc4; --line:#252b3e; --gold-text:#F6B81D;
    --logo-light:none; --logo-dark:block; color-scheme:dark;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);line-height:1.62;-webkit-font-smoothing:antialiased}
  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
  img{max-width:100%;display:block}
  a{color:inherit}
  h1,h2,h3{margin:0;line-height:1.15;text-wrap:balance;font-weight:700;letter-spacing:-.01em}
  p{margin:0}
  section{scroll-margin-top:80px}
  .wrap{max-width:var(--maxw);margin-inline:auto;padding-inline:20px}
  .eyebrow{font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--gold-text)}
  :focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:4px}

  /* Logo (dos versiones según tema) */
  .logo-l{display:var(--logo-light)} .logo-d{display:var(--logo-dark)}
  .logo-l,.logo-d{height:44px;width:auto}

  /* Botones */
  .btn{display:inline-flex;align-items:center;gap:8px;font-weight:600;text-decoration:none;border-radius:8px;padding:12px 22px;font-size:.93rem;transition:transform .12s ease}
  .btn:hover{transform:translateY(-1px)}
  .btn-gold{background:var(--gold);color:var(--on-gold)}
  .btn-line{border:1px solid rgba(255,255,255,.3);color:var(--on-navy)}

  /* Nav */
  .nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:30;background:var(--bg);border-bottom:1px solid var(--line)}
  .nav .wrap{display:flex;align-items:center;gap:22px;padding-block:12px}
  .nav-links{margin-left:auto;display:flex;gap:26px;align-items:center}
  .nav-links a{text-decoration:none;color:var(--muted);font-size:.9rem;font-weight:500}
  .nav-links a:hover{color:var(--ink)}
  .nav .btn{padding:10px 18px;font-size:.86rem}
  .nav .btn-gold{color:var(--on-gold)}
  @media (max-width:880px){.nav-links a:not(.btn){display:none}.nav-links{margin-left:auto}.logo-l,.logo-d{height:38px}}

  /* Hero */
  .hero{background:var(--navy);color:var(--on-navy);border-bottom:3px solid var(--gold)}
  .hero .wrap{display:grid;grid-template-columns:1.35fr .8fr;gap:48px;align-items:center;padding-block:72px}
  @media (max-width:880px){.hero .wrap{grid-template-columns:1fr;gap:36px;padding-block:48px}}
  .hero .eyebrow{color:var(--gold)}
  .hero h1{font-size:clamp(1.9rem,4.6vw,3rem);font-weight:800;margin-top:14px}
  .hero h1 span{color:var(--gold)}
  .hero .lead{color:var(--on-navy-dim);font-size:clamp(1rem,2vw,1.12rem);max-width:58ch;margin-top:18px}
  .pillars{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:24px;padding:0;list-style:none}
  .pillars li{display:flex;align-items:center;gap:9px;font-weight:600;font-size:.92rem;letter-spacing:.02em;text-transform:uppercase}
  .pillars li::before{content:"✓";display:grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--gold);color:var(--on-gold);font-size:.74rem;font-weight:800}
  .cta-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
  .hero small{display:block;margin-top:14px;color:var(--on-navy-dim);font-size:.8rem}
  .who{margin:0;justify-self:center;width:100%;max-width:360px;background:var(--navy-2);border-radius:14px;overflow:hidden;border-bottom:3px solid var(--gold)}
  .who img{width:100%;aspect-ratio:4/4.2;object-fit:cover;object-position:50% 12%}
  .who figcaption{padding:16px 20px}
  .who b{display:block;font-size:1.02rem}
  .who span{color:var(--on-navy-dim);font-size:.85rem}

  /* Banda de confianza */
  .trust{background:var(--surface);border-bottom:1px solid var(--line)}
  .trust .wrap{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding-block:22px}
  @media (max-width:760px){.trust .wrap{grid-template-columns:1fr;gap:12px}}
  .trust div{display:flex;flex-direction:column;min-width:0}
  .trust b{font-size:1.05rem}
  .trust span{color:var(--muted);font-size:.86rem}

  /* Secciones */
  .band{padding-block:72px}
  .band.alt{background:var(--surface)}
  .sec-head{max-width:64ch;margin-bottom:30px}
  .sec-head h2{font-size:clamp(1.55rem,3.6vw,2.2rem);margin-top:10px}
  .sec-head p{color:var(--muted);margin-top:12px}

  /* Pestañas por tipo de cliente */
  .tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}
  .tabbtn{font:inherit;font-weight:600;font-size:.9rem;padding:11px 18px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--muted);cursor:pointer}
  .tabbtn:hover{color:var(--ink);border-color:var(--muted)}
  .tabbtn[aria-selected="true"]{background:var(--navy);border-color:var(--navy);color:#fff}
  @media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .tabbtn[aria-selected="true"]{background:var(--gold);border-color:var(--gold);color:var(--on-gold)}}
  :root[data-theme="dark"] .tabbtn[aria-selected="true"]{background:var(--gold);border-color:var(--gold);color:var(--on-gold)}
  .plead{color:var(--muted);margin-bottom:22px;max-width:70ch}
  .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
  @media (max-width:980px){.cards{grid-template-columns:repeat(2,1fr)}}
  @media (max-width:640px){.cards{grid-template-columns:1fr}}
  .card{position:relative;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:24px;display:flex;flex-direction:column;gap:10px;min-width:0}
  .band.alt .card{background:var(--bg)}
  .card h3{font-size:1.06rem}
  .card .d{color:var(--muted);font-size:.9rem}
  .card ul{list-style:none;margin:4px 0 0;padding:0;display:flex;flex-direction:column;gap:7px;font-size:.88rem}
  .card li{display:flex;gap:9px}
  .card li::before{content:"";flex:none;width:6px;height:6px;border-radius:50%;background:var(--gold);margin-top:.6em}
  .foot{margin-top:auto;padding-top:16px;display:flex;flex-direction:column;gap:11px;align-items:flex-start}
  .price{font-size:.78rem;font-weight:600;letter-spacing:.01em;color:var(--muted);background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:4px 10px}
  .price.desde,.price.exito{color:var(--gold-text);border-color:color-mix(in srgb,var(--gold) 55%,var(--line));background:color-mix(in srgb,var(--gold) 12%,var(--bg))}
  .cta{font-weight:600;font-size:.88rem;text-decoration:none;color:var(--ink);border-bottom:2px solid var(--gold);padding-bottom:1px}
  .cta:hover{color:var(--gold-text)}
  .tag{position:absolute;top:16px;right:16px;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;background:var(--gold);color:var(--on-gold);padding:4px 10px;border-radius:5px}
  .card.feat{grid-column:span 2;background:var(--navy);border-color:var(--navy);border-top:3px solid var(--gold);color:var(--on-navy)}
  @media (max-width:640px){.card.feat{grid-column:span 1}}
  .card.feat h3{font-size:1.3rem;padding-right:70px}
  .card.feat .d{color:var(--on-navy-dim)}
  .card.feat ul{display:grid;grid-template-columns:1fr 1fr;gap:8px 20px}
  @media (max-width:640px){.card.feat ul{grid-template-columns:1fr}}
  .card.feat .price{background:transparent;border-color:rgba(255,255,255,.28);color:var(--on-navy)}
  .card.feat .cta{color:#fff}

  /* Proceso */
  .steps{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
  @media (max-width:760px){.steps{grid-template-columns:1fr}}
  .step{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:26px 24px}
  .step .n{font-weight:800;font-size:.95rem;color:var(--on-gold);background:var(--gold);width:34px;height:34px;border-radius:8px;display:grid;place-items:center;margin-bottom:14px}
  .step h3{font-size:1.05rem;margin-bottom:6px}
  .step p{color:var(--muted);font-size:.92rem}

  /* Opiniones */
  .rating{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin-top:14px}
  .rating b{font-size:2rem;font-weight:800;line-height:1}
  .stars{color:var(--gold);letter-spacing:2px;font-size:1.1rem}
  .rating span{color:var(--muted);font-size:.9rem}
  .reviews{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
  @media (max-width:980px){.reviews{grid-template-columns:repeat(2,1fr)}}
  @media (max-width:640px){.reviews{grid-template-columns:1fr}}
  .review{margin:0;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:22px 24px;display:flex;flex-direction:column;gap:12px;min-width:0}
  .review .stars{font-size:.95rem}
  .review blockquote{margin:0;font-size:.95rem;line-height:1.6}
  .review figcaption{margin-top:auto;display:flex;align-items:center;gap:10px;font-size:.86rem;color:var(--muted)}
  .review figcaption b{color:var(--ink);font-weight:600}
  .ini{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--navy);color:var(--gold);font-weight:700;font-size:.85rem}
  .more{margin-top:24px}
  .more a{font-weight:600;font-size:.92rem;text-decoration:none;border-bottom:2px solid var(--gold);padding-bottom:1px}

  /* El despacho */
  .about{display:grid;grid-template-columns:.8fr 1.3fr;gap:48px;align-items:center}
  @media (max-width:880px){.about{grid-template-columns:1fr;gap:28px}}
  .about img{width:100%;max-width:380px;border-radius:14px;aspect-ratio:4/4.2;object-fit:cover;object-position:50% 12%;border-bottom:3px solid var(--gold)}
  .about h2{font-size:clamp(1.55rem,3.6vw,2.2rem);margin-top:10px}
  .about p{color:var(--muted);margin-top:14px;max-width:60ch}
  .facts{display:flex;flex-wrap:wrap;gap:12px 36px;margin-top:26px}
  .facts div b{display:block;font-size:1.5rem;font-weight:800}
  .facts div span{color:var(--muted);font-size:.84rem}

  /* Contacto */
  .final{background:var(--navy);color:var(--on-navy);border-radius:14px;border-top:3px solid var(--gold);padding:clamp(30px,6vw,54px)}
  .final .grid{display:grid;grid-template-columns:1.2fr 1fr;gap:36px;align-items:center}
  @media (max-width:880px){.final .grid{grid-template-columns:1fr}}
  .final h2{font-size:clamp(1.6rem,4vw,2.3rem);font-weight:800}
  .final p{color:var(--on-navy-dim);margin-top:12px;max-width:52ch}
  .final .cta-row{margin-top:24px}
  .data{display:flex;flex-direction:column;gap:14px;font-size:.95rem;min-width:0}
  .data div{border-left:3px solid var(--gold);padding-left:14px;min-width:0;overflow-wrap:anywhere}
  .data span{display:block;color:var(--on-navy-dim);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600}
  .data b{font-weight:600}

  footer{border-top:1px solid var(--line);padding-block:30px;color:var(--muted);font-size:.82rem}
  footer .wrap{display:flex;flex-wrap:wrap;gap:16px 28px;align-items:center}
  footer .logo-l,footer .logo-d{height:34px}
  footer p{max-width:70ch;line-height:1.55}
  .social{display:flex;gap:10px;flex-wrap:wrap}
  .social a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600;font-size:.86rem;border:1px solid var(--line);border-radius:8px;padding:8px 12px;color:var(--ink)}
  .social a:hover{border-color:var(--gold)}
  .social svg{width:18px;height:18px}
  .data .social a{color:var(--on-navy);border-color:rgba(255,255,255,.25)}
  .data .social a:hover{border-color:var(--gold)}
"""

GOOGLE_PERFIL = "https://share.google/5sOMgyYVFmGWyNpgD"
GOOGLE_RATING = "5.0"
GOOGLE_TOTAL = 8

# Opiniones reales del Perfil de Negocio de Google, copiadas tal cual (octubre 2026).
# Se muestra nombre e inicial del apellido.
OPINIONES = [
    ("Beatriz B.", "Excelente servicio y atención profesional. La asesoría brindada fue clara, eficiente y de gran apoyo para resolver mis dudas. Trato amable, responsable y el compromiso demostrado durante todo el proceso. Sin duda, una consultoría altamente recomendable."),
    ("Delia M.", "Excelente asesoría acciones acertadas y resoluciones definitivas recomendable 100% el costo justo a mis posibilidades."),
    ("Verónica L.", "Asesorías muy profesionales y excelente guía con muy buenos resultados, muy recomendable"),
    ("Gerard M.", "Servicio profesional con un trato muy amable. La asesoría jurídica en materia fue muy clara y eficiente."),
    ("Alfredo G.", "Servicio profesional y pleno dominio en su materia, excelente atención Lic. Felicidades"),
    ("Roberto F.", "Buen servicio profesionistas competentes y dedicados si lo recomendaria 🤝"),
]

PROCESO = [
    ("Asesoría sin costo", "Nos cuentas tu situación por WhatsApp o por teléfono. Escuchamos y te decimos qué opciones tienes, sin compromiso."),
    ("Cotización clara", "Te presentamos el alcance, los tiempos y los honorarios por escrito antes de empezar. Sabes qué contratas y cuánto cuesta."),
    ("Ejecución y seguimiento", "Actuamos y te informamos cada avance. Puedes consultar el estado de tu asunto en un enlace privado, sin perseguir noticias."),
]


def build():
    logo_l = '<img class="logo-l" src="assets/logo-azul.png" alt="M&amp;G Consultoría Legal">'
    logo_d = '<img class="logo-d" src="assets/logo-blanco.png" alt="M&amp;G Consultoría Legal">'
    logo = logo_l + logo_d
    resenas = "".join(
        f'<figure class="review"><span class="stars" aria-label="5 de 5 estrellas">★★★★★</span>'
        f'<blockquote>“{e(t)}”</blockquote>'
        f'<figcaption><span class="ini" aria-hidden="true">{e(n[0])}</span><span><b>{e(n)}</b><br>Opinión en Google</span></figcaption></figure>'
        for n, t in OPINIONES
    )
    pasos = "".join(
        f'<div class="step"><div class="n">{i}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for i, (t, d) in enumerate(PROCESO, 1)
    )
    redes = (f'<div class="social">'
             f'<a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="M&amp;G en Facebook">{FB_SVG}Facebook</a>'
             f'<a href="{TIKTOK}" target="_blank" rel="noopener" aria-label="M&amp;G en TikTok">{TT_SVG}TikTok</a></div>')
    cta_general = wa("Hola, me gustaría agendar mi primera asesoría sin costo.")
    page = f"""<title>M&amp;G Consultoría Legal</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">
<style>{CSS}</style>

<header class="nav">
  <div class="wrap">
    <a href="#inicio" aria-label="M&amp;G Consultoría Legal">{logo}</a>
    <nav class="nav-links">
      <a href="#servicios">Servicios</a>
      <a href="#proceso">Cómo trabajamos</a>
      <a href="#opiniones">Opiniones</a>
      <a href="#despacho">El despacho</a>
      <a href="#contacto">Contacto</a>
      <a class="btn btn-gold" href="{cta_general}" target="_blank" rel="noopener">Asesoría sin costo</a>
    </nav>
  </div>
</header>

<main id="inicio">
  <section class="hero">
    <div class="wrap">
      <div>
        <p class="eyebrow">Consultoría especializada</p>
        <h1>Abogados expertos en materia <span>condominal, administrativa y civil.</span></h1>
        <p class="lead">Acompañamos a administradores, comités, propietarios y empresas en todo el Estado de México y la CDMX, y atendemos asuntos en otras entidades de la República. Resolvemos sus conflictos legales y mantenemos todo en regla, con lenguaje claro y costos definidos.</p>
        <ul class="pillars"><li>Condominal</li><li>Administrativa</li><li>Civil</li></ul>
        <div class="cta-row">
          <a class="btn btn-gold" href="{cta_general}" target="_blank" rel="noopener">Agenda tu primera asesoría sin costo</a>
          <a class="btn btn-line" href="#servicios">Ver servicios</a>
        </div>
        <small>Respuesta por WhatsApp · Sin compromiso.</small>
      </div>
      <figure class="who">
        <img src="assets/foto-lic-mena.jpg" alt="Lic. José Ángel Mena Galván">
        <figcaption><b>Lic. José Ángel Mena Galván</b><span>Licenciado en Derecho · M&amp;G Consultoría Legal</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="trust" aria-label="Datos del despacho">
    <div class="wrap">
      <div><b>+6 años de experiencia</b><span>En materia condominal y administrativa</span></div>
      <div><b>Todo el Edomex y la CDMX</b><span>Y disponibilidad en otras entidades de la República</span></div>
      <div><b>Primera asesoría sin costo</b><span>Conoce cómo trabajamos antes de decidir</span></div>
    </div>
  </section>

  <section id="servicios" class="band">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Servicios</p>
        <h2>¿Qué necesitas resolver?</h2>
        <p>Elige tu caso y mira exactamente qué incluye cada servicio. Si no encuentras el tuyo, escríbenos: lo cotizamos sin costo.</p>
      </div>
      {paneles_html()}
    </div>
  </section>

  <section id="proceso" class="band alt">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Cómo trabajamos</p>
        <h2>De tu duda a la solución, en tres pasos</h2>
      </div>
      <div class="steps">{pasos}</div>
    </div>
  </section>

  <section id="opiniones" class="band">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Opiniones de clientes</p>
        <h2>Lo que dicen quienes ya confiaron en nosotros</h2>
        <div class="rating"><b>{GOOGLE_RATING}</b><span class="stars" aria-label="5 de 5 estrellas">★★★★★</span><span>{GOOGLE_TOTAL} opiniones en Google</span></div>
      </div>
      <div class="reviews">{resenas}</div>
      <p class="more"><a href="{GOOGLE_PERFIL}" target="_blank" rel="noopener">Ver todas las opiniones en Google →</a></p>
    </div>
  </section>

  <section id="despacho" class="band alt">
    <div class="wrap about">
      <img src="assets/foto-lic-mena.jpg" alt="Lic. José Ángel Mena Galván, Licenciado en Derecho" loading="lazy">
      <div>
        <p class="eyebrow">El despacho</p>
        <h2>Un solo despacho, tres especialidades</h2>
        <p>M&amp;G Consultoría Legal está formado por abogados especializados en resolver conflictos jurídicos complejos. Nos enfocamos en materia condominal, administrativa y civil, y atendemos también trámites ante el gobierno y asuntos laborales ligados a tu propiedad o a tu negocio.</p>
        <p>Al frente está el Lic. José Ángel Mena Galván. Te explicamos cada paso en lenguaje claro y te decimos desde el inicio qué esperar.</p>
        <div class="facts">
          <div><b>+6</b><span>años de experiencia</span></div>
          <div><b>3</b><span>especialidades</span></div>
          <div><b>Nacional</b><span>Edomex, CDMX y otras entidades</span></div>
        </div>
      </div>
    </div>
  </section>

  <section id="contacto" class="band">
    <div class="wrap">
      <div class="final">
        <div class="grid">
          <div>
            <h2>Hablemos de tu caso</h2>
            <p>La primera asesoría es sin costo y sin compromiso. Cuéntanos qué necesitas y te decimos con claridad cómo podemos ayudarte.</p>
            <div class="cta-row"><a class="btn btn-gold" href="{cta_general}" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>
          </div>
          <div class="data">
            <div><span>Teléfonos</span><b>56 3339 0183 · {TEL2}</b></div>
            <div><span>Correo</span><b>{MAIL}</b></div>
            <div><span>Cobertura</span><b>Todo el Estado de México y la CDMX</b></div>
            <div><span>Otras entidades</span><b>Disponibilidad en toda la República</b></div>
            <div><span>Modalidad</span><b>Presencial y a distancia</b></div>
            <div><span>Síguenos</span>{redes}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <a href="#inicio" aria-label="M&amp;G Consultoría Legal">{logo}</a>
    {redes}
    <p>Lic. José Ángel Mena Galván. La información de este sitio es de carácter general y no constituye asesoría legal para un caso concreto; para ello, agenda una consulta. © <span id="y">2026</span> M&amp;G Consultoría Legal. Todos los derechos reservados.</p>
  </div>
</footer>

<script>
(function(){{
  var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));
  function sel(t,focus){{
    tabs.forEach(function(x){{
      var on=x===t;
      x.setAttribute('aria-selected',on?'true':'false');
      x.tabIndex=on?0:-1;
      document.getElementById(x.getAttribute('aria-controls')).hidden=!on;
    }});
    if(focus)t.focus();
  }}
  tabs.forEach(function(t,i){{
    t.addEventListener('click',function(){{sel(t,false)}});
    t.addEventListener('keydown',function(ev){{
      var k=ev.key,n=-1;
      if(k==='ArrowRight')n=(i+1)%tabs.length;
      else if(k==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;
      if(n>=0){{ev.preventDefault();sel(tabs[n],true)}}
    }});
  }});
  document.getElementById('y').textContent=new Date().getFullYear();
}})();
</script>
"""
    return page


if __name__ == "__main__":
    # Vista previa rápida (sin metadatos SEO). Para publicar usa fuente/construir.py.
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vista-previa.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(build())
    print("vista previa:", out)
