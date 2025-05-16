import os
import sys
import subprocess
import time
import threading

# === Auto-install dependencies if missing ===
RESTART_ENV_VAR = "CLIPBOARD_APP_RESTARTED"

def ensure_dependencies():
    try:
        import tkinter as tk
        import pyperclip
    except ImportError:
        print("[INFO] Installing missing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
        os.environ[RESTART_ENV_VAR] = "1"
        print("[INFO] Restarting script after installing...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

# Avoid infinite loop
if not os.environ.get(RESTART_ENV_VAR):
    ensure_dependencies()

# === Safe imports now ===
import tkinter as tk
import pyperclip

# === Clipboard Manager App ===
class ClipboardManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard History")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.history = []
        self.last_clipboard = ""

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.listbox.bind("<Double-Button-1>", self.copy_selected)

        threading.Thread(target=self.monitor_clipboard, daemon=True).start()

    def monitor_clipboard(self):
        while True:
            try:
                text = pyperclip.paste()
                if text != self.last_clipboard and text.strip():
                    self.last_clipboard = text
                    self.history.insert(0, text)
                    self.update_list()
            except Exception:
                pass
            time.sleep(0.5)

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for item in self.history[:50]:  # Limit to last 50 entries
            display = item.replace("\n", " ")[:60]
            self.listbox.insert(tk.END, display)

    def copy_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            text = self.history[selected[0]]
            pyperclip.copy(text)

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardManager(root)
    root.mainloop()
