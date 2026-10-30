import streamlit as st

# ---------------------------------------------------------
# 1. 페이지 설정 및 스타일링
# ---------------------------------------------------------
st.set_page_config(
    page_title="2학기 국어과 총괄평가 결과 조회",
    page_icon="📝",
    layout="centered"
)

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .sub-title {
        text-align: center;
        color: #475569;
        font-size: 0.95em;
        margin-bottom: 25px;
    }
    .card-container {
        background-color: #F8FAFC;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .score-badge {
        background-color: #2563EB;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        float: right;
    }
    .badge-a { color: #16A34A; font-weight: bold; } 
    .badge-b { color: #D97706; font-weight: bold; } 
    .badge-c { color: #DC2626; font-weight: bold; } 
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📝 2학기 국어과 총괄평가 결과 조회</h2>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>본인의 <b>학번 4자리</b>와 <b>이름</b>을 정확히 입력해 주세요.</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. 내장 데이터베이스 (학번: {이름, 기준B, 기준D})
# ---------------------------------------------------------
@st.cache_data
def get_student_database():
    # 1반~8반 전 학생 데이터 매핑 (일부 샘플 및 실제 데이터 연결 구조)
    db = {
        "10101": {"name": "강혜린", "b": {"seq": 2, "conn": 1, "diag": 2, "total": 5}, "d": {"expr": "X", "tone": "O", "gram": "O", "p_lang": "O", "np_lang": "X", "note": "", "total": 6}},
        "10102": {"name": "김동현", "b": {"seq": 2, "conn": 1, "diag": 0, "total": 3}, "d": {"expr": "X", "tone": "O", "gram": "O", "p_lang": "X", "np_lang": "O", "note": "", "total": 6}},
        "10103": {"name": "김라연", "b": {"seq": 3, "conn": 2, "diag": 1, "total": 6}, "d": {"expr": "X", "tone": "O", "gram": "O", "p_lang": "O", "np_lang": "X", "note": "결론미흡", "total": 5}},
        "10104": {"name": "김정원", "b": {"seq": 2, "conn": 1, "diag": 1, "total": 4}, "d": {"expr": "", "tone": "", "gram": "", "p_lang": "", "np_lang": "", "note": "중도포기", "total": 2}},
        "10105": {"name": "김지후", "b": {"seq": 3, "conn": 2, "diag": 2, "total": 7}, "d": {"expr": "O", "tone": "O", "gram": "O", "p_lang": "X", "np_lang": "X", "note": "결론미흡", "total": 5}},
        "10106": {"name": "김하은", "b": {"seq": 3, "conn": 3, "diag": 2, "total": 8}, "d": {"expr": "O", "tone": "O", "gram": "O", "p_lang": "O", "np_lang": "O", "note": "", "total": 8}},
        "10107": {"name": "노시온", "b": {"seq": 3, "conn": 3, "diag": 2, "total": 8}, "d": {"expr": "O", "tone": "O", "gram": "O", "p_lang": "O", "np_lang": "O", "note": "", "total": 8}},
        "10108": {"name": "박한율", "b": {"seq": 3, "conn": 2, "diag": 2, "total": 7}, "d": {"expr": "O", "tone": "O", "gram": "O", "p_lang": "O", "np_lang": "O", "note": "결론미흡", "total": 7}},
        "10201": {"name": "강소의", "b": {"seq": 3, "conn": 2, "diag": 1, "total": 6}, "d": {"expr": "X", "tone": "O", "gram": "O", "p_lang": "O", "np_lang": "X", "note": "", "total": 6}},
        "10801": {"name": "강민우", "b": {"seq": 1, "conn": 1, "diag": 0, "total": 2}, "d": {"expr": "", "tone": "", "gram": "", "p_lang": "", "np_lang": "", "note": "중도포기", "total": 2}},
    }
    return db

data = get_student_database()

# ---------------------------------------------------------
# 3. 메인 화면 - 학번 & 이름 입력 입력 폼
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    student_id_input = st.text_input("학번 4자리", placeholder="예: 1101", max_chars=4).strip()

with col2:
    student_name_input = st.text_input("이름", placeholder="예: 홍길동").strip()

search_button = st.button("성적 조회하기", use_container_width=True, type="primary")

# ---------------------------------------------------------
# 4. 조회 및 결과 검증 로직
# ---------------------------------------------------------
if search_button or (student_id_input and student_name_input):
    if not student_id_input or not student_name_input:
        st.warning("⚠️ 학번과 이름을 모두 입력해 주세요.")
    else:
        # 1. 학번 존재 여부 확인
        if student_id_input in data:
            info = data[student_id_input]
            # 2. 이름 일치 여부 확인 (공백 제거 후 비교)
            if info["name"].replace(" ", "") == student_name_input.replace(" ", ""):
                st.success(f"🎉 **{info['name']}** 학생의 평가 결과입니다.")
                st.write("---")

                # --- [기준 B : 조직화하기] ---
                st.subheader("📌 기준 B : 조직화하기 (발표 조직 개요 작성)")
                if "b" in info:
                    b = info["b"]
                    def map_b(score, max_val):
                        if max_val == 3:
                            if score == 3: return "높은 수준 (A)", "badge-a"
                            elif score == 2: return "보통 수준 (B)", "badge-b"
                            else: return "보완이 필요한 수준 (C)", "badge-c"
                        else:
                            if score >= 2: return "높은 수준 (A)", "badge-a"
                            elif score == 1: return "보통 수준 (B)", "badge-b"
                            else: return "보완이 필요한 수준 (C)", "badge-c"

                    seq_txt, seq_cls = map_b(b["seq"], 3)
                    conn_txt, conn_cls = map_b(b["conn"], 3)
                    diag_txt, diag_cls = map_b(b["diag"], 2)

                    st.markdown(f"""
                    <div class='card-container'>
                        <span class='score-badge'>총 {b['total']}수준 (8수준 만점)</span>
                        <p><b>• 순서 구성:</b> <span class='{seq_cls}'>{seq_txt}</span></p>
                        <p><b>• 내용 연결:</b> <span class='{conn_cls}'>{conn_txt}</span></p>
                        <p><b>• 도식화 표현:</b> <span class='{diag_cls}'>{diag_txt}</span></p>
                    </div>
                    """, unsafe_allow_html=True)

                # --- [기준 D : 언어 사용하기] ---
                st.subheader("🗣️ 기준 D : 언어 사용하기 (발표 총괄평가)")
                if "d" in info:
                    d = info["d"]
                    level = d["total"]
                    
                    st.markdown(f"""
                    <div class='card-container'>
                        <span class='score-badge'>총 {level}수준</span>
                    """, unsafe_allow_html=True)

                    if level == 0 or d["note"] == "포기":
                        st.write("**평가 피드백:** 아쉬움이 남는 평가입니다. 다음 평가에서는 꼭 도전해 봅시다.")
                    elif level == 1 or d["note"] == "자기소개":
                        st.write("**평가 피드백:** 자기소개 중심으로 참여하였습니다.")
                    elif level == 2 or d["note"] == "중도포기":
                        st.write("**평가 피드백:** 발표를 시도하였으나 중간에 마무리가 되었습니다.")
                    elif level == 3 or d["note"] == "안들림":
                        st.write("**평가 피드백:** 발표를 완료하였으나 목소리가 전달되기 어려운 수준이었습니다.")
                    else:
                        imps = []
                        if d["expr"] == 'X': imps.append("표현")
                        if d["tone"] == 'X': imps.append("말투 및 어조")
                        if d["gram"] == 'X': imps.append("문법 및 어휘")
                        if d["p_lang"] == 'X': imps.append("준언어(목소리 크기/빠르기)")
                        if d["np_lang"] == 'X': imps.append("비언어(시선/표정/자세)")

                        if imps:
                            st.write("**다음 발표에서 보완하면 좋을 요소:**")
                            for item in imps:
                                st.write(f"- 💡 **{item}**")
                        else:
                            st.write("🎉 **모든 영역(표현, 말투, 문법, 준언어, 비언어)에서 훌륭한 수준을 보여주었습니다!**")

                    if d["note"] and d["note"] not in ["포기", "자기소개", "중도포기", "안들림"]:
                        st.caption(f"※ 참고사항: {d['note']}")
                        
                    st.markdown("</div>", unsafe_allow_html=True)

            else:
                st.error("❌ 입력하신 학번과 이름이 일치하지 않습니다. 학번과 이름을 다시 확인해 주세요.")
        else:
            st.error("❌ 등록되지 않은 학번입니다. 학번 4자리를 정확히 입력했는지 확인해 주세요.")
