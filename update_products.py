#!/usr/bin/env python3
# encoding: utf-8
"""Comprehensive product update for Lumino.html"""

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── HELPERS ──────────────────────────────────────────────────────────────────
def brand_div(name, first=False):
    pad = "8px 0 10px" if first else "24px 0 10px"
    return (f'        <div style="grid-column:1/-1;padding:{pad};border-bottom:1px solid var(--line)">'
            f'<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
            f'text-transform:uppercase">{name}</span></div>')

def sub_div(text):
    return (f'        <div style="grid-column:1/-1;padding:10px 0 4px;margin-top:4px">'
            f'<span style="font-size:10px;letter-spacing:.12em;font-weight:700;color:var(--brand);'
            f'text-transform:uppercase;border-left:3px solid var(--brand);padding-left:8px">'
            f'{text}</span></div>')

def card(img, brand, name, desc, s1, s2, s3, specs, badge=None,
         s1l='Jauda', s2l='Efektivit.', s3l='Garantija'):
    b = ''
    if badge == 'popular':
        b = '<span class="rib" data-i18n="common.popular">Populārs</span>'
    elif badge == 'new':
        b = '<span class="rib new" data-i18n="common.new">Jauns</span>'
    sr = ''.join(
        f'<div class="tt-row"><span class="tt-label">{k}</span>'
        f'<span class="tt-val">{v}</span></div>' for k, v in specs)
    return (
        f'        <div class="prod-card reveal">'
        f'<div class="prod-img">{b}<img src="assets/{img}" alt=""/></div>'
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

# ── HV SOLIS SPECS (shared) ────────────────────────────────────────────────
HV_COMMON = [
    ('Akumul. spriegums', '200–800 V (augstvoltāžas)'),
    ('Maks. PV spriegums', '1000 V DC'),
    ('Maks. efektivitāte', '98,7%'),
    ('Aizsardzības klase', 'IP65'),
    ('Pārslēgšanās laiks', '< 10 ms (UPS)'),
    ('Garantija', '5 gadi'),
]

LV_COMMON = [
    ('Akumul. spriegums', '40–60 V (zemspriegums)'),
    ('Saderīgs ar', 'Pylontech US, BYD LVS, u.c.'),
    ('Maks. efektivitāte', '98,5%'),
    ('Aizsardzības klase', 'IP65'),
    ('Pārslēgšanās laiks', '< 10 ms (UPS)'),
    ('Garantija', '5 gadi'),
]

def solis_hv(model, kw, mppt, max_pv, badge=None, desc=None):
    if desc is None:
        desc = f'{kw}W trīsfāzu hibrīdais invertors ar augstvoltāžas akumulatoru saderību.'
    specs = [
        ('Nominālā jauda', f'{kw} W ({int(kw)//1000} kW)'),
        ('MPPT ieejas', mppt),
        ('Maks. PV jauda', f'{max_pv} kW'),
    ] + HV_COMMON
    kw_str = f'{int(kw)//1000} kW'
    return card('inv-solis-s6-eh.png', 'Solis', model, desc,
                kw_str, '98,7%', '5g', specs, badge)

def solis_lv(model, kw, mppt, max_pv, phase, badge=None):
    desc = f'{kw//1000}kW {"vienfāzes" if phase==1 else "trīsfāzu"} hibrīdais invertors ar zemsprieguma akumulatoru saderību.'
    specs = [
        ('Nominālā jauda', f'{kw} W ({kw//1000} kW)'),
        ('MPPT ieejas', mppt),
        ('Maks. PV jauda', f'{max_pv} kW'),
    ] + LV_COMMON
    img = 'inv-solis-s6-eh-new.png'
    kw_str = f'{kw//1000} kW'
    return card(img, 'Solis', model, desc, kw_str, '98,5%', '5g', specs, badge)

# ── BUILD NEW SOLIS SECTION ───────────────────────────────────────────────────
new_solis_parts = [
    brand_div('Solis', first=True),
    sub_div('Trīsfāzu Hibrīdi — Augstvoltāžas (200–800 V)'),
    solis_hv('S6-EH3P5K2-H-EU', 5000, '2 MPPT / 4 virknes', 10),
    solis_hv('S6-EH3P6K-H-EU',  6000, '2 MPPT / 4 virknes', 12, badge='popular'),
    solis_hv('S6-EH3P8K-H-EU',  8000, '4 MPPT / 8 virknes', 16, badge='popular'),
    solis_hv('S6-EH3P10K-H-EU', 10000,'4 MPPT / 8 virknes', 20),
    solis_hv('S6-EH3P12K-H',    12000,'4 MPPT / 8 virknes', 24),
    solis_hv('S6-EH3P15K-H',    15000,'4 MPPT / 8 virknes', 30),
    solis_hv('S6-EH3P20K-H',    20000,'4 MPPT / 8 virknes', 40),
    solis_hv('S6-EH3P30K-H',    30000,'4 MPPT / 8 virknes', 60, badge='new'),
    solis_hv('S6-EH3P50K-H',    50000,'4 MPPT / 8 virknes',100, badge='new'),
    sub_div('Vienfāzes Hibrīds — Zemspriegums (40–60 V)'),
    solis_lv('S6-EH1P5K-L-PLUS',  5000,'2 MPPT / 4 virknes',7,  1),
    sub_div('Trīsfāzu Hibrīdi — Zemspriegums (40–60 V)'),
    solis_lv('S6-EH3P8K02-NV-YD-L',  8000,'3 MPPT / 6 virknes',16, 3, badge='popular'),
    solis_lv('S6-EH3P10K02-NV-YD-L',10000,'3 MPPT / 6 virknes',20, 3),
    solis_lv('S6-EH3P12K02-NV-YD-L',12000,'3 MPPT / 6 virknes',24, 3),
    solis_lv('S6-EH3P15K02-NV-YD-L',15000,'3 MPPT / 6 virknes',30, 3),
]
new_solis = '\n'.join(new_solis_parts) + '\n'

# Replace old Solis section (from Solis divider to Huawei divider, exclusive)
SOLIS_DIV  = ('        <div style="grid-column:1/-1;padding:8px 0 10px;border-bottom:1px solid var(--line)">'
              '<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
              'text-transform:uppercase">Solis</span></div>')
HUAWEI_DIV = ('        <div style="grid-column:1/-1;padding:24px 0 10px;border-bottom:1px solid var(--line)">'
              '<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
              'text-transform:uppercase">Huawei</span></div>')

idx_s = html.index(SOLIS_DIV)
idx_h = html.index(HUAWEI_DIV)
html = html[:idx_s] + new_solis + html[idx_h:]
print('OK Solis section replaced')

# ── 2. HEAT PUMP WITH BUILT-IN BOILER ────────────────────────────────────────
# Add Daikin Altherma H section (split system with integrated boiler) after Gree section
# Insert before the closing tags before the heat subsidy banner

HEAT_GRID_END = '      </div>\n    </div>\n    <!-- Valsts atbalsts banner uz heat lapas -->'

boiler_section = '\n'.join([
    brand_div('Daikin Altherma H — ar iebūvētu boileru'),
    card(
        'hp-daikin-altherma.jpg', 'Daikin',
        'Altherma 3 H 8kW',
        'Gaiss–ūdens siltumsūknis ar iebūvētu 230L karstā ūdens tvertni. Viens no populārākajiem Latvijā.',
        '8 kW', 'A+++', '4,50', [
            ('Tips', 'Gaiss–ūdens (sadalīts, ar tvertni)'),
            ('Siltumjauda', '8 kW (A7/W35)'),
            ('Energoklase', 'A+++'),
            ('SCOP (35°C)', '4,50'),
            ('Iebūvēta tvertne', '230 L (KU)'),
            ('Min. darba temp.', '−25 °C'),
            ('Maks. ūdens temp.', '65 °C'),
            ('Aukstumagents', 'R-32'),
            ('Trokšņa līmenis', '45 dB(A)'),
        ], badge='popular',
        s2l='SCOP', s3l='Klase'
    ),
    card(
        'hp-daikin-altherma.jpg', 'Daikin',
        'Altherma 3 H 11kW',
        'Lielāka jauda ar 260L integrētu boileri. Saderīgs ar grīdas apkuri un radiatoriem.',
        '11 kW', 'A+++', '4,25', [
            ('Tips', 'Gaiss–ūdens (sadalīts, ar tvertni)'),
            ('Siltumjauda', '11 kW (A7/W35)'),
            ('Energoklase', 'A+++'),
            ('SCOP (35°C)', '4,25'),
            ('Iebūvēta tvertne', '260 L (KU)'),
            ('Min. darba temp.', '−25 °C'),
            ('Maks. ūdens temp.', '65 °C'),
            ('Aukstumagents', 'R-32'),
            ('Trokšņa līmenis', '48 dB(A)'),
        ], s2l='SCOP', s3l='Klase'
    ),
    card(
        'hp-daikin-altherma.jpg', 'Daikin',
        'Altherma 3 H 16kW',
        'Lielas mājas pilnais risinājums — apkure un karstais ūdens no vienas ierīces.',
        '16 kW', 'A++', '3,90', [
            ('Tips', 'Gaiss–ūdens (sadalīts, ar tvertni)'),
            ('Siltumjauda', '16 kW (A7/W35)'),
            ('Energoklase', 'A++'),
            ('SCOP (35°C)', '3,90'),
            ('Iebūvēta tvertne', '260 L (KU)'),
            ('Min. darba temp.', '−25 °C'),
            ('Maks. ūdens temp.', '65 °C'),
            ('Aukstumagents', 'R-32'),
        ], s2l='SCOP', s3l='Klase'
    ),
]) + '\n'

html = html.replace(HEAT_GRID_END, boiler_section + '      </div>\n    </div>\n    <!-- Valsts atbalsts banner uz heat lapas -->')
print('OK Heat pump boiler section added')

# ── 3. SOLAR PANELS ───────────────────────────────────────────────────────────
# Replace all brand sections inside the solar prod-grid
# Anchor: from Aiko brand divider to (excl.) the closing tags before solar subsidy

SOLAR_START_ANCHOR = ('        <div style="grid-column:1/-1;padding:8px 0 10px;border-bottom:1px solid var(--line)">'
                      '<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
                      'text-transform:uppercase">Aiko</span></div>')
SOLAR_END_ANCHOR   = '      </div>\n    </div>\n    <!-- Valsts atbalsts banner uz solar lapas -->'

idx_sol_s = html.index(SOLAR_START_ANCHOR)
idx_sol_e = html.index(SOLAR_END_ANCHOR)

def panel_card(img, brand, name, desc, watts, eff, guar, specs, badge=None):
    return card(img, brand, name, desc, f'{watts} W', f'{eff}%', f'{guar}g', specs, badge,
                s1l='Jauda', s2l='Efektivit.', s3l='Garantija')

PANEL_COMMON = [
    ('Darba temp.', '−40 °C līdz +85 °C'),
]

new_solar_parts = [
    brand_div('Trina Solar', first=True),
    panel_card('panel-silver.png','Trina Solar','Vertex S+ 445W',
        'TOPCon bifaciāls panelis ar sudraba rāmi. Augsta efektivitāte un uzticams veiktspējas garantija.',
        445, 22.1, 30, [
            ('Tehnoloģija', 'N-tipa TOPCon (bifaciāls)'),
            ('Nominālā jauda', '445 Wp'),
            ('Efektivitāte', '22,1%'),
            ('Voc / Isc', '41,3 V / 13,6 A'),
            ('Izmēri', '1762 × 1134 × 30 mm'),
            ('Svars', '21,3 kg'),
            ('Temper. koef.', '−0,30 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ]),
    panel_card('panel-silver.png','Trina Solar','Vertex S+ 465W',
        'Populārs TOPCon modelis ar izcilu cenas/kvalitātes samēru. Plašs izplatītāju tīkls Latvijā.',
        465, 22.5, 30, [
            ('Tehnoloģija', 'N-tipa TOPCon (bifaciāls)'),
            ('Nominālā jauda', '465 Wp'),
            ('Efektivitāte', '22,5%'),
            ('Voc / Isc', '42,6 V / 13,8 A'),
            ('Izmēri', '1762 × 1134 × 30 mm'),
            ('Svars', '21,5 kg'),
            ('Temper. koef.', '−0,30 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='popular'),
    panel_card('panel-dark.png','Trina Solar','Vertex S+ 515W',
        'Lielformāta TOPCon panelis komerciāliem projektiem un lielākām privātmāju sistēmām.',
        515, 21.7, 30, [
            ('Tehnoloģija', 'N-tipa TOPCon (bifaciāls)'),
            ('Nominālā jauda', '515 Wp'),
            ('Efektivitāte', '21,7%'),
            ('Voc / Isc', '47,8 V / 13,8 A'),
            ('Izmēri', '2094 × 1134 × 30 mm'),
            ('Svars', '25,0 kg'),
            ('Temper. koef.', '−0,30 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='new'),

    brand_div('JA Solar'),
    panel_card('panel-dark.png','JA Solar','460W LB Bifaciāls',
        'PERC bifaciāls panelis ar dubultā stikla aizsardzību. Augsta ražošana arī mākoņainā dienā.',
        460, 21.1, 30, [
            ('Tehnoloģija', 'P-tipa PERC (bifaciāls, dubults stikls)'),
            ('Nominālā jauda', '460 Wp'),
            ('Efektivitāte', '21,1%'),
            ('Bifacial koeficients', '75%'),
            ('Voc / Isc', '41,5 V / 13,9 A'),
            ('Izmēri', '1722 × 1134 × 30 mm'),
            ('Svars', '21,0 kg'),
            ('Temper. koef.', '−0,34 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='popular'),
    panel_card('panel-black.webp','JA Solar','460W LB Full Black',
        'Pilņīgi melns PERC panelis estētiski pievilcīgam izskatam. Populārs jaunām mājām.',
        460, 21.1, 30, [
            ('Tehnoloģija', 'P-tipa PERC (monofaciāls, Full Black)'),
            ('Nominālā jauda', '460 Wp'),
            ('Efektivitāte', '21,1%'),
            ('Voc / Isc', '40,1 V / 14,2 A'),
            ('Izmēri', '1722 × 1134 × 30 mm'),
            ('Svars', '21,0 kg'),
            ('Temper. koef.', '−0,34 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ]),
    panel_card('panel-dark.png','JA Solar','635W LB Bifaciāls',
        'Lielformāta N-tipa bifaciāls panelis privātmājām un komercīai ar augstu enerģijas blīvumu.',
        635, 22.0, 30, [
            ('Tehnoloģija', 'N-tipa TOPCon (bifaciāls)'),
            ('Nominālā jauda', '635 Wp'),
            ('Efektivitāte', '22,0%'),
            ('Voc / Isc', '48,5 V / 16,6 A'),
            ('Izmēri', '2278 × 1134 × 30 mm'),
            ('Svars', '28,0 kg'),
            ('Temper. koef.', '−0,30 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='new'),

    brand_div('LONGi'),
    panel_card('panel-black.webp','LONGi','Hi-MO 7 440W',
        'HPBC tehnoloģija — viens no populārākajiem modeļiem privātmājās Latvijā.',
        440, 22.8, 25, [
            ('Tehnoloģija', 'N-tipa HPBC'),
            ('Nominālā jauda', '440 Wp'),
            ('Efektivitāte', '22,8%'),
            ('Voc / Isc', '41,3 V / 13,9 A'),
            ('Izmēri', '1762 × 1134 × 30 mm'),
            ('Svars', '21,3 kg'),
            ('Temper. koef.', '−0,29 %/°C'),
            ('Produ. garantija', '15 gadi'),
            ('Ražīguma garantija', '25 gadi (88%)'),
        ], badge='popular'),
    panel_card('panel-black.webp','LONGi','Hi-MO X10 475W',
        'Jaunākās paaudzes HPBC2 tehnoloģija ar augstāko efektivitāti LONGi klāstā.',
        475, 23.1, 30, [
            ('Tehnoloģija', 'N-tipa HPBC2'),
            ('Nominālā jauda', '475 Wp'),
            ('Efektivitāte', '23,1%'),
            ('Voc / Isc', '43,0 V / 14,1 A'),
            ('Izmēri', '1762 × 1134 × 30 mm'),
            ('Svars', '21,5 kg'),
            ('Temper. koef.', '−0,28 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='new'),
    panel_card('panel-dark.png','LONGi','Hi-MO X10 530W',
        'Lielformāts ar HPBC2 — ideāls lielākām sistēmām un komerciāliem objektiem.',
        530, 22.2, 30, [
            ('Tehnoloģija', 'N-tipa HPBC2'),
            ('Nominālā jauda', '530 Wp'),
            ('Efektivitāte', '22,2%'),
            ('Voc / Isc', '47,8 V / 14,2 A'),
            ('Izmēri', '2094 × 1134 × 30 mm'),
            ('Svars', '25,0 kg'),
            ('Temper. koef.', '−0,28 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ]),

    brand_div('Jinko Solar'),
    panel_card('panel-black.webp','Jinko Solar','Tiger Neo 475W',
        'N-tipa TOPCon panelis ar izcilu efektivitāti. Viens no pārdodamākajiem paneļiem pasaulē.',
        475, 22.2, 30, [
            ('Tehnoloģija', 'N-tipa TOPCon'),
            ('Nominālā jauda', '475 Wp'),
            ('Efektivitāte', '22,2%'),
            ('Voc / Isc', '42,4 V / 14,2 A'),
            ('Izmēri', '1762 × 1134 × 30 mm'),
            ('Svars', '21,5 kg'),
            ('Temper. koef.', '−0,30 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='popular'),
    panel_card('panel-dark.png','Jinko Solar','Tiger Neo 510W',
        'Lielformāta TOPCon ar dubultā stikla aizsardzību. Augsta ražošana arī mākoņainā dienā.',
        510, 22.4, 30, [
            ('Tehnoloģija', 'N-tipa TOPCon (bifaciāls)'),
            ('Nominālā jauda', '510 Wp'),
            ('Efektivitāte', '22,4%'),
            ('Bifacial koeficients', '80%'),
            ('Voc / Isc', '45,0 V / 14,4 A'),
            ('Izmēri', '2094 × 1134 × 30 mm'),
            ('Svars', '25,5 kg'),
            ('Temper. koef.', '−0,30 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ]),

    brand_div('AIKO'),
    panel_card('panel-black.webp','AIKO','645W N-type ABC Bifaciāls',
        'Pasaulē augstākā efektivitāte seriju ražošanā — ABC N-tipa bifaciāls panelis lielākām sistēmām.',
        645, 23.9, 30, [
            ('Tehnoloģija', 'N-tipa ABC (bifaciāls, dubults stikls)'),
            ('Nominālā jauda', '645 Wp'),
            ('Efektivitāte', '23,9%'),
            ('Bifacial koeficients', '85%'),
            ('Voc / Isc', '48,9 V / 16,9 A'),
            ('Izmēri', '2278 × 1134 × 30 mm'),
            ('Svars', '∼28 kg'),
            ('Temper. koef.', '−0,24 %/°C'),
            ('Ražīguma garantija', '30 gadi'),
        ], badge='new'),
]
new_solar = '\n'.join(new_solar_parts) + '\n'
html = html[:idx_sol_s] + new_solar + html[idx_sol_e:]
print('OK Solar panels replaced')

# ── 4. BATTERIES ─────────────────────────────────────────────────────────────
BAT_START_ANCHOR = ('        <div style="grid-column:1/-1;padding:8px 0 10px;border-bottom:1px solid var(--line)">'
                    '<span style="font-size:11px;letter-spacing:.15em;font-weight:700;color:var(--muted);'
                    'text-transform:uppercase">Pylontech</span></div>')
BAT_END_ANCHOR   = '      </div>\n    </div>\n    <!-- Valsts atbalsts banner uz battery lapas -->'

idx_bat_s = html.index(BAT_START_ANCHOR)
idx_bat_e = html.index(BAT_END_ANCHOR)

def bat_card(img, brand, name, desc, cap, eff, guar, specs, badge=None,
             s1l='Kapacitāte', s2l='Efektivit.', s3l='Garantija'):
    return card(img, brand, name, desc, cap, eff, guar, specs, badge, s1l, s2l, s3l)

new_bat_parts = [
    # ── Pylontech ──────────────────────────────────────────────────────────
    brand_div('Pylontech', first=True),
    bat_card('bat-pylontech-force-h2.jpg','Pylontech','Force H2 V2 BMS',
        'BMS kontrolleris Force H2 sistēmai. Savienot ar moduļiem 7,1–106,5 kWh kapitālo kapacitāti.',
        '5 kWh', '97%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '5 kWh (1× modulis)'),
            ('Paplašināms', 'Līdz 30× moduļiem'),
            ('Nominalais spriegums', '100–200 V'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP20'),
            ('Svars', '30 kg'),
        ], badge='popular'),
    bat_card('bat-pylontech-force-h2.jpg','Pylontech','Force H2 3,55 kWh Modulis',
        'Paplašināšanas modulis Force H2 V2 sistēmai. 3,55 kWh uz moduli, saderīgs ar lielāko daļu HV invertoru.',
        '3,55 kWh', '97%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '3,55 kWh / modulis'),
            ('Nominalais spriegums', '100 V'),
            ('Uzlādes jauda', '3,55 kW'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP20'),
            ('Svars', '37,5 kg'),
        ]),
    bat_card('bat-pylontech-force-h2.jpg','Pylontech','Force H3 5,12 kWh Modulis',
        'Jaunākās paaudzes HV modulis ar lielāku kapitālo kapacitāti uz moduli. Augstāka enerģijas blīvums.',
        '5,12 kWh', '97%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '5,12 kWh / modulis'),
            ('Nominalais spriegums', '102,4 V'),
            ('Uzlādes jauda', '5,12 kW'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP20'),
            ('Svars', '46 kg'),
        ], badge='new'),
    bat_card('bat-pylontech-us5000.jpg','Pylontech','Fidus PRO 5,12 kWh',
        'Zemsprieguma LFP akumulators ar 100A uzlādes strāvu. Saderīgs ar lielāko daļu 48V invertoru.',
        '5,12 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (zemspriegums)'),
            ('Nominālā kapacitāte', '5,12 kWh'),
            ('Nominalais spriegums', '51,2 V'),
            ('Uzlādes/izlādes str.', '100 A / 100 A'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP20'),
            ('Svars', '50 kg'),
        ]),
    bat_card('bat-pylontech-us5000.jpg','Pylontech','US5000 4,8 kWh',
        'Klasisks zemsprieguma LFP akumulators. Uzticams, popārs un saderīgs ar lielāko daļu 48V invertoru.',
        '4,8 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (zemspriegums)'),
            ('Nominālā kapacitāte', '4,8 kWh'),
            ('Nominalais spriegums', '48 V'),
            ('Uzlādes/izlādes str.', '50 A / 50 A'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP20'),
            ('Svars', '43 kg'),
            ('Paplašināms', 'Jaā (seriāls)'),
        ]),

    # ── Huawei ─────────────────────────────────────────────────────────────
    brand_div('Huawei LUNA2000'),
    bat_card('bat-huawei-luna5s0.webp','Huawei','LUNA2000-5KW-C0 BMS',
        'BMS kontrolleris LUNA2000 sistēmai. Pārvaldīšana, mērījumi un AI optimizācija.',
        'BMS', '95%', '10g', [
            ('Tips', 'BMS kontrolleris'),
            ('Savienojamība', 'LUNA2000-E moduļi'),
            ('AI enerģijas pārvald.', 'Jaā'),
            ('Aizsardzības klase', 'IP55'),
            ('Svars', '13 kg'),
        ], s1l='Tips', badge='popular'),
    bat_card('bat-huawei-luna5s0.webp','Huawei','LUNA2000-5-E0',
        '5 kWh augstvoltāžas LFP modulis LUNA2000 sistēmai. Iebūvēts Smart BMS.',
        '5 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '5 kWh'),
            ('Nominalais spriegums', '100 V'),
            ('Maks. uzl./izl. str.', '25 A'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP55'),
            ('Svars', '56 kg'),
        ]),
    bat_card('bat-huawei-luna.png','Huawei','LUNA2000-7-E1',
        '7 kWh augstvoltāžas modulis ar uzlabotu BMS. Ideāls vidēja lieluma sistēmām.',
        '7 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '7 kWh'),
            ('Nominalais spriegums', '100 V'),
            ('Maks. uzl./izl. str.', '25 A'),
            ('Uzl./izl. jauda', '2,5 kW'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP55'),
            ('Svars', '78 kg'),
        ], badge='new'),
    bat_card('bat-huawei-luna10s0.webp','Huawei','LUNA2000-10kW-C1',
        'Pilna 10 kWh LUNA2000 sistēma ar BMS un aizsardzību. Ideāls ar SUN2000 L1 invertoru.',
        '10 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '10 kWh (2× 5kWh)'),
            ('Nominalais spriegums', '200 V'),
            ('Uzl./izl. jauda', '5 kW'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP55'),
            ('AI enerģijas pārvald.', 'Jaā'),
            ('Svars', '~120 kg'),
        ]),

    # ── BYD ────────────────────────────────────────────────────────────────
    brand_div('BYD'),
    bat_card('bat-byd-hvs-clean.jpg','BYD','Premium HV BCU+Base',
        'Augstvoltāžas BYD sistēmas pārvaldītājs un bāze. Paplašināms ar HVM moduļiem līdz 66 kWh.',
        'BCU', '96%', '10g', [
            ('Tips', 'BMS kontrolleris + bāze'),
            ('Savienojamība', 'BYD HVM moduļi'),
            ('Maks. kapacitāte', 'Līdz 66 kWh'),
            ('Sprieguma diapazons', '128–819,2 V'),
            ('Aizsardzības klase', 'IP55'),
        ], s1l='Tips', badge='popular'),
    bat_card('bat-byd-hvm.png','BYD','Battery-Box HVM 2,76 kWh',
        'Augstvoltāžas LFP paplašināšanas modulis BYD Premium HV sistēmai. Modulārs un mērogojams.',
        '2,76 kWh', '96%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '2,76 kWh / modulis'),
            ('Spriegums', '102,4 V / modulis'),
            ('Maks. uzl./izl. jauda', '2,76 kW'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP55'),
            ('Svars', '37,6 kg'),
        ]),

    # ── Fronius ────────────────────────────────────────────────────────────
    brand_div('Fronius'),
    bat_card('bat-huawei-luna.png','Fronius','Reserva BMS 3,15 kWh',
        'Fronius augstvoltāžas LFP akumulators ar BMS. Ideāli saderīgs ar Primo un Symo GEN24.',
        '3,15 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '3,15 kWh'),
            ('Nominalais spriegums', '\\u223c102 V'),
            ('Maks. uzl./izl. jauda', '3,15 kW'),
            ('Saderībs', 'Fronius GEN24 invertori'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP55'),
        ], badge='popular'),
    bat_card('bat-huawei-luna.png','Fronius','Reserva Pro 3,98 kWh',
        'Paplašinātā kapacitāte ar Fronius Pro moduļiem. Paplašināms līdz 23,88 kWh.',
        '3,98 kWh', '95%', '10g', [
            ('Tehnoloģija', 'LFP (augstvoltāžas)'),
            ('Nominālā kapacitāte', '3,98 kWh / modulis'),
            ('Paplašināms', 'Līdz 6× moduļiem (23,88 kWh)'),
            ('Saderībs', 'Fronius GEN24 invertori'),
            ('Ciklu skaits', '6000+ (80% SOH)'),
            ('Aizsardzības klase', 'IP55'),
        ], badge='new'),
]
new_bat = '\n'.join(new_bat_parts) + '\n'
html = html[:idx_bat_s] + new_bat + html[idx_bat_e:]
print('OK Batteries replaced')

# ── WRITE ─────────────────────────────────────────────────────────────────────
with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done. File saved.')
