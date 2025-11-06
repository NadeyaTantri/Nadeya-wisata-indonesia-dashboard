# Wisata Indonesia — Dashboard (Streamlit)

Dashboard interaktif untuk mengeksplorasi destinasi wisata Indonesia berdasarkan kategori, provinsi, rating, dan popularitas (jumlah ulasan).

## Fitur
- Filter kategori & provinsi
- 3+ visual: Bar (Top 10 review), Pie (distribusi kategori), Map (lokasi), *opsional*: Scatter & Histogram
- Insight otomatis: provinsi dengan rata-rata rating tertinggi
- Desain tema Soft Earth Tone

## Cara Jalankan (Lokal)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```

## Deploy ke Streamlit Community Cloud
1. Push file: `app.py`, `requirements.txt`, `wisata_indonesia.csv`, `.gitignore`
2. Buka https://share.streamlit.io (Streamlit Community Cloud) → `New app`
3. Pilih repo & branch (`main`), file path: `app.py` → Deploy
4. Dapatkan URL publik (kumpulkan link tersebut)

## Requirements
Lihat `requirements.txt`:
```
streamlit
pandas
plotly
statsmodels
```

## Struktur Proyek
```
.
├─ app.py
├─ requirements.txt
├─ wisata_indonesia.csv
└─ .gitignore
```

## Catatan
- Pastikan `wisata_indonesia.csv` berada di folder yang sama dengan `app.py`.
- Jika build gagal, cek log di Streamlit Cloud dan pastikan nama file/path sesuai.
