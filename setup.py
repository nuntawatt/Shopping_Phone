#!/usr/bin/env python3
"""
MePhone Setup Script
สร้างโครงสร้างโฟลเดอร์และไฟล์ที่จำเป็น
"""

import os
import shutil
from urllib.request import urlretrieve

def create_directories():
    """สร้างโฟลเดอร์ที่จำเป็น"""
    directories = [
        'templates',
        'static',
        'static/images',
        'static/css',
        'static/js'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ สร้างโฟลเดอร์: {directory}")

def download_placeholder_images():
    """ดาวน์โหลดรูปภาพตัวอย่าง"""
    placeholder_images = [
        'iphone-16-pro-max.jpg',
        'iphone-16-pro.jpg',
        'iphone-16.jpg',
        'samsung-s24-ultra.jpg',
        'airpods-pro.jpg',
        'magsafe-charger.jpg',
        'iphone-15-pro-max.jpg',
        'samsung-s24-plus.jpg'
    ]
    
    print("📥 กำลังสร้างไฟล์รูปภาพตัวอย่าง...")
    for image in placeholder_images:
        image_path = f"static/images/{image}"
        if not os.path.exists(image_path):
            # สร้างไฟล์ว่างสำหรับรูปภาพ (คุณสามารถแทนที่ด้วยรูปจริงได้)
            with open(image_path, 'w') as f:
                f.write(f"# Placeholder for {image}\n# Replace this file with actual image")
            print(f"✅ สร้างไฟล์: {image_path}")

def create_readme():
    """สร้างไฟล์ README"""
    readme_content = """# MePhone - ร้านโทรศัพท์มือถือ

## วิธีการติดตั้งและรัน

### 1. ติดตั้ง Python packages
```bash
pip install -r requirements.txt
```

### 2. รันแอพพลิเคชัน
```bash
python app.py
```

### 3. เปิดเว็บเบราว์เซอร์
ไปที่: http://localhost:5000

## โครงสร้างไฟล์
```
MePhone/
├── app.py                 # Flask application หลัก
├── requirements.txt       # Python dependencies
├── setup.py              # สคริปต์สำหรับติดตั้ง
├── templates/
│   └── index.html        # HTML template หลัก
└── static/
    └── images/           # รูปภาพสินค้า (ใส่รูปจริงที่นี่)
        ├── iphone-16-pro-max.jpg
        ├── iphone-16-pro.jpg
        ├── iphone-16.jpg
        ├── samsung-s24-ultra.jpg
        ├── airpods-pro.jpg
        ├── magsafe-charger.jpg
        ├── iphone-15-pro-max.jpg
        └── samsung-s24-plus.jpg
```

## การใส่รูปภาพสินค้า
1. ใส่รูปภาพสินค้าจริงในโฟลเดอร์ `static/images/`
2. ใช้ชื่อไฟล์ตามที่กำหนดไว้ใน `app.py`
3. รูปภาพควรมีขนาด 300x300 pixels หรือสัดส่วนสี่เหลี่ยมจัตุรัส

## ฟีเจอร์
- ✅ Responsive Design (มือถือ/เดสก์ท็อป)  
- ✅ Dark/Light Theme
- ✅ ระบบตะกร้าสินค้า
- ✅ กรองสินค้าตามประเภท
- ✅ ค้นหาสินค้า
- ✅ ฟอร์มติดต่อ
- ✅ API สำหรับจัดการข้อมูล

## การปรับแต่ง
- แก้ไขข้อมูลสินค้าใน `app.py` ในส่วน `products` array
- แก้ไข UI/UX ใน `templates/index.html`
- เพิ่มสินค้าใหม่โดยเพิ่มใน `products` array พร้อมรูปภาพ
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✅ สร้างไฟล์: README.md")

def main():
    print("🚀 กำลังติดตั้ง MePhone Application...")
    print("=" * 50)
    
    create_directories()
    download_placeholder_images()
    create_readme()
    
    print("=" * 50)
    print("✅ ติดตั้งเสร็จสิ้น!")
    print("\n📋 ขั้นตอนต่อไป:")
    print("1. pip install -r requirements.txt")
    print("2. python app.py")
    print("3. เปิดเบราว์เซอร์ไปที่ http://localhost:5000")
    print("\n📁 อย่าลืมใส่รูปภาพสินค้าจริงในโฟลเดอร์ static/images/")

if __name__ == "__main__":
    main()