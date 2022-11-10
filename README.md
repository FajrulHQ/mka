## MKA Project

> Repository terkait tugas dan project selama berkuliah di **Magister Kecerdasan Artifisial UGM**
----
Menggunakan documentation dari `django_rest_framework` 

### Installation
1. Clone the app
2. Activasi virtual environment python
3. Install dependencies: 
```
pip install -r requirements.txt
```
4. Migrasi database: 
```
python manage.py migrate
```
5. Collect file static: 
```
python manage.py collectstatic --noinput
```
6. Jalankan server: 
```
python manage.py runserver
```
7. Server berjalan di `http://localhost:8000`


### Mata Kuliah
1. Prinsip Kecerdasan Artifisial (PKA)
   - [Shortest Path using Greedy and A*](search_algorithm/notebook)
2. etc