import streamlit as st

# Set page to "wide" mode
st.set_page_config(layout="wide", page_title="Live News TV Wall")

# Custom CSS to maintain 16:9 aspect ratio in each column (responsive)
st.markdown("""
    <style>
    .video-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
        height: 0;
        margin-bottom: 20px;
        border-radius: 16px;
        overflow: hidden;
        background: #222;
        box-shadow: 0 2px 12px rgba(30,30,30,0.12);
    }
    .video-container iframe {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        border-radius: 16px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Live News TV Wall for Masoud")

channels = [
    {"name": "Iran International", "url": "https://www.youtube.com/embed/sE-YfSPcRcU"},
    {"name": "Welt", "url": "https://www.youtube.com/embed/Ydv32vK6Fx8"},
    {"name": "IRINN", "url": "https://www.telewebion.com/embed/live/irinn"},
    {"name": "BBC", "url": "https://www.youtube.com/embed/IdnTOsEow0Q"},
    {"name": "Reuters", "url": "https://www.youtube.com/embed/zqk5YprulGI"},
    {"name": "Live Tel Aviv", "url": "https://www.youtube.com/embed/Iokwjw6WiXg"},
    {"name": "Kanal 13 Israel", "url": "https://www.youtube.com/embed/dpdKugDZZAY"},
]

# 3 columns per row for a wide dashboard
num_columns = 3

for row_i in range(0, len(channels), num_columns):
    cols = st.columns(num_columns)
    for col_i, channel in enumerate(channels[row_i:row_i+num_columns]):
        with cols[col_i]:
            st.subheader(channel["name"])
            st.markdown(
                f"""
                <div class="video-container">
                    <iframe src="{channel['url']}" allowfullscreen></iframe>
                </div>
                """,
                unsafe_allow_html=True,
            )
