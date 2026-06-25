import streamlit as st
import streamlit.components.v1 as components

# Streamlit sahifa sozlamalari
st.set_page_config(
    page_title="QurilishMart — Qurilish Mollari",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML, CSS va JS kodlarini birlashtirgan to'liq tuzilma
html_content = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>QurilishMart — Qurilish Mollari</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    /* Umumiy stillar (Sodda dizayn) */
    body {
      font-family: 'Inter', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9fafb;
      color: #1f2937;
    }
    .container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      box-sizing: border-box;
    }
    header {
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 15px 0;
    }
    .header__inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .logo {
      font-size: 24px;
      font-weight: 700;
      text-decoration: none;
      color: #111827;
    }
    .logo strong { color: #f97316; }
    nav a {
      margin-left: 20px;
      text-decoration: none;
      color: #4b5563;
      font-weight: 500;
    }
    nav a:hover { color: #f97316; }
    
    /* Hero Section */
    .hero {
      padding: 60px 0;
      background: linear-gradient(135deg, #fef3c7 0%, #fff7ed 100%);
      text-align: center;
    }
    .hero__title {
      font-size: 42px;
      font-weight: 800;
      color: #111827;
      margin-bottom: 20px;
    }
    .hero__accent { color: #f97316; }
    .hero__sub {
      font-size: 18px;
      color: #4b5563;
      max-width: 600px;
      margin: 0 auto 30px;
    }
    .btn {
      display: inline-block;
      padding: 12px 24px;
      font-weight: 600;
      border-radius: 6px;
      text-decoration: none;
      cursor: pointer;
    }
    .btn--primary {
      background: #f97316;
      color: #fff;
    }
    .btn--primary:hover { background: #ea580c; }
    
    /* Kategoriyalar va qolgan bo'limlar */
    section { padding: 60px 0; }
    .section-title {
      font-size: 28px;
      font-weight: 700;
      text-align: center;
      margin-bottom: 40px;
    }
    .categories__grid, .delivery__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
    }
    .cat-card, .delivery__card {
      background: #fff;
      padding: 30px 20px;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
      border: 1px solid #e5e7eb;
    }
    .cat-card__icon, .delivery__icon {
      font-size: 40px;
      margin-bottom: 15px;
    }
    
    /* Kalkulyator va B2B */
    .calculator { background: #f3f4f6; }
    .calc__box {
      background: #fff;
      padding: 30px;
      border-radius: 8px;
      max-width: 500px;
      margin: 0 auto;
      box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .calc__field { margin-bottom: 15px; }
    .calc__field label { display: block; margin-bottom: 5px; font-weight: 500; }
    .calc__input {
      width: 100%;
      padding: 10px;
      border: 1px solid #d1d5db;
      border-radius: 6px;
      box-sizing: border-box;
    }
    .calc__result-box {
      margin-top: 20px;
      padding: 15px;
      background: #ecfdf5;
      border-radius: 6px;
      color: #065f46;
      font-weight: 600;
      text-align: center;
    }
    
    footer {
      background: #111827;
      color: #9ca3af;
      padding: 40px 0;
      text-align: center;
      font-size: 14px;
    }
  </style>
</head>
<body>

  <!-- ===== HEADER ===== -->
  <header>
    <div class="container header__inner">
      <a href="#" class="logo">⚙ Qurilish<strong>Mart</strong></a>
      <nav>
        <a href="#catalog">Katalog</a>
        <a href="#calculator">Kalkulyator</a>
        <a href="#delivery">Yetkazib berish</a>
        <a href="#b2b">B2B</a>
      </nav>
    </div>
  </header>

  <!-- ===== HERO ===== -->
  <section class="hero">
    <div class="container">
      <h1 class="hero__title">Qurilish mollari — <span class="hero__accent">tez, arzon, ishonchli</span></h1>
      <p class="hero__sub">Sement, kafel, bo'yoq, laminat va yana ko'plab mahsulotlar. Prorablar va uy egalari uchun qulaylik.</p>
      <a href="#catalog" class="btn btn--primary">Katalogni ko'rish</a>
    </div>
  </section>

  <!-- ===== CATEGORIES ===== -->
  <section id="catalog">
    <div class="container">
      <h2 class="section-title">Kategoriyalar</h2>
      <div class="categories__grid">
        <div class="cat-card">
          <div class="cat-card__icon">🪣</div>
          <h3>Sement va qum</h3>
        </div>
        <div class="cat-card">
          <div class="cat-card__icon">🪟</div>
          <h3>Kafel va plitka</h3>
        </div>
        <div class="cat-card">
          <div class="cat-card__icon">🎨</div>
          <h3>Bo'yoq va lak</h3>
        </div>
        <div class="cat-card">
          <div class="cat-card__icon">🪵</div>
          <h3>Laminat va parket</h3>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CALCULATOR ===== -->
  <section class="calculator" id="calculator">
    <div class="container">
      <h2 class="section-title">Kalkulyator (Kafel hisoblagich)</h2>
      <div class="calc__box">
        <div class="calc__field">
          <label>Uzunlik (m)</label>
          <input type="number" id="len" value="4" oninput="calculate()" class="calc__input"/>
        </div>
        <div class="calc__field">
          <label>Kenglik (m)</label>
          <input type="number" id="wid" value="3" oninput="calculate()" class="calc__input"/>
        </div>
        <div class="calc__result-box">
          Jami maydon: <span id="res">12</span> kv.m
        </div>
      </div>
    </div>
  </section>

  <!-- ===== DELIVERY ===== -->
  <section id="delivery">
    <div class="container">
      <h2 class="section-title">Xizmatlarimiz</h2>
      <div class="delivery__grid">
        <div class="delivery__card">
          <div class="delivery__icon">🚛</div>
          <h3>Tezkor yetkazib berish</h3>
          <p>Toshkent bo'ylab buyurtma kuni yukingizni manzilingizga yetkazamiz.</p>
        </div>
        <div class="delivery__card">
          <div class="delivery__icon">💳</div>
          <h3>Qulay to'lov</h3>
          <p>Click, Payme, naqd yoki bank o'tkazmalari orqali to'lov imkoniyati.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer>
    <div class="container">
      <p>© 2026 QurilishMart. Barcha huquqlar himoyalangan.</p>
    </div>
  </footer>

  <script>
    function calculate() {
      let len = document.getElementById('len').value || 0;
      let wid = document.getElementById('wid').value || 0;
      document.getElementById('res').innerText = (len * wid).toFixed(1);
    }
  </script>
</body>
</html>
"""

# HTML elementni Streamlit interfeysiga chiqarish
components.html(html_content, height=1200, scroller=True)
