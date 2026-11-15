# Journal

Проект рассчитан на Python 3.14 и Django 5.2.16.

База знаний и журнал инженеров

## Локальный запуск

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
flake8 local_deck
cd local_deck
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py runserver
```


Файл `requirements.txt` содержит только прямые зависимости задания и не
должен перезаписываться командой `pip freeze`.
