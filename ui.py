import streamlit as st
from main import get_job_ad, get_cv, cover_letter_agent, md
import subprocess
import os
from pathlib import Path
import re
from streamlit_pdf_viewer import pdf_viewer
from glob import glob

st.set_page_config(page_title="Cover Letter Generator", layout="wide")
job_ad_text = None

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = None
    st.session_state.editable_latex = None
    st.session_state.clean_text = None


job_ad_type = st.selectbox("Job AD Type", ["URL", "Text"])
if job_ad_type == "URL":
    job_ad_url = st.text_input("Enter Job ad URL")
    if job_ad_url:
        job_ad_text = get_job_ad(job_ad_url, url=True)

else:
    job_ad_input = st.text_area("Enter Job ad text")
    job_ad_text = get_job_ad(job_ad_input)

cv_pdfs = glob(os.path.join("cv", "*.pdf"))
selected_pdf = st.selectbox("Select CV", cv_pdfs)


if selected_pdf and (job_ad_text or job_ad_url):
    with st.container(height=300):
        col1, col2 = st.columns(2, border=True)
        cv = get_cv(selected_pdf)
        col1.header("CV")
        col1.markdown(cv)
        col2.header("Job AD")
        col2.markdown(job_ad_text)


if st.button("Generate Cover Letter"):
    st.header("Cover Letter")
    latex_template = md.convert("latex_template.txt").text_content

    st.session_state.cover_letter = cover_letter_agent(job_ad_text, cv, latex_template)
    st.session_state.clean_text = re.sub(
        r"```latex\n(.*?)\n```", r"\1", st.session_state.cover_letter, flags=re.DOTALL
    )

if st.session_state.clean_text:
    st.session_state.editable_latex = st.text_area(
        "Generated Cover Letter", st.session_state.clean_text, height=300
    )

if st.session_state.editable_latex:
    generate_pdf = st.button("Generate PDF")
    if generate_pdf:
        os.makedirs("cover_letters_latex", exist_ok=True)
        with open(Path("cover_letters_latex/cover_letter.tex"), "w") as f:
            f.write(st.session_state.editable_latex)
        os.chdir("cover_letters_latex")

        try:
            subprocess.run(["pdflatex", "cover_letter.tex"], check=True)
            pdf_viewer("cover_letter.pdf")
        finally:
            os.chdir("..")
