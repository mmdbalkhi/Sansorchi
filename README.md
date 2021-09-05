<p align="center">
<a href="https://www.codefactor.io/repository/github/komeilparseh/sansorchi"><img src="https://www.codefactor.io/repository/github/komeilparseh/sansorchi/badge" alt="CodeFactor"></a>
<a href="https://results.pre-commit.ci/latest/github/KomeilParseh/Sansorchi/main"><img src="https://results.pre-commit.ci/badge/github/KomeilParseh/Sansorchi/main.svg" alt="pre-commit"></a>
<a href="https://github.com/KomeilParseh/Sansorchi/actions/workflows/pylint.yml"><img src="https://github.com/KomeilParseh/Sansorchi/actions/workflows/pylint.yml/badge.svg" alt="pylint"></a>
<a href="https://github.com/KomeilParseh/Sansorchi/actions/workflows/test.yml"><img src="https://github.com/KomeilParseh/Sansorchi/actions/workflows/test.yml/badge.svg" alt="test"></a>
</p>

# Sansorchi

## Remove Persian (Farsi) Swear Words

Sansorchi is a program to remove bad and inappropriate words (currently for the Persian language)

<div dir="rtl">

### یاداشت

> برخی از کلمات در ظاهر کلمات بد به حساب نمیان ولی برای کاربردهای خاص ممکنه نیاز به فیلتر شدن داشته باشن که هر کس با توجه به نیاز باید شخصی سازی انجام بده و از این دیتاست استفاده کنه

در صورت علاقه، به تکمیل شدن این دیتاست کمک کنید

از این کتابخونه در فیلتر کردن متن ها در پروژه های خود استفاده کنید و متون پاک و سالمی را داشته باشید

منبع دیتا بیس اصلی [اینجا](https://github.com/amirshnll/Persian-Swear-Words) است .

</div>

### Installation

```bash

pip3 install Sansorchi

```

### usage

```python

from sansorchi import sansor
print(sansor("YOUR_TEXT"))

```

### Contributing

See this [file](https://github.com/KomeilParseh/Sansorchi/blob/main/CONTRIBUTING.md) to contribute
