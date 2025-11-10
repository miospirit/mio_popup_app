# app.py — LINE誘導用（SNSに貼る用）
import streamlit as st

# ✦ あなたのLINE公式アカウント（LIFFリンク）
LINE_LIFF_URL = "https://liff.line.me/1645278921-kWRPP32q/?accountId=697obqdd"

# ページ設定
st.set_page_config(page_title="澪｜幸福数字・LINEで結果受け取り", page_icon="🔮", layout="centered")
# ===== LINEポップアップ =====

def show_line_popup():
    st.markdown("""
    <style>
      #mio_popup {
        position: fixed; inset: 0; z-index: 9999;
        display: flex; align-items: center; justify-content: center;
        background: rgba(0,0,0,.35);
      }
      #mio_popup .box {
        width: min(92vw, 520px);
        background: #fff; border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0,0,0,.25);
        padding: 22px;
        text-align: center;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Sans", "Yu Gothic", "Noto Sans JP", sans-serif;
      }
      #mio_popup h3 { margin: 8px 0 14px; color: #1f274e; }
      #mio_popup p  { color: #555; line-height: 1.7; }
      #mio_popup a.btn {
        display: inline-block;
        padding: 12px 18px;
        background:#1f274e; color:#fff; border-radius:10px;
        text-decoration: none; font-weight: 700;
        border: 1px solid rgba(255,255,255,.3);
        box-shadow: 0 4px 12px rgba(0,0,0,.18);
        margin-top: 12px;
      }
      #mio_popup button.close {
        margin-top: 14px;
        background: #fff; color:#333; border:1px solid #ddd;
        padding: 8px 14px; border-radius: 8px; cursor: pointer;
      }
    </style>

    <div id="mio_popup">
      <div class="box">
        <h3>公式LINEで“診断の続き”を受け取る</h3>
        <p>LINEで <b>「診断」</b> と送ってください。<br>
           鑑定文とパワーストーンの提案をお届けします。</p>
        <a class="btn" href="{LINE_URL}" target="_blank" rel="noopener">🌙 公式LINEを開く</a>
        <br>
        <button class="close" id="mio_close_btn">閉じる</button>
        <p style="font-size:12px;color:#777;margin-top:10px;">
          ※LINEが開かない場合は、右上の三本線 →「ブラウザで開く」を押してください。
        </p>
      </div>
    </div>

    <script>
      (function(){
        const closeBtn = document.getElementById('mio_close_btn');
        const popup    = document.getElementById('mio_popup');

        // 「閉じる」ボタンで閉じる
        closeBtn && closeBtn.addEventListener('click', function(){
          popup && popup.remove();
        });

        // 背景クリックでも閉じる（中の箱クリックは無効）
        popup && popup.addEventListener('click', function(e){
          if (e.target && e.target.id === 'mio_popup') {
            popup.remove();
          }
        });
      })();
    </script>
    """.replace("{LINE_URL}", LINE_URL), unsafe_allow_html=True)

# セッション中は一度だけ表示
if "mio_line_popup_shown" not in st.session_state:
    show_line_popup()
    st.session_state.mio_line_popup_shown = True

# スタイル
st.markdown("""
<style>
.stApp{background:linear-gradient(160deg,#fde7f3 0%,#eef4ff 55%,#e8fff3 100%);}
h1,h2{color:#D4AF37; text-shadow:0 1px 1px rgba(0,0,0,.2);}
.mio-card{background:rgba(255,255,255,.92); border:1px solid rgba(0,0,0,.06);
  box-shadow:0 8px 24px rgba(0,0,0,.08); border-radius:14px; padding:18px;}
.mio-btn{display:inline-block; padding:12px 18px; border-radius:10px;
  text-decoration:none; color:#fff; background:#06C755; font-weight:700;}
.mio-ghost{padding:8px 14px; border:1px solid #ddd; background:#fff; border-radius:8px;}
</style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown("""
<div style="text-align:center">
  <h1>澪 - Mio -｜3分でわかる幸福数字</h1>
  <div>診断結果は <b>公式LINE</b> でお届けします</div>
</div>
<br>
""", unsafe_allow_html=True)

# 入力フォーム（ダミー）
with st.form("popup_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("お名前（ニックネーム可）")
    with col2:
        birth = st.date_input("生年月日（任意）")
    ok = st.form_submit_button("🔮 診断する（LINEで受け取る）")

# 診断ボタンを押した後
if ok:
    st.markdown(f"""
    <div id="mio_line_popup" style="
      position:fixed; inset:0; background:rgba(0,0,0,.45); display:flex;
      align-items:center; justify-content:center; z-index:9999;">
      <div class="mio-card" style="text-align:center; width:min(520px,92vw);">
        <h3 style="margin:6px 0 10px; color:#1f274e;">結果はLINEでお届けします</h3>
        <p style="color:#333;">下のボタンをタップして、<b>公式LINEを追加</b>してください。<br>
        トーク画面で「診断」と送ると、結果リンクが届きます。</p>
        <div style="margin:10px 0 14px;">
          <a class="mio-btn" href="{LINE_LIFF_URL}" target="_blank">🌙 公式LINEを開く</a>
        </div>
        <div style="font-size:12px; color:#666; line-height:1.6;">
          ※ LINEが開かない場合：右上の三本線 →「ブラウザで開く」で起動できます。
        </div>
        <br>
        <button onclick="document.getElementById('mio_line_popup').remove();" class="mio-ghost">閉じる</button>
      </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="mio-card" style="text-align:center">
      <p>今すぐ結果を受け取りたい方は、上の「🔮 診断する」を押してください。<br>
      公式LINEで結果リンクが届きます。</p>
      <a class="mio-btn" href="https://liff.line.me/1645278921-kWRPP32q/?accountId=697obqdd" target="_blank">
        公式LINEを直接開く
      </a>
    </div>
    """, unsafe_allow_html=True)
