import zipfile
import shutil
import re
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


class PPSXUnlocker:
    def __init__(self, root):
        self.root = root
        self.root.title("PPSX Password Remover")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        title = tk.Label(root, text="🔐 PPSX Password Remover", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        self.select_btn = tk.Button(root, text="📂 Select PPSX Files", font=("Arial", 12),
                                     command=self.select_files, bg="#4CAF50", fg="white",
                                     width=20, height=2)
        self.select_btn.pack(pady=10)

        self.unlock_btn = tk.Button(root, text="🔓 Unlock All", font=("Arial", 12),
                                     command=self.unlock_files, bg="#2196F3", fg="white",
                                     width=20, height=2, state=tk.DISABLED)
        self.unlock_btn.pack(pady=5)

        self.clear_btn = tk.Button(root, text="🗑 Clear", font=("Arial", 10),
                                    command=self.clear_log, bg="#f44336", fg="white",
                                    width=15, height=1)
        self.clear_btn.pack(pady=5)

        self.log_box = ScrolledText(root, height=12, width=70, font=("Consolas", 10))
        self.log_box.pack(pady=10, padx=10)

        self.selected_files = []

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.root.update()

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Select PPSX Files",
            filetypes=[("PowerPoint Show", "*.ppsx"), ("All Files", "*.*")]
        )
        if files:
            added = 0
            for f in files:
                if f not in self.selected_files:  # No duplicates
                    self.selected_files.append(f)
                    added += 1

            self.log(f"✅ Added {added} file(s). Total: {len(self.selected_files)}")
            for f in files:
                self.log(f"   → {os.path.basename(f)}")
            self.unlock_btn.config(state=tk.NORMAL)

    def unlock_file(self, filepath):
        filename = os.path.basename(filepath)
        temp_zip = filepath + ".temp"

        try:
            shutil.copy(filepath, temp_zip)

            with zipfile.ZipFile(temp_zip, 'r') as zin:
                with zipfile.ZipFile(filepath, 'w') as zout:
                    for item in zin.namelist():
                        data = zin.read(item)

                        if "presentation.xml" in item:
                            text = data.decode('utf-8')
                            text = re.sub(r'<p:modifyVerifier[^>]*/>', '', text)
                            data = text.encode('utf-8')

                        zout.writestr(item, data)

            os.remove(temp_zip)
            self.log(f"🔓 Unlocked: {filename}")
            return True

        except Exception as e:
            self.log(f"❌ Error with {filename}: {str(e)}")
            if os.path.exists(temp_zip):
                os.remove(temp_zip)
            return False

    def unlock_files(self):
        success = 0
        failed = 0

        self.log("\n--- Starting unlock process... ---\n")

        for filepath in self.selected_files:
            if self.unlock_file(filepath):
                success += 1
            else:
                failed += 1

        self.log(f"\n--- Done! ✅ {success} unlocked | ❌ {failed} failed ---\n")

    def clear_log(self):
        self.log_box.delete(1.0, tk.END)
        self.selected_files = []
        self.unlock_btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = PPSXUnlocker(root)
    root.mainloop()