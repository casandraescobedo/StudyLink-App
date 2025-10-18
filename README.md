# StudyLink: Collaborative Study Group Platform

 # Project Overview

StudyLink is a mobile web application designed to connect students by facilitating the creation and discovery of collaborative study groups for specific subjects, courses, or upcoming exams. Our mission is to combat academic isolation and provide new opportunities for networking, achieving better grades, and making new friends within the academic community.

# Team Members

Casandra Escobedo
Julissa Gonzalez
Carlos Rivas
Cynthia Marin

# Technology Stack

Backend / API: Django (Python)
Frontend: HTML5, CSS, JavaScript
Styling: Custom CSS / Tailwind (TBD)
Version Control: Git / GitHub

# Agile Planning: V1.0 - Initial Launch

We are organizing development using one-week Sprints, focusing on delivering core functionality (CRUD operations) first.

# Product Backlog (Prioritized User Stories)

Here are the key features prioritized for development:

# High Priority:

Create Session: User can organize a study group with all necessary details (time, location, capacity).

Browse/Filter Sessions: User can find a relevant group to join via search and filters.

Basic User Auth: User can securely log in and register.

Join/Leave Session: User can participate in a group and manage their membership.

# Medium Priority:
5. Update Session Details: Creator can keep the group updated with edits and new resources.
6. Session Lifecycle: Sessions are automatically or manually marked as "Past" after completion.
7. Share and Save Notes: User can share notes and save/like resources for later reference (Bonus Feature).

# Proposed Sprint Structure

# Sprint 1: Foundation & Creation

Goal: Establish the backend data structure, implement user authentication, and enable session creation.

Activities:
Setup initial Django Models (User, Session, Group Membership).
Implement User Registration and Login endpoints and frontend forms.
Develop the "Create Session" form and backend logic.
Implement the logic to automatically flag sessions that have passed their meeting time.

Definition of Done (DOD): Users can log in and successfully create a new study session that is properly timestamped in the database.

# Sprint 2: Reading & Joining

Goal: Implement the discovery and joining functionalities, allowing users to interact with existing sessions.

Activities:
Develop the Main Dashboard view (displaying all upcoming session cards).
Implement Search and Filtering functionality (by subject, date, and tag).
Develop the "Join Session" and "Leave Session" core logic.
Develop the form and logic for creators to edit their sessions.

Definition of Done (DOD): Users can view the dashboard, apply filters, and successfully join any available session.
