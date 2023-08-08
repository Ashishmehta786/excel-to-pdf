# importing all the libraries 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image
from IPython.display import display

# reading the dataset and cleaning it 
df=pd.read_excel(r"C:\Users\Tanishqa\Desktop\project2\query_result.xlsx")
df=df[["Child_booking_id","customer_age","customer_gender","test_name","lower_bound_female","lower_bound_male","upper_bound_male",	"upper_bound_female","Reported_Value"]]
df=df.dropna().reset_index(drop=True)

def Liver():
        list1=["Bilirubin Total", "Direct & Indirec","SGOT","SGPT","SGOT/SGPT Ratio","ALP","GGT","Total Protein" ,"Albumin,Globulin","A/G Ratio"]
        major_function=["Aids in detoxification by metabolizing drugs, alcohol, and toxins, facilitating their elimination from the body.",
"Responsible for producing bile, which aids in the digestion and absorption of fats in the small intestine.",
"Liver plays a role in the production of blood-clotting proteins, including factors essential for the coagulation process.",
"Vital for metabolizing carbohydrates, proteins, and fats. It stores and releases glucose, converts amino acids into proteins, and synthesizes cholesterol and triglycerides."]

        image_path =r"C:\Users\Tanishqa\Desktop\project2\liver.png"
        img = Image.open(image_path)

        causes=["Function can be impaired by medications, toxins, and chemicals.",
"Liver dysfunction can result from viral infections like hepatitis B, C, and E."
"genetic and inherited conditions."]
        return list1,major_function,causes,img 

def Thyroid():
    list1=["Calcium","T3","T4","FT3","FT4","VitB12","Vit D","Anti Thyroid Peroxidase Antibodies (TPO)","TSH 3rd Generation","TSH Receptor Antibody","Anti Thyroglobulin Antibodies (ATG)"]
    major_function=["The thyroid gland produces hormones that regulate metabolism, influencing energy utilization and various bodily functions.",
"plays a vital role in growth and development, ensuring normal development of organs, brain, and skeletal system.",
"regulates heart rate, blood vessel function, and cardiovascular health, ensuring proper blood circulation.",
"impact brain function, cognitive processes, mood regulation, and mental well-being by influencing development and activity."]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\tyroid.png"
    img = Image.open(image_path)
    
    causes=["Thyroiditis, inflammation of the thyroid gland, can result from infections, autoimmune disorders, or radiation exposure.",
"Genetic mutations and family history can elevate the risk of thyroid dysfunction.",
"Autoimmune disorders, like Hashimoto's thyroiditis and Graves' disease, disrupt thyroid function."]

    return list1,major_function,causes,img 

def Diabetes():
    list1=["HbA1C","Glucose Fasting (BSF)","Glucose Post Prandial (BSPP)","Glucose Random (BSR)"]
    major_function=["Provide energy to all the cell for their smooth functioning.",
"Excess blood sugar will produce excess insulin, ofsetting pancreas and will eventually lead to insulin resistance",
"Excess blood sugar will glycate all your organs leading them to perform suboptimal, ending up in multiple organ failure.",
"Releases insulin and glucagon into the bloodstream to regulate blood sugar levels: insulin lowers, while glucagon raises it."]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\diabetes.jpg"
    img = Image.open(image_path)
    
    causes=["Family history and genetics may increase diabetes risk, but not guaranteed.",
"Unhealthy habits like poor diet, inactivity, obesity, and stress increase diabetes risk.",
"Diabetes risk rises with age, especially after reaching 45 years old."]
    return list1,major_function,causes,img 

def Kidney():
    list1=["Urea","Bun","Creatinine","Bun/Creatinine Ratio","Urea/Creatinine Ratio","Uric Acid","Calcium","Phosphorus","Sodium","Potassium","Chloride"]
    major_function=["The kidneys filter the blood to remove waste products and excess substances..","The kidneys maintain the body's water balance by adjusting the amount of water reabsorbed or excreted","The kidneys eliminate waste and toxins from the body through urine production."," The kidneys produce hormones, such as erythropoietin, which regulates red blood cell production and helps maintain blood pressure."]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\kidney.jpg"
    img = Image.open(image_path)
    
    causes=["High blood pressure puts additional burden on the kidneys","Diabetes can lead to kidney damage due to high blood sugar.","Polycystic kidney disease can cause kidney damage and eventual failure."]
    return list1,major_function,causes,img 

def Lipid_Cholestrol():
    list1=["Total Cholesterol","Triglycerides","LDL Cholesterol (Calculated)","HDL Cholesterol","Non HDL Cholesterol","CHOL/HDL Ratio","HDL/LDL Ratio","LDL/HDL Ratio"]
    major_function=["Precursor of Vitamins and hormones",
"prolong the digestion by slowing down the secretion of stomach acid",
"Cholesterol maintains cell membrane stability and fluidity.",
"Transports and stores metabolic fuels"]

    image_path =r"C:\Users\Tanishqa\Desktop\project2\lipid.png"
    img = Image.open(image_path)
    
    causes=["A diet heavy in saturated and trans fats, cholesterol, and processed foods can all lead to elevated cholesterol. ",
"Cholesterol levels can be reduced by an overactive thyroid gland.",
"Inherited factors can make some individuals more prone to high cholesterol."]
    return list1,major_function,causes,img 

def Vitamin_B12():
    list1=["Vitamin B12 / Cyanocobalamin"]
    major_function=[" Vital for nervous system, myelin production, cognition, memory, brain health.",
"Crucial for nucleotide production, cell division, and growth of healthy cells.",
"Cofactor in methylation for gene regulation, protein synthesis, detoxification.",
"Essential for red blood cells, DNA synthesis, anemia prevention."]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\vitaminB12.jpg"
    img = Image.open(image_path)
    
    causes=["Medical conditions(anemia, gastrointestinal disorders, surgery)",
"Common in strict vegetarians or vegans lacking animal-derived sources.",
"Medications and treatments (e.g., PPIs, metformin, weight loss surgeries)."
]
    return list1,major_function,causes,img 
 
def Vitamin_D25():  
    list1=["Vitamin D 25 Hydroxy"]
    major_function=["aids calcium absorption, supporting bone health and mineralization.",
"assists immune system regulation, enhancing immune function and responses.",
"plays a role in cell growth, differentiation, and regulating cellular processes in the body."
"Studies indicate that vitamin D might help prevent colorectal, breast, and prostate cancer"]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\vitamin_d.jpg"
    img = Image.open(image_path)
    
    causes=["Insufficient sun exposure hampers vitamin D25 synthesis, causing deficiency risks.",
"Digestive disorders hinder vitamin D25 absorption, raising deficiency concerns.",
"Malfunctioning kidneys or liver impede vitamin D25 activation, causing potential deficiency."]
    return list1,major_function,causes,img 

def Iron():
    list1=["Iron","TIBC","UIBC","% Saturation","Transferrin","Ferritin"]
    major_function=["Improves hemoglobin, helps in circulating oxygen throughout the body",
                    "Ensure healthy pregnancy",
"Provide energy to cells to perform essentials tasks.",
"Intensifies brain function, memory & concentration"]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\iron.png"
    img = Image.open(image_path)
    
    causes=["Blood loss(menstrual bleeding, or injury)",
"Regular use of pain relievers, such as aspirin",
"Diets low in iron"]   
    return list1,major_function,causes,img 

def Bone_Care():
    list1=["Alkaline Phosphatase (ALP)","Calcium Ionized","Beta Crosslaps (Beta Ctx) (Ctx-1)","Alkaline Phosphatase (ALP) Isoenzymes","Alkaline Phosphatase (ALP) With Bone Fraction","Osteocalcin","Covid-19 RT PCR","Covid-19 IgG Antibody"]
    major_function=["Supporting strong bones and teeth, providing structural integrity.",
"Assisting in muscle contraction, enabling movement and coordination.",
"Aiding in nerve function, allowing for proper communication between cells.",
"Facilitating blood clotting to prevent excessive bleeding when injured."]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\bones.png"
    img = Image.open(image_path)
    
    causes=["Inadequate intake of calcium and vitamin D can weaken bones."
"aging and hormonal shifts can lead to decreased bone density.",
"Unhealthy habits like lack of exercise and smoking can negatively impact bone health."]
    return list1,major_function,causes,img 

def Cardiac_Care():
    list1=["LPT High Sensitivity C-Reactive Protein (Hs-CRP)","Creatine Phosphokinase (CPK)","Triglycerides","Creatine Phosphokinase MB (CPK MB)"]
    major_function=["pumping blood to supply oxygen and nutrients to tissues.",
"Regulating blood pressure to maintain circulation.",
"Facilitating gas exchange for oxygenation in the lungs.",
"Coordinating blood flow with rhythmic contractions."]
    image_path =r"C:\Users\Tanishqa\Desktop\project2\heart.png"
    img = Image.open(image_path)
    
    causes=["Unhealthy lifestyle choices, including poor diet, lack of exercise, smoking, and excessive alcohol consumption.",
"High blood pressure (hypertension), which strains the heart and blood vessels."
"High cholesterol levels, specifically elevated LDL cholesterol, which can lead to plaque buildup in arteries."]
    return list1,major_function,causes,img 

names=["Kidney","Vitamin_B12","Lipid_Cholesterol","Diabetes","Iron","Vitamin_D25","Liver","Thyroid","Cardiac_Care" ,"Bone_Care"]
print(names)
disease = input("Select: ")
chosen = globals().get(disease)
result = chosen()
list1, major_function, causes, img = result
print("List1:", list1)
print("Major Functions:", major_function)
print("Causes:", causes)
display(img)

# main file containing the unhealthy record aggregate of all the test 
unhealthy_records = pd.DataFrame(columns=["Child_booking_id", "customer_age", "customer_gender"])

# Dictionary to track whether a person is unhealthy based on their child_booking_id
unhealthy_dict = {}
total_female_count=0
total_male_count=0
unique_male_ids = set()
unique_female_ids = set()
age_group_total=[]


def filtered(test1):
    #to access the local variables  
    global unique_male_ids
    global unique_female_ids
    global unhealthy_records 
    global age_group_total
    count=1
    
    #filtering data only for the specific  test 
    filtered_data = df[df['test_name'].str.lower() == test1].copy()
    
    #changing the values into the numeric form 
    numeric_cols = ['upper_bound_male', 'lower_bound_male', 'upper_bound_female', 'lower_bound_female', 'Reported_Value']
    filtered_data[numeric_cols] = filtered_data[numeric_cols].apply(pd.to_numeric)
    
    #only selecting the male data to set unhealthy column 
    male_conditions = (filtered_data["customer_gender"] == "male")
    filtered_data.loc[male_conditions, "unhealthy"] = (filtered_data['Reported_Value'] < filtered_data['lower_bound_male']) | (filtered_data['Reported_Value'] > filtered_data['upper_bound_male'])

    # Conditions for Female
    female_conditions = (filtered_data["customer_gender"] == "female")
    filtered_data.loc[female_conditions, "unhealthy"] = (filtered_data['Reported_Value'] < filtered_data['lower_bound_female']) | (filtered_data['Reported_Value'] > filtered_data['upper_bound_female'])
    if count==1:

        newdf=filtered_data.copy()
        age_bins = [18, 31, 41, 51, float('inf')]
        age_labels = ['18-30', '30-40', '40-50', '50+']
        newdf['Age_Group'] = pd.cut(newdf['customer_age'], bins=age_bins, labels=age_labels, right=False)
        age_group_total = newdf['Age_Group'].value_counts().sort_index()       
        
    #checking if the child id is in unhealthy record or not if no then adding it 
    for index, row in filtered_data.iterrows():
        child_booking_id = row['Child_booking_id']
        if child_booking_id not in unhealthy_dict:
            if row['unhealthy']:
                unhealthy_dict[child_booking_id] = True
                new_record = pd.DataFrame({"Child_booking_id": [row["Child_booking_id"]], 
                                           "customer_age": [row["customer_age"]],
                                           "customer_gender": [row["customer_gender"]]})
                unhealthy_records = pd.concat([unhealthy_records, new_record], ignore_index=True)   
    unique_male_ids.update(filtered_data.loc[male_conditions, "Child_booking_id"])
    unique_female_ids.update(filtered_data.loc[female_conditions, "Child_booking_id"])


for test in list1:
    if test.lower() in df["test_name"].str.lower().values:
        filtered(test.lower())
        index1 = list1.index(test)     
    else:
        print(f"{test.lower()} not found in DataFrame.")
        
output_file_path = "C:/Users/Tanishqa/Desktop/project2/filtered.xlsx"
unhealthy_records.to_excel(output_file_path, index=False)
total_male_count = len(unique_male_ids)
total_female_count = len(unique_female_ids) 
print(total_male_count+total_female_count)

def gender_plot(total_male_count, total_female_count):
    global male_data,female_data
    male_data = unhealthy_records["customer_gender"].eq("male").sum()
    female_data=unhealthy_records["customer_gender"].eq("female").sum()
    genders = ["Male", "Female"]
    counts = [male_data, female_data]
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(genders, counts, color=['blue', 'pink'])

    plt.xlabel('Gender')
    plt.ylabel('Split by Gender')
    plt.title('Need Attention Bucket ')
    
    # Adding count numbers above each bar
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, str(counts[i]), ha='center', va='bottom')
        percent = (counts[i] / total_male_count) * 100 if i == 0 else (counts[i] / total_female_count) * 100
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percent:.2f}%', ha='center', va='top')
    
    # Creating the legend
    plt.text(0, -0.2, f"Male:({percent:.2f}%)", color='blue', transform=plt.gca().transAxes)
    plt.text(0, -0.25, f"Female: ({percent:.2f}%)", color='pink', transform=plt.gca().transAxes)
    plt.show()

def age_plot():
    age_bins = [18, 31, 41, 51, float('inf')]
    age_labels = ['18-30', '30-40', '40-50', '50+']
    unhealthy_records['Age_Group'] = pd.cut(unhealthy_records['customer_age'], bins=age_bins, labels=age_labels, right=False)

    # Count the number of occurrences in each age group
    age_group_counts = unhealthy_records['Age_Group'].value_counts().sort_index()
    percentage_unhealthy_age = (age_group_counts / age_group_total) * 100
    plt.figure(figsize=(8, 6))
    ax = age_group_counts.plot(kind='bar', color='orange')
    ax.set_xlabel('Age Bracket')
    ax.set_ylabel('Split By Age ')
    ax.set_title('Need Attention Bucket ')

    # Add text annotations for numbers and percentages on the bars
    for i, v in enumerate(age_group_counts):
        ax.text(i, v, f"{v} ({percentage_unhealthy_age[i]:.1f}%)", ha='center', va='bottom')

    plt.show()



def total():

    # Data for the pie chart
    categories = ["Healthy","Unhealthy"]
    values = [(total_male_count+total_female_count)-(male_data+female_data),male_data+female_data]
    colors = ['red', 'green']

    # Create a pie chart
    plt.figure(figsize=(8, 8))  # Optional: Set the size of the figure

    # Plot the pie chart
    plt.pie(values, labels=categories, colors=colors, autopct=lambda p: '{:.0f}'.format(p * sum(values) / 100))

    # Add a title
    plt.title('Sample Pie Chart')

    # Display the chart
    plt.show()
male_data=0
female_data=0
age_plot()
gender_plot(total_male_count, total_female_count)
total()
