# MyAchivement
![judul](poto/1.png)

## Tentang Program

Ada tiga class utama, yaitu **User, Category, dan Achievement**. Class `User` digunakan untuk menyimpan data pengguna, `Category` digunakan untuk mengelompokkan pencapaian, sedangkan `Achievement` digunakan untuk menyimpan data pencapaian yang dimiliki oleh pengguna.

---

## Struktur Class

### 1. Class User

`User` untuk menyimpan data pengguna.

Atribut yang digunakan:
- `nama` simpen nama pengguna.
- `username` simpen username.
- `__password` sebagai atribut private untuk menyimpan password.
- `nama_aplikasi` dan `jumlah_user` sebagai atribut class.

Method yang digunakan:
- `tampilkan()` nampilin data user.
- `info_aplikasi()` untuk menampilkan nama aplikasi dan jumlah user.
- `cek_username()` sebagai static method untuk mengecek username.
- `password` sebagai getter dan setter untuk mengakses dan mengubah password dengan validasi.

Ada dua objek User, yaitu **Rahman** dan **Yusa**.

### 2. Class Category

`Category` dipake untuk mengelompokkan achievement berdasarkan kategorinya.

Atribut yang digunakan:
- `nama` nyimpan nama kategori.
- `deskripsi` nyimpan penjelasan kategori.
- `nama_aplikasi` dan `jumlah_category` sebagai atribut class.

Method yang digunakan:
- `tampilkan()` untuk menampilkan data kategori.
- `total_category()` nampilin jumlah kategori.
- `cek_nama()` sebagai static method untuk mengecek nama kategori.

Ada dua objek Category, yaitu **Kuliah** dan **Pribadi**.

### 3. Class Achievement

Class `Achievement` digunakan untuk menyimpan data pencapaian yang dimiliki oleh user.

Atribut yang digunakan:
- `nama` nyimpan nama achievement.
- `kategori` untuk menghubungkan achievement dengan objek Category.
- `user` untuk menghubungkan achievement dengan objek User.
- `__status` sebagai atribut private untuk menyimpan status achievement.
- `status_default` dan `jumlah_achievement` sebagai atribut class.

Method yang digunakan:
- `tampilkan()` nampilkan informasi achievement.
- `info_achievement()` untuk menampilkan jumlah achievement.
- `cek_nama()` sebagai static method untuk mengecek nama achievement.
- `status` sebagai getter dan setter untuk melihat serta mengubah status achievement dengan validasi.

Ada dua objek Achievement, yaitu **Membaca 3 Buku** dan **Lari 10 Kilometer**.

---

## Uji Program

### 1. Pengujian Objek User, Category, dan Achievement

Bagian ini dibuat masing-masing dua objek dari setiap class. Hasilnya kemudian ditampilkan untuk memastikan data dari setiap objek berhasil dibuat.

![Uji Objek](poto/2.png)

**Keterangan:**  
Hasilnya menunjukkan dua user yaitu Rahman dan Yusa, dua category yaitu Kuliah dan Pribadi, serta dua achievement yang berhasil ditampilkan. Achievement juga menunjukkan hubungan dengan user dan category.

---

### 2. Pengujian Instance Method

Instance method digunakan untuk menampilkan data dari masing-masing objek. Method `tampilkan()` digunakan pada class User, Category, dan Achievement.

![Uji Instance Method](poto/3.png)

**Keterangan:**  
Method `tampilkan()` berhasil menampilkan data dari objek yang dipanggil. Jadi setiap objek dapat menampilkan datanya sendiri.

---

### 3. Pengujian Static Method

Static method digunakan sebagai fungsi bantuan tanpa menggunakan `self`

![Uji Static Method](poto/4.png)

**Keterangan:**  
Dilakukan pengecekan username, nama category, dan nama achievement. Hasil `True` berarti data memenuhi syarat, sedangkan `False` berarti data tidak memenuhi syarat.

---

### 4. Pengujian Class Method

Class method digunakan untuk mengakses informasi yang dimiliki bersama oleh seluruh objek dalam suatu class.

![Uji Class Method](poto/5.png)

**Keterangan:**  
Hasil menampilkan nama aplikasi, jumlah user, jumlah category, dan jumlah achievement. Datanya berasal dari atribut class.

---

### 5. Pengujian Setter dengan Data Valid

Setter digunakan untuk mengubah atribut private melalui property. Bagian ini digunakan data yang sesuai dengan aturan yang sudah dibuat.

![Uji Setter Valid](poto/6.png)

**Keterangan:**  
Password berhasil diubah menjadi `rahasia` karena memenuhi syarat minimal lima karakter. Status achievement juga berhasil diubah menjadi `Selesai`.

---

### 6. Pengujian Setter dengan Data Tidak Valid

Setelah data valid, setter diuji lagi menggunakan data yang tidak sesuai dengan aturan validasi.

![Uji Setter Tidak Valid](poto/7.png)

**Keterangan:**  
Password `123` tertolak karena kurang dari lima karakter. Status `Sedang Berjalan` juga ditolak karena status yang diperbolehkan hanya `Selesai` dan `Belum Selesai`. Data sebelumnya tetap tersimpan.

---