import tweepy
import os
import random
from ai16z import AutonomousAI  

# Twitter API credentials
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Initialize AI Agent
concept = {
    "name": "$CLAUDE MONET AI",
    "description": "An autonomous AI inspired by Claude Monet, generating impressionist-style paintings with serene natural themes."
}
ai_agent = AutonomousAI(name=concept["name"], description=concept["description"])

# Components for dynamic prompt generation
adjectives = ["serene", "tranquil", "golden", "peaceful", "radiant"]
locations = ["meadow", "riverbank", "garden", "forest clearing", "pond"]
details = [
    "bathed in soft morning light",
    "under a glowing sunset",
    "reflected on rippling waters",
    "framed by blooming flowers",
    "shimmering with dappled shadows"
]

# Function to generate dynamic prompts
def generate_prompt():
    adjective = random.choice(adjectives)
    location = random.choice(locations)
    detail = random.choice(details)
    return f"A {adjective} {location} {detail}."

# Generate a Monet-like painting and post
def generate_and_post():
    prompt = generate_prompt()  # Generate a random dynamic prompt
    
    try:
        # Generate an image with the AI agent
        result = ai_agent.generate_image(prompt=prompt, style="Claude Monet")
        image_path = result.get("image_path") 
        
        if image_path:
            # Prepare caption
            caption = f"{prompt}\n\nby @claudemonetAI"
            
            # Post to X (Twitter)
            api.update_status_with_media(status=caption, filename=image_path)
            print("Successfully posted on X!")
            
            # Clean up local image file
            os.remove(image_path)
        else:
            print("Image generation failed: No image path returned.")
    except Exception as e:
        print(f"Error generating and posting: {e}")

if __name__ == "__main__":
    generate_and_post()
