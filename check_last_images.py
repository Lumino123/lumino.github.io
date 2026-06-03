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
for i, img in enumerate(images[-6:]):
    idx = len(images) - 6 + i
    size = len(base64.b64decode(img['data']))
    print(f'  [{idx}] {img["media_type"]} — {size//1024} KB decoded')
