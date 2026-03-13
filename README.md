# Prowiz Python & SQL Assignment – Solutions

This repository contains the **solutions implemented for the Prowiz Analytics Python & SQL test assignment**.

The assignment consists of multiple tasks designed to evaluate skills in **Python programming, API handling, HTML parsing, FastAPI development, data analysis, and SQL queries**.

All tasks from the assignment have been implemented and the corresponding solution files are included in this repository.

---

# Tasks Implemented

## Task 1 – Python Requests API Analysis

Using the **Python `requests` library**, data was fetched from the API:

https://jsonplaceholder.typicode.com/posts

The solution performs the following operations:

- Fetch all posts from the API
- Print the retrieved posts
- Count the number of **distinct users**
- Identify the **user with the highest number of posts**
- Calculate the **average word length of post titles**

The implementation uses Python libraries such as:

- `requests`
- `pandas`
- `numpy`

---

## Task 2 – HTML Parsing

An HTML document is parsed using **BeautifulSoup**.

The solution extracts:

- All **href links** present in the HTML
- All **class attributes from `<a>` tags**

Additionally, a **recursive Python approach** was implemented to parse the HTML content **without using BeautifulSoup**.

---

## Task 3 – FastAPI Implementation

A simple API was developed using **FastAPI**.

Two endpoints were implemented:

### Endpoint 1 – Sum of Two Numbers
Accepts **two numbers as input** and returns their **sum**.

The API includes **error handling** to ensure invalid inputs (such as strings) are properly managed.

### Endpoint 2 – Convert String to Uppercase
Accepts a **lowercase string** and returns the **uppercase version** of the string.

---

## Task 4 – Data Analysis

Data analysis was performed on the **Global Electronics Retailer dataset**.

The analysis was implemented using Python with libraries such as:

- Pandas
- Matplotlib
- Seaborn

Key analyses include:

- Gender-wise sales analysis
- Brand popularity
- Popular brands among male and female customers
- Country-wise sales of products
- Brands covering multiple product categories

---

## Task 5 – SQL Queries

SQL queries were written to determine the **second topper in a class** under different ranking conditions.

The solutions include:

1. Identifying the **second highest scorer**
2. Handling ties using **alphabetical ordering**
3. Ranking students where **multiple candidates can share the same rank**

These queries demonstrate the use of:

- SQL ranking functions
- Ordering and grouping
- Conditional ranking logic

---

# Repository Structure

```
prowiz-python-and-sql-assignment
│
├── Task1.py        # Python Requests API solution
├── Task2.py        # HTML parsing solution
├── Task3.py        # FastAPI implementation
├── Task4.py        # Data analysis on Global Electronics dataset
├── Task5.sql       # SQL solutions for ranking problems
│
└── README.md       # Project documentation
```

---

# Technologies Used

## Python
- Requests
- Pandas
- NumPy
- BeautifulSoup
- FastAPI
- Matplotlib
- Seaborn

## SQL
- Window Functions
- Ranking Functions
- Aggregation

---

# How to Run the Solutions

### Clone the repository

```
git clone https://github.com/jaskaransingh16/prowiz-python-and-sql-assignment.git
```

### Navigate to the project directory

```
cd prowiz-python-and-sql-assignment
```

### Install required Python libraries

```
pip install requests pandas numpy beautifulsoup4 fastapi matplotlib seaborn
```

### Run Python tasks

Example:

```
python Task1.py
python Task2.py
python Task3.py
python Task4.py
```

SQL queries can be executed using any SQL environment.

---

# Author

**Jaskaran Singh**

GitHub:  
https://github.com/jaskaransingh16
