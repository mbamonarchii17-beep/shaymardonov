"""
QurilishMart — Qurilish Mollari
================================
Streamlit ilovasi. HTML/CSS/JS ni to'liq yuklaydi.

Ishga tushirish:
    streamlit run app.py

Talab qilinadigan kutubxonalar:
    pip install streamlit
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# ── Sahifa sozlamalari ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="QurilishMart — Qurilish Mollari",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS: Streamlit default elementlarini yashirish ──────────────────────────
st.markdown(
    """
    <style>
        /* Streamlit toolbar va padding-larni olib tashlash */
        #MainMenu { visibility: hidden; }
        header[data-testid="stHeader"] { display: none; }
        footer { visibility: hidden; }
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] {
            padding: 0;
        }
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }
        iframe {
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── HTML faylni o'qish ──────────────────────────────────────────────────────
HTML_FILE = os.path.join(os.path.dirname(__file__), "index.html")

@st.cache_resource
def load_html(path: str) -> str:
    """HTML faylni kesh bilan yuklaydi."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if os.path.exists(HTML_FILE):
    html_content = load_html(HTML_FILE)
else:
    st.error(
        "❌ `index.html` fayli topilmadi. "
        "Iltimos, `app.py` va `index.html` ni bir papkaga joylashtiring."
    )
    st.stop()

# ── HTML ni Streamlit ichida ko'rsatish ────────────────────────────────────
components.html(
    html_content,
    height=5000,      # Butun sahifani ko'rsatish uchun katta qiymat
    scrolling=False,  # Ichki scroll o'rniga tashqi sahifa scrolli
)
