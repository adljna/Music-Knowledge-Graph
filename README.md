# 🎵 Music Knowledge Graph Analysis

**Wikidata & DBpedia Integration with Graph Data Science**

---

## 📌 Overview

Project ini bertujuan untuk membangun **Knowledge Graph di domain musik** dengan mengintegrasikan data dari dua sumber terbuka, yaitu **Wikidata** dan **DBpedia**.

Setelah proses integrasi data, dilakukan analisis menggunakan **Graph Data Science (GDS)** untuk mengeksplorasi struktur jaringan musik, hubungan antar entitas, serta menemukan pola tersembunyi.

---

## 🎯 Objectives

* Menggabungkan data musik dari Wikidata dan DBpedia
* Membersihkan dan menormalisasi data
* Membangun graph berbasis relasi musik
* Melakukan analisis graph menggunakan:

  * Similarity
  * Centrality
  * Community Detection

---

## 📊 Study Case

Dataset yang digunakan berfokus pada entitas berikut:

* 🎵 Song
* 🎤 Artist (Performer, Composer, Lyricist, Producer)
* 🎼 Genre
* 🏷️ Record Label
* 🌍 Country

### 🔗 Sumber Data

* Wikidata (SPARQL endpoint)
* DBpedia (SPARQL endpoint)

Data diambil dalam bentuk CSV, kemudian dilakukan proses integrasi menggunakan Python.

---

## ⚙️ Data Integration Process

Tahapan utama integrasi data:

1. **Data Extraction**
   Mengambil data dari Wikidata dan DBpedia menggunakan SPARQL query

2. **Data Cleaning**

   * Menghapus karakter khusus
   * Normalisasi teks
   * Menghapus data tidak valid

3. **Data Joining**

   * Join berdasarkan:

     * `song`
     * `artist`
   * Menggunakan *outer join* (Pandas)

4. **Data Fusion**

   * Menggabungkan atribut dari kedua sumber
   * Menggunakan `combine_first()`

5. **Deduplication**

   * Menghapus data duplikat

📁 Output:

```bash
final_integrated_music.csv
```

---

## 🔍 Graph Algorithms

### 1. 🔗 Similarity (Jaccard Similarity)

Digunakan untuk mengukur kemiripan antar node berdasarkan relasi yang dimiliki.

**Insight:**

* Artist yang memiliki pola kolaborasi atau genre yang mirip
* Rekomendasi artist serupa

---

### 2. ⭐ Centrality (Betweenness Centrality)

Mengukur seberapa penting suatu node sebagai penghubung dalam graph.

**Insight:**

* Artist yang menjadi “bridge” antar komunitas
* Node strategis dalam jaringan musik

---

### 3. 🧩 Community Detection (Louvain)

Digunakan untuk mengelompokkan node ke dalam komunitas berdasarkan keterhubungan.

**Insight:**

* Cluster artist berdasarkan pola kolaborasi
* Struktur komunitas dalam industri musik

---

## 🛠️ Tech Stack

* Python (Pandas) → Data Integration
* SPARQL → Data Extraction
* Neo4j Graph Data Science → Graph Analysis

---

## 📈 Output & Insights

Dari analisis graph, project ini dapat:

* Mengidentifikasi artist yang berperan sebagai penghubung
* Menemukan kemiripan antar artist
* Mengelompokkan komunitas musik
* Mengungkap struktur tersembunyi dalam jaringan musik

---

## 🚀 How to Run

1. Clone repository

```bash
git clone https://github.com/your-username/music-knowledge-graph-analysis.git
```

2. Jalankan script integrasi data

```bash
python integration-data.py
```

3. Import CSV ke Neo4j

4. Jalankan Graph Data Science algorithms

---

## 📌 Conclusion

Project ini menunjukkan bagaimana **Knowledge Graph** dapat digunakan untuk mengintegrasikan data dari berbagai sumber dan menghasilkan insight yang tidak dapat diperoleh dari data tabular biasa.

---

## 👩‍💻 Author

* Nesha Shafwana - 5026231013
* Nailah Adlina - 5026231068

---
