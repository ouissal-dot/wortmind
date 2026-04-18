import streamlit as st
import random
from utils.storage import load_data, save_data

# Load data
data = load_data()
if data is None:
    data = {}

st.title("WortMind 🧠🇩🇪")
st.write("Learn German vocabulary with flashcards")

# ---------------- SELECT BOX ----------------
st.subheader("Choose a box")
cols = st.columns(len(data))
for i, (box_name, words) in enumerate(data.items()):
    with cols[i]:
        label = f"**{box_name}**\n\n{len(words)} words"
        if st.button(label, key=box_name, use_container_width=True):
            st.session_state.selected_box = box_name

selected_box = st.session_state.get("selected_box", list(data.keys())[0])
words = data[selected_box]

# ---------------- PRACTICE SECTION ----------------
st.subheader("Cards")

if len(words) > 0:
    if "current_word" not in st.session_state:
        st.session_state.current_word = random.choice(words)
    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    word = st.session_state.current_word

    if not st.session_state.show_answer:
        st.markdown(
            f"""
            <div style="background:#fff; border:1px solid #ddd; border-radius:16px;
            padding:3rem; text-align:center; font-size:2rem; font-weight:500;">
            🇩🇪 {word['de']}
            </div>
            """, unsafe_allow_html=True
        )
        if st.button("Flip Card ↩️", use_container_width=True):
            st.session_state.show_answer = True
            st.rerun()
    else:
        st.markdown(
            f"""
            <div style="background:#EEEDFE; border:1px solid #AFA9EC; border-radius:16px;
            padding:3rem; text-align:center;">
            <div style="font-size:1.8rem; font-weight:500; color:#3C3489;">{word['ar']} 🇸🇦</div>
            <div style="margin-top:1rem; font-style:italic; color:#534AB7;">✍️ {word['sentence']}</div>
            </div>
            """, unsafe_allow_html=True
        )
        if st.button("Next Word →", use_container_width=True):
            st.session_state.current_word = random.choice(words)
            st.session_state.show_answer = False
            st.rerun()
else:
    st.warning("No words in this box yet. Add some words first!")

# ---------------- ADD NEW WORD ----------------
st.subheader("➕ Add New Word")

de_word = st.text_input("German word 🇩🇪")
ar_word = st.text_input("Arabic meaning 🇸🇦")
sentence = st.text_input("Example sentence ✍️")

if st.button("Add Word"):
    if de_word and ar_word:
        new_word = {
            "de": de_word,
            "ar": ar_word,
            "sentence": sentence
        }

        data[selected_box].append(new_word)
        save_data(data)

        st.success("Word added successfully!")

