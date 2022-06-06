<p align="center">
<a href="https://www.codefactor.io/repository/github/mmdbalkhi/sansorchi"><img src="https://www.codefactor.io/repository/github/mmdbalkhi/sansorchi/badge" alt="CodeFactor"></a>
<a href="https://results.pre-commit.ci/latest/github/mmdbalkhi/Sansorchi/main"><img src="https://results.pre-commit.ci/badge/github/mmdbalkhi/Sansorchi/main.svg" alt="pre-commit"></a>
<a href="https://github.com/mmdbalkhi/Sansorchi/actions/workflows/pylint.yml"><img src="https://github.com/mmdbalkhi/Sansorchi/actions/workflows/pylint.yml/badge.svg" alt="pylint"></a>
<a href="https://github.com/mmdbalkhi/Sansorchi/actions/workflows/test.yml"><img src="https://github.com/mmdbalkhi/Sansorchi/actions/workflows/test.yml/badge.svg" alt="test"></a>
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

- remove badwords

```python
from sansorchi import Sansorchi

sansorchi = Sansorchi()

sansorchi.remove_bad_words("YOUR_TEXT")
```

- check badwords

```python
sansorchi.is_bad_word("YOUR_TEXT")
```

if yourtext has badword return True else return False

### Contributing

See this [file](https://github.com/mmdbalkhi/Sansorchi/blob/main/CONTRIBUTING.md) to contribute
