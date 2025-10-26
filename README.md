# Car Bazaar – Django Project

## Project Overview
Car Bazaar is a personal web application built with **Python (Django)** that allows users to create and manage car sale advertisements. Users can register, log in, post cars for sale, edit or delete listings, and browse other cars available for purchase. The platform implements role-based permissions, messaging, and favorite listings, making it a fully functional and user-friendly car marketplace.

---

## Features
- **User Authentication:** Register, log in, and manage account details.  
- **Car Listings:** Create, update, and delete car advertisements.  
- **Role-Based Permissions:**  
  - **Authors:** Can manage their own listings.  
  - **Staff:** Limited management privileges.  
  - **Superusers:** Full access to all listings and management tools.  
- **Favorites:** Users can save favorite cars.  
- **Messaging:** Users can contact listing authors.  
- **Reports:** Users can report inappropriate listings.  

---

## Technology Stack
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (custom design, no frameworks)  
- **Database:** SQLite (default Django DB)  
- **Authentication & Permissions:** Django built-in user model with custom roles  

---

## Project Structure
- **Apps:**  
  - `car` – Handles car listings and related functionality  
  - `owner` – Handles user accounts, favorites, messages, and reports  
- **Templates:** HTML templates for each page  
- **Static:** CSS and images  
- **URLs & Views:** RESTful routing for all features  

---

## Learning Outcomes
- Gained experience building a full-stack Django web application.  
- Implemented role-based access control and user management.  
- Learned to integrate multiple features like messaging, favorites, and reporting.  
- Practiced clean, maintainable code structure and Django best practices.  

---

## Usage
1. Clone the repository:  
   ```bash
   git clone https://github.com/GalinPatazov/Car-Bazaar.git
