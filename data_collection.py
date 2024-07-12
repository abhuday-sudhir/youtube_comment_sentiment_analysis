from  googleapiclient.discovery import  build

api_key='YOUR_API_KEY'

def video_comments(video_id):
    li = []
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                developerKey=api_key)

    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet',
    textFormat='plainText',
    videoId=video_id,
    maxResults=100
    ).execute()

    # iterate video response
    while video_response:

    # extracting required info
    # from each result object
        for item in video_response['items']:

        # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            li.append(comment)

    # Again repeat
        next_page_token = video_response.get('nextPageToken')
        if next_page_token:
          video_response = youtube.commentThreads().list(
                part='snippet',
                textFormat='plainText',
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            ).execute()
        else:
           break
    return(li)
