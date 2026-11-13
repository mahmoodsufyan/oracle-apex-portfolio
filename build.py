"""Generate the static English and Arabic portfolio pages."""

from html import escape
from pathlib import Path

from content import CASES, ROLES

ROOT = Path(__file__).resolve().parent
BASE = "https://mahmoodsufyan.github.io/oracle-apex-portfolio/"
GITHUB = "https://github.com/mahmoodsufyan"
LINKEDIN = "https://www.linkedin.com/in/mahmood-sufyan/"
EMAIL = "mahmood.sufyan.dev@gmail.com"
NAV = {
    "home": ("Home", "الرئيسية"),
    "work": ("Projects", "المشاريع"),
    "experience": ("Experience", "الخبرة"),
    "contact": ("Contact", "التواصل"),
}


def path(page, locale):
    if page == "home":
        return "./ar.html" if locale else "./"
    return f"./{page}{'-ar' if locale else ''}.html"


def link(href, label, cls=""):
    return f'<a class="{cls}" href="{escape(href, quote=True)}">{escape(label)}</a>'


def intro(label, title, summary):
    return f'<header class="page-intro"><p class="eyebrow">{label}</p><h1>{title}</h1><p class="lede">{summary}</p></header>'


def project_rows(locale):
    rows = []
    for slug, case in CASES.items():
        category, title, summary, _ = case["copy"][locale]
        rows.append(f'''
        <li><a href="{path(slug, locale)}">
          <span class="project-type">{category}</span>
          <span class="project-name"><strong>{title}</strong><span>{summary}</span></span>
          <span class="arrow" aria-hidden="true"></span>
        </a></li>''')
    return f'<ul class="project-index">{"".join(rows)}</ul>'


def home(locale):
    name = ("Mahmood Sufyan", "محمود سفيان")[locale]
    description = (
        "I build business applications with Oracle APEX and PL/SQL, from data modeling and business rules to reporting and API integration.",
        "أطوّر تطبيقات الأعمال باستخدام Oracle APEX وPL/SQL، من تصميم البيانات وقواعد العمل إلى التقارير وتكامل الأنظمة.",
    )[locale]
    title = (
        'Senior Oracle APEX<br><em>&amp; PL/SQL Developer</em>',
        'مطوّر أول<br><em dir="ltr">Oracle APEX &amp; PL/SQL</em>',
    )[locale]
    return name, description, f'''
      <section class="home-hero">
        <div class="hero-copy">
          <p class="eyebrow">{name} <span> / </span> {("Sanaa, Yemen", "صنعاء، اليمن")[locale]}</p>
          <h1>{title}</h1>
          <p class="lede">{description}</p>
          <div class="actions">
            {link(path("work", locale), ("Explore projects", "تصفّح المشاريع")[locale], "button primary")}
            {link(path("experience", locale), ("View experience", "الخبرة المهنية")[locale], "button")}
          </div>
        </div>
        <a class="showcase" href="{path("golden-cloud", locale)}">
          <div class="showcase-top"><span class="signal"></span><span>{("Featured case study", "دراسة الحالة الرئيسية")[locale]}</span></div>
          <img src="./assets/golden-cloud.webp" width="1920" height="1080" fetchpriority="high" alt="{("Golden Cloud accounting module", "واجهة قسم الحسابات في Golden Cloud")[locale]}">
          <div class="showcase-bottom"><span><strong>Golden Cloud</strong><small>{("Bilingual recruitment operations platform", "منصة ثنائية اللغة لإدارة عمليات الاستقدام")[locale]}</small></span><span class="arrow" aria-hidden="true"></span></div>
        </a>
      </section>
      <div class="stack" aria-label="{("Core technologies", "التقنيات الأساسية")[locale]}">
        <span>Oracle APEX</span><span>PL/SQL</span><span>Oracle Database</span><span>ORDS / REST</span><span>APEX Office Print</span>
      </div>
      <section class="section">
        <h2>{("Selected work", "مشاريع مختارة")[locale]}</h2>
        {project_rows(locale)}
      </section>'''


def work(locale):
    title = NAV["work"][locale]
    description = (
        "A recruitment platform case study, two public demos of financial workflows, and an Oracle APEX code example.",
        "دراسة حالة لمنصة استقدام، ونموذجان برمجيان لسير العمل المالي، ومثال عملي في Oracle APEX.",
    )[locale]
    example = ("Interactive Grid column visibility", "التحكم في ظهور أعمدة Interactive Grid")[locale]
    return title, description, f'''
      {intro(("Portfolio", "معرض الأعمال")[locale], title, description)}
      {project_rows(locale)}
      <section class="section">
        <h2>{("Code example", "مثال برمجي")[locale]}</h2>
        <article class="panel">
          <h3>{example}</h3>
          <p>{("JavaScript example for controlling which columns appear in an Oracle APEX Interactive Grid.", "مثال JavaScript للتحكم في الأعمدة المعروضة في Interactive Grid داخل Oracle APEX.")[locale]}</p>
          {link(GITHUB + "/apex_IG_hide_columns", ("View on GitHub", "عرض على GitHub")[locale], "text-link")}
        </article>
      </section>'''


def case_page(slug, locale):
    case = CASES[slug]
    category, title, summary, details = case["copy"][locale]
    sections = "".join(
        f'<article class="panel"><h3>{heading}</h3><p>{body}</p></article>'
        for heading, body in details
    )
    tags = "".join(f'<span dir="ltr">{escape(tag)}</span>' for tag in case["tags"])
    if slug == "golden-cloud":
        period = ("Primary developer on the project team · Aug 2022 – Aug 2026", "المطوّر الرئيسي ضمن فريق المشروع · أغسطس 2022 – أغسطس 2026")[locale]
        figure = f'''
        <figure class="case-media">
          <video controls playsinline preload="none" width="1920" height="1080" poster="./assets/golden-cloud.webp" aria-label="{("Golden Cloud platform walkthrough", "جولة في منصة Golden Cloud")[locale]}">
            <source src="./assets/golden-cloud.mp4" type="video/mp4">
          </video>
          <figcaption>{("60-second walkthrough in Arabic covering customers, workers, accounting, offices, HR, and request tracking.", "جولة عربية مدتها دقيقة في أقسام العملاء والعمالة والحسابات والمكاتب والموارد البشرية ومتابعة الطلبات.")[locale]}</figcaption>
        </figure>'''
        actions = (
            link("https://www.linkedin.com/feed/update/urn:li:activity:7526848608382492672/", ("Demo on LinkedIn", "العرض على LinkedIn")[locale], "button")
            + link("https://www.youtube.com/@GoldenCloud_1", ("Project YouTube channel", "قناة المشروع على YouTube")[locale], "button")
        )
    else:
        period = ("Public Python / FastAPI demo", "نموذج برمجي عام بـPython وFastAPI")[locale]
        figure = ""
        repo = GITHUB + "/" + case["repo"]
        actions = (
            link(repo, ("Source code", "الكود المصدري")[locale], "button primary")
            + link(repo + "/blob/main/docs/CASE_STUDY.md", ("Oracle case study", "دراسة حالة Oracle")[locale], "button")
        )
    return title, summary, f'''
      <div class="back">{link(path("work", locale), ("All projects", "كل المشاريع")[locale], "text-link")}</div>
      {intro(category, title, summary)}
      <p class="case-role">{period}</p>
      <div class="tags">{tags}</div>
{figure}      <section class="section case-detail">
        <h2>{("Project details", "تفاصيل المشروع")[locale]}</h2>
        <div class="panels">{sections}</div>
      </section>
      <div class="actions case-actions">{actions}</div>'''


def experience(locale):
    title = NAV["experience"][locale]
    summary = (
        "Over eight years developing Oracle applications for recruitment, microfinance, accounting, and business operations.",
        "أكثر من ثماني سنوات في تطوير تطبيقات Oracle للاستقدام والتمويل الأصغر والمحاسبة وعمليات الأعمال.",
    )[locale]
    roles = []
    for company, position, dates, description in ROLES[locale]:
        roles.append(f'''
          <article class="position"><p class="dates">{dates}</p><div><h2>{position}</h2>
          <p class="company">{company}</p><p>{description}</p></div></article>''')
    education = ("BSc in Computer Science · Taiz University · Distinction", "بكالوريوس علوم الحاسوب · جامعة تعز · امتياز")[locale]
    languages = ("Arabic native · English intermediate, technical reading and writing", "العربية اللغة الأم · الإنجليزية مستوى متوسط في القراءة والكتابة التقنية")[locale]
    return title, summary, f'''
      {intro(("Career", "المسار المهني")[locale], title, summary)}
      <div class="timeline">{"".join(roles)}</div>
      <section class="section">
        <h2>{("Education and languages", "التعليم واللغات")[locale]}</h2>
        <div class="panel"><p>{education}</p><p>{languages}</p></div>
      </section>'''


def contact(locale):
    title = NAV["contact"][locale]
    summary = (
        "For Oracle APEX, PL/SQL, and database engineering roles or project inquiries, reach me by email or LinkedIn.",
        "للتواصل بشأن فرص العمل أو المشاريع في Oracle APEX وPL/SQL وهندسة قواعد البيانات، راسلني عبر البريد أو LinkedIn.",
    )[locale]
    return title, summary, f'''
      {intro(("Mahmood Sufyan · Sanaa, Yemen", "محمود سفيان · صنعاء، اليمن")[locale], title, summary)}
      <ul class="project-index contact-index">
        <li><a href="mailto:{EMAIL}"><span>{("Email", "البريد الإلكتروني")[locale]}</span><strong dir="ltr">{EMAIL}</strong><span class="arrow" aria-hidden="true"></span></a></li>
        <li><a href="{LINKEDIN}"><span>LinkedIn</span><strong dir="ltr">mahmood-sufyan</strong><span class="arrow" aria-hidden="true"></span></a></li>
        <li><a href="{GITHUB}"><span>GitHub</span><strong dir="ltr">mahmoodsufyan</strong><span class="arrow" aria-hidden="true"></span></a></li>
      </ul>'''


def render(page, locale, title, description, body):
    lang, direction = (("en", "ltr"), ("ar", "rtl"))[locale]
    section = "work" if page in CASES else page
    nav_links = []
    for key, labels in NAV.items():
        active = ' class="active"' if key == section else ""
        current = ' aria-current="page"' if key == page else ""
        nav_links.append(f'<a href="{path(key, locale)}"{active}{current}>{labels[locale]}</a>')
    nav = "".join(nav_links)
    name = ("Mahmood Sufyan", "محمود سفيان")[locale]
    alternate = ("العربية", "English")[locale]
    page_title = f"{title} | {name}" if page != "home" else (
        "Mahmood Sufyan | Senior Oracle APEX & PL/SQL Developer",
        "محمود سفيان | مطوّر أول Oracle APEX وPL/SQL",
    )[locale]
    return f'''<!doctype html>
<html lang="{lang}" dir="{direction}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#111820">
  <title>{escape(page_title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:title" content="{escape(page_title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{BASE}assets/golden-cloud.webp">
  <link rel="canonical" href="{BASE + path(page, locale)[2:]}">
  <link rel="alternate" hreflang="en" href="{BASE + path(page, 0)[2:]}">
  <link rel="alternate" hreflang="ar" href="{BASE + path(page, 1)[2:]}">
  <link rel="icon" href="./assets/icon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="./style.css">
</head>
<body>
  <a class="skip" href="#main">{("Skip to content", "انتقل إلى المحتوى")[locale]}</a>
  <header class="site-header">
    <div class="shell masthead">
      <a class="brand" href="{path("home", locale)}"><span class="mark" aria-hidden="true">MS</span>{name}</a>
      <nav aria-label="{("Main navigation", "التنقّل الرئيسي")[locale]}">{nav}</nav>
      <a class="locale" href="{path(page, 1-locale)}" lang="{("ar", "en")[locale]}" hreflang="{("ar", "en")[locale]}">{alternate}</a>
    </div>
  </header>
  <main id="main" class="shell page page-{page}" tabindex="-1">{body}
  </main>
  <footer class="site-footer"><div class="shell foot">
    <span>{name}</span>
    <div>{link(LINKEDIN, "LinkedIn")}{link(GITHUB, "GitHub")}{link("mailto:" + EMAIL, ("Email", "البريد")[locale])}</div>
  </div></footer>
</body>
</html>
'''


if __name__ == "__main__":
    for locale in (0, 1):
        pages = {key: function(locale) for key, function in (
            ("home", home), ("work", work), ("experience", experience), ("contact", contact),
        )}
        pages.update((key, case_page(key, locale)) for key in CASES)
        for page, (title, description, body) in pages.items():
            filename = "index.html" if page == "home" and not locale else path(page, locale)[2:]
            (ROOT / filename).write_text(render(page, locale, title, description, body), encoding="utf-8", newline="\n")
