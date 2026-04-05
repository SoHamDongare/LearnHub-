# LearnHUb

A full-featured e-learning platform built with Django, where users can browse courses, manage their cart, complete purchases, and track their enrolled programs.

---

## Features

- **User Authentication** — Register, log in, and log out securely using Django's built-in auth system
- **Course Catalog** — Browse courses filtered by category (Development, Testing, Data Analytics, Data Science, DevOps)
- **Course Detail & Ratings** — View detailed course info and submit a star rating (one per user per course, with live average update)
- **Shopping Cart** — Session-based cart supporting add, remove, and quantity tracking
- **Checkout & Payment** — Order summary with a 15% discount applied at checkout, followed by a simulated payment flow
- **Enrollment Management** — Enroll in courses after successful payment; unenroll at any time from My Courses
- **User Profile** — View and edit profile details including name, contact, gender, and profile picture
- **Admin Panel** — Django admin for managing courses, users, enrollments, and ratings

---

## Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Django 5.2              |
| Database  | SQLite3 (default)       |
| Frontend  | Django Templates + HTML |
| Auth      | Django built-in auth    |
| Media     | Django media file handling |

---

## Project Structure

```
LearnHUb/
├── AuthProject/          # Project settings and root URL config
├── authapp/              # User registration, login, logout, home
├── courseapp/            # Course model, detail view, rating system
├── cartapp/              # Session-based shopping cart
├── checkout/             # Checkout flow, payment, and enrollment records
├── mycourseapp/          # My courses, enroll, unenroll
├── profileapp/           # User profile view and edit
├── templates/            # HTML templates
├── manage.py
└── db.sqlite3
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/LearnHUb.git
   cd LearnHUb
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

---

## URL Routes

| URL                        | Description                        |
|----------------------------|------------------------------------|
| `/`                        | Home page with course listings     |
| `/register`                | User registration                  |
| `/login`                   | User login                         |
| `/logout`                  | User logout                        |
| `/course`                  | Full course catalog                |
| `/detail/<id>`             | Course detail and rating           |
| `/cart/`                   | View cart                          |
| `/cart/add/<id>/`          | Add course to cart                 |
| `/cart/remove/<id>/`       | Remove course from cart            |
| `/checkout`                | Checkout with discount summary     |
| `/payment`                 | Payment page                       |
| `/success`                 | Payment success and enrollment     |
| `/mycourses/`              | View enrolled courses              |
| `/enroll/<id>/`            | Enroll in a course                 |
| `/unenroll/<id>/`          | Unenroll from a course             |
| `/profile/`                | View user profile                  |
| `/edit/`                   | Edit user profile                  |
| `/about`                   | About page                         |
| `/contact`                 | Contact page                       |
| `/admin/`                  | Django admin panel                 |

---

## Adding Courses

Courses are managed through the Django admin panel.

1. Go to `/admin/` and log in with your superuser credentials
2. Navigate to **Courseapp → Courses**
3. Add a course with a name, description, price, duration, category, and image

---

## Notes

- The payment flow is simulated (dummy payment) and does not process real transactions
- Media files (course images, profile pictures) are stored in the `media/` directory
- The `SECRET_KEY` in `settings.py` must be replaced with a secure value before deploying to production
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` for any production deployment

---

## License

This project is intended for educational purposes.

## Author

Soham Dongare  
Aspiring Full Stack Developer (Python)
<p>
  Connect with me:
  <a href="https://www.linkedin.com/in/soham-dongare/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin" />
  </a>
</p>