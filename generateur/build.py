#!/usr/bin/env python3
"""Génère les pages métier, les guides, le sitemap et robots.txt du site.

Usage (depuis la racine du dépôt) :  python3 generateur/build.py
Modifier le contenu dans metiers.py et guides.py, jamais directement dans les pages générées.
"""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from metiers import METIERS
from guides import GUIDES

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://duerp-conseil.fr"
AUJ = datetime.date.today().isoformat()
DEVIS = "https://tally.so/r/J11NXo"

LOGO = ('<svg width="28" height="28" viewBox="0 0 28 28" aria-hidden="true"><rect x="1" y="1" width="12" height="12" rx="2" fill="var(--r1)"/>'
        '<rect x="15" y="1" width="12" height="12" rx="2" fill="var(--r3)"/><rect x="1" y="15" width="12" height="12" rx="2" fill="var(--r2)"/>'
        '<rect x="15" y="15" width="12" height="12" rx="2" fill="var(--navy)"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 28 28'%3E%3Crect x='1' y='1' width='12' height='12' rx='2' fill='%23d9efe0'/%3E"
           "%3Crect x='15' y='1' width='12' height='12' rx='2' fill='%23fbd6b4'/%3E%3Crect x='1' y='15' width='12' height='12' rx='2' fill='%23fbeec3'/%3E"
           "%3Crect x='15' y='15' width='12' height='12' rx='2' fill='%231e3a5f'/%3E%3C/svg%3E")

ENTREPRISE = {
  "@type": "ProfessionalService", "@id": SITE + "/#entreprise", "name": "DUERP Conseil", "url": SITE + "/",
  "email": "contact@duerp-conseil.fr", "priceRange": "249 € - 399 €",
  "description": "Rédaction sur mesure du Document unique d'évaluation des risques professionnels (DUERP) pour les TPE de 1 à 20 salariés, à distance.",
  "address": {"@type": "PostalAddress", "streetAddress": "7 rue du Père Arson", "postalCode": "76700", "addressLocality": "Rogerville", "addressRegion": "Normandie", "addressCountry": "FR"},
  "areaServed": {"@type": "Country", "name": "France"},
  "founder": {"@type": "Person", "name": "Maxime De Witte"},
}


def jsonld(*objs):
    data = {"@context": "https://schema.org", "@graph": list(objs)}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def fil(*etapes):
    """Fil d'Ariane : etapes = [(nom, url), ...]."""
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(etapes)]
    html = " › ".join(f'<a href="{u}">{n}</a>' if i < len(etapes) - 1 else f'<span aria-current="page">{n}</span>'
                      for i, (n, u) in enumerate(etapes))
    return {"@type": "BreadcrumbList", "itemListElement": items}, f'<p class="crumbs" role="navigation" aria-label="Fil d\'Ariane">{html}</p>'


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def faq_html(faq):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)


def page(url, titre, desc, corps, ld):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="DUERP Conseil">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{url}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Public+Sans:ital,wght@0,400;0,700;1,400&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{ld}
</head>
<body>
<header>
  <div class="wrap">
    <a class="logo" href="/">{LOGO} DUERP Conseil</a>
    <nav>
      <a href="/metiers/">Métiers</a>
      <a href="/guides/">Guides</a>
      <a href="/#tarifs">Tarifs</a>
      <a class="btn btn-main" href="/#contact">Demander un devis</a>
    </nav>
  </div>
</header>
<main>
{corps}
{cta()}
</main>
{footer()}
</body>
</html>
"""


def cta():
    return f"""<section class="contact">
  <div class="wrap two">
    <div class="stack">
      <p class="eyebrow">Devis gratuit</p>
      <h2>Parlons de votre entreprise.</h2>
      <p class="lead">Dites-moi votre métier et votre nombre de salariés : je vous réponds sous 24 h avec un devis adapté, sans engagement.</p>
      <div class="ctas"><a class="btn btn-main" href="{DEVIS}" target="_blank" rel="noopener">Demander un devis</a><a class="btn btn-ghost" href="/#exemple">Voir un exemple de DUERP</a></div>
    </div>
    <div class="stack">
      <p class="small">Vous préférez écrire directement ?</p>
      <a class="mail" href="mailto:contact@duerp-conseil.fr?subject=Demande%20de%20devis%20DUERP">contact@duerp-conseil.fr</a>
    </div>
  </div>
</section>"""


def footer():
    bat = " · ".join(f'<a href="/{m["slug"]}/">{m["court"]}</a>' for m in METIERS if m["groupe"] == "batiment")
    aut = " · ".join(f'<a href="/{m["slug"]}/">{m["court"]}</a>' for m in METIERS if m["groupe"] != "batiment")
    gui = " · ".join(f'<a href="/guides/{g["slug"]}/">{g["court"]}</a>' for g in GUIDES)
    return f"""<footer>
  <div class="wrap">
    <strong>DUERP Conseil</strong>
    <span class="flinks">DUERP bâtiment : {bat}</span>
    <span class="flinks">Autres métiers : {aut} · <a href="/metiers/">Tous les métiers</a></span>
    <span class="flinks">Guides : {gui}</span>
    <span>Maxime De Witte EI · SIRET 132 028 333 00012 · RCS Le Havre · 7 rue du Père Arson, 76700 Rogerville · contact@duerp-conseil.fr</span>
    <span>Directeur de la publication : Maxime De Witte. Hébergeur : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</span>
  </div>
</footer>"""


TARIFS = """<section id="tarifs">
  <div class="wrap">
    <p class="eyebrow">Tarifs</p>
    <h2>Une étude personnalisée, tout compris.</h2>
    <div class="prices">
      <div class="price"><span class="amount">249 €</span><span class="who">1 à 5 salariés</span><span class="what">Création du DUERP</span></div>
      <div class="price"><span class="amount">299 €</span><span class="who">6 à 10 salariés</span><span class="what">Création du DUERP</span></div>
      <div class="price"><span class="amount">399 €</span><span class="who">11 à 20 salariés</span><span class="what">Création du DUERP</span></div>
      <div class="price update"><span class="amount">99 €</span><span class="who">Mise à jour</span><span class="what">Après un changement : nouveau poste, travaux, accident</span></div>
    </div>
    <div class="offer"><strong>Offre de lancement : -50 % pour les 3 premiers clients</strong>, en échange d'un témoignage écrit sur votre expérience.</div>
    <p class="small" style="margin-top:14px">Prix nets. TVA non applicable, art. 293 B du CGI. Corrections jusqu'à votre validation, sans frais.</p>
  </div>
</section>"""

METHODE = """<section>
  <div class="wrap">
    <p class="eyebrow">Comment ça marche</p>
    <h2>Trois étapes, sans déplacement.</h2>
    <div class="steps">
      <div class="step"><h3>Un questionnaire adapté à votre métier</h3><p>Environ 20 minutes, quand vous voulez, depuis votre téléphone ou votre ordinateur.</p></div>
      <div class="step"><h3>Un entretien avec vous</h3><p>20 à 30 minutes par téléphone ou en visio, le soir si vous préférez, pour comprendre votre organisation et vos situations à risque.</p></div>
      <div class="step"><h3>Votre DUERP sur mesure</h3><p>En PDF prêt à signer sous 7 jours, avec un tableau modifiable pour les mises à jour.</p></div>
    </div>
  </div>
</section>"""


def bio(m):
    bat = m["groupe"] == "batiment"
    p2 = ("J'ai aussi une solide expérience du bâtiment : je connais les chantiers, les outils et les gestes du métier de l'intérieur. "
          "Je parle le même langage que vous et vos compagnons.") if bat else (
          "J'ai aussi une solide expérience du bâtiment. J'applique la même méthode à chaque métier : comprendre comment vous travaillez vraiment avant d'écrire une ligne.")
    return f"""<section>
  <div class="wrap bio">
    <div class="mono" aria-hidden="true">M</div>
    <div class="stack">
      <p class="eyebrow">Qui rédige votre DUERP</p>
      <h2>Maxime De Witte</h2>
      <p>Je travaille dans l'industrie chimique, un secteur où la sécurité est encadrée au quotidien : analyse des risques avant chaque intervention, consignes, équipements de protection, retour d'expérience après chaque incident.</p>
      <p>{p2}</p>
      <div class="creds"><span>Industrie chimique</span><span>Bâtiment</span><span>Basé en Normandie</span><span>Partout en France, à distance</span></div>
    </div>
  </div>
</section>"""


def autres_liens(courant):
    liens = "".join(f'<li><a href="/{m["slug"]}/">DUERP {m["metier"]}</a></li>' for m in METIERS if m["slug"] != courant)
    guides = "".join(f'<li><a href="/guides/{g["slug"]}/">{g["court"]}</a></li>' for g in GUIDES)
    return f"""<section style="padding-top:0">
  <div class="wrap two">
    <div class="stack"><h3>Les autres métiers</h3><ul class="links">{liens}<li><a href="/metiers/">Tous les métiers</a></li></ul></div>
    <div class="stack"><h3>Pour aller plus loin</h3><ul class="links">{guides}</ul></div>
  </div>
</section>"""


def page_metier(m):
    url = f"/{m['slug']}/"
    grp = ("DUERP bâtiment", "/metiers/#batiment") if m["groupe"] == "batiment" else ("DUERP par métier", "/metiers/")
    bc_ld, bc = fil(("Accueil", "/"), grp, (m["court"], url))
    risques = "".join(f'<div class="rcard"><h3>{t}</h3><p>{q}</p><p class="mes"><strong>Exemples de mesures :</strong> {mes}</p></div>' for t, q, mes in m["risques"])
    regles = "".join(f"<li><strong>{t}.</strong> {x}</li>" for t, x in m["regles"])
    questions = "".join(f"<li>{q}</li>" for q in m["questions"])
    corps = f"""<section class="hero hero-page">
  <div class="wrap">
    <div class="stack">
      {bc}
      <p class="eyebrow">Document unique · {m["court"]}</p>
      <h1>{m["h1"]}</h1>
      <p class="lead">{m["intro"]}</p>
      <div class="ctas"><a class="btn btn-main" href="{DEVIS}" target="_blank" rel="noopener">Demander un devis gratuit</a><a class="btn btn-ghost" href="#risques">Les risques du métier</a></div>
      <div class="reassure"><span>Rédigé avec vous</span><span>100 % à distance</span><span>Dès 249 €</span><span>Corrections jusqu'à validation</span></div>
    </div>
  </div>
</section>
<section class="band">
  <div class="wrap stack">
    <p class="eyebrow" style="color:var(--signal)">Une situation que je regarde de près</p>
    <p class="quote">{m["situation"]}</p>
  </div>
</section>
<section id="risques">
  <div class="wrap">
    <p class="eyebrow">Les risques du métier</p>
    <h2>Ce que doit couvrir le DUERP {m.get("de", "d'un " + m["metier"])}.</h2>
    <p class="lead" style="margin-top:12px">Voici les risques qu'on retrouve presque toujours. Votre DUERP les évalue selon votre réalité, et en ajoute d'autres si votre activité le demande.</p>
    <div class="rgrid">{risques}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap two">
    <div class="stack">
      <p class="eyebrow">Réglementation</p>
      <h2>Les points souvent oubliés.</h2>
      <ul class="check">{regles}</ul>
    </div>
    <div class="stack">
      <p class="eyebrow">Sur mesure</p>
      <h2>Les questions que je vous poserai.</h2>
      <p>Un modèle générique ne pose pas ces questions. Ce sont pourtant elles qui font un DUERP utile et défendable en cas de contrôle.</p>
      <ul class="qlist">{questions}</ul>
    </div>
  </div>
</section>
{METHODE}
{bio(m)}
{TARIFS}
<section id="faq" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow">Questions fréquentes</p>
    <h2>DUERP {m["metier"]} : vos questions.</h2>
    <div style="margin-top:20px">{faq_html(m["faq"] + FAQ_COMMUNE)}</div>
  </div>
</section>
{autres_liens(m["slug"])}"""
    service = {"@type": "Service", "name": f"DUERP {m['metier']}", "serviceType": "Rédaction du Document unique d'évaluation des risques professionnels",
               "provider": {"@id": SITE + "/#entreprise"}, "areaServed": {"@type": "Country", "name": "France"}, "url": SITE + url,
               "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "249", "highPrice": "399"}}
    ld = jsonld(ENTREPRISE, service, bc_ld, faq_ld(m["faq"] + FAQ_COMMUNE))
    return url, page(url, m["titre"], m["desc"], corps, ld)


FAQ_COMMUNE = [
    ("Combien coûte un DUERP sur mesure ?", "249 € de 1 à 5 salariés, 299 € de 6 à 10, 399 € de 11 à 20. La mise à jour après un changement coûte 99 €. Prix nets, sans TVA."),
    ("Un DUERP fait à distance est-il valable ?", "Oui. La loi n'impose aucune visite. Ce qui compte, c'est que l'évaluation corresponde à votre entreprise : le questionnaire, l'entretien et vos photos servent à cela."),
]


def page_guide(g):
    url = f"/guides/{g['slug']}/"
    bc_ld, bc = fil(("Accueil", "/"), ("Guides", "/guides/"), (g["court"], url))
    corps = f"""<section class="hero hero-page">
  <div class="wrap">
    <div class="stack">
      {bc}
      <p class="eyebrow">Guide · mis à jour le {datetime.date.today().strftime('%d/%m/%Y')}</p>
      <h1>{g["h1"]}</h1>
      <p class="lead">{g["intro"]}</p>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap article">
    {g["corps"]}
    <p class="small">Cet article est une information générale, pas un conseil juridique. Textes vérifiés sur Légifrance et auprès de sources spécialisées à la date de mise à jour.</p>
  </div>
</section>
<section id="faq" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow">Questions fréquentes</p>
    <h2>En bref.</h2>
    <div style="margin-top:20px">{faq_html(g["faq"])}</div>
  </div>
</section>
{autres_liens(None)}"""
    art = {"@type": "Article", "headline": g["h1"], "description": g["desc"], "inLanguage": "fr-FR", "dateModified": AUJ,
           "author": {"@type": "Person", "name": "Maxime De Witte"}, "publisher": {"@id": SITE + "/#entreprise"},
           "mainEntityOfPage": SITE + url}
    return url, page(url, g["titre"], g["desc"], corps, jsonld(ENTREPRISE, art, bc_ld, faq_ld(g["faq"])))


def carte(m):
    return f'<a class="mcard" href="/{m["slug"]}/"><h3>{m["court"]}</h3><p>{m["risques"][0][0]}, {m["risques"][1][0].lower()}, {m["risques"][2][0].lower()}…</p></a>'


def page_hub_metiers():
    url = "/metiers/"
    bc_ld, bc = fil(("Accueil", "/"), ("DUERP par métier", url))
    bat = "".join(carte(m) for m in METIERS if m["groupe"] == "batiment")
    aut = "".join(carte(m) for m in METIERS if m["groupe"] != "batiment")
    corps = f"""<section class="hero hero-page">
  <div class="wrap"><div class="stack">
    {bc}
    <p class="eyebrow">DUERP par métier</p>
    <h1>Un DUERP adapté à votre métier, quel qu'il soit.</h1>
    <p class="lead">Chaque métier a ses risques. Je pars d'un questionnaire propre à votre activité, puis d'un entretien avec vous, pour rédiger un document unique qui décrit votre entreprise et pas une autre.</p>
  </div></div>
</section>
<section id="batiment" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow">Bâtiment et travaux publics</p>
    <h2>Les métiers du bâtiment.</h2>
    <p class="lead" style="margin-top:12px">C'est le secteur que je connais le mieux, et celui où les patrons ont le moins de temps pour la paperasse. Je m'adapte : entretien le soir, questions concrètes, vocabulaire de chantier.</p>
    <div class="mgrid">{bat}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow">Commerce et services</p>
    <h2>Les autres métiers.</h2>
    <div class="mgrid">{aut}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap two">
    <div class="stack">
      <p class="eyebrow">Votre métier n'est pas dans la liste ?</p>
      <h2>Boulangerie, restaurant, commerce, garage, bureau…</h2>
    </div>
    <div class="stack">
      <p>La méthode est la même pour toutes les TPE de 1 à 20 salariés : un questionnaire, un entretien, puis un DUERP rédigé à partir de vos réponses. Je prépare le questionnaire de votre métier avant notre échange.</p>
      <p>Écrivez-moi votre activité et votre nombre de salariés : je vous dis en 24 h comment je peux vous aider, et à quel prix.</p>
      <div class="ctas"><a class="btn btn-main" href="{DEVIS}" target="_blank" rel="noopener">Demander un devis</a></div>
    </div>
  </div>
</section>
{TARIFS}"""
    return url, page(url, "DUERP par métier : bâtiment, coiffure, auto-école, immobilier | DUERP Conseil",
                     "Document unique sur mesure pour votre métier : couvreur, maçon, électricien, plombier, peintre, coiffure, auto-école, agence immobilière et toutes les TPE de 1 à 20 salariés.",
                     corps, jsonld(ENTREPRISE, bc_ld))


def page_hub_guides():
    url = "/guides/"
    bc_ld, bc = fil(("Accueil", "/"), ("Guides", url))
    cartes = "".join(f'<a class="mcard" href="/guides/{g["slug"]}/"><h3>{g["court"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES)
    corps = f"""<section class="hero hero-page">
  <div class="wrap"><div class="stack">
    {bc}
    <p class="eyebrow">Guides</p>
    <h1>Le DUERP expliqué simplement.</h1>
    <p class="lead">Obligation, amendes, mise à jour : les réponses aux questions que se posent les chefs de petites entreprises, avec les références des textes.</p>
  </div></div>
</section>
<section style="padding-top:0"><div class="wrap"><div class="mgrid">{cartes}</div></div></section>"""
    return url, page(url, "Guides DUERP : obligation, amendes, mise à jour | DUERP Conseil",
                     "Tout comprendre au document unique : qui doit le faire, les amendes en 2026, quand le mettre à jour, la différence avec le PPSPS.",
                     corps, jsonld(ENTREPRISE, bc_ld))


def ecrire(url, html):
    chemin = os.path.join(RACINE, url.strip("/"), "index.html")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    pages = [page_hub_metiers(), page_hub_guides()] + [page_metier(m) for m in METIERS] + [page_guide(g) for g in GUIDES]
    for url, html in pages:
        ecrire(url, html)
    urls = ["/"] + [u for u, _ in pages]
    prio = lambda u: "1.0" if u == "/" else ("0.9" if u.startswith("/duerp-") else "0.7")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{SITE}{u}</loc><lastmod>{AUJ}</lastmod><priority>{prio(u)}</priority></url>" for u in urls]
    sm.append("</urlset>")
    open(os.path.join(RACINE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    open(os.path.join(RACINE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /generateur/\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"{len(pages)} pages générées, sitemap : {len(urls)} adresses")


if __name__ == "__main__":
    main()
