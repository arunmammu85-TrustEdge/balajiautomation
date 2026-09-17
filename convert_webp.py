from PIL import Image
import os

images = ['images/fuji.png', 'images/delta.png']

for img_path in images:
    if os.path.exists(img_path):
        try:
            im = Image.open(img_path).convert("RGBA")
            webp_path = img_path.replace('.png', '.webp')
            im.save(webp_path, 'webp', quality=90)
            print(f"Converted {img_path} to {webp_path}")
        except Exception as e:
            print(f"Error converting {img_path}: {e}")
    else:
        print(f"File not found: {img_path}")

