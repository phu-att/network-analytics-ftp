# Network Analytics 

## Introduction
This project deals with the topics of homophily, closure, and
performance. There is consistent evidence that selection and socialization
mechanisms – as the vessels of homophily – vastly affect entities' choices
such as partner selection, hiring, collaboration, or consumption. What is less
clear is how selection and socialization impact an entity's performance by
influencing the decision making process

## Background for the case study
To deliver the project, students may want to rely upon the following concepts
and tools:
- theoretical concept of homophily
- homophily-related network mechanisms: selection and socialization
- empirical implementations of the homophily framework

## Dataset
* The Github repo [`ewenme/trasnfers`](https://github.com/ewenme/transfers)
contains updated, longitudinal data on moves involving male professional
football players in the major European championships.
* Self-generated excel file containing ranking of teams in tier 1 leagues
from 2010 - 2020 

## Directory Structure
``` bash
network-analytics-ftp
├── LICENSE
├── README.md
├── requirements.txt
├── companion_document.pdf
├── presentation.pdf
├── datasets
│   ├── football_dataset_final.xlsx
│   └── tier1_team_performance.xlsx
└── scripts
    └── 00_analysis.ipynb
```

## File Description
* ```requirements.txt``` -> Required Python libraries 
* ```companion_document.pdf``` -> Document that explains rational and analysis of the project
* ```presentation.pdf``` -> Slideshow that shows a holistic view of the project 
### datasets
* ```football_dataset_final.xlsx``` -> The mentioned football data, but not required to download to run the code
* ```tier1_team_performance.xlsx``` -> The perfomance of the tier 1 teams spanning over 11 years
### scripts
* ```web-scraping-npl.py ``` -> This script focuses on extracting texts from articles in the Uber People Forums website
* ```topic-modelling.py``` -> This script focuses on applying topic modeling (LDA) on the data gathered, denoting Part 1 of the project
* ```coherence_eval.py ``` -> This script focuses on the implementation of the coherence score that statistically evaluates the number of topics
* ```semantic-axis-analysis.py ``` -> This script aims to analyse affective states represented in Uber drivers’ conversation, denoting Part 2 of the project. The method adopted to perform the analysis is the Semantic axis Method (SAM). The file also incorporates topic modelling for time-series analysis, denoting Part 3 of the project


