from pathlib import Path
import streamlit as st
from PIL import Image

#---- PATH SETTINGS-------#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print("The current working directory is: " + str(current_dir))

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "madhu.png"

#---------GENERAL SETTINGS------------#
PAGE_TITLE = "Digital CV | Madhusudhan B"
PAGE_ICON = ":racing_car:"
NAME = "Madhusudhan B"
DESCRIPTION = """
Data Scientist, helping businesses make better decisions enabled by data
"""
EMAIL = "madhuhotmail2005@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/madhusudhan-datascience",
    "GitHub": "https://github.com/madhuyadu"
}
PROJECTS = {
    "🏆 History-based & Potential-based product recommendations to stores on B2B App",
    "🏆 Customized item recommendations to stores via Offline route(traditional channel)",
    "🏆 Generation of Substitute & Complimentary item recommendations to stores on B2B App",
    "🏆 Store sale value forecasting using Forecasting approach",
    "🏆 Building Analytics platform for Energy Efficient heating solution"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there !")

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(
    2, gap="small")  #create columns for content insertion below

with col1:  #insert image in col1
    st.image(profile_pic, width=230)

with col2:  #include other details in col2
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(
        "📫", EMAIL
    )  #logo and email ID will be added horizontally when separated by comma

# --- SOCIAL LINKS ---
st.write('\n')  #insert new line
cols = st.columns(len(SOCIAL_MEDIA))

#Iterate through each social media link and insert it in columns
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    # ({link}) --> will insert link along with hyperlinking facility
    # [{platform}] --> ensures link is hidden within platform text
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("""
- ✔️ 7 Years experience in extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, SQL, Scala, Pyspark
- ✔️ Domain expertise in Energy, Facilities, Manufacturing & Retail
- ✔️ M.Sc in Data Science & M.Tech in Manufacturing Management
- ✔️ Strengths: Team player, taking initiatives, go-getter, quick learner
""")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("""
- 👩‍💻 Programming: Python (scikit-learn, numpy, pandas, matplotlib, seaborn, tensorflow), SQL, Pyspark, Scala
- :cloud: Cloud platform: Microsoft Azure ,Azure Machine Learning Service (Designer, SDK, AutoML)
- :elephant: Big data Ecosystem: Spark, Databricks
- :robot_face: Modeling: Regression, Classification, Clustering, Ensemble & Boosted models, Time-series forecasting
""")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 : latest job (ROLE 1)
st.write("🚧",
         "**Lead Data Analyst | Mindtree Limited**")  #for BOLD font use **
st.write("02/2022 - Present")
st.caption("""
- ► Used Azure Machine learning Service to create, run & track Machine Learning/Deep Learning (ML/DL) experiments on Scalable computer clusters
- ► Developed ML/DL based time-series & regression algorithms for forecasting sale value of retail stores, while improving the Distributor target setting process
""")

# --- JOB 1 (ROLE 2)
st.write('\n')
st.write("🚧", "**Senior Data Analyst | Mindtree Limited**")
st.write("01/2020 - 01/2022")
st.caption("""
- ► Ingested huge data sets from Data Lake storage and Performed Data pre-processing & transformation on Distributed Big data platform such as Spark
- ► Built & evaluated Machine Learning models (classification, clustering) on Azure Databricks and implemented mlflow for parameter, metric and model logging
- ► Developed Business level KPIs for client reporting and for measurement of algorithm performance
- ► Identified and analyzed factors to improve recommendation system performance thus helping in outlet acquisition, retention and understanding buying behavior
""")

# --- JOB 2 (ROLE 1)
st.write('\n')
st.write("🚧", "**Plant Data Analyst | Bosch Limited**")
st.write("01/2016 - 12/2019")
st.caption("""
- ► Administered building Analytics platform for Energy Efficient Heat pumps as alternate solution for conventional heating in component cleaning
- ► Performed Energy & Demand pattern study to analyze & reduce utility and production MAE energy consumption during peak/off-peak periods
""")
# --- JOB 2 (ROLE 2)
st.write('\n')
st.write("🚧", "**Deputy Manager | Bosch Limited**")
st.write("02/2013 - 12/2015")
st.caption("""
- ► Identified & implemented Cost Reduction and Energy Conservation Projects in utilities and production machinery/equipment
- ► Synchronized at Plant level for various initiatives such as Energy/cost allocation, energy forecasting while monitoring and reporting the status via PDCA approach
""")
# --- JOB 2 (ROLE 3)
st.write('\n')
st.write("🚧", "**Technical Engineering Functions| Bosch Limited**")
st.write("01/2010 - 01/2013")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Achievements | Rewards & Recognition")
st.write("---")
st.write(
"""
- 🏆Felicitated with **Hats Off** award thrice (in 2021, 2022) for solving complex project use case & successfully executing Project deliverables
- 🏆Recognized as **Top Talent** twice (in 2021, 2022) as part of Annual Appraisal System
- 🏆Attained Distinction in M.Sc. Data Science, Liverpool John Moores University
- 🏆Achieved CGPA of 3.62 (out of 4) during PG Diploma in Data Science, IIIT-B
- 🏆Achieved CGPA of 9.2 during M.Tech, BITS Pilani
- 🏆Secured University rank (2nd in the State) during B.E, BMS College of Engineering"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write(
"""
- :crown:Azure Data Scientist Associate | Microsoft | Aug'22
- :crown:Associate Developer Spark 3.0| Databricks | Feb'21
- :crown:Solutions Architect| Databricks | Oct'20
- :crown:SQL Analyst Associate | Databricks| Feb'22
- :crown:Spark overview for Scala Analytics | IBM | Aug '20
- :crown:A-Z Machine learning using AzureML | Udemy | Aug '20
"""
)


