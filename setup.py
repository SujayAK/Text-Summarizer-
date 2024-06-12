import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "SujayAK"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL= "sujay.k1303@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="NLP for text-summarizer Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email=AUTHOR_EMAIL,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    )
