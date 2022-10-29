PROBLEM STATEMENT:

The biggest challenge with heart disease is detecting it. Instruments are available that can predict heart disease, but they are expensive or inefficient at estimating the likelihood of heart disease in humans. Early detection of heart disease can reduce mortality and overall complications. However, it is not possible to closely monitor patients every day in all cases, and 24-hour consultation of a patient by a doctor is not available because it requires more intelligence, time and experience. Since we now have a significant amount of data around the world, we need to be able to use various machine learning algorithms to analyze the data for hidden patterns. Hidden patterns can be used for health diagnostics in medical data.

Attributes:

1. age - age in years

2. gender - (1 = male; 0 = female)

3. cp - chest pain type

    0: Typical angina: chest pain related decrease blood supply to the heart
  
    1: Atypical angina: chest pain not related to heart
  
    2: Non- angina pain: typically esophageal spasms (non heart related)
  
    3: Asymptomatic: chest pain not showing signs of disease

4. trestbps - resting blood pressure (in mm Hg on admission to the hospital) anything above 130-140 is typically cause for concern

5. chol - serum cholesterol in mg/dl

    serum = LDL + HDL + .2 * triglycerides
  
    above 200 is cause for concern

6. fbs - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

    '>126' mg/dL signals diabetes

7. restecg - resting electrocardiographic results

    0: Nothing to note
  
    1: ST-T Wave abnormality
  
      can range from mild symptoms to severe problems
    
      signals non-normal heart beat
    
    2: Possible or definite left ventricular hypertrophy
  
      Enlarged heart's main pumping chamber

8. thalach - maximum heart rate achieved

9. exang - exercise induced angina (1 = yes; 0 = no)

10. ca - number of major vessels (0-3) colored by fluoroscopy

    colored vessel means the doctor can see the blood passing through
  
    the more blood movement the better (no clots)

