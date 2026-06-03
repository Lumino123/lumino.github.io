import re

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Noņemt inline background no VISIEM prod-img divs ──────────────────────
html = re.sub(
    r'(<div class="prod-img")(\s+style="background:[^"]*")',
    r'\1',
    html
)

# ── 2. TCL Versati III → clean Gree product image ────────────────────────────
html = html.replace('assets/hp-gree.jpg', 'assets/hp-gree-versati3.png')

# ── 3. Fronius Primo GEN24 6.0 Plus → pareiza bilde ─────────────────────────
html = re.sub(
    r'(<img src="assets/inv-fronius\.png"[^>]*/></div><div class="prod-body"><div class="brand">Fronius</div><h4>Primo GEN24 6\.0 Plus</h4>)',
    lambda m: m.group(0).replace('assets/inv-fronius.png', 'assets/inv-fronius-gen24.png'),
    html
)

# ── 4. Fronius Symo GEN24 10.0 Plus → 3-phase bilde ─────────────────────────
html = re.sub(
    r'(<img src="assets/inv-fronius\.png"[^>]*/></div><div class="prod-body"><div class="brand">Fronius</div><h4>Symo GEN24 10\.0 Plus</h4>)',
    lambda m: m.group(0).replace('assets/inv-fronius.png', 'assets/inv-fronius-symo.png'),
    html
)

# ── 5. Fronius Primo 8.2-1 → grid-tie bilde ──────────────────────────────────
html = re.sub(
    r'(<img src="assets/inv-fronius\.png"[^>]*/></div><div class="prod-body"><div class="brand">Fronius</div><h4>Primo 8\.2-1</h4>)',
    lambda m: m.group(0).replace('assets/inv-fronius.png', 'assets/inv-fronius-primo.png'),
    html
)

# ── 6. Sigenergy invertori → pareiza bilde ───────────────────────────────────
html = re.sub(
    r'(<img src="assets/inv-solis-gc\.png"[^>]*/></div><div class="prod-body"><div class="brand">Sigenergy</div>)',
    lambda m: m.group(0).replace('assets/inv-solis-gc.png', 'assets/inv-sigenergy.png'),
    html
)

# ── 7. Pārbaudīt akumulatoru bildes ──────────────────────────────────────────
bat_map = {
    'bat-pylontech-us3000c': 'bat-pylontech-us3000c.jpg',
    'bat-pylontech-us5000':  'bat-pylontech-us5000.jpg',
    'bat-dyness':            'bat-dyness.png',
    'bat-byd-lvs':           'bat-byd-lvs.png',
    'bat-byd-hvs':           'bat-byd-hvs.png',
    'bat-solis-aio':         'bat-solis-aio.jpg',
    'bat-huawei-luna':       'bat-huawei-luna.png',
    'bat-sigenergy':         'bat-sigenergy.png',
}
for key, fname in bat_map.items():
    if f'assets/{fname}' not in html and f'assets/{key}' not in html:
        print(f'WARNING: {fname} not referenced in HTML!')

changes = sum(1 for a, b in zip(original, html) if a != b)
print(f'Done. ~{changes} characters changed.')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)
