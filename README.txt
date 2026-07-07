Clever College Aviation Academy - Streamlit App

Ziel
Diese App ist ein Prototyp für eine Lehrgangs- und Ausbilderplattform im Bereich Luftfahrt.
Endanwender können Lehrgänge suchen und Buchungsanfragen stellen.
Ausbilder können sich registrieren und Verfügbarkeiten nach Zeitraum und Ort in Deutschland angeben.

Dateien
- app.py: Hauptanwendung
- requirements.txt: Python-Abhängigkeiten für Streamlit
- README.txt: diese Anleitung

Lokaler Start
1. Python installieren, empfohlen ab Python 3.10
2. Projektordner öffnen
3. Virtuelle Umgebung erstellen:
   python -m venv .venv
4. Umgebung aktivieren:
   Windows: .venv\Scripts\activate
   macOS/Linux: source .venv/bin/activate
5. Abhängigkeiten installieren:
   pip install -r requirements.txt
6. App starten:
   streamlit run app.py

GitHub Hosting mit Streamlit Community Cloud
1. Neues GitHub Repository erstellen
2. app.py, requirements.txt und README.txt in das Repository hochladen
3. Auf https://share.streamlit.io einloggen
4. Repository auswählen
5. Main file path auf app.py setzen
6. Deploy starten

Hinweis zum Prototyp
Die App speichert Daten aktuell nur während der laufenden Session.
Für einen produktiven Betrieb sollten ergänzt werden:
- Benutzerkonten und Rollenrechte
- Datenbank, z. B. PostgreSQL, Supabase oder SQLite
- Zahlungsfunktion / Checkout
- DSGVO-konforme Einwilligungen und Datenschutzerklärung
- Admin-Backend für Kursverwaltung
- E-Mail-Benachrichtigungen
- Kalenderintegration für Ausbilder-Verfügbarkeiten

Branding
Das Design ist an Clever College angelehnt: dunkelblau, goldene Akzente, klare Akademie-/Aviation-Anmutung.
