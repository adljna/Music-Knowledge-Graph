import re
import pandas as pd

# 1. LOAD DATA
wikidata = pd.read_csv(r"C:\Users\Lenovo\Documents\COLLEGE\SEMESTER 6\GRAF PENGETAHUAN\UTS\wikidata.csv")
dbpedia = pd.read_csv(r"C:\Users\Lenovo\Documents\COLLEGE\SEMESTER 6\GRAF PENGETAHUAN\UTS\dbpedia.csv")

# 2. TEXT CLEANING FUNCTION
def clean_text(x):
    """Membersihkan teks (hapus kurung, simbol, karakter aneh)"""
    if pd.isna(x):
        return ""

    x = str(x)
    # hapus isi dalam kurung
    x = re.sub(r"\(.*?\)", "", x)
    # lowercase
    x = x.lower().strip()
    # hapus non-ASCII (Ã³ dll)
    x = re.sub(r"[^\x00-\x7F]+", "", x)
    # hanya huruf, angka, spasi
    x = re.sub(r"[^a-z0-9\s]", "", x)
    # rapikan spasi
    x = re.sub(r"\s+", " ", x)

    return x.strip()

# 3. APPLY CLEANING (SEMUA KOLOM)
for df in [wikidata, dbpedia]:
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].apply(clean_text)

# 4. BUAT KOLOM UNTUK JOIN
for df in [wikidata, dbpedia]:
    df["song_clean"] = df["songLabel"]
    df["artist_clean"] = df["contributorLabel"]

# 5. REMOVE INVALID DATA
wikidata = wikidata[
    (wikidata["song_clean"] != "") &
    (wikidata["artist_clean"] != "")
]

dbpedia = dbpedia[
    (dbpedia["song_clean"] != "") &
    (dbpedia["artist_clean"] != "")
]

# 6. REMOVE DUPLICATES (PRE-JOIN)
wikidata = wikidata.drop_duplicates(
    subset=["song_clean", "artist_clean", "role"]
)

dbpedia = dbpedia.drop_duplicates(
    subset=["song_clean", "artist_clean", "role"]
)

# 7. MERGE DATA (OUTER JOIN)
merged = pd.merge(
    wikidata,
    dbpedia,
    on=["song_clean", "artist_clean"],
    how="outer",
    suffixes=("_wd", "_db")
)

# 8. CLEAN & NORMALISASI COUNTRY
def clean_country(x):
    if pd.isna(x):
        return pd.NA

    x = str(x).strip()

    # handle URI DBpedia
    if "dbpedia.org/resource/" in x:
        x = x.split("/")[-1]
        x = x.replace("_", " ")

    x = x.lower()

    mapping = {
        "united states womens national soccer team": "united states",
        "united states women's national soccer team": "united states",
        "usa": "united states",
        "u s a": "united states"
    }

    x = mapping.get(x, x)
    # capitalize
    x = " ".join(word.capitalize() for word in x.split())

    return x

# combine country
merged["country"] = merged["countryLabel_wd"].combine_first(
    merged["countryLabel_db"]
)

merged["country"] = merged["country"].apply(clean_country)
merged["country"] = merged["country"].replace("", pd.NA)
merged = merged[merged["country"].notna()]

# 9. REMOVE DUPLICATES (POST-JOIN)
merged = merged.drop_duplicates(
    subset=["song_clean", "artist_clean", "role_wd", "role_db"]
)

# 10. DATA FUSION (GABUNG KOLOM)
merged["song"] = merged["songLabel_wd"].combine_first(merged["songLabel_db"])
merged["artist"] = merged["contributorLabel_wd"].combine_first(merged["contributorLabel_db"])
merged["role"] = merged["role_wd"].combine_first(merged["role_db"])
merged["genre"] = merged["genreLabel_wd"].combine_first(merged["genreLabel_db"])
merged["label"] = merged["recordLabelLabel_wd"].combine_first(merged["recordLabelLabel_db"])

# 11. FINAL DATASET
final = merged[
    ["song", "artist", "role", "genre", "label", "country"]
]

final = final.drop_duplicates()

# 12. EXPORT CSV
final.to_csv("final_integrated_music.csv", index=False)

print("Selesai! File tersimpan sebagai final_integrated_music.csv")