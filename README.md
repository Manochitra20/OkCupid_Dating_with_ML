# OkCupid_Dating_with_ML

We cleanned the data using Python, Pandas
presentation using:
Flask, Java script, Html, ccs
tableau, plotly, Machine learning

Sally Ahmed
cleanned 4 columns from the data and Graph it
using sunburst graph using plotly 
creating Tableau presentation.

Manochitra Kumar: **Clustering and creating a recommendation algorithm:**

This scope for this part of the project was to cluster the user’s profiles into groups and to try to find a match more easily with the help of machine learning algorithms. We tried different different modelling/training methods with the data we had.
The first step was to clean and preprocess the available data in way it can be understood by the algorithms. 

The preprocess consisted of splitting the data into numerical (age, income, height) and categorical variables (diet, education, job). Then the numerical variables were scaled using standardscaler and the categorical variables were transformed from string to float using ohehotencoder.

**Kmeans clustering** algorithm was chosen to cluster the profile data into different groups. The results from kmeans were plotted and from the first elbow graph we picked 7 clusters.  And when we investigate the cluster plot , we immediately see that there are no distinct clusters.

We then did feature reduction using PCA, and the elbow plot showed 7 clusters, and the cluster plot also didn’t show much distinct clusters.

We added the clusters to the original dataset. we proceeded with training the model with supervised ML.
We used **K nearest neighbour and random forest** method for this purpose. The accuracy score for the KNN method was 63% and 55% for training and testing data respectively. However, on the other hand randomforest model gave as a very good score of above 90% for both training and testing data.

Now that the model is trained, we created a pipeline to be used as the basis for processing data and predicting for the recommendation system to work. We saved the model in a pickle file and this will load the pipeline when there is new test data available.

When user inputs data in the form created in html, the pipeline predicts the cluster that the user falls into and pulls 5 random profiles from the OkCupid dataset and shows it as a table, which is similar to the way dating app works.




Ruby



Sam
