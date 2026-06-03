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

print(f'Total images: {len(images)}')

# Last image is the new M1 inverter
img = images[-1]
ext = img['media_type'].split('/')[-1]
if ext == 'jpeg': ext = 'jpg'
path = f'c:/Users/tomas/Downloads/lumowebpage/assets/inv-huawei-m1.{ext}'
with open(path, 'wb') as f:
    f.write(base64.b64decode(img['data']))
size = os.path.getsize(path)
print(f'Saved: assets/inv-huawei-m1.{ext} ({size//1024} KB)')
