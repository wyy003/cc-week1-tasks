import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

folder = r"C:\Users\wyyov\Desktop\photos"

files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

renames = []

for filename in files:
    filepath = os.path.join(folder, filename)
    date_str = None
    
    try:
        img = Image.open(filepath)
        exif = img._getexif()
        if exif:
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    date_str = datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d")
                    break
    except:
        pass
    
    if not date_str:
        mtime = os.path.getmtime(filepath)
        date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    
    new_name = f"{date_str}-{filename}"
    renames.append((filename, new_name))

print("预览重命名：\n")
for old, new in renames:
    print(f"{old} → {new}")

confirm = input("\n确认执行重命名？(y/n): ")

if confirm.lower() == 'y':
    for old, new in renames:
        old_path = os.path.join(folder, old)
        new_path = os.path.join(folder, new)
        os.rename(old_path, new_path)
    print(f"\n完成！已重命名 {len(renames)} 个文件")
else:
    print("\n已取消")
