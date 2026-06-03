from rembg import remove
from PIL import Image
import io

assets = 'c:/Users/tomas/Downloads/lumowebpage/assets/'

def process(src, dst):
    with open(assets + src, 'rb') as f:
        inp = f.read()
    out = remove(inp)
    img = Image.open(io.BytesIO(out)).convert('RGBA')
    # Place on white background
    bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    result = bg.convert('RGB')
    result.save(assets + dst, 'PNG', optimize=True)
    import os
    print(f'Saved {dst} ({os.path.getsize(assets+dst)//1024} KB)')

# TCL/Gree Versati — remove green badge and text overlays
process('hp-gree-versati3.png', 'hp-gree-versati3.png')

# Fronius Primo GEN24 — remove dark background
process('inv-fronius-primo-gen24.jpg', 'inv-fronius-primo-gen24.png')

print('Done.')
