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
        sex = st.text_input("Sex", "Type Here")
        age = st.text_input("Age", "Type Here")
        address = st.text_input("Address", "Type Here")
        famsize = st.text_input("Family Size", "Type Here")
        Pstatus = st.text_input("Parental status", "Type Here")
        Medu = st.text_input("Mother education", "Type Here")
        Fedu = st.text_input("Father education", "Type Here")
        Mjob = st.text_input("Mother Job", "Type Here")
        Fjob = st.text_input("Father Job", "Type Here")
        reason = st.text_input("Reason", "Type Here")
        guardian = st.text_input("Guardian", "Type Here")
        traveltime = st.text_input("Travel time", "Type Here")
        studytime = st.text_input("Study time", "Type Here")
        failures = st.text_input("failures", "Type Here")
        schoolsup = st.text_input("School support", "Type Here")
        famsup = st.text_input("Family support", "Type Here")
        paid = st.text_input("Paid", "Type Here")
        activities = st.text_input("Activities", "Type Here")
        nursery = st.text_input("Nursery", "Type Here")
        higher = st.text_input("Higher Education", "Type Here")
        internet = st.text_input("Internet", "Type Here")
        romantic = st.text_input("Relationship", "Type Here")
        famrel = st.text_input("Family relation", "Type Here")
        freetime = st.text_input("Free time", "Type Here")
        goout = st.text_input("Goes out", "Type Here")
        Dalc = st.text_input("Dalc", "Type Here")
        Walc = st.text_input("Walc", "Type Here")
        health = st.text_input("Health", "Type Here")
        absences = st.text_input("Absences", "Type Here")
        annual_grades_avg = st.text_input("annual_grades_avgstra", "Type Here")
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
        st.success("The output is {}".format(result))

if __name__=='__main__':
    main()