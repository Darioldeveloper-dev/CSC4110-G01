# CSC 4110 Group G01: Student Performance Factors

Kibabii University, CSC 4110 Machine Learning. We built and tested two models for Elimu Bora Trust on the public Student Performance Factors dataset: one predicts a student's exam score, the other suggests which students to invite for a mentorship scholarship interview (score of 70 or more).

## Public app
**https://REPLACE-WITH-YOUR-APP-NAME.streamlit.app**  (replace after deploying on Streamlit Community Cloud)

## Who owned each task
| Task | Content | Owner |
|---|---|---|
| 1 | Set-up and data | Whole group |
| 2.1 | Data inspection and cleaning | Dariol Temko (COM/0048/23) |
| 2.2 | Transformation, EDA and split | Raphael Wanyama (COM/0019/23) |
| 3.1 | Linear regression and gradient descent | Elisha Eddie (COM/0066/23) |
| 3.2 | Polynomial and regularised regression | Abdul Razak (COM/0032/23) |
| 4 | Classification | Emmanuel Rotich (COM/0043/23) |
| 5 | Model evaluation and selection | Elisha Eddie |
| 6 | Decision trees and ensembles | Emmanuel Rotich |
| 7 | Unsupervised and reinforcement learning | Dariol Temko |
| 8 | Neural networks | Raphael Wanyama |
| 9.1 | Model packaging and web app | Abdul Razak |
| 9.2 | Responsible AI and model card | Whole group |
| 9.3 | Publishing | Whole group |

## How to run the notebooks
1. Open the Google Drive folder CSC4110_G01 and add a shortcut to My Drive, so that /content/drive/MyDrive/CSC4110_G01 exists in Colab.
2. Open a notebook with Google Colaboratory, choose Runtime > Restart session and run all.
3. Run them in task order: each task reads files saved by the earlier ones (data/stage1_students.csv, data/clean_students.csv, models/G01_model.joblib).

## How to run the app
    pip install -r app/requirements.txt
    streamlit run app/app.py

## What the app does, for a school principal
The app is like a careful second opinion for the scholarship list. A teacher types in six things about a student: hours of study each week, attendance, the last exam score, and how motivated, supported at home and well-resourced the student is. The app answers with a percentage chance that the student will score 70 or more and says whether to invite them for an interview. It was built on a public dataset, not on your pupils, so treat it as a help for your own judgement and never as a reason to lower expectations for any student.

## Project folders
data, notebooks, models, outputs, app, tests, report. Run python tests/smoke_test.py to check that the saved model loads and predicts.
