# eyyyy

ticketing_system/
├── manage.py
├── requirements.txt
├── ticketing_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── context_processors/
│   │     └── theme.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── register.html
│           ├── profile.html
│           ├── password_reset.html
│           └── password_change.html
├── tickets/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── tickets/
│           ├── ticket_list.html
│           ├── ticket_detail.html
│           ├── ticket_create.html
│           └── ticket_edit.html
├── chat/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── chat/
│           └── chat_room.html
├── cms/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── cms/
│           └── dashboard.html
└── logs/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── logs/
            ├── email_logs.html
            ├── notification_logs.html
            ├── error_logs.html
            └── login_history.html
