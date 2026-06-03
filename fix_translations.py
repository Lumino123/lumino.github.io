import re

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. applyLang: add data-i18n-html support after existing data-i18n line ──
html = html.replace(
    "document.querySelectorAll('[data-i18n]').forEach(el=>{ const k=el.dataset.i18n; if(dict[k]) el.textContent = dict[k]; });",
    "document.querySelectorAll('[data-i18n]').forEach(el=>{ const k=el.dataset.i18n; if(dict[k]) el.textContent = dict[k]; });\n  document.querySelectorAll('[data-i18n-html]').forEach(el=>{ const k=el.dataset.i18nHtml; if(dict[k]) el.innerHTML = dict[k]; });"
)

# ── 2. Add data-i18n keys to I18N.lv ────────────────────────────────────────
LV_NEW = (
    "'common.learn.more':'Uzzināt vairāk →',"
    "'solar.subsidy.title':'Valsts atbalsts saules paneļiem — līdz <span style=\"color:var(--accent);font-size:20px\">4 000 €</span>',"
    "'solar.subsidy.sub':'EKII programma sedz līdz 70% no paneļu un invertora izmaksām. Pieejams līdz 2029. gada 31. decembrim.',"
    "'solar.how':'Kā tas strādā','solar.how.sub':'Saules gaisma → fotoelementi → līdzstrāva → invertors → maiņstrāva mājai un tīklam.',"
    "'heat.subsidy.title':'Valsts atbalsts siltumsūkņa iegādei',"
    "'heat.subsidy.sub':'<b>Gaiss–gaiss:</b> 1 200–2 400 € &nbsp;·&nbsp; <b>Gaiss–ūdens:</b> 3 700–4 700 € &nbsp;·&nbsp; <b>Zemes:</b> 5 700–13 000 €<br>EKII programma — līdz 70% no izmaksām. Pieejams līdz 2029. gada 31. decembrim.',"
    "'heat.how':'Kā siltumsūknis strādā','heat.how.sub':'Āra vienība iegūst siltumu no āra gaisa pat -25°C, un nodod to mājai caur kompresoru.',"
    "'inv.subsidy.title':'Valsts atbalsts invertora iegādei — līdz <span style=\"color:var(--accent);font-size:20px\">4 000 €</span>',"
    "'inv.subsidy.sub':'EKII programma sedz invertoru iegādi kopā ar saules paneļiem — līdz 70% no kopējām izmaksām.<br>Atbalsts pieejams līdz 2029. gada 31. decembrim. Lumino palīdz ar visu dokumentāciju.',"
    "'inv.how':'Kā invertors strādā','inv.how.sub':'Pārvērš nestabilo līdzstrāvu (DC) no paneļiem mājas tīklam piemērotā 230V maiņstrāvā (AC).',"
    "'bat.subsidy.title':'Valsts atbalsts akumulatora iegādei — līdz <span style=\"color:var(--accent);font-size:20px\">2 500 €</span>',"
    "'bat.subsidy.sub':'EKII programma sedz līdz 70% no izmaksām. Pieejams līdz 2029. gada 31. decembrim. Lumino palīdz ar dokumentiem.',"
    "'bat.how':'Kā akumulators strādā','bat.how.sub':'Dienā saules paneļi uzlādē akumulatoru. Vakarā vai miglainā laikā akumulators padod enerģiju mājai, samazinot tīkla lietošanu.',"
)
html = html.replace(
    "    'bat.spec.cap':'Kapacitāte','bat.spec.eff':'Efektivit.',",
    LV_NEW + "\n    'bat.spec.cap':'Kapacitāte','bat.spec.eff':'Efektivit.',"
)

# ── 3. Add data-i18n keys to I18N.en ────────────────────────────────────────
EN_NEW = (
    "'common.learn.more':'Learn more →',"
    "'solar.subsidy.title':'State support for solar panels — up to <span style=\"color:var(--accent);font-size:20px\">4 000 €</span>',"
    "'solar.subsidy.sub':'The EKII programme covers up to 70% of panel and inverter costs. Available until 31 December 2029.',"
    "'solar.how':'How it works','solar.how.sub':'Sunlight → photovoltaic cells → DC current → inverter → AC power for home and grid.',"
    "'heat.subsidy.title':'State support for heat pump purchase',"
    "'heat.subsidy.sub':'<b>Air-to-air:</b> 1 200–2 400 € &nbsp;·&nbsp; <b>Air-to-water:</b> 3 700–4 700 € &nbsp;·&nbsp; <b>Ground:</b> 5 700–13 000 €<br>EKII programme — up to 70% of costs. Available until 31 December 2029.',"
    "'heat.how':'How a heat pump works','heat.how.sub':'The outdoor unit extracts heat from the air down to -25°C and transfers it to the home via a compressor.',"
    "'inv.subsidy.title':'State support for inverter purchase — up to <span style=\"color:var(--accent);font-size:20px\">4 000 €</span>',"
    "'inv.subsidy.sub':'The EKII programme covers inverter purchase together with solar panels — up to 70% of total costs.<br>Support available until 31 December 2029. Lumino assists with all documentation.',"
    "'inv.how':'How an inverter works','inv.how.sub':'Converts the unstable DC from panels into 230V AC suitable for home use and the grid.',"
    "'bat.subsidy.title':'State support for battery purchase — up to <span style=\"color:var(--accent);font-size:20px\">2 500 €</span>',"
    "'bat.subsidy.sub':'The EKII programme covers up to 70% of costs. Available until 31 December 2029. Lumino helps with documentation.',"
    "'bat.how':'How a battery works','bat.how.sub':'During the day solar panels charge the battery. In the evening or on cloudy days the battery powers the home, reducing grid usage.',"
)
html = html.replace(
    "    'bat.spec.cap':'Capacity','bat.spec.eff':'Efficiency',",
    EN_NEW + "\n    'bat.spec.cap':'Capacity','bat.spec.eff':'Efficiency',"
)

# ── 4. Add data-i18n keys to I18N.ru ────────────────────────────────────────
RU_NEW = (
    "'common.learn.more':'Узнать больше →',"
    "'solar.subsidy.title':'Господдержка на солнечные панели — до <span style=\"color:var(--accent);font-size:20px\">4 000 €</span>',"
    "'solar.subsidy.sub':'Программа EKII покрывает до 70% стоимости панелей и инвертора. Доступно до 31 декабря 2029.',"
    "'solar.how':'Как это работает','solar.how.sub':'Солнечный свет → фотоэлементы → постоянный ток → инвертор → переменный ток для дома и сети.',"
    "'heat.subsidy.title':'Господдержка на покупку теплового насоса',"
    "'heat.subsidy.sub':'<b>Воздух–воздух:</b> 1 200–2 400 € &nbsp;·&nbsp; <b>Воздух–вода:</b> 3 700–4 700 € &nbsp;·&nbsp; <b>Земля:</b> 5 700–13 000 €<br>Программа EKII — до 70% от затрат. Доступно до 31 декабря 2029.',"
    "'heat.how':'Как работает тепловой насос','heat.how.sub':'Наружный блок извлекает тепло из воздуха при -25°C и передаёт его в дом через компрессор.',"
    "'inv.subsidy.title':'Господдержка на покупку инвертора — до <span style=\"color:var(--accent);font-size:20px\">4 000 €</span>',"
    "'inv.subsidy.sub':'Программа EKII покрывает покупку инвертора вместе с солнечными панелями — до 70% от общих затрат.<br>Поддержка доступна до 31 декабря 2029. Lumino помогает со всей документацией.',"
    "'inv.how':'Как работает инвертор','inv.how.sub':'Преобразует нестабильный постоянный ток от панелей в 230V переменный ток для дома и сети.',"
    "'bat.subsidy.title':'Господдержка на покупку аккумулятора — до <span style=\"color:var(--accent);font-size:20px\">2 500 €</span>',"
    "'bat.subsidy.sub':'Программа EKII покрывает до 70% стоимости. Доступно до 31 декабря 2029. Lumino помогает с документами.',"
    "'bat.how':'Как работает аккумулятор','bat.how.sub':'Днём солнечные панели заряжают аккумулятор. Вечером или в пасмурную погоду аккумулятор снабжает дом энергией, снижая потребление из сети.',"
)
html = html.replace(
    "    'bat.spec.cap':'Ёмкость','bat.spec.eff':'КПД',",
    RU_NEW + "\n    'bat.spec.cap':'Ёмкость','bat.spec.eff':'КПД',"
)

# ── 5. Solar banner: add data-i18n-html to title, data-i18n to sub and CTA ──
html = html.replace(
    '<div style="font-weight:700;font-size:17px;margin-bottom:4px">Valsts atbalsts saules paneļiem',
    '<div data-i18n-html="solar.subsidy.title" style="font-weight:700;font-size:17px;margin-bottom:4px">Valsts atbalsts saules paneļiem'
)
html = html.replace(
    '<div style="color:var(--muted);font-size:14px">EKII programma sedz līdz 70% no paneļu un invertora izmaksām.',
    '<div data-i18n="solar.subsidy.sub" style="color:var(--muted);font-size:14px">EKII programma sedz līdz 70% no paneļu un invertora izmaksām.'
)

# ── 6. Heat pump banner: add data-i18n to title, data-i18n-html to sub ──────
html = html.replace(
    '<div style="font-weight:700;font-size:17px;color:#111;margin-bottom:6px">Valsts atbalsts siltumsūkņa iegādei</div>',
    '<div data-i18n="heat.subsidy.title" style="font-weight:700;font-size:17px;color:#111;margin-bottom:6px">Valsts atbalsts siltumsūkņa iegādei</div>'
)
html = html.replace(
    '<div style="color:#333;font-size:14px;line-height:1.6">\n          <b>Gaiss–gaiss:</b>',
    '<div data-i18n-html="heat.subsidy.sub" style="color:#333;font-size:14px;line-height:1.6">\n          <b>Gaiss–gaiss:</b>'
)

# ── 7. Inverter banner: add data-i18n-html to title and sub ─────────────────
html = html.replace(
    '<div style="font-weight:700;font-size:17px;color:#111;margin-bottom:6px">Valsts atbalsts invertora iegādei',
    '<div data-i18n-html="inv.subsidy.title" style="font-weight:700;font-size:17px;color:#111;margin-bottom:6px">Valsts atbalsts invertora iegādei'
)
html = html.replace(
    '<div style="color:#333;font-size:14px;line-height:1.6">\n          EKII programma sedz invertoru',
    '<div data-i18n-html="inv.subsidy.sub" style="color:#333;font-size:14px;line-height:1.6">\n          EKII programma sedz invertoru'
)

# ── 8. Battery banner: add data-i18n-html to title, data-i18n to sub ────────
html = html.replace(
    '<div style="font-weight:700;font-size:17px;margin-bottom:4px">Valsts atbalsts akumulatora iegādei',
    '<div data-i18n-html="bat.subsidy.title" style="font-weight:700;font-size:17px;margin-bottom:4px">Valsts atbalsts akumulatora iegādei'
)
html = html.replace(
    '<div style="color:var(--muted);font-size:14px">EKII programma sedz līdz 70% no izmaksām. Pieejams',
    '<div data-i18n="bat.subsidy.sub" style="color:var(--muted);font-size:14px">EKII programma sedz līdz 70% no izmaksām. Pieejams'
)

# ── 9. All 4 "Uzzināt vairāk →" CTAs in banners ──────────────────────────────
# These appear as: <a data-go="contact" class="nav-cta" style="flex-shrink:0">Uzzināt vairāk →</a>
html = html.replace(
    '<a data-go="contact" class="nav-cta" style="flex-shrink:0">Uzzināt vairāk →</a>',
    '<a data-go="contact" data-i18n="common.learn.more" class="nav-cta" style="flex-shrink:0">Uzzināt vairāk →</a>'
)

# ── 10. Battery "how it works" h2 and p ──────────────────────────────────────
html = html.replace(
    '<h2>Kā akumulators <span class="serif">strādā</span></h2>',
    '<h2 data-i18n="bat.how">Kā akumulators strādā</h2>'
)
html = html.replace(
    '<p class="how-sub">Dienā saules paneļi uzlādē akumulatoru.',
    '<p class="how-sub" data-i18n="bat.how.sub">Dienā saules paneļi uzlādē akumulatoru.'
)

# ── Verify changes ────────────────────────────────────────────────────────────
checks = [
    ('data-i18n-html="solar.subsidy.title"', 'Solar banner title'),
    ('data-i18n="solar.subsidy.sub"', 'Solar banner sub'),
    ('data-i18n="heat.subsidy.title"', 'Heat banner title'),
    ('data-i18n-html="heat.subsidy.sub"', 'Heat banner sub'),
    ('data-i18n-html="inv.subsidy.title"', 'Inv banner title'),
    ('data-i18n-html="inv.subsidy.sub"', 'Inv banner sub'),
    ('data-i18n-html="bat.subsidy.title"', 'Bat banner title'),
    ('data-i18n="bat.subsidy.sub"', 'Bat banner sub'),
    ('data-i18n="common.learn.more"', 'Learn more CTAs'),
    ('data-i18n="bat.how"', 'Bat how h2'),
    ('data-i18n="bat.how.sub"', 'Bat how sub'),
    ('data-i18nHtml', 'JS handler'),
]
for marker, label in checks:
    count = html.count(marker)
    status = 'OK' if count > 0 else 'MISSING'
    print(f'{status} {label} ({count}x)')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone. {sum(1 for a,b in zip(original,html) if a!=b)} chars changed.')
