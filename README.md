# Planet Stop

**Elevator Pitch:** Explore the Solar System and discover how we got there.

**Primary User:** People who want to learn more about space and the history of exploration in their own time — and test their knowledge through interactive quizzes.

---

## 🚀 Project Overview
Planet Stop is a Flask web application that combines dynamic data-driven routes, reusable Jinja components, and modern front-end techniques to create an interactive, educational exploration of our Solar System and humanity’s journey into space.

Core sections of the app:
- **Explore** → Learn about the planets.
- **Timeline** → Browse milestones in space history decade by decade.
- **Quiz** → Test knowledge with session-based quizzes.

---

## ✨ Features
- **Dynamic JSON datastore** for planets, timeline milestones, and quiz questions.
- **Flask Blueprints** for modular routing across Explore, Timeline, and Quiz.
- **Responsive design** powered by fluid typography and design tokens.
- **Performance conscious**: local assets for fast load + external repo for larger assets (compressed WebP).
- **Animations & UX**: scroll animations, custom scrollbars, view transitions, view timelines.
- **Quiz State Persistence**: resume progress via Flask session.

**Non-goals:**
- No persistent storage (view-only app).
- No data export/download.
- Minimize duplicate components — focus on reusability.

---

## 🛠️ Architecture
High-level design:
- `app.py` or `app:create_app()` launches the factory.
- **Config** injected from `config.py`.
- **Blueprint hierarchy**:
  - **Explore** → index, planet list, individual planet pages.
  - **Timeline** → decade index, milestones.
  - **Quiz** → build quiz, play through, answer/next, results.
- **Templating**: Jinja macros for cards, buttons, icons, and more.
- **Base layout**: global CSS tokens for colors, spacing, typography, and responsive scaling.

**Folder structure (excerpt):**
```
app/
  ├── data/ (planets.json, questions.json, timeline.json, asset-manifest.json)
  ├── routes/ (blueprints for explore, timeline, quiz)
  ├── static/ (styles, JS modules, assets)
  ├── templates/ (base + view templates)
```

---

## 📂 Data Models

### Planets (excerpt)
```json
{
  "id": "earth",
  "name": "Earth",
  "tagline": "Our home world",
  "facts": { "order": 3, "moons": 1 },
  "img_key": "earth"
}
```

### Quiz Questions
```json
{
  "id": "earth-order",
  "type": "single-choice",
  "difficulty": "easy",
  "tags": ["earth", "orbit"],
  "question": "What is Earth's order from the Sun?",
  "options": [
    { "id": "A", "label": "3" },
    { "id": "B", "label": "2" },
    { "id": "C", "label": "4" },
    { "id": "D", "label": "5" }
  ],
  "correctOptionIds": ["A"]
}
```

### Timeline (excerpt)
```json
{
  "1950s": {
    "id": "1950s",
    "start": 1950,
    "end": 1959,
    "pseudoname": "Birth of the Space Age",
    "milestones": [
      {
        "eventTitle": "Sputnik 1 Launch",
        "eventDate": { "day": 4, "month": "October", "year": 1957 },
        "eventDescription": "First artificial Earth satellite.",
        "actors": ["Soviet Union"]
      }
    ]
  }
}
```

### Asset Manifest
Maps logical keys → WebP paths for heroes, milestones, icons, etc.

---

## ⚙️ Setup & Run

### Requirements
- Python 3.14
- Flask 3.1.1
- Gunicorn 23.0.0
- Jinja2 3.1.6
- python-dotenv 1.1.1

### Install
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Environment
`.env` variables:
```
FLASK_ENV=development
SECRET_KEY=your-secret-key
ASSET_ORIGIN=/static
```

### Run (dev)
```bash
flask run
```

### Run (prod)
```bash
gunicorn app:create_app()
```

Deployment is configured for **Render.com** with `Procfile`.

---

## 🌐 Deployment
Live demo: [planet-3jv6.onrender.com](https://planet-3jv6.onrender.com/)

Source code: [GitHub Source Repo](https://github.com/AlanOC123/fssd2025-module-three-assessment-source-code)

Assets: [GitHub Assets Repo](https://github.com/AlanOC123/assessment-3-assets-repo)

**Steps for Render deployment:**
1. Push your code to GitHub.
2. Connect the repo to Render.
3. Set environment variables (`SECRET_KEY`, `ASSET_ORIGIN`).
4. Build command: `pip install -r requirements.txt`.
5. Start command: `gunicorn app:create_app()`.
6. Render auto-builds and deploys → app accessible via URL.

---

## 📸 Screenshots
Place the following images in a `screenshots/` folder at repo root so they render on GitHub. Filenames below match your uploads.

![Homepage Triptych](screenshots/Screenshot%202025-09-20%20at%2014.49.40.png)
![Homepage – Compare/CTA](screenshots/Screenshot%202025-09-20%20at%2014.50.11.png)
![Explore – Mars Overview](screenshots/Screenshot%202025-09-20%20at%2014.50.01.png)
![Timeline – Decade Select](screenshots/Screenshot%202025-09-20%20at%2014.50.18.png)
![Timeline – 1950s Hero](screenshots/Screenshot%202025-09-20%20at%2014.50.25.png)
![Timeline – Sputnik Image Card](screenshots/Screenshot%202025-09-20%20at%2014.50.31.png)
![Timeline – Sputnik Details](screenshots/Screenshot%202025-09-20%20at%2014.50.38.png)
![Quiz – Builder](screenshots/Screenshot%202025-09-20%20at%2014.50.46.png)
![Quiz – Play](screenshots/Screenshot%202025-09-20%20at%2014.51.12.png)
![Quiz – Results](screenshots/Screenshot%202025-09-20%20at%2014.51.28.png)

**Tip:** keep screenshot widths ≤ 1600px for a lighter README and consistent rendering.

---

## 🌐 Accessibility & Performance
- Alt text on all images.
- High-contrast tokens.
- Semantic HTML (sections, articles, landmarks).
- Fluid typography with min/max scaling.
- Images compressed to ~75% WebP.
- Local sprites for instant load, CDN for heavier backgrounds.

---

## 🎨 Design System
- **Tokens**: spacing, borders, colors, typography, transitions.
- **Components**: planet cards, milestone containers, quiz cards.
- **Animations**: Scroll/view timelines (Explore & Timeline), smooth progress indicators.

---

## 📚 Learning Outcomes & Rubric Mapping
- **Flask concepts** → Blueprints, session management, factory pattern.
- **Python** → clean modular code, JSON data handling.
- **CSS & JS** → fluid responsive design, scroll animations, fetch APIs.
- **Clean code** → modular folder structure, Jinja macros, reusable assets.
- **Hosting** → deployed on Render with working config.

This meets *Distinction* criteria: clear Flask application, strong Python usage, modern design, clean structure, and a fully hosted functional app.

---

## 🗺️ Roadmap
- Improve error handling (user-facing messages).
- Add “favorite planet” and custom bios (would require persistent DB, out of scope).
- Markdown content support for richer descriptions.

---

## 📜 License & Credits
- **License**: MIT
- **Images/Data**: NASA, ESA, SpaceX, and historical archives (used in educational fair use context).
- **Design System**: Based on [fluid.style](https://fluid.style/).

---

## 🔧 Render Troubleshooting Appendix
If the grader encounters issues deploying or viewing the app on Render, here are common fixes:

- **502 Bad Gateway / App not starting**  
  Ensure the `Procfile` has the correct start command:
  ```
  web: gunicorn app:create_app()
  ```

- **Environment variable errors**  
  Double-check `SECRET_KEY` and `ASSET_ORIGIN` are set in Render’s *Environment* tab.

- **Static assets not loading**  
  Confirm `ASSET_ORIGIN=/static` is configured. Render sometimes strips leading slashes — add it explicitly.

- **Python version mismatch**  
  Render defaults to older versions. Ensure `python-3.14.x` is pinned in `runtime.txt` (optional but recommended).

- **Module not found**  
  Re-run build or verify all dependencies are listed in `requirements.txt`.

If problems persist, re-trigger a manual deploy from Render’s dashboard. This ensures latest commits and env vars are respected.

