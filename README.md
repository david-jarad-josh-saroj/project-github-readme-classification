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

This project serves as a proof of concept to demonstrate the viability of these types of classification problems using free-form text as an input.

<!-- > __Agile Story__  
    As a {persona}  
    I want {feature}  
    So that {goal}   -->

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
* [![nltk-shield](https://img.shields.io/badge/NLTK-grey?&logo=&logoColor=white)
    ](https://textblob.readthedocs.io/en/dev/)
* [![xgboost-shield](https://img.shields.io/badge/XGBoost-grey?&logo=&logoColor=white)
    ](https://xgboost.readthedocs.io/en/stable/)
* [![textblob-shield](https://img.shields.io/badge/TextBlob-grey?&logo=&logoColor=white)
    ](https://textblob.readthedocs.io/en/dev/)


Dependencies can be installed quickly with just a few lines of code.
```
%pip install notebook
%pip install numpy
%pip install pandas
%pip install matplotlib
%pip install seaborn
%pip install scipy
%pip install sklearn
%pip install nltk
%pip install xgboost
%pip install textblob
```

Additionally, our implementation of NLTK relies on some data that is not included in the base package. The following script will ensure the data is installed in your environmnet:
```
import nltk

# Ensuring required data is installed.
try:
    nltk.data.find('corpora/wordnet.zip')
except:
    nltk.download('wordnet')
try:
    nltk.data.find('corpora/omw-1.4.zip')
except:
    nltk.download('omw-1.4')
try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')
```
- env.py module with github token and github username


# About the data <a name="data"></a>

We scraped ~1000 Github repositories from the list of most forked repositories to gather readme files and information from GitHub's language statitics.

## Scope

For exploration and modeling we ignored any repositories featuring a language for which we did not scrape at least 10 samples, as well as any repositories that did not feature a language at all.

## Acquiring

- "env.py" has credentials to access the data from GitHub.com
- Data acquisition used a combination of web-scraping and GitHub's API from the "acquire.py" module.
- Acquire module collects repository name, language used and readme contents.
- 

## Preparing

To prepare the data for exploration and modeling we performed the following steps:
- Markdown links were removed from the corpus since the urls did not provide meaningful information
- HTML elements such as \<li>\</li> and \<strong>\</strong> were also removed for the same reason
- The text was then normalized and stripped of special characters
- Stopwords were removed
- New columns were created in the dataframe to represent the cleaned and lemmatized versions of the original
- Split the data into train, validate and test sets and stratify by the language
    - Train : 64 % of the data
    - Validate : 16 % of the data
    - Test : 20 % of the data

## Data Dictionary

| Column | Use | Description |  |  |
|---|---|---|---|---|
| repo | Identifier | A string formatted like "{user}/{repository}" that uniquely   identifies the repository. |  |  |
| language | Target Variable | A string that identifies the most used language in a repository.   Generated by Github's API. |  |  |
| readme_contents | Source corpus | A string that is the unmodified contents of a repositories README.md file   if it exists |  |  |
| cleaned_readme | Engineered Feature | readme_contents after normalization and stripped of stopwords and special   characters |  |  |
| tokenized_readme | Engineered Feature | cleaned_readme after "words" are tokenized and separated by   spaces |  |  |
| lemm_readme | Engineered Feature | tokenized_readme after "words" are lemmatized to their root   word |  |  |
| polarity | Exploration only | Description of lemm_readme's sentiment analysis. A value closer to 1 or   -1 describes a stronger positive or negative sentiment. |  |  |


# Project Planning <a name="plan"></a>

## Exploration

## Initial Hypotheses
- If a language is mentioned in the readme it is more likely dominated by that language
- Topics surrounding web development are more likely written in html, javascript and css
- Readmes that talk about studying or hiring are likely written in english

## Modeling
- Created a baseline model against which all models will be evaluated.
- 12 different models were compared against the baseline and model with the highest overall accuracy score was used to evaluate the test data set.


# Conclusion
### Summary

In seeking to predict programming language for GitHub repositories, we have explored our data thoroughly. \
We observed word clouds, word frequencies, and ran sentiment analyses in order to best determine any additional feature engineering that would improve our model. Although we were not able to identify any additional significant features to engineer from this exploration, we were able to identify problem areas and eliminate a host of stopwords which resulted in improved modeling.

Additionally, we have created and tested 12 different models on both uncleaned and cleaned and lemmatized data. Our 3 best performing models are:

1. Neural Network (not explicitly shown in this final notebook)
2. SVM Linear
3. XGBoost Classifier

In short, we found that our XGBoost Classifier model performed best on our uncleaned data, resulting in 58% accuracy on our test data. \
This performance beats our baseline by 115%.


### Next Steps

Despite the overall effectiveness of our best-performing model, there is always room for improvement and optimization.
If given more time to pursue better results, we could perform further investigation within exploration by:

1. Estimating each readme's school reading level. Not only would this be interesting as an anecdote, if proven useful, it could be imputed as a new feature to boost the accuracy of our model.

2. Handling ReadMes in a foreign language in a more succinct way. This could be handled more effectively by using a translator to convert all ReadMes into English for potentially better modeling accuracy. 

