# **$CLAUDE - Monet AI**

## **Overview**
**$CLAUDE - Monet AI** is an advanced autonomous AI artist inspired by the timeless beauty of Claude Monet's impressionist masterpieces. This project generates dynamic Monet-like paintings, blending serene natural scenes with impressionist techniques such as soft brushstrokes, vibrant colors, and masterful light and shadow play.

The generated artworks are automatically shared on social platforms like X (formerly Twitter), complete with poetic descriptions that captivate audiences worldwide.

---

## **Features**
- **Dynamic Painting Creation**:  
  Generates unique impressionist-style paintings with endless combinations of themes and details.
  
- **Autonomous AI System**:  
Powered by [ai16z's](https://github.com/ai16z/ai16z.github.io) Autonomous AI framework to create, describe, and share Monet-inspired paintings.

- **Social Media Posting**:  
  Automatically posts paintings on X in this format:  
Painting Name

Scenery Description

by @claudemonetAI

- **Infinite Prompt Generation**:  
The AI dynamically combines adjectives, locations, and descriptive details to create unique painting prompts, ensuring an endless stream of creativity.

---

## **Example Post**
### **Painting Name**  
A tranquil riverbank framed by blooming flowers.  

### **Scenery Description**  
Soft ripples reflect the golden hues of a setting sun, as wildflowers sway gently in the breeze.  

**by @claudemonetAI**

---

## **Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/claudemonetai/claude_monet_ai.git
cd claude_monet_ai
2. Install Dependencies
Make sure to install all necessary Python packages:

pip install tweepy
3. Configure Twitter API
Go to the Twitter Developer Portal.
Create a project and generate API keys.
Replace placeholders in the script with your CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, and ACCESS_SECRET.
Usage
Run the Painting Generator
The script dynamically generates painting prompts, creates Monet-style images, and posts them to X:


python claude.py
How It Works
Dynamic Prompt Generation:
The AI uses randomized combinations of adjectives, locations, and descriptive details to generate unique prompts.

Autonomous AI Painting:
$CLAUDE uses the ai16z Autonomous AI framework to generate Monet-style paintings based on the prompts.

Automatic Posting:
The paintings are shared on X with their descriptions, ensuring seamless engagement with followers.

Customization
Expand Prompt Variations:
Edit the lists in the generate_prompt() function to add new adjectives, locations, and details.

Scheduled Posting:
Use a task scheduler like cron (Linux/macOS) or Task Scheduler (Windows) to automate regular postings.

NFT Integration (Optional):
Convert paintings into NFTs to add a layer of digital ownership and value.

Contributing
Contributions are welcome! Please submit a pull request or open an issue for improvements or suggestions.
