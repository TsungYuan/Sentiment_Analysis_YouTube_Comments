import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
from langdetect import detect, LangDetectException

def toDataframeComments(comment_list):
    """
    Convert a list of comment dictionaries to a DataFrame with normalized fields.

    Parameters:
        comment_list (list): A list of YouTube comment objects, each containing details like text, author, and metadata.

    Returns:
        pd.DataFrame: A DataFrame containing structured columns for each comment's key details, including text, author information, and timestamps.

    all_comments = []

    for item in comment_list:
        if item.get('replies'):
            all_comments.append(item['snippet']['topLevelComment'])
            for replies in item['replies']['comments']:
                all_comments.append(replies)
        else:
            all_comments.append(item['snippet']['topLevelComment'])
    """
    try:
        all_comments = [
            comment.get('snipprt', {}).get('topLevelComment', comment)
            for item in comment_list
            for comment in ([item['snippet']['topLevelComment']] + item.get('replies', {}).get('comments', []))
        ]

        # convert to data frame
        all_comments_df = pd.json_normalize(all_comments)
        column_mapping = {
            'kind': 'Kind',
            'etag': 'Etag',
            'id': 'Comment_ID',
            'snippet.channelId': 'Channel_ID',
            'snippet.videoId': 'Video_ID',
            'snippet.textDisplay': 'Comment_Text',
            'snippet.textOriginal': 'Original_Comment_Text',
            'snippet.authorDisplayName': 'Auther_Name',
            'snippet.authorProfileImageUrl': 'Auther_Profile_Image_URL',
            'snippet.authorChannelUrl': 'Auther_Channel_URL',
            'snippet.authorChannelId.value': 'Auther_Channel_ID',
            'snippet.canRate': 'canRate',
            'snippet.viewerRating': 'Viewer_Rate',
            'snippet.likeCount': 'Comment_Like_Count',
            'snippet.publishedAt': 'Comment_Published_Date',
            'snippet.updatedAt': 'Comment_Updated_Date',
            'snippet.parentId': 'Comment_Parent_ID'
        }
        all_comments_df.rename(columns=column_mapping, inplace=True)

        # convert numeric and time columns
        all_comments_df = all_comments_df.astype({
            'Comment_Like_Count': 'float64',
            'Comment_Published_Date': 'datetime64[ns, UTC]',
            'Comment_Updated_Date': 'datetime64[ns, UTC]'
        })

    except KeyError as e:
        print(f"Key error when accessing JSON data: {e}")
        return pd.DataFrame() # return an empty dataframe on error
    except Exception as e:
        print(f"Unexcepted error in toDataFrame: {e}")
        return pd.DataFrame() # return an empty dataframe on error
    
    return all_comments_df

def toDataFrameVideoInfo(video_info):
    """
    Convert the video information dictionary to DataFrame to normalized fields.
    
    Parameter:
        video_info (list): A list of YouTube video information, contains title, channelID like count, comment count, and other metadata.

    Returns:
        pd.DataFrame: A DataFrame containing structured columns for each comment's key details, including title, channelID like count, comment count, and other information.
    """
    try:
        info = [
            {
                'Video_ID': item.get('id'),
                'Publisded_Time': item.get('snippet', {}).get('publishedAt'),
                'Channel_ID': item.get('snippet', {}).get('channelId'),
                'Video_Title': item.get('snippet', {}).get('title'),
                'Video_View_Count': item.get('statistics', {}).get('viewCount'),
                'Video_Like_Count': item.get('statistics', {}).get('likeCount'),
                'Video_Comment_Count': item.get('statistics', {}).get('commentCount')
            }
            for item in video_info
        ]
        video_info_df = pd.json_normalize(info)

        # convert numeric columns
        video_info_df = video_info_df.astype({
            'Video_View_Count': 'float64',
            'Video_Like_Count': 'float64',
            'Video_Comment_Count': 'float64'
        })

    except KeyError as e:
        print(f"Key error when accessing JSON data: {e}")
        return pd.DataFrame() # return an empty dataframe on error
    except Exception as e:
        print(f"Unexcepted error in toDataFrame: {e}")
        return pd.DataFrame() # return an empty dataframe on error

    return video_info_df



tokenizer = RegexpTokenizer(r'\w+')  # this will only capture words (alphanumeric)
stop_words = set(nltk.corpus.stopwords.words('english'))  # load english stopwords

def isEnglish(text):
   """
    Check if a given text is written in English.

    Parameters:
        text (str): The input text to check.

    Returns:
        bool: True if the text is in English, False otherwise.
   """
   try:
      return detect(str(text)) == 'en'
   except (LangDetectException, ValueError, TypeError) as e:
      print(f"Error detecting language: {e}")
      return False
   

def tokenize(text):
    return tokenizer.tokenize(text)

def removeStopwords(tokens):
    return [token for token in tokens if token not in stop_words]

def joinNoStopwordsTokenize(tokens):
    return " ".join(tokens)

def preprocessText(df, text_column):
    """
    Preprocess text by normalizing case, tokenizing, and removing stop words.

    Parameters:
        df (pd.DataFrame): The input DataFrame with a 'Comment_Text' column.

    Returns:
        pd.DataFrame: A modified DataFrame with new columns for lowercase text, tokenized words, and tokenized words with stop words removed.
    """
    df['Lowercase'] = df[text_column].str.lower() # convert to lowercase
    df = df[df['Lowercase'].apply(isEnglish)] # filter only english row
    df['No_Punctuation'] = df['Lowercase'].str.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
    df['Tokenized'] = df['No_Punctuation'].apply(tokenize) # tokenize the text
    df['No_Stopwords_Tokenized'] = df['Tokenized'].apply(removeStopwords) # remove stopwords
    df['No_Stopwords_Text'] = df['No_Stopwords_Tokenized'].apply(joinNoStopwordsTokenize) # join no stopword tokenize

    return df


def concatenate_top_1000_comments(df_list, columns, text_column): 
    """
    Concatenate the top 1,000 comments from each DataFrame, excluding NaN values in the 'CommentTextDisplay' column.

    Parameters:
        df_list (list): List of DataFrames to sample comments from.
        columns (list): List of column names to include in the final DataFrame.
        text_column (str): The column name with text data. 

    Returns:
        pd.DataFrame: Concatenated DataFrame containing the top 1,000 comments from each input DataFrame.
    """
    combined_df = (
        pd.concat(
            [df.dropna(subset=[text_column]).head(1000)[columns] for df in df_list], 
            ignore_index=True
        )
    )
    return combined_df


def concatenate_random_1000_comments(df_list, columns, text_column, random_state=None):
    """
    Concatenate a random sample of 1,000 comments from each DataFrame, excluding NaN values in 'CommentTextDisplay'.

    Parameters:
        df_list (list): List of DataFrames to sample comments from.
        columns (list): List of column names to include in the final DataFrame.
        random_state (int): Seed for reproducibility of random sampling.
        text_column (str): The column name with text data. 

    Returns:
        pd.DataFrame: Concatenated DataFrame containing a random sample of 1,000 comments from each input DataFrame.
    """
    combined_df = (
        pd.concat(
            [df.dropna(subset=[text_column]).sample(n=1000, random_state=random_state)[columns] 
             for df in df_list], 
            ignore_index=True
        )
    )
    return combined_df


def joinDataFrame(df1, df2, key_column):
    return df1.set_index(key_column).join(df2.set_index(key_column)).reset_index()


