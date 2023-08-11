# Model Card

## Model Description

### Inputs 

The inputs are key financial metrics including: 
- recommendationMean,
- beta,
- trailingEps,
- forwardEps,
- forwardPE,
- bookValue,
- priceToBook,
- ebitdaMargins,
- profitMargins,
- revenueGrowth,
- payoutRatio,
- debtToEquity,
- returnOnAssets,
- returnOnEquity,
- quickRatio,
- currentRatio

More information on these features at https://yourfinancebook.com/stock-market-financial-metrics/.

### Output

The output is the Zacks rank:
- 1 = Strong Buy
- 2 = Buy
- 3 = Hold
- 4 = Sell
- 5 = Strong Sell 

More informatin on these labels at https://advisortools.zacks.com/Content/ZAT_ZacksRankGuide.pdf.

### Model Architecture

The project tests several classifiers and optimizes a neural network called MLPClassifier. See `model.ipynb`.
The result of the optmisation process is an MLPClassifier with the following parameters:
- activation: 'tanh',
- alpha: 0.31622776601683794,
- hidden_layer_sizes: (105, 86),
- learning_rate: 'invscaling',
- solver: 'lbfgs'

## Performance

The model has an accuracy score of approximately 65% on a balanced dataset of approximately 5 classes * 1,500 records oversampled with the SMITE algorithm from an imbalanced dataset of approximately 2500 stocks with Zacks ranks saved as `./data/data.csv`.

## Limitations and Trade-offs

The main Trade-off was time limitation for this proof of concept which had to be completed in approximately 30 hours.

The model does not perform sufficiently well to be considered in production. More work should be done on feature selection and processing. More real data is needed to effectively train the model.
