# ATS Resume Checker

Simple Flask app that analyzes PDF resumes for ATS compatibility using Google GenAI.

Setup

1. Create and activate a virtual environment:

```powershell
C:/path/to/python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a local `.env` file (NOT committed) with your API key:

```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

4. Run the app:

```powershell
.\.venv\Scripts\python.exe app.py
```

Notes

- Do NOT commit `.env` or any API keys.
- If you want deterministic outputs, set the model temperature to `0.0` in `app.py`.

GitHub

- To push to a new GitHub repo, create a remote repository and then:

```powershell
git remote add origin https://github.com/yourname/yourrepo.git
git branch -M main
git push -u origin main
```
