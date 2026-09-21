"""Basit TodoList - Tkinter arayüzü.

Çalıştırmak için:  python todo_gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox


# Mantık katmanı (arayüzden bağımsız)

class Task:
    """Tek bir görevi temsil eder."""

    def __init__(self, title, priority="normal"):
        self.title = title
        self.priority = priority
        self.done = False

    def mark_done(self):
        self.done = True

    def toggle(self):
        self.done = not self.done

    def __str__(self):
        status = "✓" if self.done else " "
        return f"[{status}] {self.title} ({self.priority})"


class TodoList:
    """Görevleri ekleyip, silip, listeleyen sınıf."""

    def __init__(self, name):
        self.name = name
        self._tasks = []

    def add(self, title, priority="normal"):
        task = Task(title, priority)
        self._tasks.append(task)
        return task

    def remove(self, index):
        if not 0 <= index < len(self._tasks):
            raise IndexError("Geçersiz görev numarası")
        return self._tasks.pop(index)

    def toggle(self, index):
        if not 0 <= index < len(self._tasks):
            raise IndexError("Geçersiz görev numarası")
        self._tasks[index].toggle()

    def clear_completed(self):
        self._tasks = [t for t in self._tasks if not t.done]

    def pending(self):
        return [t for t in self._tasks if not t.done]

    def completed(self):
        return [t for t in self._tasks if t.done]

    def all(self):
        return list(self._tasks)

    def __len__(self):
        return len(self._tasks)


# ---------- Arayüz katmanı ----------
class TodoApp(tk.Tk):

    def __init__(self, todo):
        super().__init__()
        self.todo = todo

        self.title(f"Yapılacaklar -- To Do List {todo.name}")
        self.geometry("420x480")
        self.minsize(360, 400)

        self._build_widgets()
        self.refresh()

    def _build_widgets(self):
        # Üst kısım: giriş alanı
        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        self.entry = ttk.Entry(top, font=("Segoe UI", 11))
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.entry.focus()

        self.priority = tk.StringVar(value="normal")
        ttk.Combobox(
            top,
            textvariable=self.priority,
            values=["düşük", "normal", "yüksek"],
            width=8,
            state="readonly",
        ).pack(side="left", padx=6)

        ttk.Button(top, text="Ekle", command=self.add_task).pack(side="left")

        # Orta kısım: liste
        mid = ttk.Frame(self, padding=(10, 0))
        mid.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(
            mid,
            font=("Consolas", 11),
            activestyle="none",
            selectmode="browse",
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", lambda event: self.toggle_task())

        scrollbar = ttk.Scrollbar(mid, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # --- Alt kısım: butonlar ve durum ---
        bottom = ttk.Frame(self, padding=10)
        bottom.pack(fill="x")

        ttk.Button(bottom, text="Tamamlandı", command=self.toggle_task).pack(side="left")
        ttk.Button(bottom, text="Sil", command=self.delete_task).pack(side="left", padx=6)
        ttk.Button(bottom, text="Bitenleri temizle", command=self.clear_done).pack(side="left")

        self.status = ttk.Label(self, text="", padding=(10, 0, 10, 10))
        self.status.pack(fill="x")



    def add_task(self):
        title = self.entry.get().strip()
        if not title:
            messagebox.showwarning("Boş görev", "Lütfen bir görev yazın.")
            return
        self.todo.add(title, self.priority.get())
        self.entry.delete(0, tk.END)
        self.refresh()

    def _selected_index(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Seçim yok", "Önce listeden bir görev seçin.")
            return None
        return selection[0]

    def toggle_task(self):
        index = self._selected_index()
        if index is None:
            return
        self.todo.toggle(index)
        self.refresh(keep=index)

    def delete_task(self):
        index = self._selected_index()
        if index is None:
            return
        task = self.todo.all()[index]
        if messagebox.askyesno("Sil", f"'{task.title}' silinsin mi?"):
            self.todo.remove(index)
            self.refresh()

    def clear_done(self):
        self.todo.clear_completed()
        self.refresh()


    def refresh(self, keep=None):
        self.listbox.delete(0, tk.END)
        for task in self.todo.all():
            self.listbox.insert(tk.END, str(task))
            if task.done:
                self.listbox.itemconfig(tk.END, foreground="gray")

        if keep is not None and keep < len(self.todo):
            self.listbox.selection_set(keep)

        self.status.config(
            text=f"Toplam: {len(self.todo)}   "
                 f"Bekleyen: {len(self.todo.pending())}   "
                 f"Biten: {len(self.todo.completed())}"
        )


if __name__ == "__main__":
    todo = TodoList(" ")
    todo.add("Diferansiyel çalış", "yüksek")
    todo.add("Java OOP")

    app = TodoApp(todo)
    app.mainloop()