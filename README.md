# Odds Blueprint Scanner (Europe / Bet365)

An automated system that scans daily European football matches (Soccerway Europe / Bet365 odds), applies custom odds rules, and outputs only the fixtures that match your blueprint conditions.

## Features

- Automatic midnight scraping from **Soccerway Europe (Bet365 odds)**
- Full **home / draw / away** odds per match
- Fallback to **manual fixtures** if scraper fails
- Flask backend + React frontend
- GitHub Actions automation (no Windows scheduler, no manual feed)

## Project Structure

See `backend/`, `frontend/`, and `.github/workflows/auto-fetch.yml` for full layout.

## Backend Setup (Local)

```bash
cd backend
pip install -r requirements.txt
python app.py
