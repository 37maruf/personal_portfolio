# Personal Portfolio Website (Django)

Portfolio website of Md. Maruf Khan. Built with Python, Django, Bootstrap, HTML, CSS, JavaScript and SQLite.

## Pages
Home, About, Education, Experience, Skills, Projects, Resume, Contact.
Skills and projects show only a name first. Hover (or tap) a card to see the details.
The nav bar and contact page have Facebook, GitHub, LinkedIn, Gmail and WhatsApp links.

## Run it on your computer

```bash
# 1. (optional but good) make a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac / Linux

# 2. install
pip install -r requirements.txt

# 3. create the database (this also fills in your CV details)
python manage.py migrate

# 4. create YOUR admin account (choose your own strong password)
python manage.py createsuperuser

# 5. start
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Admin panel (private)
- Address: http://127.0.0.1:8000/control-room-mk/
- `/admin/` does not exist on purpose, so nobody can guess it.
- Only an active **superuser** can log in. Normal staff accounts are refused.
- To change the secret address, copy `.env.example` to `.env` and change `ADMIN_URL`.

### What you can do in the admin
| Section | What to do |
| --- | --- |
| Profile | Change name, bio, photo, links, and **upload your CV (PDF)** |
| Education | Add or edit SSC, HSC, BSc. Use "Order" to sort |
| Experience | Add jobs and internships (one point per line) |
| Skill categories | Add a category (like "Machine Learning") and add its skills below it |
| Projects | Add title, description, technologies, GitHub link. Live link is optional |
| Contact messages | Read messages visitors send you |

Tip: for a skill category icon, use a class from https://icons.getbootstrap.com (like `bi-cpu`).

## Contact messages by email (optional)
Messages always save in the admin. To also get them in Gmail, put your Gmail address and a
Gmail App Password in `.env` (see `.env.example`).

## Security built in
- Django CSRF protection on the contact form, plus a hidden spam-trap field
- Admin on a private URL, superuser only, 6 hour login session
- Secret key and settings come from `.env`, not from the code
- Before putting it online set `DJANGO_DEBUG=False`, a real `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS`

## Project structure
```
personal_portfolio/
  manage.py, requirements.txt, README.md
  portfolio_project/   settings, urls, admin_site (superuser-only), wsgi, asgi
  portfolio/
    models.py  views.py  urls.py  forms.py  admin.py
    migrations/        (0002 fills in your CV details)
    templates/portfolio/   base, home, about, education, experience, skills, projects, resume, contact
    static/portfolio/      css/, js/, images/, vendor/ (Bootstrap and icons, works offline)
```
