import time
import streamlit as st
from PIL import Image, ImageSequence

st.set_page_config(
    page_title="Birthday Surprise.",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BACKGROUND_COLOR = "#FF96D5"

st.markdown(f"""
    <style>
        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}
        .block-container {{
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }}
        header, footer, #MainMenu {{
            visibility: hidden;
            display: none !important;
        }}
        div.stButton > button {{
            width: 100%;
            border-radius: 10px;
            border: 2px solid #ffffff;
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            font-weight: bold;
            padding: 10px;
            transition: all 0.3s ease;
        }}
        div.stButton > button:hover {{
            background-color: rgba(255, 255, 255, 0.5);
            color: #000000;
            border-color: #000000;
        }}
        @media (orientation: portrait) {{
            .stApp::before {{
                content: "Please rotate your phone sideways";
                position: fixed;
                inset: 0;
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: {BACKGROUND_COLOR};
                color: white;
                font-size: 1.5rem;
                font-weight: bold;
                text-align: center;
                padding: 2rem;
            }}
        }}
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def gif_seconds(path):
    total_ms = 0
    with Image.open(path) as gif:
        for frame in ImageSequence.Iterator(gif):
            total_ms += frame.info.get("duration", 100)
    return total_ms / 1000


def play_gif(path):
    st.image(path, use_container_width=True)
    time.sleep(gif_seconds(path) + 0.5)

def go_to(step_number):
    st.session_state.step = step_number

if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    play_gif("quick_question.gif")
    st.button("Next", key="s1_next", on_click=go_to, args=(2,))

elif st.session_state.step == 2:
    play_gif("are_you_age.gif")
    st.button("Next", key="s2_next", on_click=go_to, args=(3,))

elif st.session_state.step == 3:
    play_gif("yes_or_yes.gif")
    left, right = st.columns(2)
    with left:
        st.button("Yes", key="s3_left", on_click=go_to, args=(4,))
    with right:
        st.button("Yes!", key="s3_right", on_click=go_to, args=(4,))

elif st.session_state.step == 4:
    st.balloons()
    st.markdown("""
    <style>
        .heart {
            position: fixed;
            bottom: -50px;
            font-size: 30px;
            pointer-events: none;
            animation: floatup 6s linear infinite;
        }
        @keyframes floatup {
            to { transform: translateY(-110vh); opacity: 0; }
        }
    </style>
    <div class="heart" style="left: 10%;">💖</div>
    <div class="heart" style="left: 40%; animation-delay: 2s;">💗</div>
    <div class="heart" style="left: 70%; animation-delay: 4s;">💕</div>
    """, unsafe_allow_html=True)
    st.image("happy_birthday_unc.gif", use_container_width=True)
    st.button("Play Again", key="reset_game", on_click=go_to, args=(1,))