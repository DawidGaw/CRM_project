# CRM – Django Project

CRM to system do zarządzania klientami, kontaktami i sprzedażą.  

## Cel projektu
- Zarządzanie klientami i historią kontaktów
- Automatyczne przypomnienia o follow-up
- Pipeline sprzedażowy i statystyki

## Technologie
- Django 4.x
- Django REST Framework
- PostgreSQL
- Celery + Redis (zadania w tle)
- Frontend: Django templates / React opcjonalnie

## Jak uruchomić
1. Stwórz środowisko wirtualne:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate     # Windows