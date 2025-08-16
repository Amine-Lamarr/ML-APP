<h1>this is a Machine learning Application about predicing your phone addiction depending on input features</h1>

<h2>models used:</h2>
<p>
  LIGHTgbm : 
  best score : 91.81%
  mae : 0.049
  mse : 0.005
----------------------
  XGBoost : 
  best score : 91.03%
  mae : 0.054
  mse : 0.006
</p>

<h2>concepts :</h2>
<p>
  1 . Downloading the data "teen_phone_addiction_dataset.csv" from kaggle .
  2 . data cleaning (feature enginnering, encoding, scaling, droping useless columns...) .
  3 . training two boosting models (lightGBM | XGBoost) .
  4 . plotting the results , accuracies using matplotlib , seaborn .
  5 . saving the best model .
  6 . creating another application file "app.py" .
  7 . i used streamlit to build that web app . 
  8 . the user fills in the inputs and the model gives how much the user addicted out of ten
</p>
<h2>how to run the code :</h2>

<p>
  1 . open the terminal or the command "win + R" or "Mac + R".
  2 . enter to the folder path 'cd folder_path'.
  3 . run the app with this command -> "streamlit run app.py"
  4 . there you go .
</p>
