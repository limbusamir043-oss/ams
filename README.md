# Assignment Management System

A Django-based web application for managing assignments between teachers and students. Teachers can create, edit, and delete assignments, while students can view their assigned tasks.

## Features

- **User Authentication**: Secure login system for teachers and students
- **Role-Based Access**: Different dashboards and permissions for teachers and students
- **Assignment Management**:
  - Teachers can create new assignments
  - Teachers can edit existing assignments
  - Teachers can delete assignments
  - Students can view all assignments
- **Assignment Details**: Each assignment includes:
  - Title
  - Description
  - Due date
  - Total marks
  - Creation timestamp

## Tech Stack

- **Backend**: Django (Python web framework)
- **Database**: SQLite3
- **Frontend**: HTML, CSS
- **Authentication**: Django built-in authentication system

## Project Structure

```
AssignmentManagementSystem/
├── AssignmentManagementSystem/    # Project configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # URL routing
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
├── home/                          # Main application
│   ├── models.py                  # Database models (UserProfile, Assignment)
│   ├── views.py                   # View logic
│   ├── forms.py                   # Django forms
│   ├── urls.py                    # App URL patterns
│   └── migrations/                # Database migrations
├── templates/                     # HTML templates
│   ├── login.html                 # Login page
│   ├── teacher.html               # Teacher dashboard
│   ├── student.html               # Student dashboard
│   ├── assignment_list.html       # List all assignments
│   ├── create_assignment.html     # Create new assignment
│   ├── edit_assignment.html       # Edit existing assignment
│   ├── delete_assignment.html     # Delete confirmation
│   └── student_assignment.html    # Student view of assignments
├── static/                        # Static files
│   └── style.css                  # Stylesheet
├── manage.py                      # Django management script
└── db.sqlite3                     # SQLite database
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/limbusamir043-oss/ams.git
   cd ams
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (admin account)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Teachers
1. Log in with your teacher account
2. Go to the teacher dashboard
3. Create new assignments with title, description, due date, and marks
4. Edit or delete existing assignments as needed

### For Students
1. Log in with your student account
2. Go to the student dashboard
3. View all assignments assigned by teachers
4. Check assignment details including due dates and marks

## Database Models

### UserProfile
- Extends Django's User model
- Stores user role (teacher/student)

### Assignment
- Title: Assignment name
- Description: Detailed assignment description
- Due Date: Assignment deadline
- Total Marks: Maximum marks for the assignment
- Teacher: Foreign key to the teacher who created it
- Created At: Timestamp when assignment was created

## API Endpoints

- `/login/` - User login
- `/teacher/` - Teacher dashboard
- `/student/` - Student dashboard
- `/assignment/` - List all assignments
- `/assignment/create/` - Create new assignment (teacher only)
- `/assignment/<id>/edit/` - Edit assignment (teacher only)
- `/assignment/<id>/delete/` - Delete assignment (teacher only)

## Future Enhancements

- Submission tracking for students
- Grade/marks assignment for submissions
- Notification system
- REST API endpoints
- Advanced filtering and search
- Bulk assignment creation
- Assignment categories/subjects

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the GitHub repository.
