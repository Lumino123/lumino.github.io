from rembg import remove
from PIL import Image, ImageDraw
import io, os

assets = 'c:/Users/tomas/Downloads/lumowebpage/assets/'

def rembg_to_white(src, dst):
    with open(assets + src, 'rb') as f:
        inp = f.read()
    out = remove(inp)
    img = Image.open(io.BytesIO(out)).convert('RGBA')
    bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    result = bg.convert('RGB')
    result.save(assets + dst, 'PNG', optimize=True)
    print(f'Saved {dst} ({os.path.getsize(assets+dst)//1024} KB)')

# Gree Versati: wipe bottom-left corner (green leaf remnant) with white, then save
img = Image.open(assets + 'hp-gree-versati3.png').convert('RGB')
w, h = img.size
# The leaf is roughly in the bottom-left 15% of the image
draw = ImageDraw.Draw(img)
draw.rectangle([0, int(h*0.75), int(w*0.25), h], fill=(255, 255, 255))
img.save(assets + 'hp-gree-versati3.png', 'PNG', optimize=True)
print(f'Cleaned hp-gree-versati3.png')

# Fronius Symo GEN24 — same background removal
rembg_to_white('inv-fronius-symo-gen24.jpg', 'inv-fronius-symo-gen24.png')

print('Done.')
