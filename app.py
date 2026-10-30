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
# 2. 전체 1~8반 학생 데이터베이스 (173명 전체 포함)
# ---------------------------------------------------------
@st.cache_data
def get_student_database():
    return {
        "10101": {"name": "강혜린", "b": {'seq': 2, 'conn': 1, 'diag': 2, 'total': 5}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10102": {"name": "김동현", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'O', 'note': '', 'total': 6}},
        "10103": {"name": "김라연", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '결론미흡', 'total': 5}},
        "10104": {"name": "김정원", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10105": {"name": "김지후", "b": {'seq': 3, 'conn': 3, 'diag': 1, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '결론미흡', 'total': 5}},
        "10106": {"name": "김하은", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10107": {"name": "노시온", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10108": {"name": "박한율", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '결론미흡', 'total': 7}},
        "10109": {"name": "배도윤", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'X', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10110": {"name": "배상진", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10111": {"name": "서태민", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '결론미흡', 'total': 5}},
        "10112": {"name": "송효제", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10113": {"name": "양하원", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '결론미흡', 'total': 6}},
        "10114": {"name": "이도훈", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10115": {"name": "이서연", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10116": {"name": "이시윤", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10117": {"name": "이연서", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10118": {"name": "이윤성", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10119": {"name": "이주현", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10120": {"name": "임주원", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10121": {"name": "정서현", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10122": {"name": "정소윤", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10123": {"name": "정유준", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10124": {"name": "정윤호", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10125": {"name": "정지민", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10126": {"name": "정하은", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10127": {"name": "조민준", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10128": {"name": "조아인", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10129": {"name": "조예준", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10130": {"name": "주예은", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10131": {"name": "진서우", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10132": {"name": "천우진", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10133": {"name": "최서윤", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10134": {"name": "최서정", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10135": {"name": "최예원", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10136": {"name": "최우진", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10137": {"name": "한서준", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10138": {"name": "한예린", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10139": {"name": "허윤서", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10140": {"name": "홍지유", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10141": {"name": "황서준", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10142": {"name": "황예린", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10143": {"name": "황지유", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10201": {"name": "강소의", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10202": {"name": "김미설", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10203": {"name": "김세민", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10204": {"name": "김시아", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 7}},
        "10205": {"name": "김시안", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10206": {"name": "김시은", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10207": {"name": "김운호", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 7}},
        "10208": {"name": "김하엘", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10209": {"name": "문태영", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10210": {"name": "석정민", "b": {'seq': 2, 'conn': 2, 'diag': 1, 'total': 5}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10211": {"name": "임수현", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10212": {"name": "최준서", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 7}},
        "10213": {"name": "홍수민", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 7}},
        "10214": {"name": "엄이령", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10215": {"name": "김준오", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10216": {"name": "조민수", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10217": {"name": "하은하", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10218": {"name": "김지성", "b": {'seq': 1, 'conn': 0, 'diag': 0, 'total': 1}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '포기', 'total': 0}},
        "10301": {"name": "고다경", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O
