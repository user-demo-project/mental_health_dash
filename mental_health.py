import pickle
from pathlib import Path
import pandas as pd
import numpy as np
import pandas as pd  # pip install pandas openpyxl
import sklearn
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


from PIL import Image
print(pd.__version__,np.__version__)
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="Mental Health Dashboard", page_icon=":bar_chart:", layout="wide")
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
st.markdown(f"""<style>
.css-16idsys p{{
font-size:14px;}}
.css-uf99v8 {{
margin-top: -100px;}}

 </style>""",unsafe_allow_html=True)
 
with open("style.css") as f:
    st.markdown(f'<style> {f.read()}</style>', unsafe_allow_html=True)
st.title('Mental Health Analysis')

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# --- USER AUTHENTICATION ---
names = ["test_user"]
usernames = ["user@123"]
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

print(hashed_passwords)
credentials = {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                }
        
            }
        }
# load hashed passwords
#file_path = Path(__file__).parent / "hashed_pw.pkl"


authenticator = stauth.Authenticate(credentials,"Mental Health Analysis", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
print(authentication_status ,"dd")
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    print("done")
    tab1, tab2 ,tab3= st.tabs(["📈 Data Summary ","📈 Data Insights ", "⚙️ Prediction"])
    data = np.random.randn(10, 1)

    tab1.subheader("Variable Description")
    with tab1:
        st.write("Numerical Variable")
        data_numerical = {
        'Variable': ['Age', 'Time spent on Online Class', 'Time spent on self study', 'Time spent on fitness',
                     'Time spent on sleep', 'Time spent on social media', 'Time spent on TV', 'Number of meals per day'],
        'Explanation': ['Student Age', 'Time spent on online class by student', 'Time spent on self study by student',
                        'Time spent on online fitness by student', 'Time spent on sleep by student',
                        'Time spent on social media by student', 'Time spent on TV by student',
                        'Number of meals per day by student'],
        'Min': [7.00, 0.00, 0.00, 0.00, 4.00, 0.00, 0.00, 1.00],
        'Max': [59.00, 10.00, 18.00, 5.00, 15.00, 10.00, 15.00, 8.00],
        'Average': [20.17, 3.21, 2.91, 0.77, 6.89, 2.44, 1.03, 2.92]}

        df_numerical = pd.DataFrame(data_numerical)
        st.table(df_numerical)
        
        st.write("Boolean Variable")
        
        data_boolean = {
    'Variable': ['Do you find yourself more connected with your family, close friends, relatives?',
                 'Time utilized'],
    'Explanation': ['Did students spend time with friends, family, or not',
                    'Time was utilized properly or not']
        }

        df_boolean = pd.DataFrame(data_boolean)
        
        st.table(df_boolean)
        
        st.write("Categorical Variable")
        
        data_categorical = {
    'Variable': ['Prefered social media platform', 'Change in your weight', 'Medium for online class'],
    'Explanation': ['Prefered social media by student', 'Has weight changed or not', 'Prefered medium for online class'],
    'Number of categories': [15, 3, 6]
}

        df_categorical = pd.DataFrame(data_categorical)
        st.table(data_categorical)
    with tab2:
        col21,col22= st.columns(2)
        with col21:
            option_img = st.selectbox(
    'Select variable',
    ('Time spent on online class', 'Time spent on fitness', 'Time spent on TV','Time spent on sleep','Time spent on self-study','Time spent on social-media'))
            st.write("***People having mental health condition spent less time on online classes,fitness,sleep and more time on social media")
        with col22:
          
            if option_img=="Time spent on online class":
                image_21 = Image.open('image001.png')

                st.image(image_21, width =400)
            if option_img=="Time spent on fitness":
                image_22 = Image.open('image009.png')

                st.image(image_22, width =400)
            if option_img=="Time spent on TV":
                image_23 = Image.open('image003.png')

                st.image(image_23, width =400)
            if option_img=="Time spent on sleep":
                image_24 = Image.open('image011.png')

                st.image(image_24, width =400)
            if option_img=="Time spent on self-study":
                image_25 = Image.open('image005.png')

                st.image(image_25, width =400)
            if option_img=="Time spent on social-media":
                image_26 = Image.open('image007.png')

                st.image(image_26, width =400)
        st.subheader("______________________________________________________________")
        st.write("***People having mental health spend maximum time on Instagram")
        col11, col22,col33,col44 = st.columns(4)
         
        with col11:
           
            image_1 = Image.open('image013.png')

            st.image(image_1, width =380)
        
        with col22:
            
            image_3 = Image.open('image015.png')

            st.image(image_3, width =380)
        
        with col33:
            
            image_4 = Image.open('image017.png')

            st.image(image_4, width =500)        
            st.write("The data is right skewed,most of the students are of the age range between 15-25 years")
    tab3.subheader("Please fill below details for prediction")
    with tab3:
        col1, col2,col3,col4,col5 = st.columns(5)
        with col1:
            medium=st.selectbox("Medium for Online Class", ["Laptop/Desktop",
"Smartphone",
'Tablet',
'Any Gadget',
'Smartphone or Laptop/Desktop'])
        with col2:
            social_media=st.selectbox("Preffered Social Media Platform", ["Linkedin",
"Youtube",
'Instagram',
'Whatsapp',
'None',
'Reddit',
'Snapchat',
'Omegle',
'Twitter',
'Telegram',
'Facebook',
'Elyment',
'None', 
'Quora',
'Talklife'])
        with col3:
            weight=st.selectbox("Change in your weight", ["Increased",
'Decreased',
"Remain Constant"])
        with col4:
            time_utilized=st.selectbox("Time Utilized", ["Yes","NO"])
        with col5:
            family=st.selectbox("Do you find yourself more connected to your freinds, family and relatives?", ["Yes","NO"])
        col6, col7,col8,col9,col10,col11,col12 = st.columns(7)
        with col6:
            age = st.slider('How old are you?', 0, 75, 25)
        with col7:
            meals = st.number_input('Number Of Meals per day',step=1,key="a")
        with col8:
            tv_time = st.number_input('Time spent on TV',step=.1,key="b")
        with col9:
            social_media_time = st.number_input('Time spent on social media',step=.1,key="c")
        with col10:
            study_time = st.number_input('Time spent on self study',step=.1,key="e")
        with col11:
            fitness_time = st.number_input('Time spent on fitness',step=.1,key="d")
        with col12:
            class_time = st.number_input('Time spent on online class',step=.1,key="f")
        age=np.int64(age)
        if st.button('Submit'):
            data = {
            'Age': [age],
            'Time spent on Online Class': [class_time],
            'Medium for online class': [medium],
            'Time spent on self study': [study_time],
            'Time spent on fitness': [fitness_time],
            'Time spent on social media': [social_media_time],
            'Preferred social media platform': [social_media],
            'Time spent on TV': [tv_time],
            'Number of meals per day': [meals],
            'Change in your weight': [weight],
            'Time utilized':[time_utilized],
            'Do you find yourself more connected with your family, close friends, relatives?': [family]
        }
            data = pd.DataFrame(data)
            #st.table(data)
            data["Age"]=data['Age'].astype(np.int64)
            with open(r"encoding.pickle", 'rb') as f:
                transformation_info = pickle.load(f)
            transformed_data = data.copy()
           
            for column in transformation_info.columns:
                print(type(data["Age"][0]))
                if column in data.columns:
                    transformed_data[column] = data[column].astype(transformation_info[column][0])
                    print("ssssssssssssssssssssssssssssssssssssssssssssssss")
                else:
                    transformed_data[column] = transformation_info[column][1]

            # Drop any extra columns that are not in the transformation info
            transformed_data = transformed_data[transformation_info.columns]
            print(transformed_data)
            with open(r"scaler.pickle", 'rb') as f:
                scaler = pickle.load(f)

            scaled_data = scaler.transform(transformed_data)
            scaled_df = pd.DataFrame(scaled_data, columns=transformed_data.columns)
            
            with open(r"model.pickle", 'rb') as f:
                model = pickle.load(f)

            predictions = model.predict(scaled_df)
            print(predictions[0],"df")
            st.subheader("Output: "+str(predictions[0]))
            if predictions[0]==1:
                st.subheader("Candidate has signs of mental health")
            if predictions[0]==0:
                st.subheader("Candidate has no signs of mental health")
