import json, base64, re

jsonl = 'c:/Users/tomas/.claude/projects/c--Users-tomas-Downloads-lumino-website--1--uploads/33ba7be1-db94-4d73-a416-e578aee4bf51.jsonl'

images = []
with open(jsonl, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
        except:
            continue
        # Navigate into message content looking for image blocks
        msg = entry.get('message', entry)
        content = msg.get('content', [])
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get('type') == 'image':
                    src = block.get('source', {})
                    if src.get('type') == 'base64':
                        images.append({
                            'media_type': src.get('media_type', 'image/png'),
                            'data': src.get('data', '')
                        })

print(f'Found {len(images)} images total')
# Take the last 3 (most recent = current message)
recent = images[-3:]
names = ['bat-huawei-luna5s0', 'bat-huawei-luna10s0', 'bat-huawei-luna15s0']
for i, (img, name) in enumerate(zip(recent, names)):
    ext = img['media_type'].split('/')[-1]
    if ext == 'jpeg':
        ext = 'jpg'
    fname = f'c:/Users/tomas/Downloads/lumowebpage/assets/{name}.{ext}'
    with open(fname, 'wb') as f:
        f.write(base64.b64decode(img['data']))
    import os
    size = os.path.getsize(fname)
    print(f'Saved image {i+1} -> assets/{name}.{ext} ({size//1024} KB)')
