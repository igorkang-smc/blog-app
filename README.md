![img_2.png](images/img_2.png)

# Blog Application

A minimal Django project you can use as a starter: clean settings, sane defaults, and the usual dev tasks (run server, migrations, tests).


## Requirements
- Python 3.11+ (3.12 recommended)
- pip or uv / pipenv / poetry (pick your favorite)
- Git

---

## Quick Start

```bash
# 1) Clone
git clone <your-repo-url> simple-django
cd simple-django

# 2) Python env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3) Install deps
pip install -U pip wheel
pip install -r requirements.txt  # or `pip install -e .` if using a pyproject

# 4) Environment variables
cp .env.example .env

# 5) DB + superuser
python manage.py migrate
python manage.py createsuperuser

# 6) Run
python manage.py runserver
