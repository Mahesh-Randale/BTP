Sign Language Recogntion System

We have used Convolutional Neural Networks for creating model.

Our proposed solution consists of four main steps:

• Dataset Creation

• Image Pre-processing

• Training CNN Model

• Creating a GUI
To achieve a 2-way communication between deaf people and normal people,
we have added following features to the system:
• Sign to Speech conversion
• Speech to Sign Conversion
• Word Suggestion and Correction

We have also created Desktop Application using "Tkinter" and a Web Application using "Streamlit". You can deploy web app on streamlit.io.


---------------------Usage--------------------
1. Requirements
There are 2 requirements file , one for Desktop application and one for Web app

Install th e requiements using following command:
pip install -r <requirement file>

2. Dataset Creation:
After installing the requirements , run "create_dataset.py" . 
Make sure to create the directories for training and testing dataset and internal directories for each character in both directories beforehand.
Also , change the path inside code to your directory path.

Once , all above steps are done ,run the code , adjust the hand in Region of Interest(A Square) and press "spacebar" . The images saving process will start. Make sure to change pose to create a variety of different angles for each image.

3. Model training: Once dataset is created , you can run "canny_edge_model.py" to train your model. We have used Google colab for training the model. You can use either your machine or Colab(you can use GPU which will decrease your training time). For working with colab , upload the dataset in your drive and access data from there.

I have included the pretrained models in "model" folder.

4. Desktop Application:
Once the models are trained , run "App.py" . It will take some time on first time. You can also make your own GUI using "Tkinter".

Features included in  Desktop Application:
The features include:
• Sign to Text Conversion
• Sign to Speech Conversion
• Speech to Sign Conversion
• Text to Sign Conversion
• Word Suggestions
• Shortcut Mode
• Emergency Mode

5. Web Application:
The web app was created using "Streamlit" module in python and can be easily deployed using streamlit.io.

You can also run the app on local machine using command
"streamlit run WebApp.py"

The features included in current version of web-app are:
• Sign to Text Conversion
• Text to Sign Conversion
• Real time Audio-Video Feed
