import os
from PIL import Image

# Use the previous office image
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_tech_office_bg_1789664903363.png'
dest = 'assets/images/tech_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
        print("Reverted to previous office image.")
    except Exception as e:
        print(f"Error converting: {e}")
else:
    print("Source image not found.")
