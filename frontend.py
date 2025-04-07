# import sys
# import os

# # Fix for relative imports
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# import streamlit as st
# from agents import generate_sarcastic_profile_summary

# st.set_page_config(page_title="LinkedIn Sarcastic Agent 😎", layout="centered")

# st.title("🔍 LinkedIn Sarcastic Agent")
# st.caption("Get a witty roast-style summary of any LinkedIn user. Powered by LLMs and spice.")

# username = st.text_input("🔤 Enter person's name")
# keywords = st.text_input("🧠 Enter some keywords (company, location, title, etc.)")

# if st.button("🔥 Roast 'em"):
#     if username and keywords:
#         with st.spinner("Cooking up sarcasm..."):
#             try:
#                 summary = generate_sarcastic_profile_summary(username, keywords)
#                 st.markdown("### 🤖 Agent's Take")
#                 st.write(summary)
#             except Exception as e:
#                 st.error(f"Oops! Something went wrong: {e}")
#     else:
#         st.warning("Please enter both name and keywords before launching the roast.")

#======

import sys
import os
import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Fix for relative imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents import generate_sarcastic_profile_summary

st.set_page_config(page_title="LinkedIn Sarcastic Agent 😎", layout="centered")

st.title("🔥 LinkedIn Sarcastic Agent")
st.caption("Let AI roast your LinkedIn presence. Fun, witty, and dangerously honest 😏")

# Roast Level Selector
roast_level = st.radio("Choose your roast level:", ["😂 Light Roast", "💣 Savage Mode"], index=1)

# Fun Header GIF
st.image("https://media.giphy.com/media/l41YgJZFVqXwSmeo0/giphy.gif", width=300)

username = st.text_input("👤 Who are we roasting?")
keywords = st.text_input("🔍 Add some clues (title, company, skills)")

if st.button("Roast 'em!"):
    if username and keywords:
        with st.spinner("Compiling juicy insights... 🔍💻"):
            try:
                result = generate_sarcastic_profile_summary(username, keywords)

                if "error" in result:
                    st.error(result["error"])
                else:
                    st.success("Here’s what your LinkedIn says behind your back 😂")

                    st.markdown(f"🔗 **[View LinkedIn Profile]({result['url']})**")
                    gif_url = "https://media.giphy.com/media/d31w24psGYeekCZy/giphy.gif" if roast_level == "😂 Light Roast" \
                        else "https://media.giphy.com/media/3o6Mbbs879ozZ9Yic0/giphy.gif"
                    st.image(gif_url, width=300)

                    # Display the sarcastic summary
                    st.markdown("### 🤖 Agent’s Sarcastic Take")
                    st.write(result["summary"])

                    # Add spicy observations
                    st.markdown("---")
                    st.markdown("### 🔮 Random Roast Insights")
                    st.markdown("🧠 *Their buzzword count could break LinkedIn's algorithm.*")
                    st.markdown("📉 *Endorsed for 'Leadership' by their mom. Twice.*")
                    st.markdown("🕵️ *Their title has more words than their resume.*")

                    # Save Roast as Image
                    st.markdown("---")
                    st.markdown("### 📸 Want to keep the roast?")
                    if st.button("Download Summary as Image"):
                        img = Image.new("RGB", (1000, 700), color="white")
                        d = ImageDraw.Draw(img)
                        d.text((10, 10), result["summary"], fill="black")
                        buffer = BytesIO()
                        img.save(buffer, format="PNG")
                        buffer.seek(0)
                        b64 = base64.b64encode(buffer.read()).decode()
                        href = f'<a href="data:file/png;base64,{b64}" download="linkedin_roast.png">📥 Click here to download</a>'
                        st.markdown(href, unsafe_allow_html=True)

                    st.markdown("---")
                    st.caption("Built with 💥 by an AI with too much attitude and not enough sleep.")
            except Exception as e:
                st.error(f"Oops! Something went wrong: {e}")
    else:
        st.warning("Please enter both a name and some keywords.")
