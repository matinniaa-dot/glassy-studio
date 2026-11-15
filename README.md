# Glassy Studio

ویرایشگر استوری گلس‌مورفیسم توچال — تک‌فایل HTML، بدون نصب.

## فایل‌ها

| فایل | توضیح |
|---|---|
| `glassy-studio.html` | نسخه standalone — همین را روی مرورگر باز کنید |
| `studio.src.html` | سورس (placeholder فونت و لوگو) |
| `asm.py` | assembler: فونت و لوگو را embed می‌کند → glassy-studio.html |

## ساخت مجدد

برای rebuild کردن از سورس:

```bash
python3 asm.py
```

فایل‌های فونت باید در `../tochal-hours-story/assets/fonts/` و لوگو در `logo-small.png` باشد.

## قالب‌ها

- استوری ساعت کار پیست (تاریخ شمسی خودکار)
- نرخ اجاره مدرسه ۱
- نرخ اجاره مدرسه ۲ VIP
- تب‌های شیشه‌ای گلسی

## خروجی

- تصویر JPG / PNG
- ویدیو MP4 / WebM (Chrome/Edge)
