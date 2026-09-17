from PIL import Image
import os

src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/ba_spark_logo_1789667659947.png'
dest = 'assets/images/ba_logo.webp'

# Crop out the bottom text
if os.path.exists(src):
    try:
        im = Image.open(src)
        # Crop to remove bottom text (1024x820)
        im_cropped = im.crop((0, 0, 1024, 820))
        im_cropped.save(dest, 'webp', quality=85)
        print("Cropped and saved new logo.")
    except Exception as e:
        print(f"Error processing image: {e}")

# Update index.html
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('src="assets/images/img_26_logo_cropped.webp"', 'src="assets/images/ba_logo.webp" style="border-radius: 6px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"')

with open('index.html', 'w') as f:
    f.write(html)

print("HTML updated with new logo.")
