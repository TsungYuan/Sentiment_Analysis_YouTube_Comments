import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from bertopic import BERTopic
from nltk import TweetTokenizer
from nltk.util import ngrams
from collections import Counter


def plotSentimentDistribution(df, text_column):
    """
    Plot the distribution of sentiment categories in pie chart.
     
    Paramenter:
        df (pd.DataFrame): DataFrame containing sentment data.
        text_column (str): The column name with sentiment labels.
    """
    # count the occurence of each sentiment label
    count = df[text_column].value_counts()
    # create the pie chart
    plt.figure(figsize=(6, 6))
    sns.set(style='darkgrid')
    palette_color = sns.color_palette('pastel') 

    plt.pie(
        count,
        labels=count.index,
        autopct='%1.1f%%',
        colors=palette_color
    )

    plt.title('Comment Sentiment Label Distribution', fontsize=18)
    plt.show()


def plotWordcloud(df, text_column):
    """
    Generate a word cloud from a specific text column.
    
    Paramenter:
        df (pd.DataFrame): DataFrame containing text data.
        text_column (str): The column name with text data to visualize. 
    """
    text = " ".join(comment for comment in df[text_column])
    wordcloud_total = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    plt.imshow(wordcloud_total, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def ngramCount(df, text_column, n_grams=2, top_n=20):
    """
    Generate a DataFrame of the top n most common n-grams and their counts.

    Parameters:
        df (pd.DataFrame): DataFrame containing the text data.
        text_column (str): Name of the column containing the text data.
        n_grams (int): The 'n' in n-grams, specifying the size of the n-gram (e.g., 2 for bigrams, 3 for trigrams). Default is 2.
        top_n (int): The number of top n-grams to extract and display. Default is 20.

    Returns:
        pd.DataFrame: A DataFrame containing the top n-grams and their respective counts with columns for the n-grams and their frequency.
    """
    text = " ".join(comment for comment in df[text_column])

    # tokenize the text
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(text)

    # create n-grams
    ngrams_list = list(ngrams(tokens, n_grams))

    # calculate the frequency of each bigram
    ngram_freq = Counter(ngrams_list).most_common(top_n)

    # separate n-grams and their counts
    ngram_list, ngram_count = zip(*ngram_freq)
    ngram_strings = [' '.join(ngram) for ngram in ngram_list]

    ngram_data = pd.DataFrame({
        f'{n_grams}-gram': ngram_strings,
        'count': ngram_count
    })

    return ngram_data


def visualizeNgram(df, count_column, n_grams=2, top_n=20):
    """
    Generate a top 20 most common bigram bar chart

    Paramenter:
        df (pd.DataFrame): DataFrame containing text data.
        count_column (str): The column name with the ngram count to visualize.
        n_grams: The 'n' in n-grams. Default is 2 for bigrams.
        top_n (int): The number of top n-grams to display. Default is 20.
    """
    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='count', y=f'{n_grams}-gram', data=df, palette="viridis")

    # annotate each bar with the count
    for i, count in enumerate(df[count_column]):
        ax.text(count, i, str(count), color='black', ha="right", va="center", fontsize=9)

    plt.xlabel('Counts', fontsize=12)
    plt.ylabel(f'{n_grams}-grams', fontsize=12)
    plt.title(f'Top {top_n} Most Common {n_grams}-grams', fontsize=16)
    plt.yticks(fontsize=9)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def visualizeTopics(model):
    """
    Visualize topics using BERTopic's interactive visualization.

    Parameters:
        model (BERTopic): The BERTopic model instance after fitting.
    """
    model.visualize_topics().show()


def visualizeTopicBarchart(model):
    """
    Display a bar chart of the most frequent topics.

    Parameters:
        model (BERTopic): The BERTopic model instance after fitting.
    """
    model.visualize_barchart().show()


def visualizeLikeCount(top_10_video_df):
    """
    Display a bar chart of the like count of all videos.

    Parameters:
        top_10_video_df (pd.DataFrame): DataFrame contain video information.
    """
    sns.set_style('darkgrid')
    plt.figure(figsize=(8, 4))

    repli_count = sns.barplot(
        x='Video_ID',
        y='Video_Like_Count',
        data=top_10_video_df,
        color='seagreen'
    )

    for i, count in enumerate(top_10_video_df['Video_Like_Count']):
        repli_count.text(i, count, str(count), color='black', ha="center", va="bottom", fontsize=8)

    plt.xlabel('Video ID', fontsize=12)
    plt.ylabel('Comment Like Count', fontsize=12)
    plt.title('Top 10 Videos Like Count', fontsize=18)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.show()



def visualizeReplyCount(top_10_video_df):
    """
    Display a bar chart of the reply count of all videos.

    Parameters:
        top_10_video_df (pd.DataFrame): DataFrame contain video information.
    """
    sns.set_style('darkgrid')
    plt.figure(figsize=(8, 4))

    repli_count = sns.barplot(
        x='Video_ID',
        y='Video_Comment_Count',
        data=top_10_video_df,
        color='seagreen'
    )

    for i, count in enumerate(top_10_video_df['Video_Comment_Count']):
        repli_count.text(i, count, str(count), color='black', ha="center", va="bottom", fontsize=8)

    plt.xlabel('Video ID', fontsize=12)
    plt.ylabel('Comment Reply Count', fontsize=12)
    plt.title('Top 10 Videos Reply Count', fontsize=18)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.show()


def visualizeViewCount(top_10_video_df):
    """
    Display a bar chart of the view count of all videos.

    Parameters:
        top_10_video_df (pd.DataFrame): DataFrame contain video information.
    """
    sns.set_style('darkgrid')
    plt.figure(figsize=(8, 4))

    ttl_view = sns.barplot(
        x='Video_ID',
        y='Video_View_Count',
        data=top_10_video_df
    )

    for i, count in enumerate(top_10_video_df['Video_View_Count']):
        ttl_view.text(i, count, str(count), color='black', ha="center", va="bottom", fontsize=8)

    plt.xlabel('Video ID', fontsize=12)
    plt.ylabel('Times Watched', fontsize=12)
    plt.title('Top 10 Videos Total View', fontsize=18)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.show()


def visualizeCommentPublishTrend(df):
    """
    Display the comment published trend.

    Parameters:
        top_10_video_df (pd.DataFrame): DataFrame contain video information.
    """

    # Plotting with Seaborn
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        x='Comment_Published_Date', 
        y='Comment_Count', 
        hue='Video_ID', 
        data=df
    )

    # Customizing the plot
    plt.xlabel('Date')
    plt.ylabel('Cumulative Number of Comments')
    plt.title('Comment Publish Trends for All Videos')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show plot
    plt.show()


def resamplePublishTime(df, date_column='Comment_Published_Date', video_id_column='Video_ID', resample_time='2W'):
    """
    Resample comment publish times and calculate comment count over specified time intervals.

    Parameters:
        df (pd.DataFrame): DataFrame containing video and comment data.
        date_column (str): Name of the column containing comment publish dates.
        video_id_column (str): Name of the column containing video IDs.
        resample_time (str): Resampling frequency (e.g., '1W', '2W', 'M').

    Returns:
        pd.DataFrame: A DataFrame containing the resampled time periods, comment counts, and video IDs.
    """
    # drop rows where date conversion failed
    df = df.dropna(subset=[date_column])
    
    # group by video and resample each group separately
    resampled_trends = []
    
    for video_id, group in df.groupby(video_id_column):
        group = group.set_index(date_column).resample(resample_time).size().reset_index(name='Comment_Count')
        group[video_id_column] = video_id  # add video ID for each group
        resampled_trends.append(group)
    
    # combine results
    return pd.concat(resampled_trends, ignore_index=True)


def visualizeSemtimentandRTopic(df, topic_column, sentiment_column, count_threshold=150):
    """
    Plot a stacked bar chart of sentiment label distribution by topic.

    Parameters:
        df (pd.DataFrame): DataFrame containing topic and sentiment label columns.
        topic_column (str): Name of the column with topic labels.
        sentiment_column (str): Name of the column with sentiment labels.
        count_threshold (int, optional): Minimum count to annotate the chart with percentages. Default is 150.

    Returns:
        None: Displays a stacked bar chart.
    """
    # Group and reshape the data
    temp = df[[topic_column, sentiment_column]]
    topic_sentiment = temp.groupby([topic_column, sentiment_column]).size().unstack(fill_value=0)
    topic_sentiment_percentage = topic_sentiment.div(topic_sentiment.sum(axis=1), axis=0) * 100

    # Plot the stacked bar chart
    plt.figure(figsize=(6, 3))
    ax = topic_sentiment.plot(kind='bar', stacked=True, color=sns.color_palette("bright"))

    # Annotate the chart with percentages
    for i in range(topic_sentiment.shape[0]):
        for j in range(topic_sentiment.shape[1]):
            count = topic_sentiment.iloc[i, j]
            percentage = topic_sentiment_percentage.iloc[i, j]
            if count > count_threshold:
                ax.text(
                    i,
                    sum(topic_sentiment.iloc[i, :j+1]) - count / 2,
                    f"{percentage:.0f}%",
                    ha='center',
                    va='center',
                    fontsize=8,
                    color='black'
                )

    # Customize the plot
    plt.title('Stacked Bar Chart of Comment VADER Sentiment Labels by Topic')
    plt.xlabel('Topic')
    plt.ylabel('Count')
    plt.legend(title='Sentiment Label')
    plt.xticks(rotation=0)
    plt.show()