import streamlit as st
import openai

# Define the PulseActive product details and target audience specifics
product_name = "PulseActive Smartwatch"
product_features = ["Heart rate monitoring", "GPS tracking", "Sleep analysis", "Water resistance", "Customizable watch faces"]
product_benefits = ["Real-time health tracking", "Improved fitness goals", "Enhanced motivation through personalized reminders", "Durable and stylish design"]
target_audience = "Fitness enthusiasts"
pain_points = ["Inconsistent tracking", "Difficulty staying motivated", "Lack of reliable fitness data"]
desires = ["Accurate tracking", "Motivation to reach fitness goals", "A durable, stylish accessory"]
channel = "Instagram Ad"
tone = "Motivational, energizing, and focused on performance"
cta = "Swipe up to learn more and take your fitness to the next level with PulseActive!"
image_description = "A fitness enthusiast mid-workout, wearing the PulseActive smartwatch. The watch screen displays live heart rate and GPS tracking, set against a backdrop of a scenic outdoor trail."

# Function to generate marketing copy
def generate_copy(product_name, product_features, product_benefits, target_audience, pain_points, desires, channel, tone, cta, image_description):
    prompt = f"""
    You're a marketing copywriter creating an {channel} for {product_name}, a smartwatch designed for {target_audience}.

    **Target Audience:** {target_audience}

    **Highlight:**
    * Key features: {', '.join(product_features)}
    * Benefits: {', '.join(product_benefits)}
    * Address these pain points: {', '.join(pain_points)}
    * Appeal to these desires: {', '.join(desires)}

    **Tone:** {tone}

    **Call to Action:** {cta}

    **Image Description:** {image_description}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a marketing copywriter."},
            {"role": "user", "content": prompt}
        ]
    )
    copy = response['choices'][0]['message']['content']
    caption, image_description = copy.split("\n\n")
    return caption, image_description

# Streamlit UI
st.title("PulseActive Smartwatch Marketing Copy Generator")

if st.button("Generate Marketing Copy"):
    caption, image_description = generate_copy(product_name, product_features, product_benefits, target_audience, pain_points, desires, channel, tone, cta, image_description)
    st.subheader("Instagram Ad Caption:")
    st.write(caption)
    st.subheader("Image Description:")
    st.write(image_description)
