# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:58:58 2020

@author: sbsap
"""

import glassdoor_scraper as gs 
import glassdoor_scraper2 as gs2
import pandas as pd 

path ='C:/Users/sbsap/Documents/Jupyter/Salary/chromedriver'
wait_time= 5
num=100
job_title1 = 'software developer' 
job_title2 = 'data scientist'
job_title3 = 'full stack developer'
job_title4 = 'UI/UX Designer' 
job_title5 = 'Project Manager' 
job_title6 = 'Database'
job_title7 = 'Systems Engineer'

#First method (Range)
df = gs.get_jobs(job_title7,num,False,path,wait_time)
df.to_csv(r'C:/Users/sbsap/Documents/Jupyter/Salary/sys1.csv', index = False) 

#Second method (Fixed)
df2 = gs2.get_jobs(job_title7,num,False,path,wait_time) 
df2.to_csv(r'C:/Users/sbsap/Documents/Jupyter/Salary/sys2.csv',index=False)        

