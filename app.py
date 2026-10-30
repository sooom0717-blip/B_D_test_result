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
        "10301": {"name": "고다경", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10302": {"name": "고은엽", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10303": {"name": "기나은", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10304": {"name": "김명하", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10305": {"name": "김서우", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10306": {"name": "김선준", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10307": {"name": "김은유", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10308": {"name": "서단아", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10401": {"name": "구하연", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10402": {"name": "김리원", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10403": {"name": "김소라", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10404": {"name": "김인혜", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '결론미흡', 'total': 6}},
        "10405": {"name": "나강희", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10406": {"name": "박민호", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10407": {"name": "박상현", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10408": {"name": "손규리", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10409": {"name": "유서준", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10410": {"name": "이미르", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10411": {"name": "이서현", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '결론미흡', 'total': 5}},
        "10412": {"name": "이아인", "b": {'seq': 3, 'conn': 2, 'diag': 2, 'total': 7}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10413": {"name": "이원찬", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10414": {"name": "이은우", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10501": {"name": "김민준", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10502": {"name": "김보은", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10503": {"name": "김지우", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10504": {"name": "노은성", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10505": {"name": "박현서", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10506": {"name": "박효준", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10507": {"name": "방주원", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10508": {"name": "배현민", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10509": {"name": "서예원", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10510": {"name": "서지후", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10511": {"name": "성현우", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10512": {"name": "유선호", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '자기소개', 'total': 1}},
        "10513": {"name": "유하율", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '결론미흡', 'total': 6}},
        "10514": {"name": "이유진", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '', 'total': 0}},
        "10601": {"name": "고도현", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': 'X', 'tone': 'X', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 4}},
        "10602": {"name": "김소윤", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10603": {"name": "김시연", "b": {'seq': 2, 'conn': 1, 'diag': 0, 'total': 3}, "d": {'expr': 'X', 'tone': 'X', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 4}},
        "10604": {"name": "김예지", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10605": {"name": "김정훈", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10701": {"name": "김은율", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10702": {"name": "김하빈", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10703": {"name": "김하은", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 7}},
        "10704": {"name": "노연주", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'X', 'np_lang': 'X', 'note': '', 'total': 6}},
        "10705": {"name": "모현", "b": {'seq': 2, 'conn': 1, 'diag': 1, 'total': 4}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'X', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 5}},
        "10706": {"name": "박시윤", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10707": {"name": "박한율", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10708": {"name": "배소은", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10709": {"name": "신소윤", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10710": {"name": "신승호", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10711": {"name": "신주원", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10712": {"name": "양찬영", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10713": {"name": "이경률", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기+방해', 'total': 1}},
        "10714": {"name": "이소연", "b": {'seq': 1, 'conn': 0, 'diag': 0, 'total': 1}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '포기', 'total': 0}},
        "10801": {"name": "강민우", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10802": {"name": "김가윤", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'X', 'note': '', 'total': 7}},
        "10803": {"name": "김승찬", "b": {'seq': 1, 'conn': 1, 'diag': 0, 'total': 2}, "d": {'expr': '', 'tone': '', 'gram': '', 'p_lang': '', 'np_lang': '', 'note': '중도포기', 'total': 2}},
        "10804": {"name": "김아준", "b": {'seq': 3, 'conn': 3, 'diag': 2, 'total': 8}, "d": {'expr': 'O', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 8}},
        "10805": {"name": "김유빈", "b": {'seq': 3, 'conn': 2, 'diag': 1, 'total': 6}, "d": {'expr': 'X', 'tone': 'O', 'gram': 'O', 'p_lang': 'O', 'np_lang': 'O', 'note': '', 'total': 7}},
    }

data = get_student_database()

# ---------------------------------------------------------
# 3. 메인 화면 - 학번 & 이름 입력 폼
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    student_id_input = st.text_input("학번 4자리", placeholder="예: 1101", max_chars=4).strip()

with col2:
    student_name_input = st.text_input("이름", placeholder="예: 강혜린").strip()

search_button = st.button("성적 조회하기", use_container_width=True, type="primary")

# ---------------------------------------------------------
# 4. 조회 및 결과 검증 로직
# ---------------------------------------------------------
if search_button or (student_id_input and student_name_input):
    if not student_id_input or not student_name_input:
        st.warning("⚠️ 학번과 이름을 모두 입력해 주세요.")
    else:
        if student_id_input in data:
            info = data[student_id_input]
            # 공백 제거 후 이름 일치 확인
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
