# CoverCraft – AI-Powered Cover Letter Generator

CoverCraft is an automated tool that generates personalized cover letters in LaTeX format. It extracts job descriptions from websites, converts both the job ad and resume into Markdown, and produces a high-quality, ready-to-download PDF cover letter.

## 🚀 Features

- **Scrapes job descriptions** from websites
- **Converts job ads and resumes** into Markdown
- **Generates professional cover letters** using LaTeX
- **Outputs a polished PDF file** ready for submission

## 🛠️ Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/deepukr007/covercraft.git
   cd covercraft
   ```

2. Install dependencies:

   ```sh
   pip install .
   ```

   *(Optional: Create and activate a virtual environment before installation.)*

3. Add your signature image (`sign.png`) inside the `cover_letters_latex` folder.
   
4. Add your CV inside `cv` folder.

5. Customize the LaTeX template (`latex_template.tex`) to match your preferred cover letter style.

7. Rename `.env_example` to `.env` and add your openai apikey


6. Run the application
  ```sh
   streamlit run ui.py
   ```

## 🖊️ Customization

- Modify `cover_letters_latex/latex_template.tex` to adjust the format and styling of your cover letter.
- Update `config/settings.json` to change default preferences.
- Add your own signature image (`sign.png`) for a personalized touch.


## 📧 Contact

For any queries, reach out to [deepukreddy007@example.com](mailto:deepukreddy007@gmail.com) or open an issue on GitHub.
