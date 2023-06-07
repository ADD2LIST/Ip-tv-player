import streamlit as st

import cv2

import m3u8

def play_channel(url):

    playlist = m3u8.load(url)

    if not playlist.is_variant:

        st.error('Invalid playlist format.')

        return

    video_url = playlist.segments[0].uri

    cap = cv2.VideoCapture(video_url)

    if not cap.isOpened():

        st.error('Error opening video stream or file.')

        return

    while True:

        ret, frame = cap.read()

        if not ret:

            break

        st.image(frame, channels='BGR')

    cap.release()

def main():

    st.title('IPTV Player')

    url = st.text_input('Enter IPTV playlist URL')

    if st.button('Play Channel'):

        play_channel(url)

if __name__ == '__main__':

    main()

