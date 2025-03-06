import googleapiclient.discovery
import googleapiclient.errors

def getYoutubeComments(youtube, video_ID, maxResutls=100):
    """
    Fetch comments from a YouTube video by video ID.

    Args:
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
        
    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error occured: {e}")
    except Exception as e:
        print(f"An unexcepted error occurred: {e}")

    return comment_list


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

#     comments = getYoutubeComments(youtube, video_ID)

#     print(f"Fetched {len(comments)} comments.")
