import os
import tweepy
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io

def create_tweetshot(tweet_url):
    # Twitter API credentials from environment variables
    bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

    # Authenticate with Twitter API
    client = tweepy.Client(bearer_token=bearer_token)

    # Extract tweet ID from URL
    tweet_id = tweet_url.split('/')[-1]

    try:
        # Fetch tweet data
        tweet = client.get_tweet(
            id=tweet_id,
            expansions=['author_id'],
            tweet_fields=['created_at', 'text'],
            user_fields=['name', 'username', 'profile_image_url']
        )
        
        user = tweet.includes['users'][0]

        # Set up the image
        width, height = 600, 300
        background_color = (255, 255, 255)  # White
        img = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(img)

        # Load fonts
        try:
            name_font = ImageFont.truetype("arial.ttf", 20)
            username_font = ImageFont.truetype("arial.ttf", 16)
            tweet_font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            # Fallback to default font if Arial is not available
            name_font = ImageFont.load_default()
            username_font = ImageFont.load_default()
            tweet_font = ImageFont.load_default()

        # Draw name and username
        draw.text((80, 20), user.name, fill=(0, 0, 0), font=name_font)
        draw.text((80, 45), f"@{user.username}", fill=(128, 128, 128), font=username_font)

        # Draw tweet text
        margin = 20
        offset = 80
        for line in textwrap.wrap(tweet.data.text, width=60):
            draw.text((margin, offset), line, font=tweet_font, fill=(0, 0, 0))
            offset += tweet_font.getsize(line)[1] + 5

        # Add profile picture
        profile_img_url = user.profile_image_url.replace('_normal', '')
        profile_img_response = requests.get(profile_img_url)
        profile_img = Image.open(io.BytesIO(profile_img_response.content))
        profile_img = profile_img.resize((60, 60))
        img.paste(profile_img, (10, 20))

        return img

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    tweet_url = "https://x.com/mischa_vdburg/status/1810224178491969944"
    tweet_image = create_tweetshot(tweet_url)
    if tweet_image:
        tweet_image.save("tweetshot.png")
    else:
        print("Failed to create tweetshot.")
