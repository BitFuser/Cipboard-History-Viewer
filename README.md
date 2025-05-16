# 📋 Clipboard History Viewer (GUI)

A lightweight Python app that keeps a **live history of clipboard text** using a responsive GUI. Automatically saves the last 50 copied entries and allows you to **re-copy** any item with a double-click.

---

## 🧰 Features

- 🔄 Real-time clipboard tracking (updates every 0.5s)
- 🧠 Keeps up to **50 clipboard entries**
- 🖱️ Double-click to instantly re-copy any item
- 🪟 Minimal GUI built with `tkinter`
- 🔁 Auto-installs `pyperclip` if not found

---

## 📦 Requirements

No manual install needed — the script installs missing packages automatically on first run.

You can also install manually:

```bash
pip install pyperclip
```

---

## 🚀 How to Use

1. Run the script:

   ```bash
   python clipboard_history.py
   ```

2. Copy any text — it will appear instantly in the app.

3. Double-click an item in the list to copy it back to the clipboard.

---

## 🖼️ GUI Preview

```text
+---------------------------------------------+
|              Clipboard History              |
+---------------------------------------------+
| Copied Item #1                              |
| Copied Item #2                              |
| ... up to 50 recent entries                 |
+---------------------------------------------+
(Double-click any item to copy it again)
```

---

## 🧠 Tech Stack

- `tkinter` – GUI
- `pyperclip` – Clipboard access
- `threading` – Background monitoring

---

## 🔒 Notes

- Only supports **text** clipboard data
- Limits history to **last 50 entries** for performance
- Silent fail on unsupported clipboard formats
