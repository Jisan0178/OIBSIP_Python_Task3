import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip


THEMES = {
    "light": {
        "bg": "#F3F1F8",
        "sidebar": "#241B35",
        "sidebar_active": "#7C3AED",
        "card": "#FFFFFF",
        "input": "#F8F7FB",
        "text": "#211A2E",
        "secondary": "#756B82",
        "border": "#DDD6E7",
        "button": "#7C3AED",
        "button_hover": "#6D28D9",
        "success": "#16A34A",
        "warning": "#D97706",
        "danger": "#DC2626",
        "copy": "#EEE8FF"
    },

    "dark": {
        "bg": "#15121C",
        "sidebar": "#0D0A12",
        "sidebar_active": "#8B5CF6",
        "card": "#211C2B",
        "input": "#17131F",
        "text": "#F7F3FC",
        "secondary": "#A79CAF",
        "border": "#3A3145",
        "button": "#8B5CF6",
        "button_hover": "#7C3AED",
        "success": "#22C55E",
        "warning": "#F59E0B",
        "danger": "#EF4444",
        "copy": "#30264A"
    }
}


current_theme = "dark"
COLORS = THEMES[current_theme]

password_history = []

root = tk.Tk()
root.title("SecurePass Generator")
root.geometry("1000x680")
root.minsize(760, 560)
root.configure(bg=COLORS["bg"])


pages = {}
navigation_buttons = {}

length_var = tk.IntVar(value=16)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_var = tk.BooleanVar(value=False)

password_var = tk.StringVar()
strength_var = tk.StringVar(value="—")

password_entry = None
copy_button = None
strength_label = None
strength_bar = None
character_button = None
suggestion_frame = None
suggestion_text = None


def selected_character_types():
    selected = []

    if uppercase_var.get():
        selected.append("uppercase")

    if lowercase_var.get():
        selected.append("lowercase")

    if numbers_var.get():
        selected.append("numbers")

    if symbols_var.get():
        selected.append("symbols")

    return selected


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def create_card(parent):
    return tk.Frame(
        parent,
        bg=COLORS["card"],
        highlightbackground=COLORS["border"],
        highlightthickness=1
    )


def create_button(parent, text, command, width=20):
    return tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=2,
        bg=COLORS["button"],
        fg="white",
        activebackground=COLORS["button_hover"],
        activeforeground="white",
        relief="flat",
        bd=0,
        font=("Arial", 10, "bold"),
        cursor="hand2"
    )


def create_character_sets():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    if exclude_var.get():

        ambiguous = "O0oIl1"

        uppercase = "".join(
            character
            for character in uppercase
            if character not in ambiguous
        )

        lowercase = "".join(
            character
            for character in lowercase
            if character not in ambiguous
        )

        numbers = "".join(
            character
            for character in numbers
            if character not in ambiguous
        )

        symbols = "".join(
            character
            for character in symbols
            if character not in ambiguous
        )

    return {
        "uppercase": uppercase,
        "lowercase": lowercase,
        "numbers": numbers,
        "symbols": symbols
    }


def secure_shuffle(characters):
    characters = list(characters)

    for index in range(len(characters) - 1, 0, -1):
        position = secrets.randbelow(index + 1)

        characters[index], characters[position] = (
            characters[position],
            characters[index]
        )

    return "".join(characters)


def update_character_button():
    selected = selected_character_types()

    names = {
        "uppercase": "Uppercase",
        "lowercase": "Lowercase",
        "numbers": "Numbers",
        "symbols": "Symbols"
    }

    if not selected:
        text = "Choose Character Types"

    elif len(selected) == 4:
        text = "Upper + Lower + Number + Symbol"

    else:
        text = " + ".join(
            names[item]
            for item in selected
        )

    if character_button:
        character_button.config(text=text)


def choose_character_types():

    popup = tk.Toplevel(root)

    popup.title("Character Types")
    popup.geometry("430x430")
    popup.resizable(False, False)
    popup.configure(bg=COLORS["bg"])
    popup.transient(root)
    popup.grab_set()

    tk.Label(
        popup,
        text="Character Types",
        bg=COLORS["bg"],
        fg=COLORS["text"],
        font=("Arial", 19, "bold")
    ).pack(
        pady=(28, 5)
    )

    tk.Label(
        popup,
        text="Select at least two character types",
        bg=COLORS["bg"],
        fg=COLORS["secondary"],
        font=("Arial", 10)
    ).pack(
        pady=(0, 25)
    )

    temp_vars = {
        "uppercase": tk.BooleanVar(
            value=uppercase_var.get()
        ),
        "lowercase": tk.BooleanVar(
            value=lowercase_var.get()
        ),
        "numbers": tk.BooleanVar(
            value=numbers_var.get()
        ),
        "symbols": tk.BooleanVar(
            value=symbols_var.get()
        )
    }

    options = [
        ("A  Uppercase Letters", "uppercase"),
        ("a  Lowercase Letters", "lowercase"),
        ("123  Numbers", "numbers"),
        ("@#  Symbols", "symbols")
    ]

    for text, key in options:

        tk.Checkbutton(
            popup,
            text=text,
            variable=temp_vars[key],
            bg=COLORS["bg"],
            fg=COLORS["text"],
            activebackground=COLORS["bg"],
            activeforeground=COLORS["text"],
            selectcolor=COLORS["card"],
            font=("Arial", 11),
            anchor="w"
        ).pack(
            fill="x",
            padx=65,
            pady=7
        )

    def apply_selection():

        selected = [
            key
            for key, variable in temp_vars.items()
            if variable.get()
        ]

        if len(selected) < 2:

            messagebox.showerror(
                "Invalid Selection",
                "Please select at least 2 character types.",
                parent=popup
            )

            return

        uppercase_var.set(
            temp_vars["uppercase"].get()
        )

        lowercase_var.set(
            temp_vars["lowercase"].get()
        )

        numbers_var.set(
            temp_vars["numbers"].get()
        )

        symbols_var.set(
            temp_vars["symbols"].get()
        )

        update_character_button()

        popup.destroy()

    create_button(
        popup,
        "APPLY SELECTION",
        apply_selection,
        20
    ).pack(
        pady=25
    )


def calculate_strength(length, type_count):

    if length >= 16 and type_count >= 4:
        return "STRONG"

    if length >= 14 and type_count >= 3:
        return "STRONG"

    if length >= 12 and type_count >= 3:
        return "MEDIUM"

    if length >= 10 and type_count >= 2:
        return "MEDIUM"

    return "WEAK"


def update_strength(length, type_count):

    global strength_label
    global strength_bar

    strength = calculate_strength(
        length,
        type_count
    )

    strength_var.set(strength)

    if strength == "STRONG":

        color = COLORS["success"]
        width = 280

    elif strength == "MEDIUM":

        color = COLORS["warning"]
        width = 190

    else:

        color = COLORS["danger"]
        width = 100

    if strength_label:

        strength_label.config(
            text=strength,
            fg=color
        )

    if strength_bar:

        strength_bar.config(
            bg=color,
            width=width
        )

    if suggestion_frame:

        if strength == "WEAK":

            suggestion_frame.pack(
                fill="x",
                pady=(18, 0)
            )

            suggestion_text.config(
                text=(
                    "Password strength can be improved.\n\n"
                    "• Use 12 or more characters\n"
                    "• Select more character types\n"
                    "• Include uppercase and lowercase letters\n"
                    "• Include numbers and symbols"
                )
            )

        else:

            suggestion_frame.pack_forget()


def copy_to_clipboard(password):

    try:

        pyperclip.copy(password)

    except Exception:

        messagebox.showerror(
            "Clipboard Error",
            "Unable to copy the password to the clipboard."
        )


def copy_password():

    password = password_var.get()

    if not password:

        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )

        return

    copy_to_clipboard(password)

    copy_button.config(
        text="✓ Copied"
    )

    root.after(
        1200,
        lambda: copy_button.config(text="COPY")
    )


def generate_password():

    try:
        length = int(length_var.get())

    except (ValueError, tk.TclError):

        messagebox.showerror(
            "Invalid Length",
            "Please enter a valid password length."
        )

        return

    if length < 8 or length > 64:

        messagebox.showerror(
            "Invalid Length",
            "Password length must be between 8 and 64 characters."
        )

        return

    selected = selected_character_types()

    if len(selected) < 2:

        messagebox.showerror(
            "Character Types",
            "Please select at least 2 character types."
        )

        return

    character_sets = create_character_sets()

    for character_type in selected:

        if not character_sets[character_type]:

            messagebox.showerror(
                "Character Error",
                "No characters are available for a selected type."
            )

            return

    password_characters = []

    for character_type in selected:

        password_characters.append(
            secrets.choice(
                character_sets[character_type]
            )
        )

    all_characters = ""

    for character_type in selected:
        all_characters += character_sets[character_type]

    remaining = length - len(password_characters)

    for _ in range(remaining):

        password_characters.append(
            secrets.choice(all_characters)
        )

    password = secure_shuffle(
        password_characters
    )

    password_var.set(password)

    copy_to_clipboard(password)

    copy_button.config(
        text="✓ Copied"
    )

    root.after(
        1200,
        lambda: copy_button.config(text="COPY")
    )

    update_strength(
        length,
        len(selected)
    )

    password_history.insert(
        0,
        password
    )

    if len(password_history) > 5:
        password_history.pop()

    refresh_history_page()


def clear_history():

    if not password_history:

        messagebox.showinfo(
            "Password History",
            "There is no password history to clear."
        )

        return

    answer = messagebox.askyesno(
        "Clear History",
        "Delete all passwords stored in the current session?"
    )

    if not answer:
        return

    password_history.clear()

    refresh_history_page()


def copy_history_password(password):

    copy_to_clipboard(password)


def refresh_history_page():

    if "history" not in pages:
        return

    frame = pages["history"]

    clear_frame(frame)

    tk.Label(
        frame,
        text="Password History",
        bg=COLORS["bg"],
        fg=COLORS["text"],
        font=("Arial", 25, "bold")
    ).pack(
        anchor="w",
        pady=(5, 3)
    )

    tk.Label(
        frame,
        text="Only the last 5 passwords are kept during this session.",
        bg=COLORS["bg"],
        fg=COLORS["secondary"],
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(0, 18)
    )

    if password_history:

        tk.Button(
            frame,
            text="CLEAR HISTORY",
            command=clear_history,
            bg=COLORS["danger"],
            fg="white",
            activebackground=COLORS["danger"],
            activeforeground="white",
            relief="flat",
            bd=0,
            font=("Arial", 9, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            anchor="e",
            pady=(0, 12)
        )

        for number, password in enumerate(
            password_history,
            1
        ):

            row = tk.Frame(
                frame,
                bg=COLORS["card"],
                highlightbackground=COLORS["border"],
                highlightthickness=1
            )

            row.pack(
                fill="x",
                pady=5
            )

            tk.Label(
                row,
                text=f"{number:02d}",
                bg=COLORS["card"],
                fg=COLORS["button"],
                font=("Arial", 10, "bold"),
                width=4
            ).pack(
                side="left",
                padx=(10, 0)
            )

            tk.Label(
                row,
                text=password,
                bg=COLORS["card"],
                fg=COLORS["text"],
                font=("Consolas", 11),
                anchor="w"
            ).pack(
                side="left",
                fill="x",
                expand=True,
                padx=10,
                pady=13
            )

            tk.Button(
                row,
                text="COPY",
                command=lambda p=password:
                copy_history_password(p),
                bg=COLORS["copy"],
                fg=COLORS["button"],
                activebackground=COLORS["button"],
                activeforeground="white",
                relief="flat",
                bd=0,
                font=("Arial", 8, "bold"),
                cursor="hand2",
                padx=10,
                pady=5
            ).pack(
                side="right",
                padx=10
            )

    else:

        empty_card = create_card(frame)

        empty_card.pack(
            fill="x",
            pady=20
        )

        tk.Label(
            empty_card,
            text="No passwords generated yet.",
            bg=COLORS["card"],
            fg=COLORS["secondary"],
            font=("Arial", 11)
        ).pack(
            pady=35
        )


def create_generator_page():

    global password_entry
    global copy_button
    global strength_label
    global strength_bar
    global character_button
    global suggestion_frame
    global suggestion_text

    frame = pages["generator"]

    clear_frame(frame)

    tk.Label(
        frame,
        text="SecurePass Generator",
        bg=COLORS["bg"],
        fg=COLORS["text"],
        font=("Arial", 25, "bold")
    ).pack(
        anchor="w",
        pady=(5, 3)
    )

    tk.Label(
        frame,
        text="Generate secure passwords using cryptographically strong randomness.",
        bg=COLORS["bg"],
        fg=COLORS["secondary"],
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(0, 20)
    )

    card = create_card(frame)

    card.pack(
        fill="x",
        padx=5
    )

    inside = tk.Frame(
        card,
        bg=COLORS["card"]
    )

    inside.pack(
        fill="both",
        padx=30,
        pady=28
    )

    tk.Label(
        inside,
        text="PASSWORD LENGTH",
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Arial", 10, "bold")
    ).pack(
        anchor="w"
    )

    length_spinbox = tk.Spinbox(
        inside,
        from_=8,
        to=64,
        textvariable=length_var,
        width=12,
        bg=COLORS["input"],
        fg=COLORS["text"],
        buttonbackground=COLORS["button"],
        insertbackground=COLORS["text"],
        relief="solid",
        bd=1,
        font=("Arial", 11)
    )

    length_spinbox.pack(
        anchor="w",
        pady=(7, 5)
    )

    tk.Label(
        inside,
        text="Allowed length: 8 – 64 characters",
        bg=COLORS["card"],
        fg=COLORS["secondary"],
        font=("Arial", 9)
    ).pack(
        anchor="w",
        pady=(0, 20)
    )

    tk.Label(
        inside,
        text="CHARACTER TYPES",
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Arial", 10, "bold")
    ).pack(
        anchor="w"
    )

    character_button = tk.Button(
        inside,
        text="",
        command=choose_character_types,
        width=35,
        height=2,
        bg=COLORS["input"],
        fg=COLORS["text"],
        activebackground=COLORS["copy"],
        activeforeground=COLORS["text"],
        relief="solid",
        bd=1,
        font=("Arial", 10),
        cursor="hand2"
    )

    character_button.pack(
        anchor="w",
        pady=(7, 16)
    )

    update_character_button()

    tk.Checkbutton(
        inside,
        text="Exclude ambiguous characters  (O, 0, o, I, l, 1)",
        variable=exclude_var,
        bg=COLORS["card"],
        fg=COLORS["text"],
        activebackground=COLORS["card"],
        activeforeground=COLORS["text"],
        selectcolor=COLORS["input"],
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(0, 22)
    )

    tk.Label(
        inside,
        text="GENERATED PASSWORD",
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Arial", 10, "bold")
    ).pack(
        anchor="w"
    )

    password_area = tk.Frame(
        inside,
        bg=COLORS["card"]
    )

    password_area.pack(
        fill="x",
        pady=(7, 22)
    )

    password_entry = tk.Entry(
        password_area,
        textvariable=password_var,
        bg=COLORS["input"],
        fg=COLORS["text"],
        insertbackground=COLORS["text"],
        relief="solid",
        bd=1,
        font=("Consolas", 13)
    )

    password_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=10
    )

    copy_button = tk.Button(
        password_area,
        text="COPY",
        command=copy_password,
        bg=COLORS["copy"],
        fg=COLORS["button"],
        activebackground=COLORS["button"],
        activeforeground="white",
        relief="flat",
        bd=0,
        font=("Arial", 9, "bold"),
        cursor="hand2",
        width=9,
        height=2
    )

    copy_button.pack(
        side="right",
        padx=(8, 0)
    )

    strength_header = tk.Frame(
        inside,
        bg=COLORS["card"]
    )

    strength_header.pack(
        fill="x"
    )

    tk.Label(
        strength_header,
        text="PASSWORD STRENGTH",
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Arial", 10, "bold")
    ).pack(
        side="left"
    )

    strength_label = tk.Label(
        strength_header,
        text="—",
        bg=COLORS["card"],
        fg=COLORS["secondary"],
        font=("Arial", 10, "bold")
    )

    strength_label.pack(
        side="right"
    )

    strength_background = tk.Frame(
        inside,
        bg=COLORS["border"],
        height=8
    )

    strength_background.pack(
        fill="x",
        pady=(7, 22)
    )

    strength_bar = tk.Frame(
        strength_background,
        bg=COLORS["success"],
        height=8,
        width=0
    )

    strength_bar.pack(
        side="left"
    )

    create_button(
        inside,
        "GENERATE PASSWORD",
        generate_password,
        24
    ).pack(
        pady=5
    )

    suggestion_frame = tk.Frame(
        inside,
        bg="#FFF7ED",
        highlightbackground=COLORS["warning"],
        highlightthickness=1
    )

    suggestion_text = tk.Label(
        suggestion_frame,
        text="",
        bg="#FFF7ED",
        fg="#92400E",
        justify="left",
        anchor="w",
        font=("Arial", 10),
        wraplength=650
    )

    suggestion_text.pack(
        fill="x",
        padx=15,
        pady=13
    )

    suggestion_frame.pack_forget()


def create_settings_page():

    frame = pages["settings"]

    clear_frame(frame)

    tk.Label(
        frame,
        text="Settings",
        bg=COLORS["bg"],
        fg=COLORS["text"],
        font=("Arial", 25, "bold")
    ).pack(
        anchor="w",
        pady=(5, 3)
    )

    tk.Label(
        frame,
        text="Customize the appearance of SecurePass Generator.",
        bg=COLORS["bg"],
        fg=COLORS["secondary"],
        font=("Arial", 10)
    ).pack(
        anchor="w",
        pady=(0, 20)
    )

    appearance = create_card(frame)

    appearance.pack(
        fill="x",
        pady=5
    )

    tk.Label(
        appearance,
        text="APPEARANCE",
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Arial", 13, "bold")
    ).pack(
        anchor="w",
        padx=25,
        pady=(22, 12)
    )

    tk.Button(
        appearance,
        text="☀  Light Theme",
        command=lambda: change_theme("light"),
        bg=COLORS["button"],
        fg="white",
        activebackground=COLORS["button_hover"],
        activeforeground="white",
        relief="flat",
        bd=0,
        font=("Arial", 10, "bold"),
        cursor="hand2",
        padx=15,
        pady=9
    ).pack(
        anchor="w",
        padx=25,
        pady=5
    )

    tk.Button(
        appearance,
        text="☾  Dark Theme",
        command=lambda: change_theme("dark"),
        bg=COLORS["button"],
        fg="white",
        activebackground=COLORS["button_hover"],
        activeforeground="white",
        relief="flat",
        bd=0,
        font=("Arial", 10, "bold"),
        cursor="hand2",
        padx=15,
        pady=9
    ).pack(
        anchor="w",
        padx=25,
        pady=(5, 22)
    )

    about = create_card(frame)

    about.pack(
        fill="x",
        pady=12
    )

    tk.Label(
        about,
        text="ABOUT",
        bg=COLORS["card"],
        fg=COLORS["text"],
        font=("Arial", 13, "bold")
    ).pack(
        anchor="w",
        padx=25,
        pady=(22, 8)
    )

    tk.Label(
        about,
        text=(
            "SecurePass Generator\n\n"
            "A desktop password generator built with Python and Tkinter.\n"
            "Passwords are generated using the cryptographically secure\n"
            "secrets module and are never stored permanently."
        ),
        bg=COLORS["card"],
        fg=COLORS["secondary"],
        justify="left",
        font=("Arial", 10)
    ).pack(
        anchor="w",
        padx=25,
        pady=(0, 22)
    )

    footer = tk.Frame(
        frame,
        bg=COLORS["bg"]
    )

    footer.pack(
        pady=25
    )

    tk.Label(
        footer,
        text="Developed by Jisan Ali",
        bg=COLORS["bg"],
        fg=COLORS["secondary"],
        font=("Arial", 10, "bold")
    ).pack()

    tk.Label(
        footer,
        text="© 2026 Jisan Ali",
        bg=COLORS["bg"],
        fg=COLORS["secondary"],
        font=("Arial", 9)
    ).pack(
        pady=(4, 0)
    )


def create_history_page():

    frame = pages["history"]

    clear_frame(frame)

    refresh_history_page()


def show_page(page_name):

    for page in pages.values():
        page.pack_forget()

    pages[page_name].pack(
        fill="both",
        expand=True
    )

    for name, button in navigation_buttons.items():

        if name == page_name:

            button.config(
                bg=COLORS["sidebar_active"],
                fg="white"
            )

        else:

            button.config(
                bg=COLORS["sidebar"],
                fg="white"
            )


def change_theme(theme):

    global current_theme
    global COLORS

    current_theme = theme
    COLORS = THEMES[current_theme]

    rebuild_ui()


def create_sidebar(parent):

    sidebar = tk.Frame(
        parent,
        bg=COLORS["sidebar"],
        width=235
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text="◆",
        bg=COLORS["sidebar"],
        fg=COLORS["button"],
        font=("Arial", 34, "bold")
    ).pack(
        pady=(30, 4)
    )

    tk.Label(
        sidebar,
        text="SECUREPASS",
        bg=COLORS["sidebar"],
        fg="white",
        font=("Arial", 16, "bold")
    ).pack()

    tk.Label(
        sidebar,
        text="Password Generator",
        bg=COLORS["sidebar"],
        fg="#B8ADCA",
        font=("Arial", 9)
    ).pack(
        pady=(3, 35)
    )

    navigation = [
        ("generator", "🔐   Generator"),
        ("history", "◷   History"),
        ("settings", "⚙   Settings")
    ]

    for page_name, text in navigation:

        button = tk.Button(
            sidebar,
            text=text,
            command=lambda page=page_name:
            show_page(page),
            bg=COLORS["sidebar"],
            fg="white",
            activebackground=COLORS["sidebar_active"],
            activeforeground="white",
            relief="flat",
            bd=0,
            anchor="w",
            padx=25,
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )

        button.pack(
            fill="x",
            pady=3,
            ipady=11
        )

        navigation_buttons[page_name] = button

    tk.Label(
        sidebar,
        text="Secure generation\nwith Python secrets",
        bg=COLORS["sidebar"],
        fg="#8F849D",
        font=("Arial", 8),
        justify="center"
    ).pack(
        side="bottom",
        pady=25
    )


def rebuild_ui():

    global pages
    global navigation_buttons

    for widget in root.winfo_children():
        widget.destroy()

    pages = {}
    navigation_buttons = {}

    main_area = tk.Frame(
        root,
        bg=COLORS["bg"]
    )

    main_area.pack(
        fill="both",
        expand=True
    )

    create_sidebar(main_area)

    content = tk.Frame(
        main_area,
        bg=COLORS["bg"]
    )

    content.pack(
        side="right",
        fill="both",
        expand=True,
        padx=35,
        pady=30
    )

    pages["generator"] = tk.Frame(
        content,
        bg=COLORS["bg"]
    )

    pages["history"] = tk.Frame(
        content,
        bg=COLORS["bg"]
    )

    pages["settings"] = tk.Frame(
        content,
        bg=COLORS["bg"]
    )

    create_generator_page()
    create_history_page()
    create_settings_page()

    show_page("generator")


rebuild_ui()

root.mainloop()