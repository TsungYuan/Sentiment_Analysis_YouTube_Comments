from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def categorizeSentiment(compund_score):
    """
    Categorize sentiment based on compound score.
    """
    if compund_score >= 0.05:
        return 'Positive'
    elif compund_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def sentiment_analysis(df, text_column):
    """
    Preform sentiment analysis using VADER and return a new DataFrame with sentiment columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing the text data.
        text_column (str): The name of the column containing text to analyze.
    
    Returns:
        pd.DataFrame: A new DataFrame with sentiment columns only, including scores (positive, negative, neutral, and compound) and sentiment label.
    """
    # initialize SentimentIntensityAnalyzer object
    sid_obj = SentimentIntensityAnalyzer()

    # define a function to compute and unpack the scores in a single pass
    def analyze_sentiment(text):
        try:
            scores = sid_obj.polarity_scores(text)
            return pd.Series({
                'Positive_Score': scores['pos'],
                'Neutral_Score': scores['neu'],
                'Negative_Score': scores['neg'],
                'Compound_Score': scores['compound'],
                'Sentiment_Label': categorizeSentiment(scores['compound'])
            })
        except Exception as e:
            print(f"Error analyzing sentiment for text '{text}: {e}")
            return pd.Series({
                'Positive_Score': None,
                'Neutral_Score': None,
                'Negative_Score': None,
                'Compound_Score': None,
                'Sentiment_Label': None
            })
    
    # apply the analysis function to create a new DataFrame
    sentiment_df = df[text_column].apply(analyze_sentiment)

    # add the original text column and comment id to sentiment_df
    sentiment_df[text_column] = df[text_column].values
    if 'Comment_ID' in df.columns:
        sentiment_df['Comment_ID'] = df['Comment_ID'].values

    return sentiment_df