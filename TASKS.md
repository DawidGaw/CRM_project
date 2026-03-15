# CRM Django – Lista funkcjonalności

## 1. Zarządzanie użytkownikami
- [ ] Rejestracja i logowanie użytkowników
- [ ] Role użytkowników: `admin`, `sales`, `support`
- [ ] Przypisywanie klientów do użytkownika (`owner`)

## 2. Zarządzanie klientami
- [ ] Dodawanie klientów
- [ ] Edycja klientów
- [ ] Usuwanie klientów
- [ ] Pola klienta:
  - [ ] Imię i nazwisko / nazwa firmy
  - [ ] Email
  - [ ] Telefon
  - [ ] Firma
  - [ ] Status klienta: `Lead`, `Active`, `Inactive`, `Lost`
  - [ ] Opiekun klienta (User)
- [ ] Wyszukiwanie i filtrowanie klientów
- [ ] Tagowanie klientów (np. VIP, Startup, Problematic)

## 3. Historia kontaktów (Contact)
- [ ] Rejestrowanie kontaktów z klientem:
  - [ ] Typ kontaktu: `Call`, `Email`, `Meeting`, `Video Call`, `Note`
  - [ ] Data kontaktu
  - [ ] Notatka
  - [ ] Użytkownik wykonujący kontakt
- [ ] Ustawienie następnego kontaktu (`next_followup`)
- [ ] Wyświetlanie listy kontaktów dla klienta

## 4. Zadania (Task)
- [ ] Tworzenie zadań dla siebie lub innych użytkowników
- [ ] Pola zadania:
  - [ ] Tytuł
  - [ ] Opis
  - [ ] Termin wykonania
  - [ ] Status: `To Do`, `In Progress`, `Done`, `Cancelled`
  - [ ] Priorytet
- [ ] Lista zadań przypisanych do użytkownika
- [ ] Filtry po statusie i terminach

## 5. Deals / Pipeline sprzedaży
- [ ] Tworzenie transakcji (Deal) dla klienta
- [ ] Pola Deal:
  - [ ] Tytuł
  - [ ] Wartość (np. w PLN)
  - [ ] Etap sprzedaży: `Lead`, `Contacted`, `Meeting`, `Offer`, `Won`, `Lost`
  - [ ] Prawdopodobieństwo zamknięcia
  - [ ] Data utworzenia
  - [ ] Przewidywana data zamknięcia
- [ ] Monitorowanie wartości sprzedaży w pipeline
- [ ] Przypisywanie deal do użytkownika

## 6. Przypomnienia i powiadomienia
- [ ] Automatyczne powiadomienia:
  - [ ] Brak kontaktu z klientem przez X dni
  - [ ] Zaplanowane follow-upy
  - [ ] Niezakończone zadania
- [ ] Wyświetlanie powiadomień w:
  - [ ] Panelu CRM
  - [ ] Email
  - [ ] Dashboard

## 7. Dashboard
- [ ] Liczba klientów
- [ ] Liczba klientów wymagających kontaktu
- [ ] Zadania na dziś
- [ ] Wartość sprzedaży
- [ ] Statystyki użytkowników:
  - [ ] Liczba kontaktów
  - [ ] Liczba zamkniętych sprzedaży
  - [ ] Wartość sprzedaży
- [ ] Widok pipeline sprzedaży

## 8. Notatki i tagi
- [ ] Dodawanie notatek dla klienta
- [ ] Tagowanie klientów
- [ ] Filtry po tagach

## 9. Integracje i rozszerzenia (opcjonalne)
- [ ] Celery + Redis – zadania w tle i przypomnienia
- [ ] Google Calendar / Outlook – planowanie spotkań
- [ ] AI – podsumowania kontaktów / notatek
- [ ] Raporty PDF / CSV

## 10. Minimalny MVP
- [ ] Logowanie użytkowników
- [ ] Lista klientów
- [ ] Karta klienta
- [ ] Dodawanie kontaktów
- [ ] Lista klientów wymagających follow-up
- [ ] Prosty dashboard z klientami i zadaniami