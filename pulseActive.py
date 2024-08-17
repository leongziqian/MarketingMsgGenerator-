import json

# Define your product details, target audience, channel, and desired tone
prompt_data = {
    "product_details": {
        "name": "PulseActive",
        "features": ["Heart rate monitoring", "Sleep tracking", "GPS", "Personalized workout recommendations"],
        "benefits": ["Accurate health insights", "Better sleep", "Enhanced fitness tracking", "Tailored fitness plans"]
    },
    "target_audience": {
        "description": "Fitness enthusiasts who are passionate about achieving their goals and staying on top of their progress",
        "pain_points": ["Difficulty tracking progress", "Lack of personalized workout guidance", "Inconsistent motivation"],
        "desires": ["Achieving fitness goals", "Accessing accurate health data", "Staying motivated through insights"]
    },
    "channel": "Instagram post",
    "tone": "Motivational, empowering, engaging"
}

# Craft the prompt using the structured data
prompt = f"""
You're a marketing copywriter. Write an Instagram post caption and image description to promote the {prompt_data['product_details']['name']}, a new wearable fitness tracker.

**Target audience:** {prompt_data['target_audience']['description']}

**Highlight:**
* Key features: {', '.join(prompt_data['product_details']['features'])}
* Benefits: {', '.join(prompt_data['product_details']['benefits'])}
* Address these pain points: {', '.join(prompt_data['target_audience']['pain_points'])}
* Appeal to these desires: {', '.join(prompt_data['target_audience']['desires'])}

**Tone:** {prompt_data['tone']}

**Image description:** A photo of the {prompt_data['product_details']['name']} being worn by an active individual, showing the sleek design and a glimpse of the health data displayed on the screen.
"""

# Generate the marketing copy using OpenAI
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a marketing copywriter."},
        {"role": "user", "content": prompt}
    ]
)
copy = response['choices'][0]['message']['content']

# Extract caption and image description from the response (you might need some text processing here)
caption, image_description = copy.split("\n\n")  # Assuming a newline separates caption and description

print("Instagram Caption:", caption)
print("\nImage Description:", image_description)

import openai

# Define your image generation parameters
prompt = """
🚀 Crush your fitness goals with PulseActive – the ultimate partner in your journey to success! 🌟 Say hello to accurate health insights, better sleep, and tailored workout recommendations all in one sleek wearable! 🏃‍♂️💪 #PulseActive #FitnessCompanion
"""

response = openai.Image.create(
  prompt=prompt,
  n=1,  # Number of images to generate
  size="1024x1024"  # Image size options: 1024x1024, 1024x1792, 1792x1024
)

# Get the image URL
image_url = response['data'][0]['url']
print(image_url)
