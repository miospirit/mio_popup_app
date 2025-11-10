# app.py — 澪 -Mio-｜脳科学×数秘術で導く“幸せの方程式”
import streamlit as st
import os
import datetime

# ---- Streamlit ページ設定（必ず最初）----
st.set_page_config(page_title="澪 -Mio-｜脳科学×数秘術で導く“幸せの方程式”", page_icon="🌙", layout="centered")

# ---- LINE URL（Secrets → 環境変数 → 直書きの順で取得）----
LINE_URL = st.secrets.get(
    "LINE_URL",
    os.environ.get("LINE_URL", "https://liff.line.me/1645278921-kWRPP32q/?accountId=697obqdd")
)

# ---- スタイル（本体と同じ雰囲気）----
st.markdown("""
<style>
.stApp {
  background: linear-gradient(160deg, #fde7f3 0%, #eef4ff 55%, #e8fff3 100%);
  color: #1a1a1a;
  font-family: "Hiragino Mincho ProN", "Yu Mincho", "MS PMincho", serif;
}
h1,h2,h3,.gold {
  color: #D4AF37;
  text-shadow: 0 1px 1px rgba(0,0,0,.25);
  letter-spacing: .02em;
}
.subtitle { color:#3a3a3a; }
hr { border: none; height: 1px;
     background: linear-gradient(90deg, transparent, rgba(0,0,0,.2), transparent); }
.mio-card {
  background: rgba(255,255,255,0.9);
  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: 0 6px 20px rgba(0,0,0,.08);
  border-radius: 14px;
  padding: 18px 20px;
}
.stButton>button {
  background: linear-gradient(135deg, #1f2a44, #2f3c66);
  color: #fff !important;
  border-radius: 10px;
  border: 1px solid rgba(0,0,0,0.1);
}
.stButton>button:hover { filter: brightness(1.1); }

/* === Popup === */
#mio-backdrop {
  position: fixed; inset: 0; background: rgba(0,0,0,.5); z-index: 9998;
}
#mio-modal {
  position: fixed; inset: 0; display: grid; place-items: center; z-index: 9999;
}
#mio-box {
  width: min(480px, 92vw);
  background: #fff;
  border-radius: 16px;
  padding: 22px 20px;
  box-shadow: 0 10px 40px rgba(0,0,0,.18);
  text-align: center;
}
#mio-title { font-size: 20px; font-weight: 700; margin-bottom: 8px; color:#1f274e; }
#mio-text  { font-size: 14px; color:#555; line-height:1.7; }
.mio-btn {
  display:inline-block; margin-top:16px; padding:12px 18px; border-radius:10px;
  background:#1f274e; color:#fff; text-decoration:none; font-weight:700;
  border:1px solid rgba(0,0,0,0.1);
}
#mio-close {
  margin-top:10px; background:transparent; border:none; color:#666; cursor:pointer;
}
</style>
""", unsafe_allow_html=True)

# ---- ヘッダー（本体と同じ）----
st.markdown(f"""
<div style="text-align:center;">
  <h1 class="gold" style="margin-bottom:6px;">澪 -Mio-｜脳科学×数秘術で導く“幸せの方程式”</h1>
  <div class="subtitle" style="opacity:.95; font-size:16px; line-height:1.7;">
    “運命は、偶然じゃなく構造でできている。<br>
    あなたの心理と数字を、深層心理で読み解きます。”
  </div>
  <div style="margin-top:8px;">3分でわかる、あなたの幸福な数字。</div>
</div>
<hr>
""", unsafe_allow_html=True)

# ---- ポップアップを表示する関数 ----
def show_line_popup():
    html = f"""
    <div id="mio-backdrop"></div>
    <div id="mio-modal" role="dialog" aria-modal="true">
      <div id="mio-box">
        <div id="mio-title">公式LINEで診断結果を受け取る</div>
        <div id="mio-text">
          ボタンをタップして公式LINEを追加してください。<br>
          トークで <b>「診断」</b> と送ると結果リンクが届きます。<br>
          <span style="font-size:12px;color:#888;">
            ※LINEが開かない場合は右上の三本線から「ブラウザで開く」を押してください。
          </span>
        </div>
        <a class="mio-btn" href="{LINE_URL}" target="_blank">🌙 公式LINEを開く</a><br>
        <button id="mio-close">閉じる</button>
      </div>
    </div>
    <script>
      (function(){{
        const bd = document.getElementById('mio-backdrop');
        const md = document.getElementById('mio-modal');
        const cl = document.getElementById('mio-close');
        function closeAll() {{
          bd && bd.remove();
          md && md.remove();
        }}
        cl && cl.addEventListener('click', closeAll);
        bd && bd.addEventListener('click', closeAll);
      }})();
    </script>
    """
    st.markdown(html, unsafe_allow_html=True)

# ---- フォーム（本体と同じ項目・ラベル）----
with st.form("mio_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        bdate = st.date_input(
            "生年月日",
            value=datetime.date(1990, 1, 1),
            min_value=datetime.date(1890, 1, 1),
            max_value=datetime.date.today(),
            format="YYYY-MM-DD"
        )
        gender = st.selectbox("性別", ["女性", "男性", "その他", "回答しない"])
    with col2:
        concern = st.selectbox("今の悩み", ["恋愛", "仕事", "金運", "人間関係", "その他"])
        acting  = st.selectbox("行動タイプ", ["すぐ動く", "考えてから動く", "状況で変わる"])

    agree = st.checkbox("この診断は一度のみであることに同意します")
    submitted = st.form_submit_button("🔮 幸福数字を診断する")

# ---- 送信時の動作：結果は出さず、ポップアップだけ ----
if submitted:
    if not agree:
        st.error("一度のみの実施に同意してください。")
        st.stop()
    st.success("診断の準備ができました。公式LINEで結果をお届けします。")
    show_line_popup()

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
