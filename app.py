import pandas as pd
import plotly.express as px
import streamlit as st
import os

st.set_page_config(page_title="Wisata Indonesia — Dashboard", layout="wide")
# ======== SOFT EARTH TONE THEME CSS ========
st.markdown("""
<style>

:root {
    --bg: #faf6f0;
    --panel: #ffffff;
    --text: #3f3a36;
    --muted: #7a7169;
    --primary: #c2955f;
    --accent: #6d8f6e;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
}

[data-testid="stSidebar"] {
    background: #f2ebe4 !important;
    padding: 1.5rem 1rem !important;
    border-right: 1px solid #e0d7ce !important;
}

h1, h2, h3, h4 {
    color: var(--text) !important;
    font-weight: 700 !important;
}

.stButton>button {
    background-color: var(--primary) !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
}

.stMetric {
    background: var(--panel) !important;
    padding: 1.2rem !important;
    border-radius: 12px !important;
    border: 1px solid #e5ddd3 !important;
}

</style>
""", unsafe_allow_html=True)


st.title("🗺️ Dashboard Wisata Indonesia")

# ========= LOAD DATA ===========
if not os.path.exists("wisata_indonesia.csv"):
    st.error("File 'wisata_indonesia.csv' tidak ditemukan! Taruh di folder yang sama dengan app.py")
    st.stop()

df = pd.read_csv("wisata_indonesia.csv")

# ========= FILTERS =============
st.sidebar.header("Filter")

kategori = st.sidebar.multiselect(
    "Pilih Kategori",
    df["category"].unique(),
    default=df["category"].unique(),
)

prov = st.sidebar.multiselect(
    "Pilih Provinsi",
    df["province"].unique(),
    default=df["province"].unique(),
)

df_filtered = df[
    (df["category"].isin(kategori)) &
    (df["province"].isin(prov))
]

# ========= METRICS ============
col1, col2, col3 = st.columns(3)
col1.metric("Total Destinasi", len(df_filtered))
col2.metric("Rata² Rating", round(df_filtered["rating"].mean(), 2))
col3.metric("Total Ulasan", df_filtered["review_count"].sum())

# ======== INSIGHT RATING PROVINSI ========
avg_by_province = df_filtered.groupby("province")["rating"].mean().sort_values(ascending=False)
top_province = avg_by_province.index[0]
top_rating = round(avg_by_province.iloc[0], 2)

st.info(f"📌 **Rating rata-rata tertinggi berasal dari provinsi `{top_province}` dengan nilai {top_rating}.**")


# ========= BAR CHART ============
st.subheader("📊 Top 10 Destinasi Berdasarkan Jumlah Ulasan")
top10 = df_filtered.sort_values("review_count", ascending=False).head(10)
fig_bar = px.bar(top10, x="name", y="review_count", color="category")
st.plotly_chart(fig_bar, use_container_width=True)

# ========= PIE CHART ============
st.subheader("🧁 Distribusi Kategori Wisata")
fig_pie = px.pie(df_filtered, names="category", hole=0.3)
st.plotly_chart(fig_pie, use_container_width=True)

# ========= MAP ============
st.subheader("🗺️ Peta Interaktif Destinasi Wisata")
fig_map = px.scatter_mapbox(
    df_filtered,
    lat="lat",
    lon="lon",
    size="review_count",
    color="rating",
    hover_name="name",
    zoom=4,
    mapbox_style="open-street-map"
)
st.subheader("📈 Scatter: Rating vs Jumlah Ulasan")
fig_scatter = px.scatter(
    df_filtered, x="rating", y="review_count", color="category",
    hover_name="name", trendline="ols"
)
st.plotly_chart(fig_scatter, use_container_width=True)
st.caption("Insight: Titik mewakili destinasi; tren menggambarkan korelasi antara rating dan popularitas.")

st.subheader("📊 Distribusi Rating (Histogram)")
fig_hist = px.histogram(df_filtered, x="rating", nbins=20, color="category")
st.plotly_chart(fig_hist, use_container_width=True)
st.caption("Insight: Menunjukkan sebaran rating destinasi pada data terfilter.")

st.plotly_chart(fig_map, use_container_width=True)
