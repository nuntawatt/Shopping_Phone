# MePhone - ร้านโทรศัพท์มือถือ

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
