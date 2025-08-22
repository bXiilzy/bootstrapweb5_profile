# 🚀 bootstrapweb5_profile

โปรเจกต์นี้เป็นเว็บแอปพลิเคชันที่พัฒนาด้วย Django และ Bootstrap 5 สำหรับสร้างเว็บไซต์โปรไฟล์และสาธิตฟีเจอร์ต่าง ๆ

## ✨ คุณสมบัติหลัก
- 🏠 หน้าเว็บหลัก (index)
- 👤 หน้าเกี่ยวกับ (about)
- 📞 หน้าติดต่อ (contact)
- 🔁 ฟีเจอร์วนซ้ำ (for) สำหรับสาธิตการวนซ้ำ
- 🧮 ฟีเจอร์ตารางสูตรคูณ (table) สำหรับแสดงแม่สูตรคูณ
- 🎨 ระบบ Static และ Template แยกส่วน

## 🗂️ โครงสร้างโปรเจกต์

```
bootstrapweb5/
│
├── bootstrapweb5/           # Django Project Root
│   ├── settings.py          # การตั้งค่าโปรเจกต์
│   ├── urls.py              # Routing หลักของโปรเจกต์
│   ├── wsgi.py, asgi.py     # สำหรับ deployment
│   └── __pycache__/         # ไฟล์แคช
│
├── env/                     # Python Virtual Environment
│
├── statics/                 # Static Files (CSS, JS, Images)
│   ├── assets/              # รูปภาพและ JS ตัวอย่าง
│   ├── css/                 # ไฟล์ CSS
│   └── js/                  # ไฟล์ JavaScript
│
├── templates/               # Django Templates (HTML)
│   ├── base.html            # Template หลัก
│   ├── index.html           # หน้าแรก
│   ├── about.html           # หน้าเกี่ยวกับ
│   ├── contact.html         # หน้าติดต่อ
│   ├── for.html             # ฟีเจอร์วนซ้ำ
│   └── table.html           # ฟีเจอร์ตารางสูตรคูณ
│
├── webpage/                 # Django App หลัก
│   ├── views.py             # ฟังก์ชันสำหรับแต่ละหน้า
│   ├── urls.py              # Routing ของแอป
│   ├── models.py            # โมเดลฐานข้อมูล (ยังไม่ใช้)
│   └── migrations/          # Migration files
│
├── db.sqlite3               # ฐานข้อมูล SQLite
├── manage.py                # Django management script
├── requirements.txt         # รายการ Python packages ที่ต้องใช้
├── build_files.sh           # สคริปต์สำหรับ build (ถ้ามี)
├── vercel.json              # การตั้งค่า deployment สำหรับ Vercel
└── README.md                # เอกสารประกอบโปรเจกต์
```

## ⚙️ การทำงานของแต่ละส่วน

- `settings.py` ⚡ กำหนดค่าต่าง ๆ ของโปรเจกต์ เช่น static, template, database
- `urls.py` 🌐 กำหนดเส้นทาง URL หลักและเชื่อมต่อกับแอป webpage
- `webpage/views.py` 🧩 ประกอบด้วยฟังก์ชัน view:
    - `index` 🏠 แสดงหน้าแรก
    - `about` 👤 แสดงหน้าเกี่ยวกับ
    - `contact` 📞 แสดงหน้าติดต่อ
    - `for_view` 🔁 รับค่าจากฟอร์มและแสดงการวนซ้ำ
    - `table_view` 🧮 รับค่าจากฟอร์มและแสดงแม่สูตรคูณ
- `webpage/urls.py` 🛣️ กำหนด routing สำหรับแต่ละ view
- `templates/` 🖼️ เป็นไฟล์ HTML ที่ใช้ render หน้าเว็บ
- `statics/` 🎨 เก็บไฟล์ CSS, JS, รูปภาพ

## 🛠️ วิธีการใช้งาน
1. สร้าง virtual environment และติดตั้ง dependencies:
   ```powershell
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   ```
2. รันเซิร์ฟเวอร์:
   ```powershell
   python manage.py runserver
   ```
3. เข้าชมเว็บผ่าน http://localhost:8000

## 🚚 การ deploy
- รองรับการ deploy บน Vercel ด้วยไฟล์ `vercel.json`

## 📄 License
MIT
