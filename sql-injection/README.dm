## SQL Injection Vulnerability

### Description
SQL Injection occurs when user input is directly concatenated into SQL queries without proper validation.

### Risk
An attacker can manipulate queries to:
- Bypass authentication
- Access unauthorized data
- Modify or delete database records

### Vulnerable Behavior
User input is directly inserted into the SQL query.

### Secure Fix
Prepared statements are used to separate SQL logic from user input, preventing malicious query manipulation.

### Lesson Learned
Never trust user input. Always validate and use parameterized queries.
