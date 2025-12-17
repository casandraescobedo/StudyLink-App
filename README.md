# StudyLink

**StudyLink** is a mobile web application platform designed for students to find or create study groups for specific subjects, courses, or upcoming exams. The goal is to allow students to connect with others who share their academic goals, providing opportunities for better networking, improved grades, and socializing.

## 📋 Project Status
* **Target Release:** V1.0 - Initial Launch
* **Platform:** Web App

## 🚀 Key Features
The application focuses on the following core functionalities:

### Core Functionality (CRUD)
* **Create Sessions:** Students can create new study sessions including title, description, course tags, date, time, and location (physical or virtual).
* **Browse & Filter:** Users can browse existing sessions on a dashboard and filter by subject, date, or tags to find relevant groups.
* **Update Session Info:** Session creators can edit meeting details, times, notes, or resources to keep the group updated.



## 🛠 Technology Stack

### Front End
* **Languages:** HTML, CSS, JavaScript
* **Templating:** Django Templates (DTL)

### Back End
* **Framework:** Django
* **Authentication:** Standard Email/Username & Password
* **Database:** * Development: SQLite
  * Production: PostgreSQL

## ⚙️ Installation & Setup

To run this project locally, follow these steps:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/casandraescobedo/StudyLink-App.git](https://github.com/casandraescobedo/StudyLink-App.git)
    cd StudyLink-App
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

6.  **Access the App**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## 👥 Contributors

* **Casandra Escobedo**
* **Julissa Gonzalez**
* **Carlos Rivas**
* **Cynthia Marin**

---
*Generated based on Technical Design Document - V1.0*
