<div align="center">
   <img src="src/img/icon.png" alt="CS2 NoFlash" width="200" height="200">
   <h1>🌟 CS2 NoFlash 🌟</h1>
   <p>Twoje ostateczne narzędzie przeciwko oślepianiu dla Counter-Strike 2</p>
   <a href="#funkcje"><strong>Funkcje</strong></a> •
   <a href="#instalacja"><strong>Instalacja</strong></a> •
   <a href="#użycie"><strong>Użycie</strong></a> •
   <a href="#dostosowanie"><strong>Dostosowanie</strong></a> •
   <a href="#rozwiązywanie-problemów"><strong>Rozwiązywanie problemów</strong></a> •
   <a href="#współpraca"><strong>Współpraca</strong></a>
   <br><br>
   <p><strong>🌍 Tłumaczenia:</strong></p>
   <a href="README.ru.md"><img src="https://img.shields.io/badge/lang-Russian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.fr.md"><img src="https://img.shields.io/badge/lang-French-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Spanish-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.uk-UA.md"><img src="https://img.shields.io/badge/lang-Ukrainian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.pl.md"><img src="https://img.shields.io/badge/lang-Polish-purple?style=for-the-badge&logo=googletranslate"></a>
</div>

---

# Przegląd
CS2 NoFlash to zautomatyzowane narzędzie zaprojektowane dla Counter-Strike 2, które zapobiega całkowitemu oślepieniu gracza poprzez automatyczne dostosowanie wartości alfa granatów błyskowych w grze.

## Funkcje
- **Ochrona przed oślepieniem:** Automatycznie ustawia wartość alfa granatów błyskowych na 0, zapobiegając całkowitemu oślepieniu gracza.
- **Przyłączenie do procesu:** Przyłącza się do procesu cs2.exe i odczytuje wartości pamięci, aby wprowadzać zmiany w czasie rzeczywistym.
- **Sprawdzanie aktualizacji:** Automatycznie sprawdza najnowszą wersję i informuje użytkownika o dostępności aktualizacji.
- **Logowanie błędów:** Rejestruje błędy i ważne zdarzenia w pliku dziennika w celu ułatwienia debugowania.

## Instalacja
1. **Sklonuj repozytorium:**
   
bash
   git clone https://github.com/Jesewe/cs2-noflash.git
   cd cs2-noflash


2. **Zainstaluj zależności:**
   
bash
   pip install -r requirements.txt


3. **Uruchom skrypt:**
   
bash
   python main.py


## Użycie
1. Upewnij się, że Counter-Strike 2 jest uruchomiony.
2. Uruchom skrypt za pomocą powyższej komendy.
3. Skrypt automatycznie sprawdzi aktualizacje i pobierze niezbędne offsety z dostarczonych źródeł.
4. Ochrona NoFlash rozpocznie się automatycznie, minimalizując efekt błysku granatu.

## Dostosowanie
- **Katalog logów:** Pliki dziennika są domyślnie zapisywane w katalogu %LOCALAPPDATA%\Requests\ItsJesewe\crashes. Możesz to zmienić, modyfikując zmienną LOG_DIRECTORY w skrypcie.

## Rozwiązywanie problemów
- **Nie udało się pobrać offsetów:** Upewnij się, że masz aktywne połączenie internetowe i że źródłowe URL-e są dostępne.
- **Nie można otworzyć cs2.exe:** Upewnij się, że gra jest uruchomiona i że masz odpowiednie uprawnienia.
- **Nieoczekiwane błędy:** Sprawdź plik dziennika znajdujący się w katalogu logów, aby uzyskać więcej szczegółów.

## Współpraca
Współpraca jest mile widziana! Prosimy o otwarcie zgłoszenia lub przesłanie pull requesta w [repozytorium GitHub](https://github.com/Jesewe/cs2-noflash).

## Zrzeczenie się odpowiedzialności
Ten skrypt jest przeznaczony wyłącznie do celów edukacyjnych. Korzystanie z cheatów lub hacków w grach online jest sprzeczne z warunkami korzystania z większości gier i może skutkować zbanowaniem lub innymi karami. Używaj tego skryptu na własne ryzyko.

## Licencja
Ten projekt jest licencjonowany na podstawie licencji MIT. Zobacz plik [LICENSE](LICENSE) po więcej szczegółów.