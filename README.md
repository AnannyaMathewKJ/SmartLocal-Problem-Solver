# SmartLocal: Cloud-Native Civic Issue Reporting System 🚨📍

**SmartLocal** is a web-based platform designed to bridge the communication gap between citizens and local authorities. It allows users to report infrastructure or safety issues in real-time with precise geolocation data and photographic evidence.

---

## 🚀 Key Features

* **Smart Reporting:** Capture and upload photos of civic issues (waste, water, safety) directly to the cloud.
* **Real-time Geolocation:** Automatic coordinate tracking using the Browser Geolocation API.
* **Safety Broadcasts:** Dedicated emergency alert system for high-priority community hazards.
* **Cloud-Native Storage:** Stateless architecture using Cloudinary for media and Neon for data.
* **Admin Dashboard:** Specialized views for staff to manage, track, and resolve reported incidents.
* **Responsive UI:** Fully optimized for mobile and desktop using Bootstrap 5.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python / Django |
| **Database** | Neon Serverless PostgreSQL |
| **Media Storage** | Cloudinary CDN |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5 |
| **Authentication** | Django Auth System |

---

## 🏗️ Architecture Overview

SmartLocal follows the **MVT (Model-View-Template)** pattern and utilizes a stateless cloud architecture:
1.  **Client:** Captures image and location via browser APIs.
2.  **Server (Django):** Processes logic and authenticates users.
3.  **Media (Cloudinary):** Stores photographic evidence to keep the server lightweight.
4.  **Database (Neon):** Stores relational metadata and GPS coordinates.

---

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AnannyaMathewKJ/SmartLocal-Problem-Solver]
   cd SmartLocal
