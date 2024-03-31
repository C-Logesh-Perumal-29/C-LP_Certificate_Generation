import cv2
import numpy as np
from PIL import Image
import streamlit as st
import base64
from io import BytesIO

# Icon & title of the page :
img = Image.open("ico.png")
st.set_page_config(page_title="Certificate Generation", page_icon=img, layout="wide")

# Hide Menu_Bar & Footer :
hide_menu_style = """
    <style>
    #MainMenu {visibility : hidden;}
    footer {visibility : hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Set the background image :
Background_image = """
<style>
[data-testid="stAppViewContainer"] > .main
{
background-image: url("https://img.freepik.com/free-vector/realistic-digital-lavender-background_23-2150595000.jpg?w=996&t=st=1711867421~exp=1711868021~hmac=100f43b1805888a1e6a0b32272183283cdc12b2d276518bd82ba65bd2856bf0c");
background-size : 100%;
background-position : top left;
background-position: center;
background-size: cover;
background-repeat : repeat;
background-repeat: round;
background-attachment : local;
background-image: url("https://img.freepik.com/free-vector/realistic-digital-lavender-background_23-2150595000.jpg?w=996&t=st=1711867421~exp=1711868021~hmac=100f43b1805888a1e6a0b32272183283cdc12b2d276518bd82ba65bd2856bf0c");
background-position: right bottom;
background-repeat: no-repeat;
}  
[data-testid="stHeader"]
{
background-color : rgba(0,0,0,0);
}
</style>                                
"""
st.markdown(Background_image, unsafe_allow_html=True)

col1, col2, col3 = st.columns([4, 2, 4])

with col2:
    img = Image.open("Icon.png")
    st.image(img, width=100, use_column_width=True, output_format='auto')

h = """
    <html>
        <head>
            <style>
                .title {
                    text-align: center;
                    font-family: 'Engravers MT';
                    color: white;
                }
            </style>
        </head>
        <body>
            <div style="display: flex; align-items: center; justify-content: center;">
                <h1 class="title">Certificate Generation</h1>
            </div>
        </body>
    </html>
"""
st.markdown(h, unsafe_allow_html=True)

st.balloons()

Name_List_Data = []

def Name_List():
    file_uploader = st.file_uploader("Choose the file", type=['txt'])
    if file_uploader is not None:
        file_path = file_uploader.name
        st.success("File Uploaded Successfully...")

        file = open(file_path, "r")    
        for names in file:
            Name_List_Data.append(names.strip())
            
        st.write(Name_List_Data)

    return Name_List_Data

def generate_certificate():
    coordinate_1 = st.text_input("Enter Coordinate 1 : ", placeholder="X Coordinate")
    coordinate_2 = st.text_input("Enter Coordinate 2 : ", placeholder="Y Coordinate")
    
    # Use select boxes for RGB color code
    rgb_color = st.text_input("RGB Color Code : ", placeholder="RGB Color (e.g., 255,255,255)")

    if rgb_color:
        rgb_values = rgb_color.split(',')
        if len(rgb_values) == 3:
            try:
                Red = int(rgb_values[0])
                Green = int(rgb_values[1])
                Blue = int(rgb_values[2])
            except ValueError:
                st.error("Invalid RGB color values. Please enter integers separated by commas.")
                return
        else:
            st.error("Invalid RGB color format. Please enter three integer values separated by commas.")
            return

    certificate_uploader = st.file_uploader("Upload the Certificate : ", type=["jpg", "jpeg", "png"])
    
    if certificate_uploader is not None:
        file_path = certificate_uploader.name
        
        # Display the uploaded certificate image
        st.image(certificate_uploader, caption="Your Certificate Template")
        
        for name in Name_List_Data:
            image = Image.open(certificate_uploader)
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            cv2.putText(image, name, (int(coordinate_1), int(coordinate_2)), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        ((int(Blue), int(Green), int(Red))), 6, cv2.LINE_AA)

            cv2.imwrite(f'{name}.jpg', image)

            st.write(f'Processing  {name}\'s Certificate')

            def get_image_download_link(img, filename, text):
                buffered = BytesIO()
                img.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                href = f'<a href="data:file/jpg;base64,{img_str}" download="{filename}">{text}</a>'
                return href

            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            result = Image.fromarray(image)
            st.markdown(get_image_download_link(result, file_path, 'Download Image'), unsafe_allow_html=True)

# Run functions
Name_List()
generate_certificate()
