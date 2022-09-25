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
        school = st.text_input("School","")
        sex = st.text_input("Sex", "")
        age = st.text_input("Age", "")
        address = st.text_input("Address", "")
        famsize = st.text_input("Family Size", "")
        Pstatus = st.text_input("Parental status", "")
        Medu = st.text_input("Mother education", "")
        Fedu = st.text_input("Father education", "")
        Mjob = st.text_input("Mother Job", "")
        Fjob = st.text_input("Father Job", "")
        reason = st.text_input("Reason", "")
        guardian = st.text_input("Guardian", "")
        traveltime = st.text_input("Travel time", "")
        studytime = st.text_input("Study time", "")
        failures = st.text_input("failures", "")
        schoolsup = st.text_input("School support", "")
        famsup = st.text_input("Family support", "")
        paid = st.text_input("Paid", "")
        activities = st.text_input("Activities", "")
        nursery = st.text_input("Nursery", "")
        higher = st.text_input("Higher Education", "")
        internet = st.text_input("Internet", "")
        romantic = st.text_input("Relationship", "")
        famrel = st.text_input("Family relation", "")
        freetime = st.text_input("Free time", "")
        goout = st.text_input("Goes out", "")
        Dalc = st.text_input("Dalc", "")
        Walc = st.text_input("Walc", "")
        health = st.text_input("Health", "")
        absences = st.text_input("Absences", "")
        annual_grades_avg = st.text_input("annual_grades_avg", "")
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
        st.success("The evaluation is {}".format(result.np()))

if __name__=='__main__':
    main()
