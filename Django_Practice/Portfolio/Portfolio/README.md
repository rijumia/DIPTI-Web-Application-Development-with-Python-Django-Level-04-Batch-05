# Name_ID_Portfolio

A Django portfolio project per the assignment spec.

## Steps

a) Create new Django project & app (already done in this archive).

b) Run migrations:
```bash
python manage.py migrate
```

c) Create super user (username: admin, password: 1234):
```bash
python manage.py createsuperuser --username admin --email admin@example.com
# Type password: 1234 (twice)
```

d) Register models: already registered in `Portfolio/admin.py`.

e) Run server:
```bash
python manage.py runserver
```

## URLs
- Home: `/`
- Register: `/register/`
- Login: `/login/`
- Dashboard (admin updates profile): `/dashboard/`
- Resume: `/resume/<username>/`
- Contact: `/contact/`
- Admin: `/admin/`

## Notes
- A `Profile` is auto-created for each new `User` via signals.
- Media uploads enabled for profile photos and project images (configure MEDIA_ROOT).
