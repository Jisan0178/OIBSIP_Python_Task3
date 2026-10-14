# 🔐 SecurePass Generator

A secure desktop password generator built with **Python and Tkinter**. SecurePass Generator helps users create strong, customizable passwords using Python's cryptographically secure `secrets` module.

The application includes password strength analysis, clipboard copying, password history, ambiguous-character exclusion, and light and dark themes.

---

## 📌 Project Overview

**SecurePass Generator** is a desktop application designed to make password creation simple and convenient. Users can customize password length and character types, generate passwords securely, check their estimated strength, and copy passwords directly to the clipboard.

The application also provides a session-based history of recently generated passwords and suggestions for improving weak passwords.

## ✨ Features

### 🔑 1. Secure Password Generation

- Generates passwords using Python's `secrets` module.
- Supports password lengths from **8 to 64 characters**.
- Allows users to customize password composition.
- Includes at least one character from each selected character type.
- Securely shuffles generated password characters.

### 🔤 2. Customizable Character Types

Users can select from four character categories:

- **Uppercase letters:** `A-Z`
- **Lowercase letters:** `a-z`
- **Numbers:** `0-9`
- **Symbols:** Special characters and punctuation

At least **two character types** must be selected before generating a password.

### 🚫 3. Exclude Ambiguous Characters

The application provides an option to exclude characters that can be easily confused when reading or typing passwords.

Excluded characters:

```text
O 0 o I l 1
```

This feature can make passwords easier to read and enter manually.

### 💪 4. Password Strength Indicator

SecurePass Generator estimates password strength using password length and the number of selected character types.

| Strength | Description |
|---|---|
| 🔴 WEAK | Does not meet the application's stronger-password criteria |
| 🟠 MEDIUM | Meets the application's moderate-strength criteria |
| 🟢 STRONG | Meets the application's stronger-password criteria |

When a password is classified as weak, the application displays suggestions to help improve it.

### 📋 5. Copy to Clipboard

- Copies generated passwords to the clipboard.
- Uses the `pyperclip` library.
- Provides visual feedback after a successful copy, such as `✓ Copied`.

### 🕒 6. Password History

- Keeps the **last five generated passwords** during the current application session.
- Allows users to view previously generated passwords.
- Supports copying individual passwords.
- Includes an option to clear the history.

**Note:** Password history is stored in memory only. It is not permanently saved and is cleared when the application closes.

### 🌗 7. Light and Dark Themes

The application supports two interface themes:

- ☀️ Light Theme
- 🌙 Dark Theme

Users can switch between themes through the Settings page.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Tkinter** | Building the graphical user interface |
| **secrets** | Cryptographically secure random selection |
| **string** | Providing character sets |
| **pyperclip** | Copying passwords to the clipboard |

---

## 📦 Installation and Setup

### Prerequisites

- Python 3 installed on your computer.
- Git installed if you want to clone the repository.

### Step 1: Clone the Repository

Open your terminal or VS Code terminal and run:

```bash
git clone https://github.com/Jisan0178/OIBSIP_Python_Task3.git
```

### Step 2: Open the Project Folder

```bash
cd OIBSIP_Python_Task3
```

### Step 3: Install Dependencies

Install the required external library:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the dependency directly:

```bash
pip install pyperclip
```

**Note:** Tkinter is included with many Python installations. On some Linux systems, it may need to be installed separately.

---

## ▶️ Running the Application

Run the Python file from the project directory:

```bash
python random_pass.py
```

Alternatively, on Windows:

```bash
py random_pass.py
```

The SecurePass Generator window should open.

**Important:** If your Python file has a different name, replace `securepass.py` with the actual filename.

---

## 🔄 How It Works

The password generation process follows these steps:

```text
Select Password Length
         ↓
Choose Character Types
         ↓
Optionally Exclude Ambiguous Characters
         ↓
Create the Available Character Sets
         ↓
Select Characters from Each Chosen Type
         ↓
Fill the Remaining Password Length
         ↓
Securely Shuffle the Characters
         ↓
Estimate Password Strength
         ↓
Display the Generated Password
         ↓
Copy the Password to the Clipboard
         ↓
Store It in Session History
```

---

## 🔐 Security Information

SecurePass Generator uses Python's built-in `secrets` module instead of the standard `random` module for password generation.

The `secrets` module is designed for generating random values suitable for security-sensitive applications.

For example:

```python
secrets.choice(character_set)
```

selects a character using a cryptographically secure random source.

The module also provides:

```python
secrets.randbelow(number)
```

which returns a securely selected integer below the specified limit.

The application uses secure random selection and shuffling for password generation.

**Security note:** The strength indicator is a simplified estimate, not a guarantee that a password is secure. The application does not check passwords against known data breaches. Avoid sharing generated passwords or storing them in publicly accessible files.

---

## 📊 Password Strength Logic

The application estimates password strength based on password length and the number of selected character types.

### Strong

A password is classified as strong when it meets either condition:

```text
Length ≥ 16 AND 4 character types
```

or:

```text
Length ≥ 14 AND at least 3 character types
```

### Medium

A password is classified as medium when it meets either condition:

```text
Length ≥ 12 AND at least 3 character types
```

or:

```text
Length ≥ 10 AND at least 2 character types
```

### Weak

Passwords that do not satisfy the above conditions are classified as weak.

*These rules describe the intended strength criteria. Ensure they match the conditions implemented in your current Python code.*

---

## 🧩 Python Concepts Demonstrated

This project demonstrates several Python programming concepts:

- Variables and data types
- Functions
- Conditional statements
- Loops
- Lists and dictionaries
- String manipulation
- Exception handling
- Lambda functions
- Global variables
- Modules and imports
- Tkinter widgets and variables
- Event-driven programming
- Secure random generation
- Clipboard operations
- GUI theme management

---

## 📚 Python Modules Used

### Built-in Modules

```python
import tkinter as tk
from tkinter import messagebox
import string
import secrets
```

### External Library

```python
import pyperclip
```

The built-in modules provide the interface, character sets, and secure random generation. The external `pyperclip` library handles clipboard operations.

---

## 📁 Project Structure

The repository can be organized as follows:

```text
OIBSIP_Python_Task3/
│
├── random_pass.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Developing a desktop application using Python and Tkinter.
- Generating passwords using cryptographically secure randomness.
- Working with user input and validation.
- Implementing password strength feedback.
- Integrating clipboard functionality.
- Managing session-based password history.
- Designing a graphical interface with light and dark themes.
- Organizing a Python project for GitHub.

---

## 👨‍💻 Author

**Jisan Ali**

B.Tech — Computer Science and Engineering (AI & ML)

**Internship:** Oasis Infobyte — Python Programming

## 🔗 Project Links

- **GitHub Repository:** [OIBSIP_Python_Task3](https://github.com/Jisan0178/OIBSIP_Python_Task3)
- **Oasis Infobyte:** [Official Website](https://oasisinfobyte.com/)

## 🎥 Demo Video

- **Project Demonstration:** [Watch the Demo](https://lnkd.in/p/dUkjuUh9)

---
