# ARDC_GRP_2 - iLab 2 project 

## Project Overview
In the era of real-time information, social media, especially Twitter, has become invaluable during natural disasters. To tackle the overwhelming volume of data generated, we've developed a machine learning model that detects and analyzes emotions in disaster-related tweets. Our chatbot, HurricaneBot, offers tailored recommendations based on these emotions, providing guidance during crises.

Our primary goal is to streamline disaster response by identifying emotions like anxiety and fear in tweets. HurricaneBot steps in to provide vital information, including evacuation guidance, safety tips, and emergency contacts, ensuring more efficient and emotionally intelligent support.

In our future scope, we plan to integrate geolocation data from tweets, allowing precise location-based aid delivery. This innovation will empower agencies and organizations to provide timely assistance during disasters, ultimately improving disaster response effectiveness.

![plot](https://github.com/BharaniSurya/ARDC_GRP_2/blob/main/overall_flow.png)

## Tools and installing support 
- Python(3.11.4) - https://www.python.org/downloads/
- Jupyter - https://jupyter.org/install
- pycharm - https://www.jetbrains.com/help/pycharm/installation-guide.html
- githubdesktop - https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop
## Hybrid annotation 
![plot](https://github.com/BharaniSurya/ARDC_GRP_2/blob/main/hybrid_annotation.png)

In the project's early stages, a critical challenge was acquiring tweet data annotated with emotional content. However, this task proved to be highly resource and time-intensive, and publicly available annotated datasets were scarce. To address this challenge, we adopted a hybrid annotation approach that combined the capabilities of Large Language Models (LLMs) and the NRC Lexicon for initial annotation, followed by a comprehensive verification process conducted by a human annotator.

### NRC Lexicon for Annotating 'fear,' 'sadness,' and 'anger'

The methodology for annotating text data with specific emotions, notably fear, sadness, and anger, was meticulously structured to gain deeper insights into the emotional content embedded within textual information. In this section, we delineate the systematic approach employed to analyze and annotate text data, focusing on emotions such as fear, anxiety, sadness, anger, helplessness, relief, frustration, confusion, empathy, and hope.

To ensure precision in sentiment analysis, we commenced by defining a comprehensive list of emotions referred to as "emotions_to_check." This list included specific emotions of interest, thereby providing clear guidance for sentiment analysis. The data underwent a systematic loop, addressing missing values, utilizing the NRCLex library for emotion analysis, and evaluating emotion presence based on emotional scores from the NRC Emotion Lexicon. Each text's emotional presence or absence was captured, resulting in a binary representation of emotion presence. The results were collected systematically for all texts and added as columns in the dataset. These additional columns indicated the presence or absence of specific emotions, contributing to a structured dataset for further analysis. A crucial step involved manual verification to ensure that the automated emotion assignments matched the emotions presented in the output, enhancing the reliability and accuracy of the annotated dataset for subsequent project phases. This approach provided a robust foundation for emotional analysis within the project.


## Disaster Classification Model 
![plot](https://github.com/BharaniSurya/ARDC_GRP_2/blob/main/classification.png)

Data preprocessing for the Hurricane Harvey dataset, as utilized in this section, adhered to the same rigorous cleaning procedures detailed in Section 4.1.1, ensuring consistency and data integrity. The primary objective of our Emotion Classification model was to discern and categorize a spectrum of emotions, including fear, sadness, joy, and others, embedded within textual content. Our approach extended beyond merely identifying specific emotions; it also encompassed quantifying the percentage of each emotion present in the text. To achieve this, we adopted a hybrid annotation method, which seamlessly combined human annotation and automated processes. This hybrid approach guaranteed the quality and accuracy of the labeled data, a pivotal component of our analysis.

Our next step involved a comprehensive analysis of the distribution of the top 5 emotions, which led to the identification of the predominant emotional responses commonly observed during disaster situations. These primary emotions included fear, anger, frustration, sadness, and anxiety. To evaluate our model's performance, we divided our dataset of 2,000 rows into an 80:20 split, maintaining the integrity of our model's assessment.

For the classification task, we employed a multilabel classification model with the capability to predict multiple emotions for each text. The model's objective was to determine the likelihood of different emotions present in the text, such as fear, sadness, and joy. To accomplish this, we opted for the Random Forest model, renowned for its robust performance in multilabel classification scenarios.

Following the training and testing phases of our model, we conducted a comprehensive assessment of the accuracy of emotion prediction for each class. This evaluation provided valuable insights into the model's effectiveness in identifying specific emotions within the text. The accuracy of emotion prediction varied across different classes, as follows:

-Fear: 78%
-Anxiety: 71%
-Sadness: 55%
-Anger: 65%
-Frustration: 74%

In addition to classifying emotions, we delved further into the analysis by incorporating predicted probabilities for each emotion. These probabilities offered a valuable metric to quantify the extent of each emotion's presence within the text. This granular approach allowed us to express emotions in terms of percentages, providing a more detailed and insightful perspective on the emotional content embedded within the text.

## Disaster chatBot
### interface Sample

![plot](https://github.com/BharaniSurya/ARDC_GRP_2/blob/main/MicrosoftTeams-image%20(3).png)

### work flow
![plot](https://github.com/BharaniSurya/ARDC_GRP_2/blob/main/MicrosoftTeams-image%20(4).png)
#### Fine-Tuning and Saving the Model: 
We began by fine-tuning the model and saving both the model and tokenizer for future use. This step was crucial for deploying the chatbot in real-world scenarios and ensuring its long-term viability.

#### Integration with Lang Chain:
Connecting the fine-tuned model to Lang Chain expanded its capabilities for use in production environments. We established a pipeline for generating responses, enabling the chatbot to interact with users effectively and showcasing its potential to offer valuable assistance during disasters.

#### Template Framework Development: 
To prepare the chatbot for action, we developed a series of templates that guided the model in generating compassionate, supportive, and empathetic responses. These templates provided a structured framework for crafting responses that were non-judgmental and genuinely helpful.

#### API Development with Flask: 
The final piece of the puzzle involved creating the chatbot's API using Flask. We developed an API endpoint capable of accepting user queries and delivering responses generated by the fine-tuned model. This API ensured the chatbot's seamless integration into various platforms and services, enhancing its accessibility and utility.

#### Streamlit Frontend: 
We used Streamlit to design and develop the chatbot's frontend, providing an intuitive and user-friendly interface for users to interact with the chatbot.
