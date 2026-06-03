with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Support band card 2: amount 4700→2400, label remove air-to-water ───────
html = html.replace(
    '<div class="sc-amount">1 200–<span class="serif">4 700 €</span></div>',
    '<div class="sc-amount">1 200–<span class="serif">2 400 €</span></div>'
)
html = html.replace(
    '<div class="sc-label" data-i18n="support.sc2.label">Gaiss-gaiss un gaiss-ūdens siltumsūknim</div>',
    '<div class="sc-label" data-i18n="support.sc2.label">Gaiss-gaiss siltumsūknis</div>'
)

# ── 2. Heat pump banner HTML: remove air-to-water line ────────────────────────
html = html.replace(
    '          <b>Gaiss–gaiss:</b> 1 200–2 400 € &nbsp;·&nbsp;\n          <b>Gaiss–ūdens:</b> 3 700–4 700 € &nbsp;·&nbsp;\n          <b>Zemes:</b> 5 700–13 000 €<br>',
    '          <b>Gaiss–gaiss:</b> 1 200–2 400 € &nbsp;·&nbsp; <b>Zemes:</b> 5 700–13 000 €<br>'
)

# ── 3. I18N.lv: update support.sc2.label and heat.subsidy.sub ─────────────────
html = html.replace(
    "'support.sc2.label':'Gaiss-gaiss un gaiss-ūdens siltumsūknim'",
    "'support.sc2.label':'Gaiss-gaiss siltumsūknis'"
)
html = html.replace(
    "'heat.subsidy.sub':'<b>Gaiss–gaiss:</b> 1 200–2 400 € &nbsp;\xb7&nbsp; <b>Gaiss–ūdens:</b> 3 700–4 700 € &nbsp;\xb7&nbsp; <b>Zemes:</b> 5 700–13 000 €<br>EKII programma — līdz 70% no izmāksām. Pieejams līdz 2029. gada 31. decembrim.'",
    "'heat.subsidy.sub':'<b>Gaiss–gaiss:</b> 1 200–2 400 € &nbsp;\xb7&nbsp; <b>Zemes:</b> 5 700–13 000 €<br>EKII programma — līdz 70% no izmāksām. Pieejams līdz 2029. gada 31. decembrim.'"
)

# ── 4. I18N.en: update support.sc2.label and heat.subsidy.sub ─────────────────
html = html.replace(
    "'support.sc2.label':'Air-to-air and air-to-water heat pump'",
    "'support.sc2.label':'Air-to-air heat pump'"
)
html = html.replace(
    "'heat.subsidy.sub':'<b>Air-to-air:</b> 1 200–2 400 € &nbsp;\xb7&nbsp; <b>Air-to-water:</b> 3 700–4 700 € &nbsp;\xb7&nbsp; <b>Ground:</b> 5 700–13 000 €<br>EKII programme — up to 70% of costs. Available until 31 December 2029.'",
    "'heat.subsidy.sub':'<b>Air-to-air:</b> 1 200–2 400 € &nbsp;\xb7&nbsp; <b>Ground:</b> 5 700–13 000 €<br>EKII programme — up to 70% of costs. Available until 31 December 2029.'"
)

# ── 5. I18N.ru: update support.sc2.label and heat.subsidy.sub ─────────────────
html = html.replace(
    "'Тепловой насос воздух-воздух и воздух-вода'",
    "'Тепловой насос воздух-воздух'"
)
html = html.replace(
    "'heat.subsidy.sub':'<b>Воздух–воздух:</b> 1 200–2 400 € &nbsp;\xb7&nbsp; <b>Воздух–вода:</b> 3 700–4 700 € &nbsp;\xb7&nbsp; <b>Земля:</b> 5 700–13 000 €<br>Программа EKII — до 70% от затрат. Доступно до 31 декабря 2029.'",
    "'heat.subsidy.sub':'<b>Воздух–воздух:</b> 1 200–2 400 € &nbsp;\xb7&nbsp; <b>Земля:</b> 5 700–13 000 €<br>Программа EKII — до 70% от затрат. Доступно до 31 декабря 2029.'"
)

# ── Verify ────────────────────────────────────────────────────────────────────
checks = [
    ('2 400', '2 400 in card'),
    ('4 700', '4 700 should be gone'),
    ('Gaiss-gaiss siltumsūknis', 'LV label updated'),
    ('Air-to-air heat pump', 'EN label updated'),
    ('Gaiss-ūdens', 'LV air-to-water removed'),
    ('Air-to-water', 'EN air-to-water removed'),
]
for needle, label in checks:
    n = html.count(needle)
    print(f'({n}x) {label}: {needle!r}')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone. {sum(1 for a,b in zip(original,html) if a!=b)} chars changed.')
