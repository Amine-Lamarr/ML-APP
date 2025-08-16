<h1 style="color:#2c3e50; text-align:center; font-family:Arial, sans-serif; background:#ecf0f1; padding:15px; border-radius:10px;">
  this is a Machine learning Application about predicing your phone addiction depending on input features
</h1>

<h2 style="color:#e74c3c; font-family:Verdana, sans-serif; background:#fdecea; padding:8px; border-radius:6px;">
  models used:
</h2>
<p>
  LIGHTgbm : <br>
  best score : 91.81%<br>
  mae : 0.049<br>
  mse : 0.005<br>
----------------------<br>
  XGBoost : <br>
  best score : 91.03%<br>
  mae : 0.054<br>
  mse : 0.006<br>
</p>

<h2 style="color:#27ae60; font-family:Verdana, sans-serif; background:#eafaf1; padding:8px; border-radius:6px;">
  concepts :
</h2>
<p>
  1 . Downloading the data "teen_phone_addiction_dataset.csv" from kaggle . <br>
  2 . data cleaning (feature enginnering, encoding, scaling, droping useless columns...) .<br>
  3 . training two boosting models (lightGBM | XGBoost) . <br>
  4 . plotting the results , accuracies using matplotlib , seaborn .<br>
  5 . saving the best model .<br>
  6 . creating another application file "app.py" .<br>
  7 . i used streamlit to build that web app . <br>
  8 . the user fills in the inputs and the model gives how much the user addicted out of ten.<br>
</p>

<h2 style="color:#2980b9; font-family:Verdana, sans-serif; background:#eaf2fb; padding:8px; border-radius:6px;">
  how to run the code :
</h2>
<p>
  1 . open the terminal or the command "win + R" or "Mac + R".<br>
  2 . enter to the folder path 'cd folder_path'.<br>
  3 . run the app with this command -> "streamlit run app.py"<br>
  4 . there you go .
</p>
