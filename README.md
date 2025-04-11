## 🌳 Decision Tree

**Decision Tree** adalah model machine learning berbentuk struktur pohon yang terdiri dari **node** (keputusan) dan **cabang** (konsekuensi). Model ini membagi dataset ke dalam subset yang semakin kecil dan homogen hingga ditemukan sebuah hasil akhir atau keputusan. Decision Tree populer karena sederhana dan sangat efektif untuk **klasifikasi** maupun **regresi**.

### 📚 Jenis-Jenis Decision Tree:

- **Classification Tree**  
  Untuk memecahkan masalah klasifikasi, di mana target (label) berupa data kategorikal.

- **Regression Tree**  
  Untuk memecahkan masalah regresi, dengan target berupa nilai kontinu.

- **Multi-output Tree**  
  Untuk kasus kompleks yang melibatkan lebih dari satu target, baik klasifikasi maupun regresi.

---

### 🔧 Tahapan Proses Pembuatan Decision Tree:

1. **Pengumpulan dan Persiapan Data**  
   - Menyediakan data target dan prediktor (fitur).
   - Data bisa berupa numerik maupun kategorikal.

2. **Pembentukan Model**  
   - Menggunakan algoritma seperti: `ID3`, `C4.5`, `CART`, atau `CHAID`.

3. **Pruning (Pemangkasan)**  
   - Menghapus cabang yang tidak penting agar model tidak overfitting.

4. **Evaluasi Model**  
   - Menggunakan data validasi/testing.
   - Metrik: Akurasi, Precision, Recall, F1-Score, dll.

5. **Prediksi Data Baru**  
   - Model digunakan untuk memprediksi target berdasarkan fitur input baru.

---

### ✅ Kelebihan Decision Tree:

- Mudah dipahami (interpretable)
- Cocok untuk data non-linier
- Tidak memerlukan normalisasi
- Mendukung data kategorikal
- Dapat digunakan untuk klasifikasi dan regresi
- Bisa menunjukkan fitur yang paling berpengaruh

---

### ⚠️ Kekurangan Decision Tree:

- Cenderung **overfitting** (terlalu pas dengan data latih)
- Tidak stabil terhadap perubahan data
- Kurang efisien untuk data kontinu (kecuali dengan binning/penyesuaian)
- Sensitif terhadap noise
- Memerlukan tuning parameter (seperti max_depth, min_samples_split, dll.)

### Pada notebook ini adalah latihan dari Decision Tree
