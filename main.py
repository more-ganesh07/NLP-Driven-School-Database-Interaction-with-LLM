from langchain_helper import get_few_shot_db_chain
import streamlit as st

st.markdown("<h2 style='text-align: center;'>Modern School Result Q&A</h2>", unsafe_allow_html=True)

# Brief information about TeeVogue shop
st.markdown("""
            Our Q&A platform features three main tables: Students, Teachers and Marks. 
            The Students Table holds data on student ID, name, grade, gender and coaching class attendance. 
            The Teachers Table contains information on teacher ID, name and subjects taught. 
            The Marks Table records student marks, including subject code, name, marks obtained and grade. 
            These tables offer insights into student demographics, teacher expertise and academic performance for easy exploration and inquiry.
""")

question = st.text_input("Ask a Question:")

# Centering the Submit button
col1, col2, col3 = st.columns([8, 10, 1])
with col2:
    submit_button = st.button("Submit", key="submit_button")

if submit_button:
    if question:
        chain = get_few_shot_db_chain()
        answer = chain.run(question)
        st.header("Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")

# Adding space to align the footer
st.write("<div style='margin-top: px'></div>", unsafe_allow_html=True)

# Add a centered footer
st.markdown("---", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by Human Intelligence, utilizing the power of Artificial Intelligence (LLM).</p>", unsafe_allow_html=True)


