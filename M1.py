
import streamlit as st
import random

st.set_page_config(page_title="Portfolio | Wishyawan Fuangfung", page_icon= "📚", layout= "wide")

col1, col2 = st.columns([1, 2.5])
with col1:
    pass
with col2:
    st.title("Wishyawan Fuangfung (Aom)")
    st.subheader("Student grade 9")
    st.write("""
    omcoim,fmivnu9kefkonzcxmsdasd
    """)

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["🎓💼 Experience and Activities","🛠️🧠 skills", "🎮🕹️ minigames", "📞📱 contact information"])

with tab1:
    st.markdown("### 🎓 Experience")
    st.write("- grade 9 student")
    st.write("- lead actor and singer in school show")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 💼 Activities")

    col_p1, col_p2, col_p3, col_p4 = st.columns(4)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### School show and director")
            st.write("Roles: Sea Chorus, Young Anna, Belle")
            st.write("Director trainee in the present")
    with col_p2:
        with st.container(border=True):
            st.markdown("#### TedxAmnuaysilpa")
            st.write("Tedx speaker: Paradox of Selfishness")
            st.write("MC: introduce and create flow to the show")
    with col_p3:
        with st.container(border=True):
            st.markdown("#### spark")
            st.write("Spark member for 3 years")
            st.write("Spark leader to various events in the present")
    with col_p4:
        with st.container(border=True):
            st.markdown("#### Operation smile")
            st.write("operation smile member event 1 for 2 years")
            st.write("ISLC member in the present")

    st.write("- **Director")
    st.write("- School show experience for 4 years")
    st.write("- **student council member")
    st.write("- 3 year experience being oart of the council team")

with tab2:
    st.markdown("### 🛠️🧠 skills")
    st.write("- singing")
    st.write("- badminton")
    st.write("- piano")
    st.write("- golf")
    st.write("- drums")

