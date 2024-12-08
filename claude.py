import tweepy
import os
import json
from ai16z import AutonomousAI  
from itertools import cycle
from PIL import Image
import random

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_SECRET = 'your_access_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Define Concept JSON
concept = {
    "name": "$CLAUDE MONET AI",
    "fullName": "$CLAUDE - The Impressionist Visionary of Crypto Culture",
    "description": "A groundbreaking AI project that reimagines Claude Monet’s impressionist style through the lens of modern blockchain and cryptocurrency themes.",
    "purpose": "To blend timeless artistic techniques with the bold innovation of blockchain, inspiring a fusion of creativity and technology.",
    "identity": {
        "name": "$CLAUDE",
        "origin": "Impressionist master with a modern crypto twist",
        "status": "timeless yet technologically avant-garde"
    }
}

# Initialize the ai16z Autonomous AI agent
agent = AutonomousAI(name=concept["name"], description=concept["description"])

# Function to load painting templates from an external JSON file
def load_painting_templates(file_path="painting_templates.json"):
    """
    Load painting templates from a JSON file.
    The JSON file should be structured as a list of dictionaries with "name" and "description".
    """
    try:
        with open(file_path, "r") as file:
            templates = json.load(file)
        return cycle(templates)  # Return a cycle for infinite iteration
    except Exception as e:
        print(f"Error loading painting templates: {e}")
        return cycle([])

# Function to generate a painting dynamically
def generate_painting(painting_templates):
    """
    Dynamically generate a painting name and description using templates.
    Adds random modifiers to ensure variety.
    """
    template = next(painting_templates)
    random_modifier = random.choice(["at Twilight", "in Spring", "under Blockchain Skies", "with Token Ripples"])
    return {
        "name": f"{template['name']} {random_modifier}",
        "description": f"{template['description']} This unique view is enhanced with the hues of {random_modifier.lower()}."
    }

def generate_image_with_ai16z(prompt, name):
    """
    Use the ai16z AutonomousAI agent to generate Claude Monet-style images.
    """
    try:
        # Assuming the repository provides a `generate_image` method
        result = agent.generate_image(prompt=prompt, style="Claude Monet")
        image_path = result.get("image_path")  # Hypothetical response structure
        if image_path:
            return image_path, name
        else:
            raise Exception("Image generation failed. No image path returned.")
    except Exception as e:
        raise Exception(f"Error generating image: {e}")

def post_image_to_twitter(image_path, name, description):
    """
    Post an image to Twitter with the given name and description in the required format.
    """
    caption = f"{name}\n\n{description}\n\nby @claudemonetAI"
    api.update_status_with_media(status=caption, filename=image_path)
    print(f"Posted '{name}' to Twitter successfully.")
    os.remove(image_path)

if __name__ == "__main__":
    try:
        # Load painting templates from JSON file
        painting_templates = load_painting_templates()

        while True:
            # Generate a new painting
            painting = generate_painting(painting_templates)
            prompt = f"{concept['description']} {painting['description']}"
            print(f"Generating image for '{painting['name']}'...")
            
            # Generate the image
            image_path, name = generate_image_with_ai16z(prompt, painting['name'])
            
            # Post to Twitter
            post_image_to_twitter(image_path, name, painting["description"])

    except Exception as e:
        print(f"Error: {e}")
