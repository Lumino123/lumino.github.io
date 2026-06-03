import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

with open('Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Find all image src references
imgs = re.findall(r'src="(assets/[^"]+)"', html)
missing = []
for img in imgs:
    if not os.path.exists(img):
        missing.append(img)

print('=== MISSING IMAGES ===')
if missing:
    for m in sorted(set(missing)):
        print(f'  MISSING: {m}  (used {imgs.count(m)}x)')
else:
    print('  All images found!')

from collections import Counter
img_counts = Counter(imgs)
print(f'\nTotal img refs: {len(imgs)}, unique: {len(img_counts)}')

# 2. Known bad images still present?
bad_imgs = [
    'assets/bat-huawei-luna.png',
    'assets/bat-byd-hvm.png',
    'assets/hp-daikin-1.jpg',
    'assets/hp-daikin-2.jpg',
    'assets/inv-huawei-10ktl.png',
    'assets/hp-noqq-2.png',
]
print('\n=== BAD IMAGE CHECK ===')
for b in bad_imgs:
    n = html.count(b)
    status = 'STILL PRESENT' if n > 0 else 'OK'
    print(f'  {status}: {b} ({n}x)')

# 3. Known text typos
typos = [
    ('Jaā', 'should be "Jā"'),
    ('Saderībs', 'should be "Saderīgs"'),
    ('izmāksām', 'should be "izmaksām"'),
    ('AI enerģijas pārvald.', 'check truncation'),
    ('Pieprasīt', 'OK'),
]
print('\n=== TEXT ISSUES ===')
for needle, note in typos:
    n = html.count(needle)
    if n > 0:
        print(f'  {n}x FOUND: {needle!r} ({note})')

# 4. Check data-go links exist
go_targets = re.findall(r'data-go="([^"]+)"', html)
valid_go = {'home','solar','heat','inverters','batteries','contact','about'}
print('\n=== NAV LINKS ===')
invalid_go = [t for t in set(go_targets) if t not in valid_go]
if invalid_go:
    for t in invalid_go:
        print(f'  UNKNOWN data-go: "{t}" ({go_targets.count(t)}x)')
else:
    print('  All data-go targets valid:', sorted(set(go_targets)))

# 5. Check i18n keys exist in all 3 languages
lv_keys = set(re.findall(r"'([a-z0-9._-]+)':", html[html.find('I18N.lv'):html.find('I18N.en')]))
en_keys = set(re.findall(r"'([a-z0-9._-]+)':", html[html.find('I18N.en'):html.find('I18N.ru')]))
ru_keys = set(re.findall(r"'([a-z0-9._-]+)':", html[html.find('I18N.ru'):html.find('function applyLang')]))

used_i18n = set(re.findall(r'data-i18n(?:-html)?="([^"]+)"', html))
print('\n=== I18N MISSING KEYS ===')
missing_in_en = used_i18n - en_keys
missing_in_ru = used_i18n - ru_keys
missing_in_lv = used_i18n - lv_keys

shown = False
for k in sorted(missing_in_lv):
    print(f'  LV missing: {k}')
    shown = True
for k in sorted(missing_in_en):
    print(f'  EN missing: {k}')
    shown = True
for k in sorted(missing_in_ru):
    print(f'  RU missing: {k}')
    shown = True
if not shown:
    print('  All i18n keys present in all 3 languages!')

print('\n=== DONE ===')
