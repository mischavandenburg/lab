from youtube_transcript_api import YouTubeTranscriptApi
import sys


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"An error occurred: {str(e)}"


one = 1
two = 2

    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <YouTube_Video_ID>")
        sys.exit(1)
    
    video_id = sys.argv[1]
    transcript_text = get_transcript(video_id)
    print(transcript_text)
