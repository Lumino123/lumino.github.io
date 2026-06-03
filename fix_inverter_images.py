with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── Solis S6-EH3P HV (9 models) ───────────────────────────────────────────────
# All currently use inv-solis-s6-eh.png — assign unique images per model

replacements = [
    # HV 3-phase — rotate through 7 distinct images
    # 5kW → keep s6-eh (it IS the S6-EH image)
    # 6kW → s6-gr (modern square touch panel)
    ('S6-EH3P6K-H-EU</h4>',   'inv-solis-s6-eh.png',      'inv-solis-s6-gr.png'),
    # 8kW → s5-gr (landscape, modern display with battery icon)
    ('S6-EH3P8K-H-EU</h4>',   'inv-solis-s6-eh.png',      'inv-solis-s5-gr.png'),
    # 10kW → rhi3p (3-phase hybrid, "hybrid 4th gen" label)
    ('S6-EH3P10K-H-EU</h4>',  'inv-solis-s6-eh.png',      'inv-solis-rhi3p.png'),
    # 12kW → gc (commercial landscape, fits 12kW 3-phase)
    ('S6-EH3P12K-H</h4>',     'inv-solis-s6-eh.png',      'inv-solis-gc.png'),
    # 15kW → s6-gr-new
    ('S6-EH3P15K-H</h4>',     'inv-solis-s6-eh.png',      'inv-solis-s6-gr-new.png'),
    # 20kW → s6-eh-new (visually same S6-EH but distinct file)
    ('S6-EH3P20K-H</h4>',     'inv-solis-s6-eh.png',      'inv-solis-s6-eh-new.png'),
    # 30kW → big commercial
    ('S6-EH3P30K-H</h4>',     'inv-solis-s6-eh.png',      'inv-solis-big.png'),
    # 50kW → big commercial
    ('S6-EH3P50K-H</h4>',     'inv-solis-s6-eh.png',      'inv-solis-big.png'),
]

for model_tag, old_img, new_img in replacements:
    # Find the card containing this model name and swap its image
    idx = html.find(model_tag)
    if idx == -1:
        print(f'MISSING: {model_tag}')
        continue
    # Look backwards to find the img src in this card
    card_start = html.rfind('<div class="prod-card', 0, idx)
    card_end = html.find('</div></div>', idx) + 12
    card = html[card_start:card_end]
    new_card = card.replace(f'assets/{old_img}', f'assets/{new_img}', 1)
    if new_card == card:
        print(f'NO CHANGE: {model_tag} — src not found as {old_img}')
    else:
        html = html[:card_start] + new_card + html[card_end:]
        print(f'OK {model_tag} → {new_img}')

# ── Solis LV 1-phase: S6-EH1P5K-L-PLUS → rhi.png (slim single-phase unit) ────
idx = html.find('S6-EH1P5K-L-PLUS</h4>')
if idx != -1:
    card_start = html.rfind('<div class="prod-card', 0, idx)
    card_end = html.find('</div></div>', idx) + 12
    card = html[card_start:card_end]
    new_card = card.replace('assets/inv-solis-s6-eh-new.png', 'assets/inv-solis-rhi.png', 1)
    html = html[:card_start] + new_card + html[card_end:]
    print(f'OK S6-EH1P5K-L-PLUS → inv-solis-rhi.png')

# ── Solis LV 3-phase (4 models) — currently all s6-eh-new.png ─────────────────
lv3_models = [
    ('S6-EH3P8K02-NV-YD-L</h4>',  'inv-solis-s5-gr.png'),
    ('S6-EH3P10K02-NV-YD-L</h4>', 'inv-solis-s6-eh.png'),
    ('S6-EH3P12K02-NV-YD-L</h4>', 'inv-solis-s6-gr.png'),
    ('S6-EH3P15K02-NV-YD-L</h4>', 'inv-solis-gc.png'),
]
for model_tag, new_img in lv3_models:
    idx = html.find(model_tag)
    if idx == -1:
        print(f'MISSING: {model_tag}')
        continue
    card_start = html.rfind('<div class="prod-card', 0, idx)
    card_end = html.find('</div></div>', idx) + 12
    card = html[card_start:card_end]
    new_card = card.replace('assets/inv-solis-s6-eh-new.png', f'assets/{new_img}', 1)
    if new_card == card:
        print(f'NO CHANGE: {model_tag}')
    else:
        html = html[:card_start] + new_card + html[card_end:]
        print(f'OK {model_tag} → {new_img}')

# ── Fronius Symo GEN24 10.0 Plus → correct Symo image ─────────────────────────
html = html.replace(
    '<h4>Symo GEN24 10.0 Plus</h4>',
    '<h4>Symo GEN24 10.0 Plus</h4>'
)
# Find the Symo GEN24 card and fix its image
idx = html.find('Symo GEN24 10.0 Plus</h4>')
if idx != -1:
    card_start = html.rfind('<div class="prod-card', 0, idx)
    card_end = html.find('</div></div>', idx) + 12
    card = html[card_start:card_end]
    new_card = card.replace('assets/inv-fronius-symo-gen24.png', 'assets/inv-fronius-symo.png', 1)
    if new_card != card:
        html = html[:card_start] + new_card + html[card_end:]
        print('OK Symo GEN24 10.0 Plus → inv-fronius-symo.png')
    else:
        print('NO CHANGE: Symo GEN24 card image')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone. {sum(1 for a,b in zip(original,html) if a!=b)} chars changed.')
