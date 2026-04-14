# 📊 Price Monitor — Automated Data Pipeline

## 🚀 Overview

Price Monitor is a complete data pipeline project that automates the collection, storage, processing, and visualization of product pricing data from the web.

This project demonstrates real-world backend and data engineering skills, including web scraping, data processing, database integration, and cloud deployment.

---

## 🧠 Features

* 🔎 Automated web scraping of product data
* 💾 Data storage in PostgreSQL database
* 🧹 Data processing and cleaning with Pandas
* 📈 Interactive dashboard for data visualization
* ⚙️ Automated pipeline execution (scheduler-ready)
* ☁️ Cloud deployment (database + dashboard)

---

## 🏗️ Architecture

```text
Web Scraping → Data Processing → Database → Dashboard
```

* Scraper collects product data from a test e-commerce website
* Data is processed and structured using Pandas
* Data is stored in a PostgreSQL database
* Dashboard reads from the database and displays insights

---

## 🛠️ Technologies Used

* Python
* Selenium
* Pandas
* PostgreSQL
* SQLAlchemy
* Streamlit

---

## 📊 Dashboard

The dashboard provides a simple and interactive way to explore collected data.

### Features:

* Table visualization of products
* Price analysis
* Real-time data from database

---

## ⚙️ Automation

The project includes a scheduler-based automation system capable of running the pipeline periodically.

Due to deployment platform limitations, automation is demonstrated locally but designed to be easily adapted to cloud workers or cron jobs.

---

## 🗄️ Database

* Hosted on cloud using PostgreSQL
* Automatically populated by the scraping pipeline
* Structured for efficient querying and analysis

---

## 🚀 Deployment

* **Database:** Cloud-hosted PostgreSQL
* **Dashboard:** Streamlit Cloud

> The system is fully functional with real-time data integration.

---

## 📦 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/price-monitor.git
cd price-monitor
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` or set:

```
DB_URL=your_database_url
```

### 5. Run the pipeline

```bash
python main.py
```

### 6. Run dashboard

```bash
streamlit run dashboard.py
```

---

## 🎯 Project Purpose

This project was developed as a portfolio piece to demonstrate:

* Data pipeline design
* Backend development
* Database integration
* Automation concepts
* Real-world deployment practices

---

## 📌 Future Improvements

* API layer for data access
* Advanced data analytics
* Improved dashboard UI/UX
* Scalable scraping system
* Full cloud automation (cron/worker)

---

## 🧑‍💻 Author

Developed by Luis Gabriel

---

## ⭐ Notes

This project uses a public test website for scraping purposes:
https://books.toscrape.com

---

## 🔗 Live Demo

Dashboard:
(ADD YOUR STREAMLIT LINK HERE)

---
