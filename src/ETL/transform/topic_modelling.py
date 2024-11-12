from bertopic import BERTopic
import pandas as pd

def create_bertopic_model(df, text_column, id_column, topic_num, verbose=True):
    """
    Create and fit a BERTopic model on the provided text data.

    Parameters:
        df (pd.DataFrame): DataFrame containing the text data to model.
        text_column (str): Name of the column with preprocessed text data.
        topic_num (int): Number of topics to reduce to, if needed.
        verbose (bool): If true, displat verbose output from BERTopic.

    Returns:
        BERTopic: A trained BERTopic model.
        list: List of topics for each document.
        list: List of probabilities for each topic per document.
    """
    # create topic modelling model
    model = BERTopic(verbose=verbose, nr_topics=topic_num)

    # prepare documents from the specified text column
    docs = df[text_column].tolist()
    ids = df[id_column].tolist()

    # fit the model to the document and transform
    topics, probabilities = model.fit_transform(docs)

    topic_modelling_df = pd.DataFrame({
        "No_Stopwords_Text": docs, 
        "Topic": topics,
        "Comment_ID": ids
    })

    return model, topics, probabilities, topic_modelling_df


    