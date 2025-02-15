from markitdown import MarkItDown
from openai import OpenAI
from rich.console import Console
import os

from dotenv import load_dotenv

md = MarkItDown()
console = Console()

load_dotenv(".env")


def get_job_ad(url_or_text: str, url: bool = False):
    console.rule("[bold red]Job Ad")
    if url:
        print(url_or_text)
        job_ad = md.convert(url_or_text).text_content
    else:
        job_ad = url_or_text
    console.log(job_ad)
    return job_ad


def get_cv(cv_path):
    console.rule("CV")
    cv = md.convert(cv_path).text_content
    console.log(cv)
    return cv


def gpt_agent():
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    return client


def cover_letter_agent(job_ad: str, cv: str, latex_template: str):
    console.rule("Cover letter")
    client = gpt_agent()

    system_prompt = (
        f"Write a professional and tailored cover letter in latex for the give latex template . "
        f"Highlight my skills given in my cv which also includes my background, "
        f"achievements, education, e.g.,.\n\n"
        f"Focus on why I’m an excellent fit for the role, my enthusiasm for the company, and how my skills align with their needs. "
        f"Keep the tone professional and enthusiastic\n\n"
        f"Summarize my skills and experience relevant to this position, showcasing my qualifications and background"
        f"Explain how my skills , projects and experience match the requirements for the the given position."
        f"Try to complete main content in 300-400 words\n\n"
        f"Do not forget to put \\ and vspace after each paragraph\n\n"
        f"There are varibles in latex template which needs to be replaced with values for eg salutation , managername , comapany name , jobtitile etc.. \n\n"
        f"If you do not find the manager name put Hiring Manager\n\n"
        f"If you do not find the address of the company comment out the address lines\n\n"
        f"If you cant find the values for the variables in the job ad , you can put xxxxxxx in that place\n\n"
        f"for date in latex you can use \today command \n\n"
        f"Make sure to draft the cover letter in a factal way"
        f"Make sure to use the job ad to draft the cover letter"
        f"<latextemplate>{latex_template}</latextemplate> \n"
        f"Do not output anything other than latex"
        f"Do not make up the job role/position always use the job ad for the job role"
        f"Alwasy output latex in this format```latex\n\n latex code \n\n```"
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": job_ad},
            {"role": "user", "content": cv},
        ],
    )

    cover_letter = completion.choices[0].message.content
    console.log(cover_letter)

    return cover_letter
