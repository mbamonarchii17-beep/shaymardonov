import streamlit as st
import streamlit.components.v1 as components

# Streamlit sahifa sozlamalari
st.set_page_config(
    page_title="QurilishMart — Qurilish Mollari",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Siz taqdim etgan to'liq va mukammal HTML/CSS/JS tuzilmasi
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
    /* BU YERGA STYLE.CSS ANDOZASIDAGI ASOSIY STILLAR INTEGRATSIYA QILINGAN */
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
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .logo strong { color: #f97316; }
    nav a {
      margin-left: 20px;
      text-decoration: none;
      color: #4b5563;
      font-weight: 500;
    }
    nav a:hover { color: #f97316; }
    
    .header__actions {
      display: flex;
      align-items: center;
      gap: 15px;
    }
    .search-bar {
      position: relative;
      display: flex;
      align-items: center;
    }
    .search-bar__input {
      padding: 8px 12px;
      border: 1px solid #d1d5db;
      border-radius: 6px;
      outline: none;
    }
    .search-bar__btn {
      background: none;
      border: none;
      cursor: pointer;
      margin-left: -30px;
      color: #6b7280;
    }
    .cart-btn {
      background: none;
      border: none;
      position: relative;
      cursor: pointer;
      color: #111827;
    }
    .cart-badge {
      position: absolute;
      top: -8px;
      right: -8px;
      background: #f97316;
      color: white;
      font-size: 11px;
      padding: 2px 6px;
      border-radius: 50%;
    }

    /* Hero Section */
    .hero {
      padding: 60px 0;
      background: linear-gradient(135deg, #fef3c7 0%, #fff7ed 100%);
    }
    .hero__inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 40px;
      flex-wrap: wrap;
    }
    .hero__content { flex: 1; min-width: 300px; }
    .hero__badge {
      display: inline-block;
      background: #ffedd5;
      color: #ea580c;
      padding: 6px 12px;
      border-radius: 20px;
      font-weight: 600;
      font-size: 14px;
      margin-bottom: 15px;
    }
    .hero__title {
      font-size: 42px;
      font-weight: 800;
      color: #111827;
      margin-bottom: 20px;
      line-height: 1.2;
    }
    .hero__accent { color: #f97316; }
    .hero__sub { font-size: 18px; color: #4b5563; margin-bottom: 30px; }
    .hero__cta { display: flex; gap: 15px; }
    
    .btn {
      display: inline-block;
      padding: 12px 24px;
      font-weight: 600;
      border-radius: 6px;
      text-decoration: none;
      cursor: pointer;
      border: none;
    }
    .btn--primary { background: #f97316; color: #fff; }
    .btn--primary:hover { background: #ea580c; }
    .btn--outline { background: transparent; border: 2px solid #d1d5db; color: #4b5563; }
    .btn--outline:hover { background: #f3f4f6; }
    .btn--full { width: 100%; margin-bottom: 10px; text-align: center; }

    .hero__visual { flex: 1; min-width: 300px; display: flex; justify-content: center; }
    .hero__card-stack { display: flex; flex-direction: column; gap: 15px; width: 100%; max-width: 350px; }
    .hero__card {
      background: white;
      padding: 15px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      gap: 15px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.05);
      border: 1px solid #e5e7eb;
    }
    .hero__card-icon { font-size: 24px; }
    .hero__card-name { font-weight: 600; }
    .hero__card-price { color: #f97316; font-size: 14px; font-weight: 500; }

    /* Kategoriyalar */
    .categories { padding: 60px 0; }
    .section-title { font-size: 28px; font-weight: 700; text-align: center; margin-bottom: 10px; }
    .section-sub { text-align: center; color: #6b7280; margin-bottom: 40px; }
    .categories__grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
    }
    .cat-card {
      background: #fff;
      padding: 25px 20px;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0,0,0,0.05);
      border: 1px solid #e5e7eb;
      cursor: pointer;
      transition: transform 0.2s;
    }
    .cat-card:hover { transform: translateY(-5px); }
    .cat-card__icon { font-size: 40px; margin-bottom: 15px; }
    .cat-card__name { font-weight: 600; font-size: 16px; margin-bottom: 5px; }
    .cat-card__count { color: #9ca3af; font-size: 13px; }

    /* Kalkulyator mukammal dizayni */
    .calculator { background: #f3f4f6; padding: 60px 0; }
    .calc__tabs { display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; }
    .calc__tab {
      background: #fff;
      padding: 10px 20px;
      border-radius: 20px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid #d1d5db;
    }
    .calc__tab--active { background: #f97316; color: white; border-color: #f97316; }
    .calc__panels { background: #fff; padding: 30px; border-radius: 12px; max-width: 700px; margin: 0 auto; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .calc__panel { display: none; }
    .calc__panel--active { display: block; }
    .calc__row { display: flex; gap: 15px; margin-bottom: 15px; flex-wrap: wrap; }
    .calc__field { flex: 1; min-width: 140px; }
    .calc__field label { display: block; margin-bottom: 5px; font-weight: 500; font-size: 14px; }
    .calc__input { width: 100%; padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; box-sizing: border-box; }
    .calc__result { margin-top: 25px; padding: 20px; background: #f0fdf4; border-radius: 8px; border: 1px solid #bbf7d0; }
    .calc__result-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; text-align: center; margin-bottom: 15px; }
    .calc__result-val { display: block; font-size: 24px; font-weight: 700; color: #16a34a; }
    .calc__result-key { color: #4b5563; font-size: 13px; }

    /* Yetkazib berish va B2B */
    .delivery__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; padding: 40px 0; }
    .delivery__card { background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.03); border: 1px solid #e5e7eb; }
    .delivery__icon { font-size: 32px; margin-bottom: 10px; }
    .b2b { background: #111827; color: white; padding: 60px 0; }
    .b2b__inner { display: flex; justify-content: space-between; align-items: center; gap: 40px; flex-wrap: wrap; }
    .b2b__content { flex: 1; min-width: 300px; }
    .b2b__badge { color: #f97316; font-weight: 600; margin-bottom: 10px; }
    .b2b__list { list-style: none; padding: 0; margin: 20px 0; }
    .b2b__list li { margin-bottom: 10px; color: #d1d5db; }
    .b2b__btns { display: flex; gap: 15px; }

    /* Savatcha (Cart Drawer) */
    .cart-drawer {
      position: fixed;
      top: 0;
      right: -400px;
      width: 100%;
      max-width: 400px;
      height: 100%;
      background: white;
      box-shadow: -4px 0 10px rgba(0,0,0,0.1);
      z-index: 200;
      transition: right 0.3s ease;
      display: flex;
      flex-direction: column;
    }
    .cart-drawer.active { right: 0; }
    .cart-drawer__header { padding: 20px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; }
    .cart-drawer__items { padding: 20px; flex: 1; overflow-y: auto; }
    .cart-empty { text-align: center; color: #9ca3af; padding-top: 40px; }
    .cart-empty__icon { font-size: 48px; margin-bottom: 10px; }
    .cart-drawer__footer { padding: 20px; border-top: 1px solid #e5e7eb; background: #f9fafb; }
    .cart-summary__row { display: flex; justify-content: space-between; margin-bottom: 10px; color: #4b5563; }
    .cart-summary__total { font-weight: 700; font-size: 18px; color: #111827; border-top: 1px solid #d1d5db; padding-top: 10px; }
    .cart-overlay { position: fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.4); z-index:190; display:none; }
    .cart-overlay.active { display:block; }

    footer { background: #1f2937; color: #9ca3af; padding: 40px 0; font-size: 14px; }
    .footer__inner { display: flex; justify-content: space-between; gap: 30px; flex-wrap: wrap; }
    .footer__links { display: flex; flex-direction: column; gap: 10px; }
    .footer__links a { color: #9ca3af; text-decoration: none; }
    .footer__links a:hover { color: white; }
    .footer__bottom { border-top: 1px solid #374151; padding-top: 20px; margin-top: 20px; text-align: center; }
  </style>
</head>
<body>

  <header>
    <div class="container header__inner">
      <a href="#" class="logo">
        <span class="logo__icon">⚙</span>
        <span class="logo__text">Qurilish<strong>Mart</strong></span>
      </a>

      <nav>
        <a href="#catalog">Katalog</a>
        <a href="#calculator">Kalkulyator</a>
        <a href="#delivery">Yetkazib berish</a>
        <a href="#b2b">B2B</a>
      </nav>

      <div class="header__actions">
        <div class="search-bar">
          <input type="text" placeholder="Mahsulot qidiring..." class="search-bar__input" />
          <button class="search-bar__btn">🔍</button>
        </div>

        <button class="cart-btn" onclick="toggleCart()">
          🛒 <span class="cart-badge" id="cartBadge">0</span>
        </button>
      </div>
    </div>
  </header>

  <section class="hero">
    <div class="container hero__inner">
      <div class="hero__content">
        <div class="hero__badge">🏗️ Toshkent bo'ylab yetkazib berish</div>
        <h1 class="hero__title">Qurilish mollari —<br/><span class="hero__accent">tez, arzon, ishonchli</span></h1>
        <p class="hero__sub">Sement, kafel, bo'yoq, laminat va yana 5000+ mahsulot. Prorablar va uy egalariga bir xil qulaylik.</p>
        <div class="hero__cta">
          <a href="#catalog" class="btn btn--primary">Katalogni ko'rish</a>
          <a href="#calculator" class="btn btn--outline">Hisoblash</a>
        </div>
      </div>
      
      <div class="hero__visual">
        <div class="hero__card-stack">
          <div class="hero__card">
            <div class="hero__card-icon">🧱</div>
            <div>
              <div class="hero__card-name">G'isht A1</div>
              <div class="hero__card-price">850 so'm/dona</div>
            </div>
          </div>
          <div class="hero__card">
            <div class="hero__card-icon">🪣</div>
            <div>
              <div class="hero__card-name">Sement M400</div>
              <div class="hero__card-price">98 000 so'm/qop</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="categories" id="catalog">
    <div class="container">
      <h2 class="section-title">Kategoriyalar</h2>
      <p class="section-sub">Kerakli bo'limni tanlang</p>
      <div class="categories__grid">
        <div class="cat-card">
          <div class="cat-card__icon">🪣</div>
          <div class="cat-card__name">Sement va qum</div>
          <div class="cat-card__count">120+ mahsulot</div>
        </div>
        <div class="cat-card">
          <div class="cat-card__icon">🪟</div>
          <div class="cat-card__name">Kafel va plitka</div>
          <div class="cat-card__count">340+ mahsulot</div>
        </div>
        <div class="cat-card">
          <div class="cat-card__icon">🎨</div>
          <div class="cat-card__name">Bo'yoq va lak</div>
          <div class="cat-card__count">210+ mahsulot</div>
        </div>
        <div class="cat-card">
          <div class="cat-card__icon">🪵</div>
          <div class="cat-card__name">Laminat va parket</div>
          <div class="cat-card__count">180+ mahsulot</div>
        </div>
      </div>
    </div>
  </section>

  <section class="calculator" id="calculator">
    <div class="container">
      <h2 class="section-title">Kalkulyator</h2>
      <p class="section-sub">Qancha material kerakligini hisoblang</p>

      <div class="calc__tabs">
        <button class="calc__tab calc__tab--active" onclick="switchCalc('kafel')">🪟 Kafel</button>
        <button class="calc__tab" onclick="switchCalc('paint')">🎨 Bo'yoq</button>
        <button class="calc__tab" onclick="switchCalc('cement')">🪣 Sement</button>
      </div>

      <div class="calc__panels">
        <div class="calc__panel calc__panel--active" id="panel-kafel">
          <div class="calc__form">
            <div class="calc__row">
              <div class="calc__field">
                <label>Xona uzunligi (m)</label>
                <input type="number" id="kafel-len" value="4" oninput="calcKafel()" class="calc__input"/>
              </div>
              <div class="calc__field">
                <label>Xona kengligi (m)</label>
                <input type="number" id="kafel-wid" value="3" oninput="calcKafel()" class="calc__input"/>
              </div>
            </div>
          </div>
          <div class="calc__result">
            <div class="calc__result-grid">
              <div class="calc__result-item"><span class="calc__result-val" id="kr-area">12</span><span class="calc__result-key">kv.m maydon</span></div>
              <div class="calc__result-item"><span class="calc__result-val" id="kr-boxes">6</span><span class="calc__result-key">taxminiy quti</span></div>
            </div>
          </div>
        </div>

        <div class="calc__panel" id="panel-paint">
          <div class="calc__form">
            <div class="calc__row">
              <div class="calc__field">
                <label>Devor yuzi (kv.m)</label>
                <input type="number" id="paint-area" value="40" oninput="calcPaint()" class="calc__input"/>
              </div>
            </div>
          </div>
          <div class="calc__result">
            <div class="calc__result-grid">
              <div class="calc__result-item"><span class="calc__result-val" id="pr-liters">10</span><span class="calc__result-key">litr bo'yoq</span></div>
            </div>
          </div>
        </div>

        <div class="calc__panel" id="panel-cement">
          <div class="calc__form">
            <div class="calc__row">
              <div class="calc__field">
                <label>Devor maydoni (kv.m)</label>
                <input type="number" id="cement-area" value="20" oninput="calcCement()" class="calc__input"/>
              </div>
            </div>
          </div>
          <div class="calc__result">
            <div class="calc__result-grid">
              <div class="calc__result-item"><span class="calc__result-val" id="cr-bags">2</span><span class="calc__result-key">qop (50kg)</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="delivery" id="delivery">
    <div class="container">
      <h2 class="section-title">Yetkazib berish va To'lov</h2>
      <div class="delivery__grid">
        <div class="delivery__card">
          <div class="delivery__icon">🚛</div>
          <h3>Tezkor yetkazib berish</h3>
          <p>Buyurtma kuni yoki ertasi kuni Toshkent bo'yicha yetkazib beramiz.</p>
        </div>
        <div class="delivery__card">
          <div class="delivery__icon">💳</div>
          <h3>Qulay to'lov</h3>
          <p>Payme, Click, naqd pul yoki bank o'tkazmasi orqali to'lov.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="b2b" id="b2b">
    <div class="container b2b__inner">
      <div class="b2b__content">
        <div class="b2b__badge">Prorablar va qurilish kompaniyalari uchun</div>
        <h2>B2B hamkorlik</h2>
        <p>Katta hajmdagi xaridlar uchun shaxsiy menejer va maxsus ulgurji narxlar taqdim etiladi.</p>
        <div class="b2b__btns">
          <button class="btn btn--primary">📥 Prayst-listni yuklab olish</button>
        </div>
      </div>
    </div>
  </section>

  <div class="cart-overlay" id="cartOverlay" onclick="toggleCart()"></div>
  <div class="cart-drawer" id="cartDrawer">
    <div class="cart-drawer__header">
      <h3>Savatcha</h3>
      <button onclick="toggleCart()">✕</button>
    </div>
    <div class="cart-drawer__items">
      <div class="cart-empty">
        <div class="cart-empty__icon">🛒</div>
        <p>Savatcha bo'sh</p>
      </div>
    </div>
  </div>

  <footer>
    <div class="container footer__inner">
      <div class="footer__links">
        <h4>Sahifalar</h4>
        <a href="#catalog">Katalog</a>
        <a href="#calculator">Kalkulyator</a>
      </div>
      <div class="footer__links">
        <h4>Aloqa</h4>
        <a href="tel:+998901234567">+998 90 123 45 67</a>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 QurilishMart. Barcha huquqlar himoyalangan.</span>
    </div>
  </footer>

  <script>
    function toggleCart() {
      document.getElementById('cartDrawer').classList.toggle('active');
      document.getElementById('cartOverlay').classList.toggle('active');
    }

    function switchCalc(type) {
      document.querySelectorAll('.calc__panel').forEach(p => p.classList.remove('calc__panel--active'));
      document.querySelectorAll('.calc__tab').forEach(t => t.classList.remove('calc__tab--active'));
      
      document.getElementById('panel-' + type).classList.add('calc__panel--active');
      event.currentTarget.classList.add('calc__tab--active');
    }

    function calcKafel() {
      let len = document.getElementById('kafel-len').value || 0;
      let wid = document.getElementById('kafel-wid').value || 0;
      let area = len * wid;
      document.getElementById('kr-area').innerText = area.toFixed(1);
      document.getElementById('kr-boxes').innerText = Math.ceil(area / 2);
    }

    function calcPaint() {
      let area = document.getElementById('paint-area').value || 0;
      document.getElementById('pr-liters').innerText = Math.ceil(area / 4);
    }

    function calcCement() {
      let area = document.getElementById('cement-area').value || 0;
      document.getElementById('cr-bags').innerText = Math.ceil(area / 10);
    }
  </script>
</body>
</html>
"""

# Streamlit interfeysiga HTML komponentini chiqarish
# Xatolikka sabab bo'lgan scroller=True parametri o'rniga scrolling=True ishlatildi!
components.html(html_content, height=1500, scrolling=True)
