import googleapiclient.discovery
import googleapiclient.errors
import logging
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def getYouTubeClient():
    """
    Build the YouTube API client.
    """
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        logger.error("YOUTUBE_API_KEY not found in environment variables")
        raise ValueError("YOUTUBE_API_KEY not set")
    logger.info("Building YouTube client.")
    return googleapiclient.discovery.build(
        "youtube",
        "v3",
        developerKey=api_key
    )
        
def getYoutubeComments(youtube, video_ID, maxResutls=100):
    """
    Fetch comments from a YouTube video by video ID.

    Parameters:
        youtube: YouTube API service instance.
        video_ID (str): The IDof the YouTube video.
    Retures:
        list: A list of comments and their metadata.
    """
    comment_list = []

    try:
        response = youtube.commentThreads().list(
            part=["id", "replies", "snippet"],
            videoId=video_ID,
            maxResults = maxResutls
        ).execute()
        comment_list.extend(response['items'])

        while response.get('nextPageToken', None):
            response = youtube.commentThreads().list(
                part=["id", "replies", "snippet"],
                videoId=video_ID,
                pageToken=response['nextPageToken']
            ).execute()
            comment_list.extend(response['items'])

            logger.info(f" Fetched {len(comment_list)} comments so far")
        
    except googleapiclient.errors.HttpError as e:
        logger.error(f"An HTTP error occured: {str(e)}")
    except Exception as e:
        logger.error(f"An unexcepted error occurred: {str(e)}")

    return comment_list

def getVideos(youtube, videoID_list):
    """
    Fetch comments from a YouTube video by video ID.

    Parameters:
        youtube: YouTube API service instance.
        videoID_list (list): A list for YouTube Video ID.
    Retures:
        list: A list of comments and their metadata.
    """
    logger.info(f" Fetch video info for IDs: {videoID_list}")
    video = []

    try:
        # YouTube API can take multiple video IDs (comma-separated) in one request
        response = youtube.videos().list(
            part=["id", "snippet", "statistics"],
            id=videoID_list,
            maxResults=100
        ).execute()
        video.extend(response['items'])

        logger.info(f" Fetch info for {len(video)} videos.")

    except googleapiclient.errors.HttpError as e:
        logger.error(f"An HTTP error occurred: {str(e)}")
    except Exception as e:
        logger.error(f"An exception error occurred: {str(e)}")
    
    return video