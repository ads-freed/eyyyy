
# ticketing_system/

an example of a complete Django‑based ticketing system


## Project Structure

```javascript
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

```

## Deployment(Ubuntu Server)
#### Installation
## 1. System Preparation
#### 1.1. Update and Install Required Packages
Open a terminal and update your package lists. Then install Python, pip, virtual environment tools, Git, and Nginx:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git nginx -y
```

## 2. Application Setup
#### 2.1. Clone Your Repository
Clone your project repository into your desired directory:
```bash
git clone https://github.com/ads-freed/eyyyy /var/www/eyyyy
cd /var/www/eyyyy
```

#### 2.2. Create and Activate Virtual Environment
Set up a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2.3. Install Dependencies
Within your virtual environment, install your project dependencies:
```bash
pip install -r requirements.txt
```

#### 2.4. Configure Django Settings
- DEBUG: Ensure `DEBUG = False` in your `ticketing_system/settings.py`.
- ALLOWED_HOSTS: Set `ALLOWED_HOSTS` to include your server domain/IP.
- Static & Media Files: Verify paths for static and media files.
- Database: Confirm your production database settings (SQLite is fine for testing but consider PostgreSQL or MySQL in production).
  
## 3. Database and Static Files
#### 3.1. Apply Migrations and Create Superuser
Run Django migrations and create an admin account:
```bash
python manage.py migrate
python manage.py createsuperuser
```

#### 3.2. Collect Static Files
Collect static files to the directory defined in your settings:
```bash
python manage.py collectstatic
```

## 4. Gunicorn Configuration
#### 4.1. Install Gunicorn
Inside your virtual environment, install Gunicorn:
```bash
pip install gunicorn
```

#### 4.2. Create a Systemd Service File for Gunicorn
Create a Gunicorn systemd service file at `/etc/systemd/system/gunicorn.service`:(ini)

```
[Unit]
Description=gunicorn daemon for eyyyy
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/eyyyy
ExecStart=/var/www/eyyyy/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/eyyyy/gunicorn.sock ticketing_system.wsgi:application

[Install]
WantedBy=multi-user.target
```
Note:
- Adjust the `User` and `Group` if needed.
- The `WorkingDirectory` should point to your project’s root.
- The socket file (`gunicorn.sock`) is used for communication between Gunicorn and Nginx.

#### 4.3. Start and Enable Gunicorn Service
Reload systemd to register the new service, then start and enable it:
```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```
Check the status to ensure it’s running:
```bash
sudo systemctl status gunicorn
```

## 5. Nginx Configuration
#### 5.1. Create an Nginx Site Configuration File
Create a new file (e.g., `/etc/nginx/sites-available/eyyyy`):
```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /var/www/eyyyy;
    }

    location /media/ {
        root /var/www/eyyyy;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/eyyyy/gunicorn.sock;
    }
}
```
Note: Replace `your_domain_or_IP` with your actual domain name or server IP.

#### 5.2. Enable the Nginx Site
Create a symbolic link to enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/eyyyy /etc/nginx/sites-enabled
```

#### 5.3. Test and Reload Nginx
```
Test the configuration and reload Nginx:
```bash
sudo nginx -t
sudo systemctl restart nginx
```

## 6. Firewall and Security
#### 6.1. Configure UFW (if applicable)
If you’re using UFW, allow Nginx Full:
```bash
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

#### 6.2. Secure Your Application
SSL: Use Let’s Encrypt to secure your site with SSL. For example, install Certbot and run:
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your_domain_or_IP
```

Django Security: Ensure you have proper settings for production:

- Set `DEBUG = False`.
- Use a strong `SECRET_KEY`.
- Configure proper logging and error reporting.
## 7. Additional Deployment Considerations
#### 7.1. Environment Variables
Use environment variables or a configuration management tool (like [django-environ]_(https://django-environ.readthedocs.io/)) to store sensitive data (e.g., `SECRET_KEY`, database credentials).

#### 7.2. Monitoring and Logging
- Gunicorn Logs: Configure Gunicorn logging options as needed.
- Django Logs: Adjust logging settings in your settings.py to log errors and warnings.
- System Monitoring: Consider tools such as Supervisor, systemd timers, or third-party monitoring services to keep track of your application’s performance and uptime.
  
#### 7.3. Regular Updates and Backups
- Updates: Regularly update your dependencies and Django version.
- Backups: Implement a backup strategy for your database and static/media files.
  
#### 7.4. Scaling
For higher loads, consider:

- Increasing Gunicorn workers.
- Using a dedicated database server.
- Implementing caching (e.g., with Redis or Memcached).
  
## 8. Final Verification
#### 1. Access the Application:
Visit your domain or server IP in a web browser to ensure the site is live.

#### 2. Check Logs:
Monitor Gunicorn and Nginx logs to verify that there are no errors:

```bash
sudo journalctl -u gunicorn
sudo tail -f /var/log/nginx/error.log
```
#### 3. Test Functionality:
Log in as an admin and perform test actions (ticket creation, chat messages, etc.) to verify all integrated features work correctly.






























## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Appendix

Any additional information goes here


## Authors

- [@octokatherine](https://www.github.com/octokatherine)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Demo

Insert gif or link to demo


## Documentation

[Documentation](https://linktodocumentation)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Feedback

If you have any feedback, please reach out to us at fake@fake.com


## 🚀 About Me
I'm a full stack developer...


# Hi, I'm Katherine! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


## Other Common Github Profile Sections
👩‍💻 I'm currently working on...

🧠 I'm currently learning...

👯‍♀️ I'm looking to collaborate on...

🤔 I'm looking for help with...

💬 Ask me about...

📫 How to reach me...

😄 Pronouns...

⚡️ Fun fact...


## 🛠 Skills
Javascript, HTML, CSS...


    
## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?


## License

[MIT](https://choosealicense.com/licenses/mit/)


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


## Optimizations

What optimizations did you make in your code? E.g. refactors, performance improvements, accessibility


## Related

Here are some related projects

[Awesome README](https://github.com/matiassingers/awesome-readme)


## Roadmap

- Additional browser support

- Add more integrations


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Support

For support, email fake@fake.com or join our Slack channel.


## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express


## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## Used By

This project is used by the following companies:

- Company 1
- Company 2

