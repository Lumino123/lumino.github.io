with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

def fix_card_image(html, model_tag, old_img, new_img):
    idx = html.find(model_tag)
    if idx == -1:
        print(f'MISSING: {model_tag}')
        return html
    card_start = html.rfind('<div class="prod-card', 0, idx)
    card_end = html.find('</div></div>', idx) + 12
    card = html[card_start:card_end]
    new_card = card.replace(f'assets/{old_img}', f'assets/{new_img}', 1)
    if new_card == card:
        print(f'NO CHANGE: {model_tag}')
        return html
    print(f'OK {model_tag} -> {new_img}')
    return html[:card_start] + new_card + html[card_end:]

# Huawei LUNA2000-7-E1: lifestyle photo -> clean 10s0 image (visually identical module)
html = fix_card_image(html, 'LUNA2000-7-E1</h4>', 'bat-huawei-luna.png', 'bat-huawei-luna10s0.webp')

# BYD HVM 2.76 kWh: blank image -> clean BYD HVS (same product family look)
html = fix_card_image(html, 'Battery-Box HVM 2,76 kWh</h4>', 'bat-byd-hvm.png', 'bat-byd-hvs-clean.jpg')
# try alternate title format
if 'bat-byd-hvm.png' in html:
    html = fix_card_image(html, 'HVM 2,76', 'bat-byd-hvm.png', 'bat-byd-hvs-clean.jpg')
if 'bat-byd-hvm.png' in html:
    html = fix_card_image(html, 'HVM 2.76', 'bat-byd-hvm.png', 'bat-byd-hvs-clean.jpg')

# Fronius Reserva BMS 3.15 kWh: lifestyle photo -> clean white tower battery
html = fix_card_image(html, 'Reserva BMS 3,15 kWh</h4>', 'bat-huawei-luna.png', 'bat-dyness-tower.jpg')
if original.count('Reserva BMS 3.15') > 0:
    html = fix_card_image(html, 'Reserva BMS 3.15 kWh</h4>', 'bat-huawei-luna.png', 'bat-dyness-tower.jpg')

# Fronius Reserva Pro 3.98 kWh: lifestyle photo -> clean white tower battery
html = fix_card_image(html, 'Reserva Pro 3,98 kWh</h4>', 'bat-huawei-luna.png', 'bat-dyness-tower.jpg')
if original.count('Reserva Pro 3.98') > 0:
    html = fix_card_image(html, 'Reserva Pro 3.98 kWh</h4>', 'bat-huawei-luna.png', 'bat-dyness-tower.jpg')

# Check if any bat-huawei-luna.png remain (should be none if all fixed)
remaining = html.count('bat-huawei-luna.png')
print(f'\nRemaining bat-huawei-luna.png uses: {remaining}')
remaining_hvm = html.count('bat-byd-hvm.png')
print(f'Remaining bat-byd-hvm.png uses: {remaining_hvm}')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done. {sum(1 for a,b in zip(original,html) if a!=b)} chars changed.')
