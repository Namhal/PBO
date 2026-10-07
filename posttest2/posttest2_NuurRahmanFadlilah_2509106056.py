import os
os.system("cls" if os.name == "nt" else "clear")


class ProfilUser:
    def __init__(self, nama, username):
        self.nama = nama
        self.username = username
        self.level = "Pemula"

    def tampilkan(self):
        print("Profil       :", self.nama)
        print("Username     :", self.username)
        print("Level        :", self.level)


class User:
    nama_aplikasi = "MyAchivement"
    jumlah_user = 0

    def __init__(self, nama, username):
        self.nama = nama
        self.username = username
        self.__password = "12345"
        self._categories = []
        self.__profil = ProfilUser(nama, username)
        User.jumlah_user += 1

    def tampilkan(self):
        print(self.nama, "-", self.username)

    def tampilkan_profil(self):
        self.__profil.tampilkan()

    def tambah_category(self, category):
        self._categories.append(category)

    def tampilkan_category(self):
        print("Category milik", self.username, ":")
        for category in self._categories:
            print("-", category.nama)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_baru):
        if len(password_baru) < 5:
            print("Password minimal 5 karakter")
        else:
            self.__password = password_baru
            print("Password berhasil diubah")

    @classmethod
    def info_aplikasi(cls):
        print("Aplikasi:", cls.nama_aplikasi)
        print("Jumlah user:", cls.jumlah_user)

    @staticmethod
    def cek_username(username):
        return len(username) >= 3


class Category:
    nama_aplikasi = "MyAchivement"
    jumlah_category = 0

    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi
        Category.jumlah_category += 1

    def tampilkan(self):
        print(self.nama, "-", self.deskripsi)

    @classmethod
    def total_category(cls):
        print("Total category:", cls.jumlah_category)

    @staticmethod
    def cek_nama(nama):
        return nama.strip() != ""


class Achievement:
    status_default = "Belum Selesai"
    jumlah_achievement = 0

    def __init__(self, nama, kategori, user):
        self._nama = nama
        self._kategori = kategori
        self._user = user
        self.__status = Achievement.status_default
        Achievement.jumlah_achievement += 1

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru.lower() == "selesai":
            self.__status = "Selesai"
        elif status_baru.lower() == "belum selesai":
            self.__status = "Belum Selesai"
        else:
            print("Status hanya boleh Selesai atau Belum Selesai")

    def tampilkan(self):
        print("Achievement :", self._nama)
        print("Kategori    :", self._kategori.nama)
        print("User        :", self._user.username)
        print("Status      :", self.__status)

    @classmethod
    def info_achievement(cls):
        print("Total achievement:", cls.jumlah_achievement)

    @staticmethod
    def cek_nama(nama):
        return nama.strip() != ""


class AchievementKuliah(Achievement):
    def __init__(self, nama, kategori, user, tingkat_kesulitan):
        super().__init__(nama, kategori, user)
        self.tingkat_kesulitan = tingkat_kesulitan

    def tampilkan(self):
        print("Achievement :", self._nama)
        print("Kategori    :", self._kategori.nama)
        print("User        :", self._user.username)
        print("Tingkat     :", self.tingkat_kesulitan)
        print("Status      :", self.status)


class AchievementPribadi(Achievement):
    def __init__(self, nama, kategori, user, target):
        super().__init__(nama, kategori, user)
        self.target = target


print("==----------------==")
print("===-MYACHIVEMENT-===")
print("==----------------==")

print("\n- CLASS USER -")
user1 = User("Rahman", "rahman")
user2 = User("Yusa", "yusa")

user1.tampilkan()
user2.tampilkan()

print("\n- CLASS PROFIL USER -")
user1.tampilkan_profil()
print()
user2.tampilkan_profil()

print("\n- CLASS CATEGORY -")
category1 = Category("Kuliah", "Achievement tentang perkuliahan")
category2 = Category("Pribadi", "Achievement tentang kehidupan sehari-hari")

category1.tampilkan()
category2.tampilkan()

print("\n- RELASI AGREGASI -")
user1.tambah_category(category1)
user1.tambah_category(category2)
user2.tambah_category(category2)

user1.tampilkan_category()
user2.tampilkan_category()

print("\n- CLASS ACHIEVEMENT -")
achievement1 = AchievementKuliah(
    "Menyelesaikan Tugas PBO",
    category1,
    user1,
    "Tinggi"
)

achievement2 = AchievementPribadi(
    "Lari 10 Kilometer",
    category2,
    user2,
    "10 Kilometer"
)

achievement1.tampilkan()
print()
achievement2.tampilkan()

print("\n- RELASI ASOSIASI -")
print("Achievement 1 terhubung dengan user:", achievement1._user.username)
print("Achievement 1 terhubung dengan category:", achievement1._kategori.nama)

print("\n- RELASI KOMPOSISI -")
print("Profil user1 dimiliki oleh:", user1.username)
print("Profil user2 dimiliki oleh:", user2.username)

print("\n- INSTANCE METHOD -")
user1.tampilkan()
category1.tampilkan()
achievement1.tampilkan()

print("\n- STATIC METHOD -")
print("Cek username 'rahman':", User.cek_username("rahman"))
print("Cek username 'ab':", User.cek_username("ab"))
print("Cek nama category 'Kuliah':", Category.cek_nama("Kuliah"))
print("Cek nama achievement kosong:", Achievement.cek_nama(""))

print("\n- CLASS METHOD -")
User.info_aplikasi()
Category.total_category()
Achievement.info_achievement()

print("\n- SETTER VALID -")
user1.password = "rahasia"
print("Password user1:", user1.password)

achievement1.status = "Selesai"
print("Status achievement1:", achievement1.status)

print("\n- SETTER TIDAK VALID -")
user1.password = "123"
print("Password user1:", user1.password)

achievement1.status = "Sedang Berjalan"
print("Status achievement1:", achievement1.status)