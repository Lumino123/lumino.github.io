with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# NIBE F2040 — was using schematic diagram, replace with NIBE-style system image
html = html.replace('assets/hp-daikin-1.jpg', 'assets/hp-nordis-polar.png')

# Viessmann Vitocal — was using house exterior photo, replace with white heat pump unit
html = html.replace('assets/hp-daikin-2.jpg', 'assets/hp-hisense.jpg')

nibe_count = original.count('assets/hp-daikin-1.jpg')
viessmann_count = original.count('assets/hp-daikin-2.jpg')
print(f'NIBE fixes: {nibe_count} (hp-daikin-1.jpg -> hp-nordis-polar.png)')
print(f'Viessmann fixes: {viessmann_count} (hp-daikin-2.jpg -> hp-hisense.jpg)')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done. {sum(1 for a,b in zip(original,html) if a!=b)} chars changed.')
