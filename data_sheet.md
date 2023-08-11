# Datasheet Template

## Motivation

- The dataset was created to train a classifier to replicate the Zacks rank from key financial metrics. 
- The dataset was created by Jacques L. Chereau in August 2023 for the final project of the Imperial College Professional Certificate in Machine Learning and Artificial Intelligence.
 
## Composition

- `./data/all_tickers.txt` is a list of US stock tickers sourced from https://github.com/rreichel3/US-Stock-Symbols
- `./data/features.csv` contains key financial metrics available on Yahoo Finance for these stock tickers (some are missing)
- `./data/labels.csv` contains Zacks ranks available on Zacks.com for these stock tickers (some are missing)
- `./data/data.csv` is a cleaned dataset where eache feature is converted to a Z-score by industry

This data is public and therefore not confidential.

## Collection process

- The data was collected from Yahoo Finance and Zacks.com. For more information check the notebook `data.ipnyb`.
- The sampling strategy was scoped by the list of stock tickers from `./data/all_tickers.txt`.
- The data was collected during the week of 7 August 2023.

## Preprocessing/cleaning/labelling

- Columns with too many missing values were removed. Then rows with missing values were removed. All feature columns were converted to a Z-score within their industry. For more information check the notebook `prepare.ipnyb`.
- The raw data is contained in `./data/features.csv` and `./data/labels.csv`. The preprocessed/cleaned/labeled data is contained in `./data/data.csv`.
- The resulting dataset is imbalanced. Records with a Zacks rank of 3 are over-represented. This is dealt with in `model.ipynb`.
 
## Uses

- The only purpose of this dataset is a (failed) proof of concept for a classifier to replicate the Zacks rank from key financial metrics. 
- The dataset is not reliable and should not be used for stock trading. Use at your own risks (financial risks).

## Distribution

- The dataset has only been posted on emeritus.insendi.com for grading by Imperial College
- Zacks ranks are public but proprietary information from Zacks.com

## Maintenance

- This dataset is not maintained.

