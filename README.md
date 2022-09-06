# Predicting GitHub Repo Programming Language
By David Schneemann, Jarad Angel, Joshua Mayes, and Saroj Duwal

## Readme Outline
- [Project Description](#project_desc)  
    - [Scenario](#scenario)
    - [Goals](#goals)
        - [Deliverables](#deliverables)
    - [Project Dependencies](#dependencies)

- [About the data](#data)
    - Scope
    - Acquiring
    - Preparing
    - Data Dictionary

- [Project Planning](#plan)  


# About the project <a name="project_desc"></a>
Using the text of the README files, this project aims to predict the most popular coding language present in a repository.

## Scenario <a name="scenario"></a>

{Describe the use case or business context that is the driver behind the project}

> __Agile Story__  
    As a {persona}  
    I want {feature}  
    So that {goal}  

## Goals <a name="goals"></a>

Classify the dominant project language within 80% accuracy using machine learning algorithms.  Engineer features from the project's README.md file using TF and IDF, as well as the occurrance of certain keywords inside of a document.

### Deliverables <a name="deliverables"></a>

- Report notebook titled `Report.ipynb`
- Google Slides presentation consisting of 2-5 content slides.

## Reproducing this project <a name="requirements"></a>

<!-- Add NLTK and the NLTK downloads -->

### Dependencies

This project makes use of several technologies that will need to be installed
* [![python-shield](https://img.shields.io/badge/Python-3-blue?&logo=python&logoColor=white)
    ](https://www.python.org/)
* [![jupyter-shield](https://img.shields.io/badge/Jupyter-notebook-orange?logo=jupyter&logoColor=white)
    ](https://jupyter.org/)
* [![numpy-shield](https://img.shields.io/badge/Numpy-grey?&logo=numpy)
    ](https://numpy.org/)
* [![pandas-shield](https://img.shields.io/badge/Pandas-grey?&logo=pandas)
    ](https://pandas.pydata.org/)
* [![matplotlib-shield](https://img.shields.io/badge/Matplotlib-grey.svg?)
    ](https://matplotlib.org)
* [![seaborn-shield](https://img.shields.io/badge/Seaborn-grey?&logoColor=white)
    ](https://seaborn.pydata.org/)
* [![scipy-shield](https://img.shields.io/badge/SciPy-grey?&logo=scipy&logoColor=white)
    ](https://scipy.org/)
* [![sklearn-shield](https://img.shields.io/badge/_-grey?logo=scikitlearn&logoColor=white&label=scikit-learn)
    ](https://scikit-learn.org/stable/)

Dependencies can be installed quickly with just a few lines of code.
```
%pip install notebook
%pip install numpy
%pip install pandas
%pip install matplotlib
%pip install seaborn
%pip install scipy
%pip install sklearn
```

# About the data <a name="data"></a>

We scraped ~1000 Github repositories from the list of most forked repositories to gather readme files and information from GitHub's language statitics.

## Scope

For exploration and modeling we ignored any repositories featuring a language for which we did not scrape at least 10 samples, as well as any repositories that did not feature a language at all.

## Acquiring

Data acquisition used a combination of web-scraping and GitHub's API.

## Preparing

To prepare the data for exploration and modeling we performed the following steps:
- Markdown links were removed from the corpus since the urls did not provide meaningful information
- HTML elements such as \<li>\</li> and \<strong>\</strong> were also removed for the same reason
- The text was then normalized and stripped of special characters
- Stopwords were removed
- New columns were created in the dataframe to represent the cleaned and lemmatized versions of the original

## Data Dictionary


# Project Planning <a name="plan"></a>

## Initial Hypotheses
- If a language is mentioned in the readme it is more likely dominated by that language
- Topics surrounding web development are more likely written in html, javascript and css
- Readmes that talk about studying or hiring are likely written in english
