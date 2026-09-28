# World-Cup-outcome-predicting-model
Machine learning project for predicting FIFA World Cup match outcomes using historical match data, feature engineering, and a chronological validation approach.
# World Cup Match Prediction

A junior machine-learning project that uses historical FIFA World Cup match data to estimate the probability of three possible match outcomes:

- Team A win
- Draw
- Team B win

The project includes exploratory data analysis, data cleaning, time-aware feature engineering, model comparison, chronological evaluation, a reusable trained model, and a Tkinter graphical user interface.

The goal is to demonstrate a complete data-science workflow. The model is educational and should not be treated as a perfectly accurate sports prediction system.

## Project highlights

- Historical World Cup matches from 1930–2022
- Pre-match features designed to avoid using the current match result
- Rolling form features based on previous matches
- Team and tournament context features
- Historical tournament-strength features from `Rating_wc.csv`
- Comparison of several classification models
- Chronological and walk-forward evaluation
- Exported best model in `model.pkl`
- Interactive GUI for match simulation

## Project structure

```text
WC_DS_project/
├── data/
│   ├── raw/
│   │   ├── matches_1930_2022.csv
│   │   └── Rating_wc.csv
│   └── processed/
│       ├── matches_1930_2022.csv
│       └── matches_1930_2022_cleaned.csv
├── notebooks/
│   ├── 1_EDA.ipynb
│   ├── 2_Data_Cleaning.ipynb
│   ├── 3_Model_Building.ipynb
│   └── GUI/
│       ├── GUI.ipynb
│       └── gui.py
├── screenshots/
├── model.pkl
├── requirements.txt
└── README.md
```

## Data

The main match dataset contains historical World Cup match information, including teams, dates, tournament stage, host information, managers, and match results.

`Rating_wc.csv` is used during data preparation to add historical tournament-strength features. For each match, the feature engineering uses only the team’s most recent completed World Cup before that match year. The current tournament’s final position is therefore not used to predict matches from that same tournament.

The target variable is encoded as:

```text
0 = Team A win
1 = Draw
2 = Team B win
```

## Machine-learning workflow

### 1. Exploratory data analysis

`1_EDA.ipynb` examines the historical data, match-result distributions, tournament stages, and possible data-quality issues.

### 2. Data cleaning and feature engineering

`2_Data_Cleaning.ipynb`:

- Normalizes text and team names
- Loads and cleans `Rating_wc.csv`
- Creates the three-class target
- Sorts matches chronologically
- Builds rolling form features from earlier matches
- Adds host and historical tournament-strength features
- Removes current-match and post-match leakage columns
- Checks missing values and target validity
- Saves `data/processed/matches_1930_2022_cleaned.csv`

### 3. Model training and evaluation

`3_Model_Building.ipynb` compares multiple classifiers using accuracy, precision, recall, and F1-score. The notebook also performs chronological evaluation, where earlier tournaments are used for training and later tournaments are used for testing.

The reusable model artifact is exported at the end of the notebook as:

```text
model.pkl
```

This file contains the trained model and the saved feature/state information required by the GUI. It prevents the user from having to retrain the model every time they want to run the application.

## Installation

Python 3.10 or newer is recommended.

From the project root, install the dependencies:

```bash
pip install -r requirements.txt
```

Tkinter is included with most standard Python installations. On some Linux systems it may need to be installed separately through the operating system package manager.

## How to run the project

Open a terminal in the project root and start Jupyter:

```bash
jupyter notebook
```

Run the notebooks in this order:

1. Open and run `notebooks/1_EDA.ipynb`.
2. Open and run `notebooks/2_Data_Cleaning.ipynb`.
3. Open and run `notebooks/3_Model_Building.ipynb` from top to bottom.

The final cell of `3_Model_Building.ipynb` saves the best trained model to `model.pkl`.

After `model.pkl` exists, the GUI can be started without rerunning the training process:

```bash
python notebooks/GUI/gui.py
```

In the GUI, select Team A, Team B, the relevant years, and an optional host team. Click **Simulate Match** to see the probabilities for each outcome and the most likely prediction.

## Using the saved model

The normal user workflow is:

```text
Run notebooks once → create model.pkl → start gui.py whenever needed
```

If the data, feature engineering, or model configuration changes, rerun the model-building notebook to create a new `model.pkl`.

## Evaluation note

Football match outcomes are difficult to predict, and draws are especially challenging because the classes are not perfectly balanced. The project therefore reports several evaluation metrics and uses chronological testing to better reflect real-world prediction.

The model’s imperfect performance is an expected limitation of this junior project. The main purpose is to demonstrate data preparation, leakage-aware feature engineering, model evaluation, serialization, and deployment through a simple GUI.

## Portfolio screenshots

The README should include approximately five clear screenshots:

1. Exploratory data-analysis chart
2. Final cleaned dataset and missing-value check
3. Model comparison table
4. Final chronological evaluation or confusion matrix
5. GUI displaying a prediction and probabilities

Screenshots should show notebook outputs, charts, tables, or the GUI rather than large blocks of code.

### Exploratory analysis

![Match-result distribution](screenshots/output%20distribution.png)

![Distribution by tournament stage](screenshots/output%20distribution%20by%20stages.png)

### Cleaned dataset

![Final cleaned dataset](screenshots/example%20of%20final%20cleaned%20dataset.png)

### Model comparison

![Model comparison](screenshots/comparing%20all%20models%20results.png)

### GUI prediction

![GUI prediction](screenshots/model%20with%20GUI%20visualization.png)

## Limitations and possible improvements

- The dataset contains a limited number of World Cup matches.
- International football changes over time, so older matches may not represent current team strength.
- Match injuries, lineups, player form, and detailed tactical information are not included.
- Probabilities are estimates, not guarantees.
- Future improvements could include richer player-level data, Elo updates, external rankings, calibration analysis, and more advanced time-series validation.

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Jupyter Notebook
- Tkinter

## License

This project is intended for educational and portfolio use. Add a specific open-source license if you decide to publish the repository for reuse by others.
