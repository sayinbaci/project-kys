# KYS PROJESİ

Bu proje kapsamında admin ve ziyaretçi için ayrı yetkilendirme olan blog sitesi oluşturulmuştur.

##### Admin
+ Gönderi paylaşabilmektedir.
+ Giriş çıkış yapabilmektedir.
+ Gönderi silme, düzenleme, inceleme yetkisine sahiptir.
+ Arama çubuğundan yazar, içerik ve başlık kullanarak arama yapabilir.

##### Ziyaretçi
+ Gönderileri inceleme yetkisine sahiptir.
+ Arama çubuğundan yazar, içerik ve başlık kullanarak arama yapabilir.

## Kullanılan Teknolojiler

- Django
- Sqlite3 (Şimdilik)

## Kurulum

İndirdikten sonra proje dizini cmd ekranında sırasıyla aşağıdaki adımları gerçekleştiriniz.

`virtualenv my_kys`

+ Mac & Linux: `my_kys/bin/activate`
+ Windows: `my_kys\Scripts\activate.bat`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuper`

`python manage.py runserver`

## Blog Sitesi

### 

