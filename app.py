import streamlit as st

import pyxstream

# Get the playlist URL from the user

playlist_url = st.text_input("Enter the playlist URL:")

# Create a pyxstream player

player = pyxstream.Player()

# Play the channel from the playlist

player.play(playlist_url)

# Display the player in the Streamlit app

st.video(player.video_stream)
