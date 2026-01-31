## Student_ExamPerformance_Indicator
<!--git add README.md
git commit -m "Message"
git status
git branch -M main

git remote add origin https://github.com/Azhagammai/DS_End_To_End_Project.git
git remote -v
# then push 
git push -u origin main

# if you first  time you go to the 
# git configuration and then do a two step command

# change my email id use this command
git config --global user.email "new.email"

# update my changes use 
git pull


# install 
pip install requirements.txt

-e . is indicate the setup.py then all the package was installed successfully

-- that create the folder called 
DSProject.egg-info


git add .

git status - shows which are added 

git commit -m "message"

git push -u origin main


create a components folder inside the src

- data_ingestion.py
- data_transformation.py
- model_trainer.py

create a pipeline folder
- train_pipeline.py
- predict_pipeline.py 
- __init__.py

inside the src folder
-- logger.py
-- exception.py
-- utils.py


# Project - Student performer indicater

- notebook folder setup 

# Data ingestion
- data_ingestion.py

# install the .dotenv
pip install python-dotenv


- run on the command prompt then it will create the arti  folder - it combine and run the utils.py


# Data Transformtion 
- data_transformation.py 

# data utils
- utils.py

# model training and evaluation

- model_trainer.py
-->

# 🔄 Project Workflow

## 1️⃣ Data Collection
- Load dataset from CSV file
- Understand dataset structure
- Identify features and target variable

## 2️⃣ Data Preprocessing
- Handle missing values
- Encode categorical variables
- Apply feature scaling
- Create preprocessing pipeline

## 3️⃣ Model Training
- Split dataset into training and testing sets
- Train machine learning model
- Evaluate model performance
- Select the best-performing model

## 4️⃣ Model Saving
- Save trained model using pickle
- Save preprocessing pipeline

## 5️⃣ Web Application Integration
- Create frontend using HTML and CSS
- Develop backend using Flask
- Load trained model and preprocessor
- Connect user input to prediction logic

## 6️⃣ Prediction Output
- Accept user input from web form
- Process input using preprocessing pipeline
- Generate prediction
- Display result on the webpage

---

# ⚙️ Prerequisites

Make sure the following are installed:

- Python 3.8 or above
- pip (Python package manager)
- Virtual Environment (recommended)

---

# 📦 Required Libraries

Install required dependencies:

- pandas
- numpy
- scikit-learn
- flask
- matplotlib
- seaborn
- pickle

You can install all dependencies using:

```bash
pip install -r requirements.txt
````

Or install manually:

```bash
pip install pandas numpy scikit-learn flask matplotlib seaborn
```

---

# 📂 Project Structure

```
DS_End_To_End_Project/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── templates/
│   ├── index.html
│
├── static/
│   ├── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run the Project

## Step 1: Extract or Clone the Project

If using ZIP file:

* Extract `Student_ExamPerformance-Indicator-main.zip`

If using Git:

```bash
git clone <repository_url>
cd Student_ExamPerformance-Indicator
```

---

## Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Run the Application

```bash
python app.py
```

---

# 🌐 Access the Web Application

After running `app.py`, open your browser and visit:

```
http://localhost:5000/predictdata
```

OR

```
http://127.0.0.1:5000/predictdata
```

If HTTPS is configured:

```
https://localhost/predictdata
```

---

# 📁 Important File Paths

## 🟢 Main Application File

```
app.py
```

## 🟢 Trained Model File

```
artifacts/model.pkl
```

## 🟢 Preprocessor File

```
artifacts/preprocessor.pkl
```

## 🟢 HTML Template

```
templates/index.html
```

## 🟢 CSS File

```
static/style.css
```

---

# Application Output
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/37395bb3-71dd-4b32-a405-f4d45fe97685" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c40e6725-85c7-4f45-b2f7-837341b928e0" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4b030525-8da3-4174-bf02-3053ade1dd15" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/225cf447-5b62-457e-851d-630aabe310ef" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b4499b57-7ebb-4858-8039-85e6ccd545fb" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ea70ddda-18d2-46f8-b36a-839f46b72508" />

---

# 🧠 Machine Learning Model

* Built using scikit-learn
* Includes preprocessing pipeline
* Trained on structured dataset
* Saved using pickle
* Integrated with Flask backend

---

# 🚀 Future Improvements

* Deploy to cloud platforms (AWS / Render / Railway)
* Add Docker containerization
* Improve frontend UI design
* Add logging and monitoring
* Implement automated model retraining pipeline

---
