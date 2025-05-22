# Warehouse Monitoring System with Kafka and Spark
## Fikri Aulia As Sa'adi - 5027231026

## Deskripsi

Proyek ini bertujuan untuk memonitor suhu dan kelembaban di beberapa gudang menggunakan Apache Kafka untuk pengiriman data secara real-time dan Apache Spark untuk pemrosesan stream data. Data suhu dan kelembaban dikirimkan oleh dua produser Kafka yang memproduksi data secara acak, yang kemudian diproses oleh Spark untuk menghasilkan laporan status gudang dan memberikan peringatan berdasarkan ambang batas suhu dan kelembaban yang ditetapkan.

## Komponen

### 1. **Kafka Producer (sensor-suhu-gudang dan sensor-kelembaban-gudang)**

Produser Kafka bertanggung jawab untuk mengirimkan data suhu dan kelembaban ke Kafka broker. Setiap data yang dikirim terdiri dari:

- **gudang_id**: Identifikasi Gudang (misal: G1, G2, G3)
- **suhu/kelembaban**: Nilai suhu atau kelembaban yang diukur
- **timestamp**: Waktu saat data dihasilkan (dalam format UNIX timestamp)

#### File:
- [producer_suhu.py](file-4NnXChUemeSggN1e3BF5DX)
- [producer_kelembaban.py](file-DP8aE8FwdYHeEVfpNQ8t6Q)

### 2. **Kafka Consumer (Spark Streaming)**

Spark Streaming mengambil stream data suhu dan kelembaban dari Kafka dan melakukan analisis berdasarkan kondisi tertentu:

- Peringatan suhu tinggi (suhu > 80°C)
- Peringatan kelembaban tinggi (kelembaban > 70%)
- Laporan status gabungan berdasarkan suhu dan kelembaban

Hasil dari stream ini mencetak status gudang ke console dan memberikan peringatan jika data memenuhi kriteria yang ditetapkan.

#### File:
- [spark_consumer.py](file-AyM5NezknA1BcXWLerHp3w)

### 3. **Docker Compose**

File `docker-compose.yml` digunakan untuk mengatur dan menjalankan lingkungan yang dibutuhkan untuk Kafka, Zookeeper, dan Spark. Ini mencakup layanan untuk Zookeeper, Kafka broker, Spark master dan worker, serta Spark History Server (opsional).

#### File:
- [docker-compose.yml](file-KGJqourU7h546iKyUULEp6)

## Langkah-langkah untuk Menjalankan Proyek

1. **Persyaratan**:
   - Docker dan Docker Compose harus sudah terpasang di sistem Anda.
   - Pastikan Apache Kafka dan Zookeeper dapat berjalan di dalam container Docker.

2. **Menjalankan Kafka dan Spark dengan Docker Compose**:
   Jalankan perintah berikut untuk memulai semua layanan menggunakan Docker Compose:

   ```bash
   docker-compose up
   
3. ** Menjalankan Kafka Producer
Jalankan produser suhu dan kelembaban secara terpisah di terminal:

```bash
python producer_suhu.py
python producer_kelembaban.py
```

4. ** Menjalankan Spark Consumer
Jalankan aplikasi Spark Streaming untuk memproses data dari Kafka:

```bash
python spark_consumer.py
```

5. ** Dokumentasi
- Producer

![Screenshot 2025-05-22 233151](https://github.com/user-attachments/assets/8635345b-9f0b-4deb-832b-4c3b90a90cdc)
![Screenshot 2025-05-22 232902](https://github.com/user-attachments/assets/9db60a76-84ef-41d5-9d87-977f8fb3e059)

- Spark

![Screenshot 2025-05-22 233430](https://github.com/user-attachments/assets/d74a656c-1135-4d7f-8fa8-399e88cdb618)

- Peringatan jika melewati batas

![Screenshot 2025-05-22 233655](https://github.com/user-attachments/assets/b9f7faa8-8626-4100-9c35-2b62a01d1d38)





