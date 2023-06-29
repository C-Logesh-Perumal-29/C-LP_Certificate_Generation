# Importing the libraries :
import cv2
import numpy as np
from PIL import Image
import streamlit as st

# Icon & title of the page :
img = Image.open("13.jpg")
st.set_page_config(page_title="Certificate Generation",page_icon=img,layout="wide")

# Hide Menu_Bar & Footer :
hide_menu_style = """
    <style>
    #MainMenu {visibility : hidden;}
    footer {visibility : hidden;}
    </style>
"""
st.markdown(hide_menu_style , unsafe_allow_html=True)

# Set the background image :

Background_image = """

<style>
[data-testid="stAppViewContainer"] > .main
{
background-image: url("https://img.freepik.com/premium-vector/abstract-blur-bokeh-lens-flare-vintage-blue-purple_147586-112.jpg?size=626&ext=jpg&ga=GA1.2.2087154549.1663432512&semt=ais");

background-size : 100%
background-position : top left;

background-position: center;
background-size: cover;
background-repeat : repeat;
background-repeat: round;


background-attachment : local;

background-image: url("https://img.freepik.com/premium-vector/abstract-blur-bokeh-lens-flare-vintage-blue-purple_147586-112.jpg?size=626&ext=jpg&ga=GA1.2.2087154549.1663432512&semt=ais");
background-position: right bottom;
background-repeat: no-repeat;
}  

[data-testid="stHeader"]
{
background-color : rgba(0,0,0,0);
}

</style>                                
"""

st.markdown(Background_image,unsafe_allow_html=True)

col1,col2 = st.columns([1,5])

with col1:
    img = Image.open("13.jpg")
    st.image(img,width=150)

with col2:
    
    h = """
        <html>
            <head>
                <title></title>
            </head>
            <body>
                <h1 style = "align:right;font-family:Engravers MT;color:#191970"> Certificate Generation </h1>
            </body>
        </html>
    """
    st.markdown(h,unsafe_allow_html=True)

st.balloons()

Name_List_Data = []

def Name_List():
    
        file_uploader = st.file_uploader("Choose the file",type = ['txt'])
        if file_uploader is not None:
            file_path = file_uploader.name 
            st.success("File Uploaded Successfully...")
            st.snow()       
        file = open(file_path,"r")    
        for names in file:
            Name_List_Data.append(names.strip())
            
        st.write(Name_List_Data)
        st.snow()

def generate_certificate():
    st.snow()
    coordinate_1 = st.text_input("Enter Coordinate 1 : ",placeholder="X Coordinate")
    
    if coordinate_1:
    
        coordinate_2 = st.text_input("Enter Coordinate 2 : ",placeholder="Y Coordinate")
        st.snow()
        
    if coordinate_2:
            
        RGB = st.text_input("RGB Color Code : ",placeholder="RGB Color")
        l = RGB.split(',')
        Red = int(l[0])
        Green = int(l[1])
        Blue = int(l[2])
        st.snow()
        Certificate_Uploader = st.file_uploader("Upload the Certificate : ",type = ["jpg","jpeg","png"])
        st.image(Certificate_Uploader,caption="Your Certificate Template")
        st.snow()
        
    for index,name in enumerate(Name_List_Data):
         
        if Certificate_Uploader is not None:
                
            image = Image.open(Certificate_Uploader)
            image = np.array(image)
    
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
              
            cv2.putText(image,name,(int(coordinate_1),int(coordinate_2)),cv2.FONT_HERSHEY_SIMPLEX,2,((int(Blue),int(Green),int(Red))),6,cv2.LINE_AA)
            
            cv2.imwrite(f'{name}.jpg',image)
            
            st.write(f'Processing {index + 1} / {len(Name_List_Data)}')
            
        else:
            print('File not available')      


    st.info("\n !!!!!!!!!!!!!!!! Certificates Saved Successfully !!!!!!!!!!!!!!!!")
    
    st.balloons()
    st.snow()
                                                
Name_List()

generate_certificate()





