#!/usr/bin/env python3
# encoding: utf-8
"""Add 2 AIKO + 1 Jinko panels; rewrite heat pump section (90% with built-in boiler)"""

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── HELPERS (same as before) ──────────────────────────────────────────────────
def brand_div(name, first=False):
    pad = "8px 0 10px" if first else "24px 0 10px"
    return (f'        <div style="grid-column:1/-1;padding:{pad};border-bottom:1px solid var(--line)">'
            f'<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
            f'text-transform:uppercase">{name}</span></div>')

def card(img, brand, name, desc, s1, s2, s3, specs, badge=None,
         s1l='Jauda', s2l='Efektivit.', s3l='Garantija', kw_badge=None):
    b = ''
    if badge == 'popular':
        b = '<span class="rib" data-i18n="common.popular">Populārs</span>'
    elif badge == 'new':
        b = '<span class="rib new" data-i18n="common.new">Jauns</span>'
    kw = f'<span class="kw-badge">{kw_badge}</span>' if kw_badge else ''
    sr = ''.join(
        f'<div class="tt-row"><span class="tt-label">{k}</span>'
        f'<span class="tt-val">{v}</span></div>' for k, v in specs)
    return (
        f'        <div class="prod-card reveal">'
        f'<div class="prod-img">{b}{kw}<img src="assets/{img}" alt=""/></div>'
        f'<div class="prod-body"><div class="brand">{brand}</div>'
        f'<h4>{name}</h4><p>{desc}</p>'
        f'<div class="prod-specs">'
        f'<div class="sp"><b>{s1}</b><span>{s1l}</span></div>'
        f'<div class="sp"><b>{s2}</b><span>{s2l}</span></div>'
        f'<div class="sp"><b>{s3}</b><span>{s3l}</span></div>'
        f'</div></div>'
        f'<div class="prod-foot"><a data-go="contact" data-i18n="common.inquire">'
        f'Pieprasīt →</a></div>'
        f'<div class="prod-tooltip"><div class="tt-title">Tehniskie dati</div>'
        f'{sr}</div></div>'
    )

# ══════════════════════════════════════════════════════════════════════════════
# 1. SOLAR — add Jinko 430W Full Black (before AIKO divider)
# ══════════════════════════════════════════════════════════════════════════════
AIKO_DIV = ('        <div style="grid-column:1/-1;padding:24px 0 10px;border-bottom:1px solid var(--line)">'
            '<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
            'text-transform:uppercase">AIKO</span></div>')

jinko_new = card(
    'panel-black.webp', 'Jinko Solar', 'Tiger Neo 430W Full Black',
    'Kompakta formāta N-tipa TOPCon panelis pilnmelna dizainā. Ideāls privātmājas jumtam.',
    '430 W', '22,0%', '30g', [
        ('Tehnoloģija', 'N-tipa TOPCon (Full Black)'),
        ('Nominālā jauda', '430 Wp'),
        ('Efektivitāte', '22,0%'),
        ('Voc / Isc', '39,7 V / 13,6 A'),
        ('Izmēri', '1762 × 1134 × 30 mm'),
        ('Svars', '21,3 kg'),
        ('Temper. koef.', '−0,30 %/°C'),
        ('Ražīguma garantija', '30 gadi'),
    ]
) + '\n'

html = html.replace(AIKO_DIV, jinko_new + AIKO_DIV)
print('OK Jinko 430W added')

# ══════════════════════════════════════════════════════════════════════════════
# 2. SOLAR — add 2 AIKO panels after the 645W card
# ══════════════════════════════════════════════════════════════════════════════
SOLAR_GRID_CLOSE = '      </div>\n    </div>\n    <!-- Valsts atbalsts banner uz solar lapas -->'

aiko_extra = '\n'.join([
    card('panel-silver.png', 'AIKO', 'Neostar 2S 450W',
         'Bifaciāls N-tipa ABC panelis ar sudraba rāmi — visvairāk pārdotais AIKO modelis Latvijā.',
         '450 W', '23,6%', '30g', [
             ('Tehnoloģija', 'N-tipa ABC (bifaciāls)'),
             ('Nominālā jauda', '450 Wp'),
             ('Efektivitāte', '23,6%'),
             ('Voc / Isc', '44,5 V / 13,4 A'),
             ('Izmēri', '1722 × 1134 × 30 mm'),
             ('Svars', '21,2 kg'),
             ('Temper. koef.', '−0,29 %/°C'),
             ('Ražīguma garantija', '30 gadi (87% pēc 30g)'),
         ], badge='popular'),
    card('panel-black.webp', 'AIKO', 'Abel 440W Full Black',
         'Pilnmelns N-tipa ABC panelis ar izcilu estētiku. Augstākā efektivitāte Full Black kategorijai.',
         '440 W', '23,2%', '30g', [
             ('Tehnoloģija', 'N-tipa ABC (Full Black)'),
             ('Nominālā jauda', '440 Wp'),
             ('Efektivitāte', '23,2%'),
             ('Voc / Isc', '43,3 V / 12,9 A'),
             ('Izmēri', '1722 × 1134 × 30 mm'),
             ('Svars', '21,2 kg'),
             ('Temper. koef.', '−0,29 %/°C'),
             ('Ražīguma garantija', '30 gadi'),
         ]),
]) + '\n'

html = html.replace(SOLAR_GRID_CLOSE, aiko_extra + SOLAR_GRID_CLOSE)
print('OK AIKO Neostar 2S 450W + Abel 440W added')

# ══════════════════════════════════════════════════════════════════════════════
# 3. HEAT PUMPS — replace entire grid (90% with built-in boiler)
# ══════════════════════════════════════════════════════════════════════════════
HEAT_FIRST_DIV = ('        <div style="grid-column:1/-1;padding:8px 0 10px;border-bottom:1px solid var(--line)">'
                  '<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
                  'text-transform:uppercase">Daikin</span></div>')
HEAT_GRID_END = '      </div>\n    </div>\n    <!-- Valsts atbalsts banner uz heat lapas -->'

idx_hs = html.index(HEAT_FIRST_DIV)
idx_he = html.index(HEAT_GRID_END)
old_heat_grid = html[idx_hs:idx_he]

def hp(img, brand, name, desc, kw, klase, scop, specs, badge=None, kw_badge=None):
    return card(img, brand, name, desc, kw, klase, scop, specs, badge,
                s1l='Jauda', s2l='Klase', s3l='SCOP', kw_badge=kw_badge)

new_heat_parts = [
    # ── Daikin Altherma 3 H — ar iebūvētu boileru ─────────────────────────
    brand_div('Daikin Altherma 3 H — ar iebūvētu boileru', first=True),
    hp('hp-daikin-altherma.jpg', 'Daikin', 'Altherma 3 H 8kW',
       'Gaiss–ūdens siltumsūknis ar iebūvētu 230 L karstā ūdens tvertni. #1 populārākais modelis Latvijā.',
       '8 kW', 'A+++', '4,50', [
           ('Tips', 'Gaiss–ūdens (sadalīts, ar boileri)'),
           ('Siltumjauda', '8 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,50'),
           ('Iebūvēta tvertne', '230 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
           ('Trokšņa līmenis', '45 dB(A)'),
       ], badge='popular', kw_badge='8 kW'),
    hp('hp-daikin-altherma.jpg', 'Daikin', 'Altherma 3 H 11kW',
       '11 kW ar iebūvētu 260 L boileri. Pilna mājas apkure un karstais ūdens no vienas ierīces.',
       '11 kW', 'A+++', '4,25', [
           ('Tips', 'Gaiss–ūdens (sadalīts, ar boileri)'),
           ('Siltumjauda', '11 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,25'),
           ('Iebūvēta tvertne', '260 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
           ('Trokšņa līmenis', '48 dB(A)'),
       ], kw_badge='11 kW'),
    hp('hp-daikin-altherma.jpg', 'Daikin', 'Altherma 3 H 16kW',
       'Lielas mājas pilnais risinājums — apkure un karstais ūdens no vienas iekārtas.',
       '16 kW', 'A++', '3,90', [
           ('Tips', 'Gaiss–ūdens (sadalīts, ar boileri)'),
           ('Siltumjauda', '16 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '3,90'),
           ('Iebūvēta tvertne', '260 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
       ], kw_badge='16 kW'),

    # ── Samsung EHS ClimateHub — ar iebūvētu boileru ──────────────────────
    brand_div('Samsung EHS ClimateHub — ar iebūvētu boileru'),
    hp('hp-samsung.png', 'Samsung', 'EHS ClimateHub 8kW',
       'Split sistēma ar iebūvētu 200 L tvertni. Kluss (37 dB) un kompakts mājas risinājums.',
       '8 kW', 'A++', '3,80', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '8 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '3,80'),
           ('Iebūvēta tvertne', '200 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
           ('Trokšņa līmenis', '37 dB(A)'),
       ], badge='popular', kw_badge='8 kW'),
    hp('hp-samsung.png', 'Samsung', 'EHS ClimateHub 12kW',
       'Lielāka jauda ar 200 L integrētu boileri. Smart Home saderība un Wi-Fi vadība.',
       '12 kW', 'A++', '3,50', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '12 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '3,50'),
           ('Iebūvēta tvertne', '200 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
       ], kw_badge='12 kW'),
    hp('hp-samsung.png', 'Samsung', 'EHS ClimateHub 16kW',
       'Maksimālā jauda ar 260 L iebūvētu boileri. Lielas mājas un komercobjekti.',
       '16 kW', 'A+', '3,20', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '16 kW (A7/W35)'),
           ('Energoklase', 'A+'),
           ('SCOP (35°C)', '3,20'),
           ('Iebūvēta tvertne', '260 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
       ], kw_badge='16 kW'),

    # ── NIBE F2040 + VBU 200 — ar iebūvētu boileru ────────────────────────
    brand_div('NIBE F2040 — ar iebūvētu boileru'),
    hp('hp-daikin-1.jpg', 'NIBE', 'F2040-6 + VBU 200',
       'Zviedru klases split sistēma ar 180 L iebūvētu karstā ūdens tvertni. Plaši izplatīts Latvijā.',
       '6 kW', 'A++', '4,00', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '6 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '4,00'),
           ('Iebūvēta tvertne', '180 L KU (VBU 200)'),
           ('Min. darba temp.', '−20 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
           ('Trokšņa līmenis', '44 dB(A)'),
       ], kw_badge='6 kW'),
    hp('hp-daikin-1.jpg', 'NIBE', 'F2040-9 + VBU 200',
       '9 kW ar iebūvētu 180 L boileri. Ideāls vidēja lieluma privātmājai ar augstu komfortu.',
       '9 kW', 'A++', '3,80', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '9 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '3,80'),
           ('Iebūvēta tvertne', '180 L KU (VBU 200)'),
           ('Min. darba temp.', '−20 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
       ], badge='popular', kw_badge='9 kW'),
    hp('hp-daikin-1.jpg', 'NIBE', 'F2040-12 + VBU 200',
       '12 kW ar iebūvētu 180 L boileri. Liela māja ar vairākiem vannas istabas lietotājiem.',
       '12 kW', 'A++', '3,60', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '12 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '3,60'),
           ('Iebūvēta tvertne', '180 L KU (VBU 200)'),
           ('Min. darba temp.', '−20 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-32'),
       ], kw_badge='12 kW'),

    # ── Viessmann Vitocal 252-A — ar iebūvētu boileru ─────────────────────
    brand_div('Viessmann Vitocal 252-A — ar iebūvētu boileru'),
    hp('hp-daikin-2.jpg', 'Viessmann', 'Vitocal 252-A 6kW',
       'Vācijas inženieru darbs — A+++ klase ar 220 L iebūvētu karstā ūdens cilindru.',
       '6 kW', 'A+++', '4,68', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '6 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,68'),
           ('Iebūvēta tvertne', '220 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-290 (propāns)'),
           ('Trokšņa līmenis', '43 dB(A)'),
       ], badge='new', kw_badge='6 kW'),
    hp('hp-daikin-2.jpg', 'Viessmann', 'Vitocal 252-A 10kW',
       'Vidēja lieluma mājai ar 220 L boileri. Propāna aukstumagents — ļoti zems CO₂ nospiedums.',
       '10 kW', 'A+++', '4,53', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '10 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,53'),
           ('Iebūvēta tvertne', '220 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-290 (propāns)'),
       ], kw_badge='10 kW'),
    hp('hp-daikin-2.jpg', 'Viessmann', 'Vitocal 252-A 14kW',
       'Lielas mājas risinājums ar 300 L iebūvētu boileri. Augstākā efektivitātes klase.',
       '14 kW', 'A++', '4,10', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '14 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '4,10'),
           ('Iebūvēta tvertne', '300 L KU'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '65 °C'),
           ('Aukstumagents', 'R-290 (propāns)'),
       ], kw_badge='14 kW'),

    # ── Vaillant aroTHERM plus + uniSTOR — ar iebūvētu boileru ────────────
    brand_div('Vaillant aroTHERM plus — ar iebūvētu boileru'),
    hp('hp-daikin-altherma.jpg', 'Vaillant', 'aroTHERM plus 5kW + uniSTOR',
       'Augstas efektivitātes split sistēma ar 190 L karstā ūdens cilindru. R-290 propāna tehnoloģija.',
       '5 kW', 'A+++', '5,13', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '5 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '5,13'),
           ('Iebūvēta tvertne', '190 L KU (uniSTOR ACS)'),
           ('Min. darba temp.', '−15 °C'),
           ('Maks. ūdens temp.', '60 °C'),
           ('Aukstumagents', 'R-290 (propāns)'),
           ('Trokšņa līmenis', '40 dB(A)'),
       ], kw_badge='5 kW'),
    hp('hp-daikin-altherma.jpg', 'Vaillant', 'aroTHERM plus 8kW + uniSTOR',
       'Populārs modelis ar iebūvētu 190 L boileri. Ļoti kluss darbības režīms un garš mūžs.',
       '8 kW', 'A+++', '4,88', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '8 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,88'),
           ('Iebūvēta tvertne', '190 L KU (uniSTOR ACS)'),
           ('Min. darba temp.', '−15 °C'),
           ('Maks. ūdens temp.', '60 °C'),
           ('Aukstumagents', 'R-290 (propāns)'),
           ('Trokšņa līmenis', '42 dB(A)'),
       ], badge='popular', kw_badge='8 kW'),
    hp('hp-daikin-altherma.jpg', 'Vaillant', 'aroTHERM plus 12kW + uniSTOR',
       'Lielāka jauda ar 300 L iebūvētu boileri. Lielas mājas ar augstu siltumvadītspēju.',
       '12 kW', 'A+++', '4,91', [
           ('Tips', 'Gaiss–ūdens (split, ar boileri)'),
           ('Siltumjauda', '12 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,91'),
           ('Iebūvēta tvertne', '300 L KU (uniSTOR ACS)'),
           ('Min. darba temp.', '−15 °C'),
           ('Maks. ūdens temp.', '60 °C'),
           ('Aukstumagents', 'R-290 (propāns)'),
       ], kw_badge='12 kW'),

    # ── Midea M-Thermal Plus — ar iebūvētu boileru ────────────────────────
    brand_div('Midea M-Thermal Plus — ar iebūvētu boileru'),
    hp('hp-midea.jpg', 'Midea', 'M-Thermal Plus 8kW + 200L',
       'Monobloks ar integrētu 200 L karstā ūdens tvertni. Darbojas līdz −35 °C. Laba cena.',
       '8 kW', 'A+++', '5,10', [
           ('Tips', 'Gaiss–ūdens (monobloks, ar boileri)'),
           ('Siltumjauda', '8 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '5,10'),
           ('Iebūvēta tvertne', '200 L KU'),
           ('Min. darba temp.', '−35 °C'),
           ('Maks. ūdens temp.', '60 °C'),
           ('Aukstumagents', 'R-32'),
           ('Trokšņa līmenis', '44 dB(A)'),
       ], badge='popular', kw_badge='8 kW'),
    hp('hp-midea.jpg', 'Midea', 'M-Thermal Plus 12kW + 200L',
       'Lielāka jauda ar 200 L iebūvētu boileri. Ideāls risinājums Latvijas klimatam.',
       '12 kW', 'A+++', '4,80', [
           ('Tips', 'Gaiss–ūdens (monobloks, ar boileri)'),
           ('Siltumjauda', '12 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '4,80'),
           ('Iebūvēta tvertne', '200 L KU'),
           ('Min. darba temp.', '−35 °C'),
           ('Maks. ūdens temp.', '60 °C'),
           ('Aukstumagents', 'R-32'),
       ], kw_badge='12 kW'),

    # ── Bez iebūvēta boilera (~10%) ────────────────────────────────────────
    brand_div('Bez iebūvēta boilera'),
    hp('hp-gree-versati3.png', 'Gree', 'Versati IV 8kW',
       'Kompakts gaiss-ūdens monobloks bez boilera. Piemērots, ja jau ir esošā karstā ūdens sistēma.',
       '8 kW', 'A+++', '5,00', [
           ('Tips', 'Gaiss–ūdens (monobloks)'),
           ('Siltumjauda', '8 kW (A7/W35)'),
           ('Energoklase', 'A+++'),
           ('SCOP (35°C)', '5,00'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '60 °C'),
           ('Aukstumagents', 'R-32'),
           ('Trokšņa līmenis', '43 dB(A)'),
       ], kw_badge='8 kW'),
    hp('hp-nordis-polar.png', 'Nordis', 'Polar+ 10kW',
       'Speciāli pielāgots Baltijas klimatam. Darbojas efektīvi līdz −25 °C. Vietējs serviss.',
       '10 kW', 'A++', '4,20', [
           ('Tips', 'Gaiss–ūdens siltumsūknis'),
           ('Siltumjauda', '10 kW (A7/W35)'),
           ('Energoklase', 'A++'),
           ('SCOP (35°C)', '4,20'),
           ('Min. darba temp.', '−25 °C'),
           ('Maks. ūdens temp.', '55 °C'),
           ('Aukstumagents', 'R-32'),
           ('Piemērots', 'Baltijas klimatam'),
       ], kw_badge='10 kW'),
]

new_heat_grid = '\n'.join(new_heat_parts) + '\n'
html = html[:idx_hs] + new_heat_grid + html[idx_he:]
print('OK Heat pump section replaced (20 models, 18 with boiler = 90%)')

# ── WRITE ─────────────────────────────────────────────────────────────────────
with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done. File saved.')
