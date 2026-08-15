
import streamlit as st
import random

st.set_page_config(page_title="Portfolio | Wishyawan Fuangfung", page_icon= "📚", layout= "wide")

col1, col2 = st.columns([1, 2.5])
with col1:
    st.image("https://i.pinimg.com/736x/5a/1a/ff/5a1aff946125bacc436779ab7c685563.jpg", width=220)
with col2:
    st.title("Wishyawan Fuangfung (Aom)")
    st.subheader("Grade 9 student (Freshman year)")

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎓💼 Experience and Activities","🛠️🧠 skills", "🎮🕹️ minigames", "🌟🎉Achievements", "📞📱 contact information"])

with tab1:
    st.markdown("### 🎓 Experience")
    st.write("- Grade 9 student from Amnuaysilpa school in freshman year studying IGCSE and A levels")
    st.write("- Many achievemnts in different categories suh as: Sports and Music")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 💼 Activities")

    col_p1, col_p2, col_p3, col_p4, col_p5, col_p6= st.columns(6)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### School show")
            st.write("Roles in previous years: Sea Chorus, Young Anna, Belle")
            st.write("partiipated in Little mermaid, Frozen and Beauty and the beast")
            st.write("Role in present year: Full time Student director")
    with col_p2:
        with st.container(border=True):
            st.markdown("#### Duke of Edinburg")
            st.write("4 activities to complete: Adventurous trip, Skills, Fundraising, Sports")
            st.write("Students participating in duk ewill have to log in all their activities each week and go on an adventurous trip to complete the bronze level")
            st.write("This year: Completing the Silver level of Duke of Edinburg")
    with col_p3:
        with st.container(border=True):
            st.markdown("#### Spark")
            st.write("Previous years: Part of spark, supporting aand oing on trips to help people in need")
            st.write("This year: Leader of Spark whith duties such as: plan trips, fundraising, doing events in school")
    with col_p4:
        with st.container(border=True):
            st.markdown("#### Piano and Singing shows")
            st.write("Singing: many show events as well as competitions")
            st.write("Piano: Currenly learning piano Yamaha grade 6 and attended maany show events")
    with col_p5:
        with st.container(border=True):
            st.markdown("###Operation smile")
            st.wite("Part of Operation smile from Y7-present")
            st.write("Helped organise events at school")
    with col_p6:
        with st.container(border=True):
            st.markdown("### Model United Nations")
            st.write("Participted in internal event in the WHO committee")
            st.write("In the future: attend 1 external event, 1 more internal event, and Chair")


with tab2:
    st.markdown("### 🛠️🧠 skills")
    st.write("- singing")
    st.write("- badminton")
    st.write("- piano")
    st.write("- golf")
    st.write("- drums")

