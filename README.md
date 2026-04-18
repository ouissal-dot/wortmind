# WortMind 🧠🇩🇪

A German–Arabic vocabulary flashcard app built with Streamlit. Practice words using a Leitner-style box system — flip cards to reveal the Arabic meaning and an example sentence.

---

## Features

- **Box selector** — choose your study box with clickable cards
- **Flip flashcards** — see the German word first, tap to reveal the Arabic translation and example sentence
- **Add new words** — add German words with their Arabic meaning and an example sentence
- **Persistent storage** — vocabulary is saved locally via JSON

---

## Project Structure

```
wortmind/
├── app.py                  # Main Streamlit app
├── utils/
│   └── storage.py          # Load and save vocabulary data
├── data/
│   └── words.json          # Vocabulary data (auto-created)
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/wortmind.git
cd wortmind
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## Requirements

```
streamlit==1.45.0
```

---

## Deploy on Streamlit Community Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **New app** → select this repo → set `app.py` as the main file
5. Click **Deploy**

> ⚠️ Note: the default local JSON storage resets on every cloud restart. For persistent cloud storage, replace `utils/storage.py` with a Supabase or Firebase integration.

---

## How It Works

Words are organized into **boxes** (like the Leitner spaced repetition system). Each box contains a list of word objects:

```json
{
  "Box 1": [
    {
      "de": "der Hund",
      "ar": "الكلب",
      "sentence": "Der Hund läuft schnell im Park."
    }
  ]
}
```

---

## Built With

- [Streamlit](https://streamlit.io) — UI framework
- Python 3.14

---

## License

MIT
