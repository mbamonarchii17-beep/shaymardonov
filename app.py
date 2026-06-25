import streamlit as st
import streamlit.components.v1 as components

# Streamlit sahifa sozlamalari
st.set_page_config(
    page_title="QurilishMart — Qurilish Mollari",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# To'liq integratsiya qilingan HTML, CSS va JS kodlari
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
    /* ASOSIY STILLAR */
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
      font-size: 20px;
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

    /* Qidiruv Natijalari Overlay */
    .search-overlay {
      position: fixed;
      top: 70px;
      left: 0;
      width: 100%;
      background: white;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      z-index: 90;
      padding: 20px 0;
      border-bottom: 2px solid #f97316;
    }
    .search-overlay__header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
    }
    .search-overlay__header button {
      background: none;
      border: none;
      font-size: 18px;
      cursor: pointer;
    }

    /* Hero */
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
    .btn--ghost { background: #f3f4f6; color: #4b5563; }

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
      transition: all 0.2s;
      width: 100%;
    }
    .cat-card:hover { transform: translateY(-5px); border-color: #f97316; }
    .cat-card__icon { font-size: 40px; margin-bottom: 15px; }
    .cat-card__name { font-weight: 600; font-size: 16px; margin-bottom: 5px; color: #111827; }
    .cat-card__count { color: #9ca3af; font-size: 13px; }

    /* Katalog va Mahsulotlar Tarmog'i */
    .catalog { padding: 40px 0; background: #fff; }
    .catalog__toolbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid #e5e7eb; }
    .products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 25px;
    }
    .product-card {
      background: white;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .product-card__icon { font-size: 48px; text-align: center; margin-bottom: 15px; background: #f9fafb; padding: 20px; border-radius: 6px; }
    .product-card__title { font-size: 16px; font-weight: 600; margin-bottom: 8px; color: #111827; }
    .product-card__category { font-size: 12px; color: #f97316; font-weight: 500; margin-bottom: 10px; }
    .product-card__price { font-size: 18px; font-weight: 700; color: #111827; margin-bottom: 15px; }

    /* Kalkulyator */
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
    .calc__result-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; text-align: center; }
    .calc__result-val { display: block; font-size: 24px; font-weight: 700; color: #16a34a; }
    .calc__result-key { color: #4b5563; font-size: 13px; }

    /* Yetkazib berish va B2B */
    .delivery__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; padding: 20px 0; }
    .delivery__card { background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.03); border: 1px solid #e5e7eb; }
    .delivery__icon { font-size: 32px; margin-bottom: 10px; }
    .b2b { background: #111827; color: white; padding: 60px 0; }
    .b2b__inner { display: flex; justify-content: space-between; align-items: center; gap: 40px; flex-wrap: wrap; }
    .b2b__content { flex: 1; min-width: 300px; }
    .b2b__badge { color: #f97316; font-weight: 600; margin-bottom: 10px; }
    .b2b__btns { display: flex; gap: 15px; margin-top: 20px; }

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
    .cart-drawer__footer { padding: 20px; border-top: 1px solid #e5e7eb; background: #f9fafb; }
    .cart-summary__row { display: flex; justify-content: space-between; margin-bottom: 10px; color: #4b5563; }
    .cart-summary__total { font-weight: 700; font-size: 18px; color: #111827; border-top: 1px solid #d1d5db; padding-top: 10px; }
    .cart-overlay { position: fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.4); z-index:190; display:none; }
    .cart-overlay.active { display:block; }
    .cart-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #eee; }

    /* Buyurtma shakli (Checkout Modal) */
    .modal-overlay { position: fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:250; display:none; align-items:center; justify-content:center; }
    .modal-overlay.active { display:flex; }
    .modal--checkout { background: white; padding: 30px; border-radius: 12px; max-width: 500px; width: 100%; box-shadow: 0 10px 25px rgba(0,0,0,0.1); position: relative; }
    .form-group { margin-bottom: 15px; }
    .form-group label { display: block; margin-bottom: 5px; font-weight: 500; }
    .form-input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }

    footer { background: #1f2937; color: #9ca3af; padding: 40px 0; font-size: 14px; }
    .footer__inner { display: flex; justify-content: space-between; gap: 30px; flex-wrap: wrap; }
    .footer__links { display: flex; flex-direction: column; gap: 10px; }
    .footer__links a { color: #9ca3af; text-decoration: none; }
    .footer__bottom { border-top: 1px solid #374151; padding-top: 20px; margin-top: 20px; text-align: center; }
    .no-results { text-align: center; padding: 40px; color: #6b7280; font-size: 16px; width: 100%; grid-column: 1 / -1; }
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
          <input type="text" id="globalSearch" placeholder="Mahsulot qidiring..." class="search-bar__input" oninput="handleSearch(this.value)" />
          <button class="search-bar__btn">🔍</button>
        </div>

        <button class="cart-btn" onclick="toggleCart()">
          🛒 <span class="cart-badge" id="cartBadge">0</span>
        </button>
      </div>
    </div>
  </header>

  <div class="search-overlay" id="searchOverlay" style="display:none">
    <div class="container">
      <div class="search-overlay__header">
        <h3>Qidiruv natijalari</h3>
        <button onclick="closeSearch()">✕</button>
      </div>
      <div class="products-grid" id="searchResults"></div>
    </div>
  </div>

  <section class="hero">
    <div class="container hero__inner">
      <div class="hero__content">
        <div class="hero__badge">🏗️ Toshkent bo'ylab yetkazib berish</div>
        <h1 class="hero__title">Qurilish mollari —<br/><span class="hero__accent">tez, arzon, ishonchli</span></h1>
        <p class="hero__sub">Sement, kafel, bo'yoq, laminat va yana ko'plab mahsulotlar. Prorablar va uy egalariga bir xil qulaylik.</p>
        <div class="hero__cta">
          <a href="#catalog" class="btn btn--primary">Katalogni ko'rish</a>
          <a href="#calculator" class="btn btn--outline">Hisoblash</a>
        </div>
      </div>
    </div>
  </section>

  <section class="categories">
    <div class="container">
      <h2 class="section-title">Kategoriyalar</h2>
      <p class="section-sub">Kerakli bo'limni tanlang va mahsulotlarni ko'ring</p>
      <div class="categories__grid">
        <button class="cat-card" onclick="filterByCategory('Sement va qum')">
          <div class="cat-card__icon">🪣</div>
          <div class="cat-card__name">Sement va qum</div>
          <div class="cat-card__count">Barcha mahsulotlar</div>
        </button>
        <button class="cat-card" onclick="filterByCategory('Kafel va plitka')">
          <div class="cat-card__icon">🪟</div>
          <div class="cat-card__name">Kafel va plitka</div>
          <div class="cat-card__count">Barcha mahsulotlar</div>
        </button>
        <button class="cat-card" onclick="filterByCategory('Bo\'yoq va lak')">
          <div class="cat-card__icon">🎨</div>
          <div class="cat-card__name">Bo'yoq va lak</div>
          <div class="cat-card__count">Barcha mahsulotlar</div>
        </button>
        <button class="cat-card" onclick="filterByCategory('Laminat va parket')">
          <div class="cat-card__icon">🪵</div>
          <div class="cat-card__name">Laminat va parket</div>
          <div class="cat-card__count">Barcha mahsulotlar</div>
        </button>
      </div>
    </div>
  </section>

  <section class="catalog" id="catalog">
    <div class="container">
      <div class="catalog__toolbar">
        <h3 id="catalogTitle">Barcha mahsulotlar</h3>
        <button class="btn btn--outline" onclick="filterByCategory('all')">Hammasini ko'rsatish</button>
      </div>

      <div class="products-grid" id="productsGrid">
        </div>
    </div>
  </section>

  <section class="calculator" id="calculator">
    <div class="container">
      <h2 class="section-title">Kalkulyator</h2>
      <p class="section-sub">Qancha material kerakligini hisoblang</p>

      <div class="calc__tabs">
        <button class="calc__tab calc__tab--active" onclick="switchCalc('kafel', this)">🪟 Kafel</button>
        <button class="calc__tab" onclick="switchCalc('paint', this)">🎨 Bo'yoq</button>
        <button class="calc__tab" onclick="switchCalc('cement', this)">🪣 Sement</button>
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
            <button style="margin-top:15px;" class="btn btn--primary" onclick="addCalcToCart('Kafel (Kalkulyator)', '6 quti')">Savatchaga qo'shish</button>
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
            <button style="margin-top:15px;" class="btn btn--primary" onclick="addCalcToCart('Bo\'yoq (Kalkulyator)', '10 litr')">Savatchaga qo'shish</button>
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
            <button style="margin-top:15px;" class="btn btn--primary" onclick="addCalcToCart('Sement (Kalkulyator)', '2 qop')">Savatchaga qo'shish</button>
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

  <section class="b2b" id="b2b">
    <div class="container b2b__inner">
      <div class="b2b__content">
        <div class="b2b__badge">Prorablar va kompaniyalar uchun</div>
        <h2>B2B hamkorlik</h2>
        <p>Katta buyurtmalar uchun shaxsiy menejer va maxsus shartnomaviy narxlar.</p>
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
    <div class="cart-drawer__items" id="cartItems">
      <div class="cart-empty">
        <div class="cart-empty__icon">🛒</div>
        <p>Savatcha bo'sh</p>
      </div>
    </div>
    <div class="cart-drawer__footer" id="cartFooter" style="display:none;">
      <div class="cart-summary">
        <div class="cart-summary__row">
          <span>Jami to'lov:</span>
          <span id="cartTotalText">0 so'm</span>
        </div>
      </div>
      <button class="btn btn--primary btn--full" onclick="openCheckout()">Buyurtma berish</button>
      <button class="btn btn--ghost btn--full" onclick="clearCart()">Tozalash</button>
    </div>
  </div>

  <div class="modal-overlay" id="checkoutModal">
    <div class="modal--checkout">
      <h2 style="margin-top:0;">Buyurtma rasmiylashtirish</h2>
      <div class="form-group">
        <label>Ism va familiya</label>
        <input type="text" id="co-name" placeholder="Jasur Abdullayev" class="form-input"/>
      </div>
      <div class="form-group">
        <label>Telefon raqam</label>
        <input type="tel" id="co-phone" placeholder="+998 90 123 45 67" class="form-input"/>
      </div>
      <button class="btn btn--primary btn--full" onclick="submitOrder()">Tasdiqlash</button>
      <button class="btn btn--ghost btn--full" onclick="closeCheckout()">Yopish</button>
    </div>
  </div>

  <footer>
    <div class="container footer__inner">
      <div class="footer__links">
        <h4>Sahifalar</h4>
        <a href="#catalog" style="color:#9ca3af; text-decoration:none;">Katalog</a><br>
        <a href="#calculator" style="color:#9ca3af; text-decoration:none;">Kalkulyator</a>
      </div>
      <div class="footer__links">
        <h4>Aloqa</h4>
        <span style="color:white">+998 90 123 45 67</span>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 QurilishMart. Barcha huquqlar himoyalangan.</span>
    </div>
  </footer>

  <script>
    // MAHSULOTLAR BAZASI (ARRAY)
    const products = [
      { id: 1, name: "Sement Huaxin M400", category: "Sement va qum", price: 95000, icon: "🪣" },
      { id: 2, name: "Qora Qum (Yuvilgan)", category: "Sement va qum", price: 120000, icon: "⏳" },
      { id: 3, name: "Kafel Premium 60x60", category: "Kafel va plitka", price: 85000, icon: "🪟" },
      { id: 4, name: "KeramoGranit Daniya", category: "Kafel va plitka", price: 145000, icon: "🧱" },
      { id: 5, name: "Akrilik Ichki Bo'yoq Caparol", category: "Bo'yoq va lak", price: 210000, icon: "🎨" },
      { id: 6, name: "Yaltiroq Lak (Yog'och uchun)", category: "Bo'yoq va lak", price: 65000, icon: "🖌️" },
      { id: 7, name: "Laminat Kronopol 8mm", category: "Laminat va parket", price: 110000, icon: "🪵" },
      { id: 8, name: "Eman Parket (Natural)", category: "Laminat va parket", price: 320000, icon: "🌳" }
    ];

    let cart = [];

    // KATEGORIYA BO'YICHA FILTRLASH FUNKSIYASI
    function filterByCategory(categoryName) {
      const grid = document.getElementById('productsGrid');
      const title = document.getElementById('catalogTitle');
      grid.innerHTML = "";

      let filtered = [];
      if (categoryName === 'all') {
        filtered = products;
        title.innerText = "Barcha mahsulotlar";
      } else {
        filtered = products.filter(p => p.category === categoryName);
        title.innerText = categoryName + " bo'limi mahsulotlari";
      }

      if (filtered.length === 0) {
        grid.innerHTML = `<div class="no-results">Ushbu bo'limda hozircha mahsulot yo'q.</div>`;
        return;
      }

      filtered.forEach(p => {
        grid.innerHTML += `
          <div class="product-card">
            <div>
              <div class="product-card__icon">\${p.icon}</div>
              <div class="product-card__category">\${p.category}</div>
              <div class="product-card__title">\${p.name}</div>
            </div>
            <div>
              <div class="product-card__price">\${p.price.toLocaleString()} so'm</div>
              <button class="btn btn--primary btn--full" onclick="addToCart(\${p.id})">Savatchaga qo'shish</button>
            </div>
          </div>
        `;
      });

      // Foydalanuvchini katalog bo'limiga avtomatik tushirish (Scroll)
      document.getElementById('catalog').scrollIntoView({ behavior: 'smooth' });
    }

    // QIDIRUV PANELINI BOSHQARISH
    function handleSearch(val) {
      const overlay = document.getElementById('searchOverlay');
      const resultsGrid = document.getElementById('searchResults');
      
      if (!val.trim()) {
        overlay.style.display = 'none';
        return;
      }

      overlay.style.display = 'block';
      resultsGrid.innerHTML = "";

      let filtered = products.filter(p => p.name.toLowerCase().includes(val.toLowerCase()));

      if (filtered.length === 0) {
        resultsGrid.innerHTML = `<div class="no-results">Hech narsa topilmadi.</div>`;
        return;
      }

      filtered.forEach(p => {
        resultsGrid.innerHTML += `
          <div class="product-card" style="background:#f9fafb;">
            <div class="product-card__title">\${p.name}</div>
            <div class="product-card__price">\${p.price.toLocaleString()} so'm</div>
            <button class="btn btn--primary" onclick="addToCart(\${p.id})">Qo'shish</button>
          </div>
        `;
      });
    }

    function closeSearch() {
      document.getElementById('searchOverlay').style.display = 'none';
      document.getElementById('globalSearch').value = "";
    }

    // SAVATCHA LOGIKASI
    function toggleCart() {
      document.getElementById('cartDrawer').classList.toggle('active');
      document.getElementById('cartOverlay').classList.toggle('active');
    }

    function addToCart(id) {
      const prod = products.find(p => p.id === id);
      cart.push({ name: prod.name, price: prod.price });
      updateCartUI();
    }

    function addCalcToCart(name, spec) {
      cart.push({ name: `\${name} - \${spec}`, price: 0 });
      updateCartUI();
      toggleCart();
    }

    function updateCartUI() {
      document.getElementById('cartBadge').innerText = cart.length;
      const itemsDiv = document.getElementById('cartItems');
      const footerDiv = document.getElementById('cartFooter');
      
      if (cart.length === 0) {
        itemsDiv.innerHTML = `<div class="cart-empty"><div class="cart-empty__icon">🛒</div><p>Savatcha bo'sh</p></div>`;
        footerDiv.style.display = 'none';
        return;
      }

      footerDiv.style.display = 'block';
      itemsDiv.innerHTML = "";
      let total = 0;

      cart.forEach((item, idx) => {
        total += item.price;
        itemsDiv.innerHTML += `
          <div class="cart-item">
            <div><strong>\${item.name}</strong><br><small>\${item.price > 0 ? item.price.toLocaleString() + " so'm" : "Hisoblangan material"}</small></div>
            <button onclick="removeItem(\${idx})" style="background:none; border:none; color:red; cursor:pointer;">❌</button>
          </div>
        `;
      });

      document.getElementById('cartTotalText').innerText = total.toLocaleString() + " so'm";
    }

    function removeItem(idx) {
      cart.splice(idx, 1);
      updateCartUI();
    }

    function clearCart() {
      cart = [];
      updateCartUI();
    }

    // BUYURTMA OYNALARI
    function openCheckout() { document.getElementById('checkoutModal').classList.add('active'); }
    function closeCheckout() { document.getElementById('checkoutModal').classList.remove('active'); }
    function submitOrder() {
      alert("Rahmat! Buyurtmangiz qabul qilindi. Tez orada operatorlarimiz bog'lanishadi.");
      clearCart();
      closeCheckout();
      toggleCart();
    }

    // KALKULYATOR TAB TIZIMI
    function switchCalc(type, btn) {
      document.querySelectorAll('.calc__panel').forEach(p => p.classList.remove('calc__panel--active'));
      document.querySelectorAll('.calc__tab').forEach(t => t.classList.remove('calc__tab--active'));
      
      document.getElementById('panel-' + type).classList.add('calc__panel--active');
      btn.classList.add('calc__tab--active');
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

    // SAYT YUKLANGANDA TO'G'RIDAN-TO'G'RI BARCHA MAHSULOTLARNI CHIQARISH
    window.onload = function() {
      filterByCategory('all');
    };
  </script>
</body>
</html>
"""

# Streamlit interfeysiga to'liq ishlaydigan HTML/JS andozasini uzatish
components.html(html_content, height=1600, scrolling=True)
