# StudyLink

[cite_start]**StudyLink** is a mobile web application platform designed for students to find or create study groups for specific subjects, courses, or upcoming exams[cite: 3]. [cite_start]The goal is to allow students to connect with others who share their academic goals, providing opportunities for better networking, improved grades, and socializing[cite: 3].

## 📋 Project Status
* [cite_start]**Target Release:** V1.0 - Initial Launch [cite: 2]
* [cite_start]**Platform:** Mobile Web App [cite: 1]

## 🚀 Key Features
[cite_start]The application focuses on the following core functionalities (CRUD)[cite: 12]:

### Core Functionality
* [cite_start]**Create Sessions:** Students can create new study sessions including title, description, course tags, date, time, and location (physical or virtual)[cite: 14, 15, 16].
* [cite_start]**Browse & Filter:** Users can browse existing sessions on a dashboard and filter by subject, date, or tags to find relevant groups[cite: 22, 23].
* **Session Management:**
    * [cite_start]Creators can update meeting details, notes, or resources[cite: 26].
    * [cite_start]The system automatically marks sessions as "Past" after the meeting date[cite: 30].
* **Social Interaction:**
    * [cite_start]Users can join sessions (public, private, or campus-only)[cite: 18].
    * [cite_start]**Bonus:** Members can like or save shared notes and summaries for future reference[cite: 31, 32].

## 🛠 Technology Stack

### Back End
* [cite_start]**Framework:** Django [cite: 8]
* [cite_start]**Authentication:** `django.contrib.auth` (Email/Username & Password) [cite: 36]
* **Database:**
    * [cite_start]**Development:** SQLite [cite: 36]
    * [cite_start]**Production:** PostgreSQL [cite: 36]

### Front End
* [cite_start]**Languages:** HTML, CSS, JavaScript [cite: 7]
* [cite_start]**Templating:** Django Templates (DTL) [cite: 36]

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

* [cite_start]**Casandra Escobedo** [cite: 2]
* [cite_start]**Julissa Gonzalez** [cite: 2]
* [cite_start]**Carlos Rivas** [cite: 2]
* [cite_start]**Cynthia Marin** [cite: 2]

## 🔮 Future Work (V2.0)
[cite_start]The following features were considered but descoped for the V1.0 launch[cite: 38]:
* [cite_start]**Capacity Limits:** Implementing strict maximum capacity logic for groups[cite: 39].
* [cite_start]**Advanced Maps:** Interactive map integration for physical locations (currently handled via text/links)[cite: 36].
* [cite_start]**Social Login:** OAuth integration for Google/Facebook login[cite: 36].

---
*Generated based on Technical Design Document - V1.0*
