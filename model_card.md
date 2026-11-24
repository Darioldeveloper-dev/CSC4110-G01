# Model card: scholarship nomination helper (Group G01)

## Model purpose
Estimate the probability that a secondary-school student scores 70 or more in the examination (high_score = 1), so that Elimu Bora Trust can shortlist students for a mentorship scholarship interview.

## Intended users
Elimu Bora Trust programme staff and teachers in the 40 partner schools in Bungoma County. The output supports a human decision; it does not replace it.

## Data source and licence
Student Performance Factors, a public dataset of 6,607 student records (20 columns). Owner, link, licence and download date are recorded in the Task 1 notebook (G01_T01_setup.ipynb). The data is not from Elimu Bora schools, so the model has not yet been tested on them.

## Features used
Hours_Studied, Attendance, Previous_Scores, Motivation_Level, Parental_Involvement, Access_to_Resources. Exam_Score is not a feature. No personal identifier is used (flagged names: none). No candidate feature has a correlation above 0.95 with the target (largest: effort, 0.58).

## Performance on test data
Logistic regression on 1,322 held-out students (20% stratified split, random_state=42), decision threshold 0.3:
accuracy 0.902, precision 0.771, recall 0.858, F1 0.812, AUC 0.950.

## Fairness check results
Recall for high_score = 1 by group (test rows in brackets):
- Gender = Female: recall 0.850 (555 students, 127 high scorers)
- Gender = Male: recall 0.864 (767 students, 198 high scorers)
- School_Type = Private: recall 0.851 (412 students, 101 high scorers)
- School_Type = Public: recall 0.862 (910 students, 224 high scorers)
Largest gap within an attribute: Gender (0.013).

## Limitations
- Trained on a public dataset, not on Bungoma County schools; scores may differ there.
- Uses six inputs only, so it is less accurate than a model using all 20 columns.
- Precision at threshold 0.3 is 0.77: some students flagged will not reach 70.
- Past performance and attendance dominate the prediction, so late improvers can be missed.
- Self-reported inputs (hours studied, motivation) may be inaccurate.

## Who should not use the model
Anyone who wants to decide a student's grade, placement, discipline or fees; anyone using it on a different age group or curriculum without re-testing; anyone using it as the only basis for refusing a scholarship.

## Testing before release
- Test set: the 1,322 held-out students above, never used for training or tuning.
- Scores the model must reach: recall of at least 0.80 for high_score = 1 overall and in every Gender and School_Type group, and AUC of at least 0.90.
- Pilot: a small group of Trust staff and two or three volunteer schools use the app first, and their teachers compare its suggestions with their own shortlist before any wider release.

## Rule for schools
The model must never be used to lower expectations for any student: a low probability is not a reason to withhold support, teaching time or encouragement.
