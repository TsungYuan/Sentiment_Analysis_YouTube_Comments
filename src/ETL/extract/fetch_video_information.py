import googleapiclient.discovery
import googleapiclient.errors

def getVideos(youtube, videoID_list):
    """
    Fetch comments from a YouTube video by video ID.

    Args:
        youtube: YouTube API service instance.
        videoID_list (list): A list for YouTube Video ID.
    Retures:
        list: A list of comments and their metadata.
    """
    video_list = []

    try:
        # YouTube API can take multiple video IDs (comma-separated) in one request
        response = youtube.videos().list(
            part=["id", "snippet", "statistics"],
            id=videoID_list,
            maxResults=100
        ).execute()
        video_list.extend(response['items'])

    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error occurred: {e}")
    except Exception as e:
        print(f"An exception error occurred: {e}")
    
    return video_list


# if __name__ == "__main__":
#     api_service_name = "youtube"
#     api_version = "v3"
#     DEVELOPER_KEY = "API_KEY"
#     video_ID = "SIm2W9TtzR0"

#     youtube = googleapiclient.discovery.build(
#         api_service_name,
#         api_version,
#         developerKey=DEVELOPER_KEY
#     )

#     comments = getVideos(youtube, video_ID)

#     print(f"Fetched {len(comments)} comments.")
