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
* ```00_analysis.ipynb``` -> The code contains data processing process & conducted analysis, including all outputs shown in the companion document


