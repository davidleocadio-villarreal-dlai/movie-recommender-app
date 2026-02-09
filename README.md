# Movie Recommender Web App

A simple web app that uses OpenAI's API and Pydantic validation to recommend movies.

## Setup & Run

1. Make sure you have your `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-...
   ```

2. Install dependencies and run:
   ```bash
   uv pip install -r requirements.txt && uv run python app.py
   ```

3. Open your browser to: http://localhost:5000

## Files

- `app.py` - Flask web server
- `models.py` - Pydantic model for movie recommendations
- `templates/index.html` - Web interface
- `requirements.txt` - Python dependencies
- `.env` - Your API key (create this file)
