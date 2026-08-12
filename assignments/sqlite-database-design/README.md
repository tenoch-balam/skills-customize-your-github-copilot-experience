# 📘 Assignment: SQLite Database Design and Advanced Queries

## 🎯 Objective

Design and build a normalized SQLite relational database with multiple related tables, then write sophisticated SQL queries involving joins, aggregations, and data analysis. You'll learn database schema design principles and master advanced SQL operations.

## 📝 Tasks

### 🛠️ Design and Create a Normalized Database Schema

#### Description
Create a relational database schema for a real-world scenario (e.g., a school, library, or e-commerce system) with at least 3 related tables. Define appropriate data types, primary keys, foreign keys, and constraints to maintain data integrity.

#### Requirements
Completed program should:

- Design at least 3 tables with clear relationships (one-to-many or many-to-many)
- Use appropriate data types (TEXT, INTEGER, REAL, DATE, etc.)
- Define primary keys for each table
- Implement foreign key constraints to enforce referential integrity
- Create the database schema using Python and the `sqlite3` module
- Include an initialization script that creates all tables with sample data


### 🛠️ Write Complex Queries with Joins and Aggregations

#### Description
Write advanced SQL queries that retrieve and analyze data across multiple tables using joins, GROUP BY, ORDER BY, and aggregate functions.

#### Requirements
Completed program should:

- Implement at least 3 queries using INNER/LEFT/RIGHT joins
- Use aggregate functions (COUNT, SUM, AVG, MAX, MIN) with GROUP BY
- Filter results using WHERE and HAVING clauses
- Sort and limit results with ORDER BY and LIMIT
- Return results as formatted output or DataFrames using Pandas
- Example queries: "Show all orders by customer with total spent", "Find the most popular product by category", etc.


### 🛠️ Advanced: Optimize with Indexes and Transactions (Stretch Goal)

#### Description
Improve database performance and reliability by adding indexes to frequently queried columns and implementing transactions for multi-step operations.

#### Requirements
Completed program should:

- Create indexes on foreign keys and commonly searched columns
- Implement CRUD operations (Create, Read, Update, Delete) using transactions
- Handle transaction rollback on errors to ensure data consistency
- Demonstrate performance improvements with and without indexes
- Document query execution times or use SQLite's EXPLAIN QUERY PLAN
