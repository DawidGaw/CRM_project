# CRM Django – Specyfikacja wymagań

## 1. Wymagania funkcjonalne

### 1.1 Zarządzanie użytkownikami
- System umożliwia rejestrację i logowanie użytkowników.
- System wymaga uwierzytelnienia do dostępu do zasobów CRM.
- System obsługuje role użytkowników:
  - `admin`
  - `sales`
  - `support`
- System ogranicza dostęp do danych na podstawie roli:
  - `admin` ma pełny dostęp
  - `sales` widzi tylko swoich klientów
  - `support` ma dostęp do klientów i kontaktów, bez zarządzania dealami
- System umożliwia przypisanie klienta do użytkownika (owner).

---

### 1.2 Zarządzanie klientami
- System umożliwia dodanie nowego klienta przez zalogowanego użytkownika.
- System wymaga podania:
  - nazwy (osoba lub firma)
  - adresu email (unikalny)
- System umożliwia edycję danych klienta.
- System umożliwia usunięcie klienta tylko przez użytkownika z rolą `admin`.
- System przechowuje następujące dane klienta:
  - nazwa
  - email (unikalny)
  - telefon (opcjonalny)
  - firma (opcjonalna)
  - status: `Lead`, `Active`, `Inactive`, `Lost`
  - owner (użytkownik)
- System umożliwia:
  - wyszukiwanie klientów po nazwie i emailu
  - filtrowanie po statusie, ownerze i tagach
- System umożliwia przypisywanie wielu tagów do klienta.

---

### 1.3 Historia kontaktów
- System umożliwia rejestrowanie kontaktów z klientem.
- Każdy kontakt zawiera:
  - typ: `Call`, `Email`, `Meeting`, `Video Call`, `Note`
  - datę kontaktu
  - notatkę
  - użytkownika wykonującego kontakt
- System umożliwia ustawienie daty następnego kontaktu (`next_followup`).
- System wyświetla historię kontaktów klienta w porządku chronologicznym.

---

### 1.4 Zadania
- System umożliwia tworzenie zadań przypisanych do użytkownika.
- Zadanie zawiera:
  - tytuł (wymagany)
  - opis (opcjonalny)
  - termin wykonania
  - status: `To Do`, `In Progress`, `Done`, `Cancelled`
  - priorytet
- System umożliwia:
  - edycję zadania przez jego właściciela
  - filtrowanie po statusie i terminie
- System wyświetla listę zadań przypisanych do użytkownika.

---

### 1.5 Deals / Pipeline sprzedaży
- System umożliwia tworzenie transakcji (deal) powiązanych z klientem.
- Deal zawiera:
  - tytuł
  - wartość (liczbowa)
  - etap: `Lead`, `Contacted`, `Meeting`, `Offer`, `Won`, `Lost`
  - prawdopodobieństwo (0–100%)
  - datę utworzenia
  - przewidywaną datę zamknięcia
- System umożliwia zmianę etapu dealu zgodnie z logiką biznesową:
  - `Won` i `Lost` są stanami końcowymi
- System umożliwia przypisanie dealu do użytkownika.
- System umożliwia podgląd pipeline sprzedaży.

---

### 1.6 Powiadomienia i przypomnienia
- System generuje powiadomienia gdy:
  - brak kontaktu z klientem przez określoną liczbę dni
  - zbliża się termin `next_followup`
  - zadanie jest przeterminowane
- System umożliwia konfigurację progu dni (X).
- Powiadomienia są dostępne:
  - w panelu aplikacji
  - opcjonalnie przez email

---

### 1.7 Dashboard
- System wyświetla dashboard zawierający:
  - liczbę klientów
  - klientów wymagających kontaktu
  - zadania na dziś
  - wartość pipeline
- System prezentuje statystyki użytkownika:
  - liczba kontaktów
  - liczba zamkniętych deali
  - wartość sprzedaży

---

### 1.8 Notatki i tagi
- System umożliwia dodawanie notatek do klienta.
- System umożliwia przypisywanie wielu tagów do klientów.
- System umożliwia filtrowanie klientów po tagach.

---

## 2. Wymagania niefunkcjonalne

### 2.1 Bezpieczeństwo
- Hasła użytkowników muszą być przechowywane w formie haszowanej.
- System musi stosować mechanizmy ochrony przed:
  - CSRF
- Dostęp do zasobów musi być autoryzowany na podstawie roli.

---

### 2.2 Wydajność
- Czas odpowiedzi API nie powinien przekraczać 500 ms dla standardowych zapytań.
- Lista klientów musi obsługiwać paginację.
- System powinien obsługiwać co najmniej 10 000 klientów bez zauważalnego spadku wydajności.

---

### 2.3 Skalowalność
- System powinien obsługiwać minimum 100 jednoczesnych użytkowników.
- Architektura powinna umożliwiać wdrożenie na bazie PostgreSQL.
- Zadania asynchroniczne powinny być obsługiwane przez Celery + Redis.

---

### 2.4 Architektura
- Backend: Django + Django REST Framework
- Architektura oparta o podział:
  - models
  - services (logika biznesowa)
  - API (views/serializers)

---

### 2.5 Testowanie
- System powinien posiadać testy jednostkowe dla modeli.
- System powinien posiadać testy API.
- Minimalne pokrycie testami: 60%.

---

### 2.6 Użyteczność (UX)
- Interfejs powinien być responsywny (mobile-friendly).
- Kluczowe funkcje (dodanie klienta, kontakt) dostępne w maks. 3 kliknięciach.

---

## 3. MVP (Minimalna wersja)
System MVP musi zawierać:
- logowanie użytkownika
- zarządzanie klientami (CRUD)
- historię kontaktów
- follow-up (next_contact + lista klientów do kontaktu)