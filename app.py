import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# ページ基本設定
# ---------------------------------------------------------
st.set_page_config(page_title="徳島国際工科大学（TITC）", layout="wide")

# ---------------------------------------------------------
# カスタムCSS（ネイビー・フォーマルデザイン）
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* メインヘッダー */
    .navy-header {
        background-color: #0b1f33;
        color: #ffffff;
        padding: 22px 28px;
        border-radius: 4px;
        margin-bottom: 25px;
        border-bottom: 3px solid #004080;
    }
    .navy-header h1 {
        color: #ffffff !important;
        margin: 0;
        font-size: 2.1rem;
        font-weight: 700;
        letter-spacing: 0.05em;
    }
    .navy-header p {
        color: #b0c4de !important;
        margin: 6px 0 0 0;
        font-size: 0.9rem;
        font-family: 'Times New Roman', serif;
    }
    .domain-badge {
        display: inline-block;
        background-color: #162d47;
        color: #87cefa;
        padding: 2px 8px;
        border-radius: 3px;
        font-family: monospace;
        font-size: 0.8rem;
        margin-top: 10px;
    }
    /* 見出し装飾 */
    h2 {
        color: #0b1f33 !important;
        border-left: 5px solid #0b1f33;
        padding-left: 10px;
        font-size: 1.5rem;
        margin-top: 1.5em;
    }
    h3 {
        color: #111111 !important;
        border-bottom: 1px solid #cccccc;
        padding-bottom: 4px;
        font-size: 1.2rem;
    }
    /* サイドバー背景 */
    [data-testid="stSidebar"] {
        background-color: #f7f9fa;
        border-right: 1px solid #e1e4e8;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# ヘッダーエリア
# ---------------------------------------------------------
st.markdown(
    """
    <div class="navy-header">
        <h1>徳島国際工科大学</h1>
        <p>Tokushima Institute of Technology and Commerce (TITC)</p>
        <div class="domain-badge">https://kokushin-u.jp</div>
    </div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# サイドバー（ナビゲーション＆校章）
# ---------------------------------------------------------
st.sidebar.markdown("### TITC 大学ポータル")

# 校章画像を表示
st.sidebar.image(
    "https://i.ibb.co/8kzP4wy/image.png",
    caption="校章：歯車と藍の葉",
    use_container_width=True,
)

page = st.sidebar.radio(
    "メニュー",
    [
        "トップページ",
        "大学概要・沿革",
        "学部・学科紹介",
        "キャンパスライフ・学食",
        "就職・進路実績",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("学校法人 徳島工学園")
st.sidebar.caption("© Tokushima Institute of Technology and Commerce.")

# ---------------------------------------------------------
# ページ1：トップページ
# ---------------------------------------------------------
if page == "トップページ":
    st.subheader("建学の精神")
    st.info(
        "【建学の精神】\n『阿波の藍より出でて、世界の青に勝る』\n地域で培った技術と学術を練磨し、世界へ羽ばたく技術者を育成する。"
    )

    # キャンパス画像を表示
    st.image(
        "https://i.ibb.co/cjGkrGG/IMG-0132.jpg",
        caption="蔵本キャンパス 全景（徳島市）",
        use_container_width=True,
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 大学からのお知らせ")
        st.write(
            "・2026/07/15: 常三島ベイキャンパス 最先端AIラボの竣工式について"
        )
        st.write(
            "・2026/07/01: バイオ・スマート農工学部"
            " LEDアグリテック技術プレスリリース"
        )
        st.write(
            "・2026/06/20: 2027年度 総合型選抜・学校推薦型選抜の募集要項公開"
        )

    with col2:
        st.write("### 重要なお知らせ（学内者向け）")
        with st.expander("【蔵本】キャンパス間シャトルバスのダイヤ改正について"):
            st.write(
                "蔵本〜常三島ベイキャンパス間の平日運行便数が変更となります。詳細は学内掲示板を確認してください。"
            )
        with st.expander("後期 留学生チューター募集案内"):
            st.write(
                "今年度後期の留学生サポーターを募集します（国際フロンティア工学部推奨）。"
            )

# ---------------------------------------------------------
# ページ2：大学概要・沿革
# ---------------------------------------------------------
elif page == "大学概要・沿革":
    st.header("大学概要・沿革")

    st.write("### 沿革")
    history_data = {
        "年号": [
            "明治8年 (1875)",
            "明治34年 (1901)",
            "昭和24年 (1949)",
            "平成20年 (2008)",
        ],
        "事項": [
            "徳島藩の藍産業および機械技術の近代化を目的に「阿波製藍・機械伝習所」創立",
            "「私立徳島高等工業学校」に改称",
            "学制改革に伴い「徳島工科大学」開設。工学部を設置",
            (
                "「徳島国際工科大学」へ改称。国際フロンティア工学部、スマート農工学部を新設"
            ),
        ],
    }
    st.table(pd.DataFrame(history_data))

    st.write("### キャンパス所在地")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 蔵本キャンパス（本部・1〜2年次）")
        st.write("・所在地: 徳島県徳島市蔵本町")
        st.write("・対象: 全学部の教養科目および基礎専門科目")
    with c2:
        st.markdown("#### 常三島ベイキャンパス（3〜4年次・大学院）")
        st.write("・所在地: 徳島県徳島市港町")
        st.write("・対象: 専門研究、産学連携プロジェクト、先端実験施設")

# ---------------------------------------------------------
# ページ3：学部・学科紹介
# ---------------------------------------------------------
elif page == "学部・学科紹介":
    st.header("学部・学科構成")

    tab1, tab2, tab3 = st.tabs(
        ["工学部", "国際フロンティア工学部", "バイオ・スマート農工学部"]
    )

    with tab1:
        st.subheader("工学部")
        st.write("・機械システム工学科（精密機械・ロボティクス）")
        st.write("・電気電子情報工学科（半導体・電子制御・エネルギー）")
        st.write("・社会環境デザイン学科（治水・防災・都市土木工学）")

    with tab2:
        st.subheader("国際フロンティア工学部")
        st.write("・AI・データサイエンス学科（一部講義を英語で実施）")
        st.write("・グローバル技術経営（MOT）学科（技術マネジメント・技術起業）")

    with tab3:
        st.subheader("バイオ・スマート農工学部")
        st.write(
            "・阿波イノベーション農工学科（LEDアグリテック・発酵工学・植物成分分析）"
        )

# ---------------------------------------------------------
# ページ4：キャンパスライフ・学食
# ---------------------------------------------------------
elif page == "キャンパスライフ・学食":
    st.header("キャンパスライフ")

    st.write("### 学生食堂『阿波らんち』")
    st.info(
        "食堂人気メニュー：徳島ラーメンセット（藍ドレッシングサラダ付） /"
        " 450円"
    )

    st.write("### 在学生メッセージ")
    st.text(
        "「3年次のキャンパス移動に際し、蔵本から常三島への転居か吉野川沿いの通学かを検討することになります」（工学部"
        " 3年）"
    )
    st.text(
        "「キャンパス内には海外からの留学生も多く、日常的に異文化交流が行われています」（国際フロンティア工学部"
        " 2年）"
    )
    st.text(
        "「農工学科の研究用LED植物工場で収穫された野菜が学食で提供されることがあります」（バイオ・スマート農工学部"
        " 4年）"
    )

# ---------------------------------------------------------
# ページ5：就職・進路実績（新規追加）
# ---------------------------------------------------------
elif page == "就職・進路実績":
    st.header("就職・進路実績")

    st.write("### 就職状況サマリー（2025年度実績）")
    st.info(
        "【就職率】 99.8%（就職希望者数：420名 / 就職決定者数：419名）\n【進学率】"
        " 18.5%（本学大学院工学研究科・他大学院含む）"
    )

    st.write("### 学部別 主な就職先・進路")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### ■ 工学部")
        st.write(
            "・**自動車・重工業:** トヨタ自動車、本田技研工業、川崎重工業、デンソー"
        )
        st.write("・**電機・半導体:** パナソニック、ソニー、村田製作所、日立製作所")
        st.write(
            "・**建設・インフラ:**"
            " 鹿島建設、四国電力、中日本高速道路（NEXCO中日本）"
        )

        st.markdown("#### ■ 国際フロンティア工学部")
        st.write(
            "・**IT・通信:** NTTデータ、ソフトバンク、楽天グループ、Google Japan"
        )
        st.write(
            "・**コンサル・SIer:** 野村総合研究所（NRI）、アクセンチュア、TIS"
        )
        st.write("・**グローバル企業:** 外資系IT企業、海外現地法人（エンジニア職）")

    with col2:
        st.markdown("#### ■ バイオ・スマート農工学部")
        st.write(
            "・**食品・アグリ:**"
            " クボタ、ヤンマーホールディングス、サントリーグループ"
        )
        st.write("・**製薬・化学:** 大塚製薬、アステラス製薬、味の素、日亜化学工業")
        st.write(
            "・**公務・研究機構:**"
            " 農林水産省、徳島県庁（農業土木・技術職）、農業・食品産業技術総合研究機構（農研機構）"
        )

    st.markdown("---")

    st.write("### キャリア支援体制")
    st.write("・**1〜2年次:** キャリア形成支援科目（キャリアデザイン、企業OB講演会）")
    st.write("・**3年次:** 実践的インターンシップ（県内・国内外提携企業への派遣）")
    st.write(
        "・**4年次:** 個別面接指導、学内合同企業説明会（年間150社以上が参加）"
    )
