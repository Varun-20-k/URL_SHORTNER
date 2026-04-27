# URL Shortener

A simple and elegant Django-based URL shortener application that allows users to create custom short aliases for long URLs.

## Features

- **URL Shortening**: Convert long URLs into short, memorable aliases
- **Custom Aliases**: Create personalized short names for your URLs
- **Click Tracking**: Monitor how many times each shortened URL has been clicked
- **Timestamp Tracking**: Keep track of when each URL was created
- **Duplicate Prevention**: Prevent duplicate custom aliases

## Technology Stack

- **Backend**: Django 5.2.13
- **Database**: SQLite
- **Frontend**: HTML, Bootstrap (Bootstrap 5)
- **Python**: 3.x

## Project Structure

```
URL_shortner/
├── URL_shortner/          # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── myapp/                 # Main application
│   ├── models.py          # URL model definition
│   ├── views.py           # View logic
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Django admin configuration
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JS)
│   │   ├── style.css
│   │   └── bootstrap.min.css
│   ├── templates/         # HTML templates
│   │   └── index.html
│   └── tests.py           # Unit tests
├── manage.py              # Django management script
└── db.sqlite3             # SQLite database
```

## Installation

### Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd URL_shortner
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv myvenv
   
   # On Windows
   myvenv\Scripts\activate
   
   # On macOS/Linux
   source myvenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django asgiref sqlparse
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage

### Creating a Shortened URL

1. Navigate to the home page
2. Enter the long URL you want to shorten
3. Enter a custom alias (short name) for your URL
4. Click the submit button
5. Your shortened URL will be generated and displayed

### Example

- **Long URL**: `https://www.example.com/very/long/url/that/is/hard/to/share`
- **Custom Alias**: `mylink`
- **Shortened URL**: `http://localhost:8000/mylink`

## Database Schema

### URL Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer (Primary Key) | Auto-generated unique identifier |
| `longurl` | URLField | The original long URL |
| `custom_name` | CharField | Unique custom alias for the shortened URL |
| `date` | DateTimeField | Timestamp when the URL was created |
| `clicks` | Integer | Number of times the shortened URL has been accessed |

## API Endpoints

- `GET /` - Display the URL shortening form and results
- `POST /` - Submit a new URL to be shortened

## Error Handling

- **Duplicate Alias**: If you try to use an alias that already exists, you'll receive an error message
- **Invalid URL**: The application validates URLs before creating shortcuts

## Development

### Running Tests

```bash
python manage.py test
```

### Create a Superuser (for Django Admin)

```bash
python manage.py createsuperuser
```

Then access the admin panel at: `http://127.0.0.1:8000/admin/`

## Future Enhancements

- [ ] QR code generation for shortened URLs
- [ ] User authentication and personal URL management
- [ ] Analytics dashboard
- [ ] URL expiration dates
- [ ] Bulk URL shortening
- [ ] API endpoints for programmatic access
- [ ] Custom domain support

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, please reach out through GitHub issues.

---

**Note**: This is a development version. For production deployment, make sure to:
- Set `DEBUG = False` in `settings.py`
- Use a secure `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Use a production-grade database (PostgreSQL, MySQL, etc.)
- Set up proper CSRF and security settings
