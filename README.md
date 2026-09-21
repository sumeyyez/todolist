EN
# TodoList
A simple to-do list application written in Python with Tkinter.
Built as an object-oriented programming (OOP) exercise.

## Features
- Add and delete tasks
- Set priority (low/normal/high)
- Mark tasks as done (double-clicking a list item works too)
- Clear all completed tasks at once
- Total/pending/completed counters

## Installation and usage
No extra libraries are required; Tkinter ships with Python.

```bash
git clone https://github.com/[your-username]/todolist5.git
cd todolist5
python main.py
```
## Structure
The application is split into two layers:
- **Logic layer** — the `Task` and `TodoList` classes. Completely independent of the
  interface; they know nothing about Tkinter. This means the same classes could later
  be wired up to a web interface.
- **Interface layer** — the `TodoApp` class. It only draws the screen and holds no data
  of its own; everything is asked of the `TodoList` object.

## Ideas for future development
- Saving tasks to a JSON file and loading them at startup
- Adding due dates
- Sorting tasks by priority





TR
# TodoList
Python ve Tkinter ile yazılmış basit bir yapılacaklar listesi uygulaması.
Nesne yönelimli programlama (OOP) pratiği olarak geliştirildi.

## Özellikler
- Görev ekleme ve silme
- Öncelik belirleme (düşük/normal/yüksek)
- Görevi tamamlandı olarak işaretleme (listeye çift tıklayarak da olur)
- Tamamlanan görevleri toplu temizleme
- Toplam/bekleyen/biten sayaçları

## Kurulum ve çalıştırma
Ek bir kütüphane gerekmiyor; Tkinter Python ile birlikte gelir.

```bash
git clone https://github.com/[kullanici-adin]/todolist5.git
cd todolist5
python main.py
```
## Yapı
Uygulama iki katmana ayrılmıştır:
- **Mantık katmanı** — `Task` ve `TodoList` sınıfları. Arayüzden tamamen bağımsızdır,
  Tkinter'ı hiç bilmez. Bu sayede aynı sınıflar ileride bir web arayüzüne de bağlanabilir.
- **Arayüz katmanı** — `TodoApp` sınıfı. Yalnızca ekranı çizer, veriyi kendisi tutmaz;
  her şeyi `TodoList` nesnesine sorar.

## Geliştirme fikirleri
- Görevleri JSON dosyasına kaydetme, açılışta geri yükleme
- Son tarih (deadline) ekleme
- Görevleri önceliğe göre sıralama
