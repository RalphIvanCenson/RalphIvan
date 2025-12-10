# Django Portfolio

A modern, responsive Django-based portfolio website to showcase your projects, skills, and professional information.

## Features

- 🎨 **Modern Design**: Beautiful, responsive UI built with Bootstrap 5
- 📱 **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- 🖼️ **Portfolio Management**: Easy-to-use admin interface to manage projects, skills, and about information
- 🏢 **Project Showcase**: Display your projects with images, descriptions, technologies, and links
- 🛠️ **Skills Section**: Organize and display your technical skills with proficiency levels
- 👤 **About Section**: Present your professional information, contact details, and social links
- 📧 **Contact Information**: Display email, phone, location, and social media profiles
- 🔍 **SEO Friendly**: Built with best practices for search engine optimization
- ⚡ **Fast & Lightweight**: Optimized performance for quick loading times

## Tech Stack

- **Backend**: Django 6.0
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (default, easily switchable to PostgreSQL)
- **Image Processing**: Pillow
- **Server**: Gunicorn (for production)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-portfolio.git
   cd django-portfolio
   ```

2. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and update SECRET_KEY and other settings
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The site will be available at `http://localhost:8000`

9. **Access the admin panel**
   - Navigate to `http://localhost:8000/admin`
   - Log in with your superuser credentials
   - Add your portfolio content (projects, skills, about information)

## Project Structure

```
django-portfolio/
├── Ralph/                      # Main project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   ├── asgi.py                # ASGI configuration
│   └── wsgi.py                # WSGI configuration
├── Ivan/                       # Portfolio app
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # App URL routes
│   ├── admin.py               # Admin configuration
│   ├── templates/
│   │   └── portfolio/
│   │       ├── index.html
│   │       ├── projects_list.html
│   │       ├── project_detail.html
│   │       └── skills.html
│   └── static/
│       └── portfolio/
│           ├── css/
│           └── js/
├── templates/
│   └── base.html              # Base template
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## Models

### Project
- **Title**: Project name
- **Description**: Detailed project description
- **Image**: Project screenshot/image
- **Link**: Live project URL
- **GitHub Link**: Repository URL
- **Technologies**: Technologies used (comma-separated)
- **Date Created**: Project creation date
- **Order**: Display order in portfolio

### Skill
- **Name**: Skill name
- **Category**: Skill category (e.g., Frontend, Backend, Tools)
- **Level**: Proficiency level (Beginner, Intermediate, Advanced, Expert)
- **Proficiency Percentage**: Skill proficiency (0-100%)
- **Order**: Display order

### About
- **Title**: Section title
- **Bio**: Your biography
- **Profile Image**: Your profile picture
- **Email**: Contact email
- **Phone**: Contact phone number
- **Location**: Your location
- **Resume Link**: Link to your resume
- **GitHub Profile**: GitHub profile URL
- **LinkedIn Profile**: LinkedIn profile URL
- **Twitter Profile**: Twitter profile URL

## Usage

### Adding Projects

1. Go to `/admin`
2. Click on "Projects"
3. Click "Add Project"
4. Fill in the project details
5. Upload a project image
6. Save and publish

### Adding Skills

1. Go to `/admin`
2. Click on "Skills"
3. Click "Add Skill"
4. Fill in skill details
5. Set proficiency percentage
6. Save and publish

### Updating About Section

1. Go to `/admin`
2. Click on "About"
3. Click on the existing entry (or create one if it doesn't exist)
4. Update your information
5. Save

## Customization

### Changing Colors

Edit `static/css/style.css` and modify the CSS variables:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f093fb;
    --text-dark: #2d3748;
    --text-light: #718096;
    --border-color: #e2e8f0;
}
```

### Modifying Templates

Edit the HTML templates in `Ivan/templates/portfolio/` to customize the layout and styling.

## Deployment

### Using Heroku

1. Install Heroku CLI
2. Create a `Procfile`:
   ```
   web: gunicorn Ralph.wsgi
   ```

3. Create a `runtime.txt`:
   ```
   python-3.11.0
   ```

4. Update `settings.py` for production
5. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Using DigitalOcean/VPS

1. Install Python, pip, and virtualenv
2. Clone the repository
3. Create virtual environment and install dependencies
4. Configure Gunicorn and Nginx
5. Use Supervisor to manage the application
6. Set up SSL with Let's Encrypt

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please create an issue in the GitHub repository.

## Roadmap

- [ ] Add blog functionality
- [ ] Implement contact form with email notifications
- [ ] Add testimonials section
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Analytics integration
- [ ] SEO optimization

## Credits

- Built with [Django](https://www.djangoproject.com/)
- Styled with [Bootstrap 5](https://getbootstrap.com/)
- Icons from [Font Awesome](https://fontawesome.com/)

---

**Made with ❤️ by Your Name**
