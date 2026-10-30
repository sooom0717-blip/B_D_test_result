import streamlit as st
import pandas as pd
import glob
import os

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
        margin-bottom: 20px;
    }
    .card-container {
        background-color: #F8FAFC;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #E2E8F0;
    }
    .score-badge {
        background-color: #2563EB;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        float: right;
    }
    .level-text {
        font-size: 1.1em;
        font-weight: 600;
        color: #0F172A;
    }
    .badge-a { color: #16A34A; font-weight: bold; } /* 상 / 잘함 */
    .badge-b { color: #D97706; font-weight: bold; } /* 중 / 보통 */
    .badge-c { color: #DC2626; font-weight: bold; } /* 하 / 보완필요 */
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>📝 2학기 국어과 총괄평가 결과 조회</h2>", unsafe_allow_html=True)
st.caption("자신의 학번 4자리(예: 1학년 1반 1번 ➡️ 1101)를 입력하면 평가 결과를 확인할 수 있습니다.")

# ---------------------------------------------------------
# 2. 데이터 로드 및 정형화 함수
# ---------------------------------------------------------
@st.cache_data
def load_all_data():
    """
    각 반별 기준 B 및 기준 D CSV 파일을 병합하여 하나의 데이터프레임으로 변환합니다.
    """
    records = {}

    # 기준 B 변환 기준 (3,2,1점 -> 상,중,하 라벨링)
    score_map_3pt = {3: ("높은 수준 (A)", "badge-a"), 2: ("보통 수준 (B)", "badge-b"), 1: ("보완이 필요한 수준 (C)", "badge-c")}
    score_map_2pt = {2: ("높은 수준 (A)", "badge-a"), 1: ("보통 수준 (B)", "badge-b"), 0: ("보완이 필요한 수준 (C)", "badge-c")}

    # 1~8반 파일 순회 (기준 B)
    for grade_class in range(1, 9):
        b_files = glob.glob(f"*기준B_총괄_{grade_class}반*.csv")
        if not b_files:
            continue
        
        file_path = b_files[0]
        # 헤더 전 정크 데이터가 있을 경우 처리
        try:
            df = pd.read_csv(file_path)
            # 헤더 행 찾기 ('순서' 열 포함 행)
            header_idx = None
            for idx, row in df.iterrows():
                if '순서' in row.values:
                    header_idx = idx
                    break
            
            if header_idx is not None:
                df = pd.read_csv(file_path, skiprows=header_idx + 1)
            
            # 컬럼 정제
            df.columns = [str(c).strip() for c in df.columns]
            
            # 번호 및 학생 데이터 추출
            for _, row in df.iterrows():
                try:
                    num = int(row.iloc[0]) # 번호
                    name = str(row.iloc[1]).strip()
                    student_id = f"1{grade_class:02d}{num:02d}" # 예: 1101
                    
                    seq_score = int(row['순서']) if pd.notnull(row['순서']) else 0
                    conn_score = int(row['연결']) if pd.notnull(row['연결']) else 0
                    diag_score = int(row['도식화']) if pd.notnull(row['도식화']) else 0
                    total_b = int(row['총점']) if pd.notnull(row['총점']) else (seq_score + conn_score + diag_score)
                    
                    if student_id not in records:
                        records[student_id] = {"name": name}
                    
                    records[student_id]["criterion_b"] = {
                        "sequence": score_map_3pt.get(seq_score, ("미제출/미완성", "badge-c")),
                        "connection": score_map_3pt.get(conn_score, ("미제출/미완성", "badge-c")),
                        "diagram": score_map_2pt.get(diag_score, ("미제출/미완성", "badge-c")),
                        "total_level": total_b
                    }
                except (ValueError, TypeError, KeyError):
                    continue
        except Exception:
            pass

    # 1~8반 파일 순회 (기준 D)
    for grade_class in range(1, 9):
        d_files = glob.glob(f"*기준D_총괄_{grade_class}반*.csv")
        if not d_files:
            continue
            
        file_path = d_files[0]
        try:
            df = pd.read_csv(file_path)
            header_idx = None
            for idx, row in df.iterrows():
                if '표현' in row.values:
                    header_idx = idx
                    break
            
            if header_idx is not None:
                df = pd.read_csv(file_path, skiprows=header_idx + 1)
                
            df.columns = [str(c).strip() for c in df.columns]
            
            for _, row in df.iterrows():
                try:
                    num = int(row.iloc[0])
                    student_id = f"1{grade_class:02d}{num:02d}"
                    
                    expr = str(row.get('표현', '')).upper()
                    tone = str(row.get('말투', '')).upper()
                    gram = str(row.get('문법', '')).upper()
                    p_lang = str(row.get('준언어', '')).upper()
                    np_lang = str(row.get('비언어', '')).upper()
                    special_note = str(row.get('포/자/중/안', ''))
                    
                    total_d = int(row['총점']) if pd.notnull(row.get('총점')) else 0
                    
                    # 보완 필요(X) 항목 추출
                    improvements = []
                    if expr == 'X': improvements.append("표현")
                    if tone == 'X': improvements.append("말투 및 어조")
                    if gram == 'X': improvements.append("문법 및 어휘")
                    if p_lang == 'X': improvements.append("준언어(목소리 크기/빠르기)")
                    if np_lang == 'X': improvements.append("비언어(시선/표정/자세)")
                    
                    if student_id not in records:
                        records[student_id] = {"name": str(row.iloc[1]).strip()}
                        
                    records[student_id]["criterion_d"] = {
                        "total_level": total_d,
                        "improvements": improvements,
                        "note": special_note if special_note != 'nan' else ""
                    }
                except (ValueError, TypeError, KeyError):
                    continue
        except Exception:
            pass

    return records

data = load_all_data()

# ---------------------------------------------------------
# 3. 사용자 입력 및 결과 조회 UI
# ---------------------------------------------------------
student_id_input = st.text_input("학번 4자리를 입력하세요 (예: 1101)", max_chars=4)

if student_id_input:
    if student_id_input in data:
        info = data[student_id_input]
        st.success(f"**{info['name']}** 학생의 성적 결과입니다.")
        st.write("---")

        # --- [기준 B : 조직화하기] ---
        st.subheader("📌 기준 B : 조직화하기 (발표 조직 개요 작성)")
        if "criterion_b" in info:
            b_res = info["criterion_b"]
            seq_txt, seq_cls = b_res["sequence"]
            conn_txt, conn_cls = b_res["connection"]
            diag_txt, diag_cls = b_res["diagram"]
            
            st.markdown(f"""
            <div class='card-container'>
                <span class='score-badge'>총 {b_res['total_level']}수준 (8수준 만점)</span>
                <p><b>• 순서 구성:</b> <span class='{seq_cls}'>{seq_txt}</span></p>
                <p><b>• 내용 연결:</b> <span class='{conn_cls}'>{conn_txt}</span></p>
                <p><b>• 도식화 표현:</b> <span class='{diag_cls}'>{diag_txt}</span></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("기준 B 평가 결과 데이터가 없습니다.")

        # --- [기준 D : 언어 사용하기] ---
        st.subheader("🗣️ 기준 D : 언어 사용하기 (발표 총괄평가)")
        if "criterion_d" in info:
            d_res = info["criterion_d"]
            level = d_res["total_level"]
            imps = d_res["improvements"]
            
            st.markdown(f"""
            <div class='card-container'>
                <span class='score-badge'>총 {level}수준</span>
            """, unsafe_allow_html=True)

            # 수준별 세부 설명
            if level == 0:
                st.write("**평가 피드백:** 아쉬움이 남는 평가입니다. 다음 평가에서는 꼭 도전해 봅시다.")
            elif level == 1:
                st.write("**평가 피드백:** 자기소개 중심으로 참여하였습니다.")
            elif level == 2:
                st.write("**평가 피드백:** 발표를 시도하였으나 중간에 마무리가 되었습니다.")
            elif level == 3:
                st.write("**평가 피드백:** 발표를 완료하였으나 목소리가 전달되기 어려운 수준이었습니다.")
            else:
                if imps:
                    st.write(f"**다음 발표에서 보완하면 좋을 요소:**")
                    for item in imps:
                        st.write(f"- 💡 **{item}**")
                else:
                    st.write("🎉 **모든 영역(표현, 말투, 문법, 준언어, 비언어)에서 훌륭한 수준을 보여주었습니다!**")
            
            if d_res["note"]:
                st.caption(f"※ 참고사항: {d_res['note']}")
                
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("기준 D 평가 결과 데이터가 없습니다.")

    else:
        st.error("입력한 학번을 찾을 수 없습니다. 학번을 정확히 입력했는지 확인해 주세요.")