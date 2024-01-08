
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="my website ",page_icon="🔝",layout="wide")

#image 


img_Rl=Image.open("images\RL.png")
img_eng=Image.open("images\eng.png")
img_contact_from=Image.open("images\oi.png")



#amotion 
lottie_coding="https://lottie.host/72713f88-41d1-4481-b732-639ba72596aa/uig2ZBMcth.json"
lottie_coding2="https://lottie.host/95bd72f4-53a3-481b-8f70-04d90f60783e/JTxnPqEyzg.json"

def load_lottieurl(url):
    r=requests.get(url)
    if r.request !=200:
        return None
    return r.json()


#use local css 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style",unsafe_allow_html=True)

local_css("style/style.css")




coding_lottie=load_lottieurl("https://lottie.host/72713f88-41d1-4481-b732-639ba72596aa/uig2ZBMcth.json")


#header section 
with st.container():
    
    st.subheader("Hi everynoe I'm Abdulrahman Salem Saud :wave:")
    st.title("A Data science student ")
    st.write("Hello everyone, I'm Abdulrahman Salem Saud. As a dedicated data science student, I have a strong passion for learning and improving my skills in artificial intelligence and data science. Alongside my studies, I also have experience in team management, which has honed my ability to work efficiently under pressure. I pride myself on being hardworking and ambitious, always striving to achieve the best results\n"

            "In terms of technical skills, I am proficient in Python and R, and I have hands-on experience in data analysis, machine learning, and data visualization. These skills enable me to extract meaningful insights from complex datasets and communicate them effectively.\n"

            "I have also pursued additional education to enhance my expertise. I have completed courses in data entry and word processing, as well as an English language course, where I excelled and received a recommendation letter for my outstanding performance. Furthermore, I have acquired knowledge in Excel, PowerPoint, and Photoshop through introductory courses.\n"
            "Thank you for taking the time to learn a little about me. Feel free to connect with me on LinkedIn for further engagement: LinkedIn Profile")

            
    st.write("[linkden >](https://www.linkedin.com/in/abdulrahman-saud-915130245/)")


#What I do
    
with st.container():
    st.write("---")
    left_culomn,righ_column= st.columns(2)
    with left_culomn:
        st.header('What I do')
        st.write("- I work on Python\n"
                 "- I work on R language\n"
                 "- Data analysis and machine learning\n"
                 "- Data visualization\n"
                 "- Able to manage teams and work under high pressure")

    with righ_column:
        st_lottie(lottie_coding,height=300,key='coding')




#skills
        

with st.container():
    st.write('---')
    st.header("My Certificates:")
    st.write("##")

    image_column,text_column=st.columns((1,2))

    with image_column:
        st.image(img_contact_from)

        with  text_column:
            st.subheader("Data entry and word processing course")

            st.write("- I passed this six-month course from the FAO Institute")

#-------------------------------------------#
            
with st.container():
    image_column,text_column=st.columns((1,2))

    with image_column:
        st.image(img_Rl)
    
    with text_column:
        st.subheader("Recommendation letter")
        st.write("- This recommendation from my instructor I have passed English101, and I was the first in my class ,additional I got 100 out of 100 in his course.")

#-------------------------------------------#
with st.container():
    image_column,text_column=st.columns((1,2))

    with image_column:
        st.image(img_eng)

    with text_column:
        st.subheader("English Language Certificate")
        st.write("- I passed this six-month of English course from the FAO Institute")

#-------------------------------------------#
with st.container():
    image_column,text_column=st.columns((1,2))

    with image_column:
        st_lottie(lottie_coding2,height=300,key='str')
        

    with text_column:
        st.subheader("Certificates And Additional Courses")
        st.write("- Introduction to Excel \n"
                 "- Introduction to PowerPoint\n"
                 "- Introduction to Photoshop\n"
                 "- I have a STEP test\n"
                 )
        



with st.container():
    st.write('---')
    st.header('Personal Information')
    st.write('##')

    st.write("- Name:   Abdulrahman Salem Saud \n"
                 "- Major:   Data Science\n"
                 "- Phone:   0538081148\n"
                 "- Email:   abdulrahmansaud1998@gmail.com\n")




#------contact--------#
        

with st.container():
    st.write('---')
    st.header('GET IN Touch With Me! ')
    st.write('##')


    contact_from=  """
    <form action="https://formsubmit.co/abdulrahmansaud1998@gmail.com" method="POST">
     <input type ="hidden" namr="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name " required>
     <input type="email" name="email" placeholder="Your Email " required>
     <textarea name ="Message" placeholder="Your Massage Here  " requires></textarea>
     <button type="submit">Send</button>
     </form>           """
    
    left_culomn,righ_column=st.columns(2)
    with left_culomn:
        st.markdown(contact_from, unsafe_allow_html=True)
    with righ_column:
        st.empty()
#---------------------------------------------------#
        






