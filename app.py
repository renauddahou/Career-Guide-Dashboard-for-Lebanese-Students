# import streamlit as st
# from multiapp import MultiApp
# from apps import home,job_analysis,job_information # importing app modules
#
# ## This multi-page app was prepared using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar]
#
# app = MultiApp()
#
# ## Setting the Width (Streamlit Wide Layout is too wide)
# st.markdown(
#         f"""
# <style>
#     .reportview-container .main .block-container{{
#        max-width: {1450}px;
#     }}
#     .reportview-container .main {{
#         color: {'OffBlack'};
#     }}
# </style>
# """,
#         unsafe_allow_html=True,
#     )
#
# ## Title
# st.image('/Users/user/Desktop/capstone/header1.jpg',width= 1450)
# st.markdown(f"<h1 style='text-align:center;' >{'<b>Career Guide Dashboard fo Students in Lebanon</b>'}</h1>", unsafe_allow_html=True)
# st.markdown(f"<h3 style='text-align:center;' >{'by Luna Baalbaki'}</h3>", unsafe_allow_html=True)
#
# # skipping some lines
# st.write("")
# st.write("")
# st.write("")
# st.write("")
#
# ## Adding the Applications
# app.add_app("Home", home.app)
# app.add_app("Job Market Analysis in Lebanon", job_analysis.app)
# app.add_app("Job Information", job_information.app)
#
# # The main app
# app.run()
#
# # Footer, code source: https://discuss.streamlit.io/t/streamlit-footer/12181
#
# # footer= """<style>
# # a:link , a:visited{
# # color: black;
# # background-color: transparent;
# # text-decoration: underline;
# # }
# # a:hover,  a:active {
# # color: teal;
# # background-color: transparent;
# # text-decoration: underline;
# # }
# # .footer {
# # position: fixed;
# # left: 0;
# # bottom: 0;
# # width: 100%;
# # background-color: white;
# # color: black;
# # text-align: center;
# # }
# # </style>
# # <div class="footer">
# # <p>Developed by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/sarah-el-moughrabi/" target="_blank">Sarah El Moughrabi</a></p>
# # <p>as part of Data-Driven Digital Marketing (MSBA 370) course taught at OSB-AUB.</p>
# # </div>
# # """
# st.markdown(footer,unsafe_allow_html=True)





###
import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
# The main app
app.run()