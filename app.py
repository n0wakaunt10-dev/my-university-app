import pandas as pd
import streamlit as st

# ページの設定（タイトルやレイアウト）
st.set_page_config(
    page_title="徳島国際工科大学（TITC）", page_icon="🏫", layout="wide"
)

# ---------------------------------------------------------
# カスタムCSS（濃紺/ネイビーテーマの設定）
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* メインヘッダー・アクセントカラー */
    .navy-header {
        background-color: #0d233a;
        color: #ffffff;
        padding: 20px 25px;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .navy-header h1 {
        color: #ffffff !important;
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
    }
    .navy-header p {
        color: #b0c4de !important;
        margin: 5px 0 0 0;
        font-size: 0.95rem;
    }
    .domain-badge {
        display: inline-block;
        background-color: #1e3a5f;
        color: #87cefa;
        padding: 3px 10px;
        border-radius: 4px;
        font-family: monospace;
        font-size: 0.85rem;
        margin-top: 8px;
    }
    /* サブタイトルの下線風アクセント */
    h2, h3 {
        color: #0d233a !important;
        border-bottom: 2px solid #0d233a;
        padding-bottom: 5px;
    }
    /* サイドバーのカスタマイズ */
    [data-testid="stSidebar"] {
        background-color: #f4f7f9;
        border-right: 1px solid #d0d7de;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# ヘッダーエリア（濃紺デザイン）
# ---------------------------------------------------------
st.markdown(
    """
    <div class="navy-header">
        <h1>徳島国際工科大学</h1>
        <p>Tokushima Institute of Technology and Commerce (TITC)</p>
        <div class="domain-badge">🌐 https://kokushin-u.jp</div>
    </div>
""",
    unsafe_allow_html=True,
)

# サイドバー（ナビゲーション）
st.sidebar.header("🎓 TITC 大学ポータル")
page = st.sidebar.radio(
    "メニューを選択",
    ["トップページ", "大学概要・沿革", "学部・学科紹介", "キャンパスライフ・学食"],
)

st.sidebar.markdown("---")
st.sidebar.caption("学校法人 徳島工学園")
st.sidebar.caption("© Tokushima Institute of Technology and Commerce.")

# --- ページ1：トップページ ---
if page == "トップページ":
    st.subheader("建学の精神")
    st.info("### 『阿波の藍より出でて、世界の青に勝る』\n地域で培った技術と学術を練磨し、世界へ羽ばたく技術者を育成する。")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📢 大学からのお知らせ")
        st.write("・**2026/07/15**: 常三島ベイキャンパス 最先端AIラボの竣工式が執り行われました")
        st.write("・**2026/07/01**: 【バイオ・スマート農工学部】LEDを活用した新アグリテック技術に関するプレスリリース")
        st.write("・**2026/06/20**: 2027年度 総合型選抜・学校推薦型選抜の要項を公開しました")

    with col2:
        st.write("### 🗓 重要なお知らせ（学生・教職員向け）")
        with st.expander("【蔵本キャンパス】3年生向け シャトルバス運用変更について"):
            st.write("蔵本〜常三島ベイキャンパス間の平日運行便数が一部変更となります。時間割を確認してください。")
        with st.expander("留学生チューター制度 募集開始"):
            st.write("今年度後期の留学生サポーターを募集します（国際フロンティア工学部推奨）。")

# --- ページ2：大学概要・沿革 ---
elif page == "大学概要・沿革":
    st.header("大学概要・沿革")

    st.write("### 沿革")
    history_data = {
        "年": ["明治8年 (1875)", "明治34年 (1901)", "昭和24年 (1949)", "平成20年 (2008)"],
        "出来事": [
            "徳島藩の藍産業および機械技術の近代化を目的に「阿波製藍・機械伝習所」創立",
            "「私立徳島高等工業学校」に改称。四国屈指の技術者養成機関となる",
            "学制改革により「徳島工科大学」開校。工学部を設置",
            "「徳島国際工科大学」へ改称。国際フロンティア工学部、スマート農工学部などを新設",
        ],
    }
    st.table(pd.DataFrame(history_data))

    st.write("### キャンパス案内")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 蔵本キャンパス（本部・1〜2年）")
        st.write("・**所在地**: 徳島県徳島市蔵本町")
        st.write("・**特徴**: 吉野川沿いの伝統ある緑豊かなキャンパス。基礎教育と教養科目を主に展開。")
    with c2:
        st.markdown("#### 常三島ベイキャンパス（3〜4年・大学院）")
        st.write("・**所在地**: 徳島県徳島市港町")
        st.write("・**特徴**: 徳島港近く。産学連携・最先端ラボが集結する先端研究拠点。")

# --- ページ3：学部・学科紹介 ---
elif page == "学部・学科紹介":
    st.header("学部・学科構成")

    tab1, tab2, tab3 = st.tabs(["工学部", "国際フロンティア工学部", "バイオ・スマート農工学部"])

    with tab1:
        st.subheader("工学部（伝統の看板学部）")
        st.write("・**機械システム工学科**: 明治からの伝統を受け継ぐ精密機械・ロボティクス分野")
        st.write("・**電気電子情報工学科**: 次世代の半導体・エネルギー技術を追求")
        st.write("・**社会環境デザイン学科**: 吉野川の治水技術から発展した防災・都市土木工学")

    with tab2:
        st.subheader("国際フロンティア工学部（2008年新設）")
        st.write("・**AI・データサイエンス学科**: 授業の半数を英語で実施。グローバル市場で戦えるIT人材を育成")
        st.write("・**グローバル技術経営（MOT）学科**: 技術理解と経営マインドを兼ね備えたリーダーを育成")

    with tab3:
        st.subheader("バイオ・スマート農工学部（地域密着・先端農工）")
        st.write("・**阿波イノベーション農工学科**: LED照明を活用したアグリテック、発酵工学、藍染め成分の化学分析などを高度に研究")

# --- ページ4：キャンパスライフ・学食 ---
elif page == "キャンパスライフ・学食":
    st.header("TITC キャンパスライフ")

    st.write("### 🍲 名物学食メニュー")
    st.info("**食堂『阿波らんち』名物：** 藍ドレッシングサラダ付き・徳島ラーメンセット（450円）")

    st.write("### 💬 在学生のリアルな声（TITCあるある）")
    st.chat_message("user").write("3年生になるときに蔵本からベイキャンパスへ移動するので、引越しするか吉野川を自転車で爆走するかマジで悩む（工学部3年）")
    st.chat_message("user").write("キャンパス内に留学生が多くて、学食で英語やフランス語が飛び交ってるのが日常風景（国際フロンティア2年）")
    st.chat_message("user").write("農工学科のLED植物工場で育った野菜が学食でたまに出てくるの好き（スマート農工4年）")
