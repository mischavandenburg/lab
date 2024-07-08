from youtube_transcript_api import YouTubeTranscriptApi

# Function to download transcript
def download_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return str(e)

# Example usage
video_id = "iagjeLuxnMs"  # Replace with your YouTube video ID
transcript = download_transcript(video_id)

# Save transcript to a file
if isinstance(transcript, list):
    with open("transcript.txt", "w", encoding="utf-8") as file:
        for entry in transcript:
            file.write(f"{entry['start']}: {entry['text']}\n")
else:
    print("Error:", transcript)

# Output the transcript
print(transcript)
