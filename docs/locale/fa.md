[![Testing](https://github.com/KomeilParseh/Sansorchi/actions/workflows/test.yml/badge.svg)](https://github.com/KomeilParseh/Sansorchi/actions/workflows/test.yml)
<div dir="rtl">

# سانسورچی

## حذف کلمات نامناسب فارسی

سانسورچی یک کتابخانه برای حذف کلمات مناسب فارسی(فعلا) است

### یاداشت

> برخی از کلمات در ظاهر کلمات بد به حساب نمیان ولی برای کاربردهای خاص ممکنه نیاز به فیلتر شدن داشته باشن که هر کس با توجه به نیاز باید شخصی سازی انجام بده و از این دیتاست استفاده کنه

در صورت علاقه، به تکمیل شدن این دیتاست کمک کنید

از این کتابخونه در فیلتر کردن متن ها در پروژه های خود استفاده کنید و متون پاک و سالمی را داشته باشید

منبع دیتا بیس اصلی [اینجا](https://github.com/amirshnll/Persian-Swear-Words) است .

### نصب

</div>

```bash

pip3 install Sansorchi

```

<div dir="rtl">

### استفاده

</div>

```python

from Sansorchi import sansor
print(sansor("YOUR_TEXT"))

```
