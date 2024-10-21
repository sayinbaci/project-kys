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

## Blog Sitesi Ekranları

İlk açılan sayfa herkes için Anasayfadır.

### Anasayfa
Ziyarteçler için görünen Anasayfa
![image](https://github.com/user-attachments/assets/229811d6-6496-498a-b8e4-4937b75b4d38)

### Üye Olma Sayfası
![image](https://github.com/user-attachments/assets/c492682d-7433-4ae3-9a75-f8b7656aff29)

### Giriş Yapma Sayfası
![image](https://github.com/user-attachments/assets/86e19573-96e5-4bea-811c-4c3596217d93)

Üye olmuş ve giriş yapmış bir kullanıcının göreceği Anasayfa aşağıdaki gibidir. Bu kullanıcı kendi eklediği gönderileri güncelleyebilir ve yeni gönderi ekleyebilir.

### Anasayfa 2
![image](https://github.com/user-attachments/assets/93d0c809-5ff0-486e-a426-4832efe6ad19)

![image](https://github.com/user-attachments/assets/fef40f03-94a3-4336-b2b3-dccd3f495f0e)

### Yeni Gönderi Ekranı
Giriş yapmış tüm kullanıcılar yeni gönderi ekleyebilmektedir.
![image](https://github.com/user-attachments/assets/d30d9d2d-5f8a-4f90-ba3c-b7dd5c09fba2)

### Gönderi İnceleme Ekranı
Gönderi inceleme ekranında giriş yapmış veya ziyaretçi olan tüm kullanıcılargönderiye yorum yapmayetkisine sahiptir.
![image](https://github.com/user-attachments/assets/f70071ed-30ca-4782-8e47-57114ea06ced)

### Filtreleme
Bu özellikle tüm gönderiler arasından filtreleme yapılabilmektedir.
![image](https://github.com/user-attachments/assets/74ff08af-aebc-4693-8b60-f97f1e815459)

### Profil Güncelleme
Üyelik oluşturmuş olan herkes üyelik bilgilerini Profil Güncelleme sayfasından güncelleyebilir.
![image](https://github.com/user-attachments/assets/a3ba1ea1-e748-4fb3-8629-a19d57798871)




