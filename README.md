# Delivery App & Telegram Bot

Aplikacja webowa zintegrowana z botem Telegram, zaprojektowana do optymalizacji i obsługi dostaw na terenie Bełchatowa. Projekt łączy intuicyjny interfejs przeglądarkowy z automatyzacją powiadomień i komunikacji poprzez komunikator.

## 🚀 Główne funkcjonalności
* **Integracja z API Telegrama:** Szybka interakcja, powiadomienia i obsługa logiki biznesowej z poziomu bota.
* **Interfejs Webowy:** Responsywny panel użytkownika zbudowany bez użycia ciężkich frameworków.
* **Geolokalizacja i mapowanie:** Obsługa koordynatów ułatwiająca zarządzanie dostawami w obszarze miasta.

## 🛠️ Wykorzystane technologie
* **Backend:** Python 3, `pyTelegramBotAPI` (Telebot)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)

## 💻 Jak uruchomić projekt lokalnie?

1. Sklonuj repozytorium:
`git clone https://github.com/patrykdobrakowski/delivery-app-telegram.git`

2. Zainstaluj wymagane zależności dla Pythona:
`pip install pyTelegramBotAPI`

3. Konfiguracja bota:
W pliku `bot.py` podmień wartość `"MÓJ_TOKEN_TUTAJ"` na swój wygenerowany token od BotFathera.

4. Uruchom serwer bota:
`python bot.py`

5. Uruchomienie frontendu:
Otwórz plik `index.html` przy użyciu rozszerzenia Live Server (w VS Code) lub dowolnego lokalnego serwera HTTP.
