from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="affan khalid",
    author_email= "affankhalid560@gmail.com",
    install_requires = ["python-dotenv","streamlit","langchain","langchain-openai","langchain-community","langchain-groq","PyPDF"],
    packages = find_packages()
)