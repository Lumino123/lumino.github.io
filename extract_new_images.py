import json, base64, os

jsonl = 'c:/Users/tomas/.claude/projects/c--Users-tomas-Downloads-lumino-website--1--uploads/33ba7be1-db94-4d73-a416-e578aee4bf51.jsonl'

images = []
with open(jsonl, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            continue
        msg = entry.get('message', entry)
        content = msg.get('content', [])
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get('type') == 'image':
                    src = block.get('source', {})
                    if src.get('type') == 'base64':
                        images.append({'media_type': src.get('media_type','image/png'), 'data': src.get('data','')})

print(f'Total images in conversation: {len(images)}')

# Last 5 are from current message
# Order in message:
# 1 = Pylontech Force H2 (blue/gray tower)
# 2 = Dyness Tower (white tower)
# 3 = Fronius Primo GEN24 6.0 Plus (transparent bg)
# 4 = Fronius Primo GEN24 (white bg) - used for Symo GEN24 10.0 Plus
# 5 = Nordis Polar (indoor+outdoor HP pair)
names = [
    'bat-pylontech-force-h2',
    'bat-dyness-tower',
    'inv-fronius-primo-gen24',
    'inv-fronius-symo-gen24',
    'hp-nordis-polar',
]

recent = images[-5:]
for img, name in zip(recent, names):
    ext = img['media_type'].split('/')[-1]
    if ext == 'jpeg': ext = 'jpg'
    path = f'c:/Users/tomas/Downloads/lumowebpage/assets/{name}.{ext}'
    with open(path, 'wb') as f:
        f.write(base64.b64decode(img['data']))
    size = os.path.getsize(path)
    print(f'Saved: assets/{name}.{ext} ({size//1024} KB)')
