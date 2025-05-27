import streamlit as st

st.title("🌱 Growth Mindset Challenge")

st.markdown("""
    <h1 style='text-align: center; color: #6a0dad; font-size: 3em; animation: glow 1.5s ease-in-out infinite alternate;'>
        🌱 Growth Mindset Challenge
    </h1>
    <style>
        @keyframes glow {
            from {
                text-shadow: 0 0 10px #6a0dad, 0 0 20px #ba55d3;
            }
            to {
                text-shadow: 0 0 20px #dda0dd, 0 0 30px #ba55d3;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stButton>button {
            background-color: #f4f4f4;
            color: #6a0dad;
            border: 2px solid #6a0dad;
            padding: 0.5em 1em;
            font-weight: bold;
            transition: 0.3s;
            border-radius: 12px;
        }
        .stButton>button:hover {
            background-color: #6a0dad;
            color: white;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

if st.button("💡 Get Today's Challenge"):
    st.success("Write down 3 things you learned this week and how they made you grow!")

with st.expander("💭 Reflect on Your Week"):
    q1 = st.text_input("What is one challenge you overcame?")
    q2 = st.text_input("What new skill did you try or improve?")
    q3 = st.text_input("How did you show resilience?")

    if q1 and q2 and q3:
        st.success("👏 Great reflection! You're building a strong growth mindset.")

if st.button("🌟 Submit Reflection"):
    st.balloons()
    st.success("Reflection Submitted! Keep going 🚀")

st.markdown("---")
st.markdown("<p style='text-align:center;'>Created with ❤️ by Almas ImdadAli</p>", unsafe_allow_html=True)


