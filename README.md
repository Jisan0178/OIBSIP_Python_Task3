# 🔐 SecurePass Generator

A secure desktop password generator built with **Python and Tkinter**.
The application allows users to generate strong and customizable passwords using Python's cryptographically secure `secrets` module.

It also provides password strength analysis, password history, clipboard copying, ambiguous-character exclusion, and light/dark themes.

---

## 📌 Project Overview

**SecurePass Generator** is a desktop-based password generation application designed to make it easy to create strong and secure passwords.

Users can customize:

* Password length
* Character types
* Uppercase letters
* Lowercase letters
* Numbers
* Symbols
* Ambiguous character exclusion

The application automatically evaluates password strength and provides suggestions when a generated password is weak.

---

## ✨ Features

### 🔑 Secure Password Generation

Passwords are generated using Python's `secrets` module, which is designed for security-sensitive applications.

The application:

* Generates random passwords securely
* Supports passwords from **8 to 64 characters**
* Ensures at least one character from every selected character type
* Uses secure random selection
* Securely shuffles the generated password

---

### 🔤 Character Type Selection

Users can select different character types:

* **Uppercase Letters** — `A-Z`
* **Lowercase Letters** — `a-z`
* **Numbers** — `0-9`
* **Symbols** — punctuation and special characters

The application requires users to select at least **two character types**.

---

### 🚫 Exclude Ambiguous Characters

Users can enable an option to exclude characters that can easily be confused with each other.

Excluded characters:

```text
O 0 o I l 1
```

This is useful when passwords need to be manually read or typed.

---

### 💪 Password Strength Indicator

The application evaluates the generated password based on:

* Password length
* Number of selected character types

Password strength is categorized as:

| Strength  | Description                                 |
| --------- | ------------------------------------------- |
| 🔴 WEAK   | Short password or limited character types   |
| 🟠 MEDIUM | Reasonably strong password                  |
| 🟢 STRONG | Long password with multiple character types |

For weak passwords, the application displays suggestions for improving password strength.

---

### 📋 Copy to Clipboard

Generated passwords can be copied directly to the clipboard using the **COPY** button.

The application uses the `pyperclip` library for clipboard functionality.

After copying, the button temporarily changes to:

```text
✓ Copied
```

---

### 🕒 Password History

The application keeps the **last 5 generated passwords** during the current application session.

Users can:

* View previously generated passwords
* Copy individual passwords
* Clear the entire history

> Password history is stored only in memory and is not saved permanently.

---

### 🌗 Light and Dark Themes

SecurePass Generator supports two themes:

* ☀️ Light Theme
* 🌙 Dark Theme

The interface can be switched from the **Settings** page.

---

### 🖥️ User-Friendly GUI

The application uses **Tkinter** to provide a graphical interface with:

* Sidebar navigation
* Generator page
* History page
* Settings page
* Responsive password controls
* Password strength visualization
* Theme customization

---

## 🛠️ Technologies Used

| Technology    | Purpose                                    |
| ------------- | ------------------------------------------ |
| **Python**    | Main programming language                  |
| **Tkinter**   | Graphical User Interface                   |
| **secrets**   | Cryptographically secure random generation |
| **string**    | Character sets                             |
| **pyperclip** | Clipboard functionality                    |


---

## ⚙️ Requirements

Before running the application, make sure Python is installed.

### Python

Recommended:

```text
Python 3.9+
```

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jisan0178/OIBSIP_Python_Task3.git
```

```

## ▶️ Running the Application

Run the Python file:

```bash
python securepass.py
```

or:

```bash
py securepass.py
```

The SecurePass Generator window should open.

---

## 🔄 How It Works

The password generation process follows these steps:

```text
Select Password Length
        ↓
Select Character Types
        ↓
Optional: Exclude Ambiguous Characters
        ↓
Create Character Sets
        ↓
Select At Least One Character
from Each Selected Type
        ↓
Fill Remaining Characters
        ↓
Securely Shuffle Password
        ↓
Calculate Password Strength
        ↓
Display Password
        ↓
Copy Password to Clipboard
        ↓
Store in Session History
```

---

## 🔐 Security

This project uses Python's:

```python
secrets
```

module instead of the standard `random` module for password generation.

For example:

```python
secrets.choice(character_set)
```

and:

```python
secrets.randbelow(number)
```

are used to generate and shuffle password characters.

This makes the password generation process more appropriate for security-sensitive use cases.

---

## ⚠️ Privacy

SecurePass Generator does **not** permanently store generated passwords.

Password history is maintained only while the application is running.

When the application is closed:

```text
Password History → Deleted from Memory
```

The application does not use a database or external server.

---

## 📊 Password Strength Logic

The application uses password length and the number of selected character types to estimate strength.

### Strong

A password is considered strong when:

```text
Length ≥ 16 AND 4 character types
```

or:

```text
Length ≥ 14 AND 3+ character types
```

### Medium

A password is considered medium when:

```text
Length ≥ 12 AND 3+ character types
```

or:

```text
Length ≥ 10 AND 2+ character types
```

### Weak

Passwords that do not satisfy the above conditions are classified as:

```text
WEAK
```

> This strength indicator is a simple application-level estimate. It is not a replacement for a professional password-strength estimator or breach database.

---

## 🧩 Main Python Concepts Used

This project demonstrates several important Python concepts:

* Variables
* Functions
* Conditional statements
* Loops
* Lists
* Dictionaries
* String handling
* Exception handling
* Lambda functions
* Global variables
* Tkinter widgets
* Tkinter variables
* Event-driven programming
* Modules and imports
* Secure random generation
* Clipboard operations

---

## 📚 Python Modules Used

### Built-in Modules

```python
import tkinter as tk
from tkinter import messagebox
import string
import secrets
```

### External Module

```python
import pyperclip
```
---


## 👨‍💻 Author

**Jisan Ali**

B.Tech — Computer Science and Engineering (AI & ML)

© 2026 Jisan Ali
