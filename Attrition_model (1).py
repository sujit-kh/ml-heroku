#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Attrition_model = pickle.load(open('model_file.pkl', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Employee Attrition Prediction System',
                          
                          ['Attrition Prediction'],
                          icons=['person'],
                          default_index=0)
    
    
# Employee Attrition Prediction Page
if (selected == 'Attrition Prediction'):
    
    # page title
    st.title('Employee Attrition Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        Age = st.text_input('Number of Age')
        
    with col2:
        Attrition = st.text_input('Attrition')
    
    with col3:
        BusinessTravel = st.text_input('BusinessTravel')
    
    with col4:
        DailyRate = st.text_input('DailyRate')
    
    with col1:
        Department = st.text_input('Department')
    
    with col2:
        Education = st.text_input('Education')
    
    with col3:
        EducationField = st.text_input('EducationField')
    
    with col4:
        EnvironmentSatisfaction = st.text_input('EnvironmentSatisfaction')
    
    with col1:
        Gender = st.text_input('Gender')
        
    with col2:
        HourlyRate = st.text_input('HourlyRate')
    
    with col3:
        JobInvolvement = st.text_input('JobInvolvement')
    
    with col4:
        JobLevel = st.text_input('JobLevel')
    
    with col1:
        JobSatisfaction = st.text_input('JobSatisfaction')
    
    with col2:
        MaritalStatus = st.text_input('MaritalStatus')
    
    with col3:
        MonthlyIncome = st.text_input('MonthlyIncome')
    
    with col4:
        MonthlyRate = st.text_input('MonthlyRate')
    
    with col1:
        NumCompaniesWorked = st.text_input('NumCompaniesWorked')
        
    with col2:
        OverTime = st.text_input('OverTime')
    
    with col3:
        PercentSalaryHike = st.text_input('PercentSalaryHike')
    
    with col4:
        PerformanceRating = st.text_input('PerformanceRating')
    
    with col1:
        RelationshipSatisfaction = st.text_input('RelationshipSatisfaction')
    
    with col2:
        TotalWorkingYears = st.text_input('TotalWorkingYears')
    
    with col3:
        TrainingTimesLastYear = st.text_input('TrainingTimesLastYear')
    
    with col4:
        WorkLifeBalance = st.text_input('WorkLifeBalance')
        
    with col1:
        YearsAtCompany = st.text_input('YearsAtCompany')
    
    with col2:
        YearsInCurrentRole = st.text_input('YearsInCurrentRole')
    
    with col3:
        YearsSinceLastPromotion = st.text_input('YearsSinceLastPromotion')
    
    with col4:
        YearsWithCurrManager = st.text_input('YearsWithCurrManager')
    
    # code for Prediction
    Attrition_pred = ''
    
    # creating a button for Prediction
    
    if st.button('Attrition Test Result'):
        Attr_pred = Attrition_model.predict([[Age, Attrition, BusinessTravel, DailyRate, Department, 
                                              DistanceFromHome, Education, EducationField, EnvironmentSatisfaction, 
                                              Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, 
                                              JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, 
                                              NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, 
                                              RelationshipSatisfaction, TotalWorkingYears, TrainingTimesLastYear, 
                                              WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, 
                                              YearsSinceLastPromotion, YearsWithCurrManager]])
        
        if (Attr_pred[0] == 1):
          Attrition_pred = 'The person will left the company'
        else:
          Attrition_pred = 'The person will stay in company'
        
    st.success(Attrition_pred)


# In[2]:


pip install streamlit


# In[4]:


pip install pickle-mixin


# In[3]:


pip install option_menu

