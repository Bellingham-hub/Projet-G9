# CS27 – Library Management System
### The Relational Model & Databases
**Burkina Institute of Technology | Academic Year 2025–2026**

---

## 👥 Group Information

| Role | Name |
|------|------|
| **Instructor** | Kweyakie Afi Blebo |
| **Group Leader** | ZABRE Tania |
| **Member** | SAWADOGO Rachelle |
| **Member** | KINI Jacob |
| **Member** | ILBOUDO Balkissa |
| **Member** | YAMEOGO Cedric |
| **Member** | NASSA Didier |

---

##  Project Overview

This project designs and implements a fully functional **Library Management System** using the relational model. The system manages books, authors, members, loans, and categories while enforcing data integrity through primary keys, foreign keys, and normalization up to **Third Normal Form (3NF)**.

---

##  Repository Structure

```
library-management-system/
  ├── library_db.sql    ← Database structure + all data (import this)
  ├── queries.sql       ← UPDATE, DELETE, SELECT, aggregate queries
  └── README.md         ← This file
```

---

##  Database Schema

The database contains **5 tables** :

| Table | Description | Primary Key |
|-------|-------------|-------------|
| `Authors` | Stores author information | AuthorID |
| `Categories` | Book categories and descriptions | CategoryID |
| `Books` | Book records with FK to Authors and Categories | BookID |
| `Members` | Library members | MemberID |
| `Loans` | Borrowing records linking Members and Books | LoanID |

### Relationships

| Tables | Type | Foreign Key |
|--------|------|-------------|
| Authors → Books | 1:M | Books.AuthorID |
| Categories → Books | 1:M | Books.CategoryID |
| Members → Loans | 1:M | Loans.MemberID |
| Books → Loans | 1:M | Loans.BookID |

---

##  How to Import the Database

1. Open **phpMyAdmin** in your browser
2. Click on the **Import** tab at the top
3. Click **Choose File** and select `library_db.sql`
4. Leave the format as **SQL**
5. Click **Go**
6. The `library_db` database will be created automatically with all 5 tables and data

---

##  What is Included

### Part 2.1 — Tables Created
- `Authors` — with NOT NULL, AUTO_INCREMENT
- `Categories` — with UNIQUE constraint on CategoryName
- `Books` — with FOREIGN KEY to Authors and Categories
- `Members` — with UNIQUE constraint on Email
- `Loans` — with FOREIGN KEY to Books and Members, NULL allowed on ReturnDate

### Part 2.2 — Sample Data
- 11 Authors from various African and international literary traditions
- 5 Categories (Fiction, Dystopian, Magical Realism, Historical, Autobiography)
- 11 Books with realistic ISBN numbers
- 11 Members with unique email addresses
- 12 Loan records (some returned, some still active)

### Part 2.3 — Data Manipulation
- 3 UPDATE statements (member date, loan return, author nationality)
- 2 DELETE statements (member with no loans, old loan record)
- 1 referential integrity violation demonstration (commented out)

### Part 2.4 — SELECT Queries
- Basic SELECT with WHERE, ORDER BY, LIMIT
- BETWEEN, LIKE, IN filters
- INNER JOIN across 2 tables
- LEFT JOIN with explanation
- JOIN across 3 tables
- IS NULL / IS NOT NULL

### Part 3 — Aggregate Functions
- COUNT, MAX, MIN, AVG
- GROUP BY with aggregate functions
- HAVING to filter grouped results
- Full summary report combining JOIN + GROUP BY + HAVING

---

## 🔒 Key Design Decisions

- **Surrogate keys** (INT AUTO_INCREMENT) used for all primary keys — more stable than natural keys like ISBN or Email
- **NULL for ReturnDate** — semantically correct, means the book has not been returned yet
- **UNIQUE on Members.Email** — prevents duplicate member registrations
- **Loans as a bridge table** — resolves the M:N relationship between Members and Books into clean transactional records
- **Categories extracted to 3NF** — eliminates transitive dependency between BookID and CategoryDescription

---

## 📽️ Video Walkthrough

A 5–10 minute video demonstration is available on YouTube covering:
- Scenario overview and schema explanation
- Live MySQL demo in phpMyAdmin
- Walkthrough of at least 3 key queries

> Link: *(add your YouTube link here)*

---

## 📝 Submission

Submitted via Microsoft Forms by the Group Leader.

> Form link: https://forms.cloud.microsoft/r/JjA4ZiaS2g

---

*CS27 — Computer Science Department | Burkina Institute of Technology*
