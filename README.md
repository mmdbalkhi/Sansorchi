[![Python package](https://github.com/KomeilParseh/Sansorchi/actions/workflows/python-package.yml/badge.svg)](https://github.com/KomeilParseh/Sansorchi/actions/workflows/python-package.yml)
[![Upload Python Package](https://github.com/KomeilParseh/Sansorchi/actions/workflows/python-publish.yml/badge.svg)](https://pypi.org/project/Sansorchi/)

# Sansorchi

## Remove Persian (Farsi) Swear Words

Sansorchi is a program to remove bad and inappropriate words (currently for the Persian language)

<div dir="rtl">

### یاداشت

برخی از کلمات در ظاهر کلمات بد به حساب نمیان ولی برای کاربردهای خاص ممکنه نیاز به فیلتر شدن داشته باشن که هر کس با توجه به نیاز باید شخصی سازی انجام بده و از این دیتاست استفاده کنه

در صورت علاقه، به تکمیل شدن این دیتاست کمک کنید

از این دیتاست در فیلتر کردن متن ها در پروژه های خود استفاده کنید و متون پاک و سالمی را داشته باشید

منبع دیتا بیس اصلی [اینجا](https://github.com/amirshnll/Persian-Swear-Words) است .

</div>

### Installation

```bash

    pip3 install Sansorchi

```

### usage

```python

    from Sansorchi import sansor
    print(sansor("YOUR_TEXT"))

```
