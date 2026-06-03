import re

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# panel-silver.png actually shows a FULL-BLACK panel (misnamed)
# panel-black.webp actually shows a SILVER-FRAME panel (misnamed)
# So: silver-frame products → panel-black.webp, full-black products → panel-silver.png

def fix_card(html, model_name, new_img):
    """Replace image src inside the prod-card that contains model_name in its h4."""
    def replacer(m):
        block = m.group(0)
        if model_name in block:
            block = re.sub(r'src="assets/panel-[^"]*"', f'src="assets/{new_img}"', block)
        return block
    return re.sub(r'<div class="prod-card[^>]*>.*?</div></div></div>', replacer, html, flags=re.DOTALL)

# Silver-frame panels → use panel-black.webp (which actually shows silver frame)
html = fix_card(html, 'Neostar 2S 450W',         'panel-black.webp')   # Aiko Neostar 2S — silver bifacial
html = fix_card(html, 'Tiger Neo 580W',           'panel-black.webp')   # Jinko Tiger Neo — silver frame
html = fix_card(html, 'Hi-MO X6 440W',           'panel-black.webp')   # LONGi Hi-MO X6 — silver frame

# Full-black panels → use panel-silver.png (which actually shows full-black)
html = fix_card(html, 'Abel 440W Full Black',     'panel-silver.png')   # Aiko Abel — full black
html = fix_card(html, 'Tiger Neo 430W Full Black','panel-silver.png')   # Jinko Tiger Neo 430 — full black
html = fix_card(html, 'Hi-MO 6 Full Black 420W', 'panel-silver.png')   # LONGi Hi-MO 6 — full black

# Huawei SUN2000-10KTL-M1: lifestyle image → clean Huawei product image
html = fix_card(html, 'SUN2000-10KTL-M1', 'inv-huawei-l1.png')

# Verify
checks = [
    ('Neostar 2S 450W',          'panel-black.webp'),
    ('Tiger Neo 580W',           'panel-black.webp'),
    ('Hi-MO X6 440W',           'panel-black.webp'),
    ('Abel 440W Full Black',     'panel-silver.png'),
    ('Tiger Neo 430W Full Black','panel-silver.png'),
    ('Hi-MO 6 Full Black 420W', 'panel-silver.png'),
    ('SUN2000-10KTL-M1',        'inv-huawei-l1.png'),
]

for model, expected_img in checks:
    pattern = f'<h4>{re.escape(model)}</h4>'
    # find the card containing this model
    card_match = re.search(
        r'<div class="prod-card[^>]*>(.*?)</div></div></div>',
        html, re.DOTALL
    )
    # search around the h4
    idx = html.find(f'<h4>{model}</h4>')
    if idx == -1:
        print(f'NOT FOUND: {model}')
        continue
    # get nearby img src
    nearby = html[max(0,idx-500):idx]
    img_match = re.search(r'src="assets/([^"]+)"', nearby)
    actual = img_match.group(1) if img_match else 'no img found'
    status = 'OK' if actual == expected_img else f'WRONG (got {actual})'
    print(f'{status} | {model} -> {expected_img}')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

changed = sum(1 for a,b in zip(original,html) if a!=b)
print(f'\nDone. ~{changed} chars changed.')
