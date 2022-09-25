import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image


pickle_in = open("pipe.pkl","rb")
model= pickle.load(pickle_in)

def welcome():
    return "Welcome All"
def performance_predictor(df):
    prediction= model.predict(df)
    print(prediction)
    return prediction

def main():
        st.title("Performance Predictor")
        schoollist = ["Select your school", "GP", "MS"]
        school = st.selectbox("School", schoollist)
        sexlist= ['F','M']
        sex = st.selectbox("Sex", sexlist)
        age = st.text_input("Age", "Type Here")
        addresslist=['U','R']
        address = st.selectbox("Address", addresslist)
        famsizelist=['LE3','GT3']
        famsize = st.selectbox("Family Size", famsizelist)
        Pstatuslist=['A','T']
        Pstatus = st.selectbox("Parental status", Pstatuslist)
        Medulist=['1','2','3','4']
        Medu = st.selectbox("Mother education", Medulist)
        Fedulist = ['1', '2', '3', '4']
        Fedu = st.selectbox("Father education", Fedulist)
        Mjoblist=['services','teacher','health','other','at_home']
        Mjob = st.selectbox("Mother Job", Mjoblist)
        Fjoblist = ['services', 'teacher', 'health', 'other', 'at_home']
        Fjob = st.selectbox("Father Job", Fjoblist)
        reasonlist=['course','reputation','home','other']
        reason = st.selectbox("Reason", reasonlist)
        guardianlist=['father','mother','other']
        guardian = st.selectbox("Guardian",guardianlist)
        travellist=['1','2','3','4']
        traveltime = st.selectbox("Travel time", travellist)
        studylist = ['1', '2', '3', '4']
        studytime = st.selectbox("Study time", studylist)
        failureslist=['0','1','2','3']
        failures = st.selectbox("failures", failureslist)
        yesorno=['yes','no']
        schoolsup = st.selectbox("School support", yesorno)
        famsup = st.selectbox("Family support", yesorno)
        paid = st.selectbox("Paid", yesorno)
        activities = st.selectbox("Activities", yesorno)
        nursery = st.selectbox("Nursery", yesorno)
        higher = st.selectbox("Higher Education", yesorno)
        internet = st.selectbox("Internet", yesorno)
        romantic = st.selectbox("Relationship", yesorno)
        famrellist=["1",'2','3','4','5']
        famrel = st.selectbox("Family relation",famrellist)
        freetime = st.selectbox("Free time", famrellist)
        goout = st.selectbox("Goes out", famrellist)
        Dalc = st.selectbox("Dalc", famrellist)
        Walc = st.selectbox("Walc", famrellist)
        health = st.selectbox("Health", famrellist)
        absences = st.text_input("Absences", "")
        annual_grades_avg = st.text_input("annual_grades_avg out of 20 ", "")
        result = ""
        if(st.button("Predict")):
            dict = { "school":school,"sex":sex,"age":age,"address":address,"famsize":famsize,"Pstatus":Pstatus
                     ,"Medu":Medu,"Fedu":Fedu,"Mjob":Mjob,"Fjob":Fjob,"reason":reason,"guardian":guardian,"traveltime":traveltime,
                     "studytime":studytime,"failures":failures,"schoolsup":schoolsup,"famsup":famsup,"paid":paid,
                     "activities":activities,"nursery":nursery,"higher":higher,"internet":internet,"romantic":romantic,
                     "famrel":famrel,"freetime":freetime,"goout":goout,"Dalc":Dalc,"Walc":Walc,"health":health,
                     "absences":absences,"annual_grades_avg":annual_grades_avg}
            df=pd.DataFrame(dict,index=[0])
            # result= performance_predictor(school, sex, age, address, famsize, Pstatus, Medu, Fedu,
            #            Mjob, Fjob, reason, guardian, traveltime, studytime,
            #            failures, schoolsup, famsup, paid, activities, nursery,
            #            higher, internet, romantic, famrel, freetime, goout, Dalc,
            #            Walc, health, absences, annual_grades_avg)
            result= performance_predictor(df)
        st.success("The evaluation is {}".format(result))

if __name__=='__main__':
    main()
