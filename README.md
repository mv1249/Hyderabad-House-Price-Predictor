## Hyderabad House Price Predictor
ML model which predicts the price of a house based on features like total Sq. ft area,total number of bedrooms,balconies etc.
The front-end of this model is made by boot-strap and Flask,where as the backend is a Machine learning model which is trained on the housing-price dataset and the  algorithm used is Random-Forest
the model is hosted at------>  https://homepricepredictor.herokuapp.com/



## General Overview of the Project 

Starting of with the home page which is designed using bootstrap classes,here we in this template the general overview of the project is mentioned,along with that the parameters which are required for predicting the price of the house are also mentioned here,here's a glimpse of it

![.](images/1.PNG)

Now here's a glimpse of the parameters page,which is giving the information about the parameters which are used for predicting the model,one can read the matter by clicking on param's option on the navigation,here is a small glimpse of it

![.](images/3.PNG)

After having read about the details of the parameters,its time for predicting the price of the house based on the parameters which are mentioned in the params' section,so inorder to predict the price we have to switch ourselves from the params' tab to the predict price tab,which is present in the navigation bar after the parameters tab,just click on that and here is a glimpse of the form

![.](images/4.PNG)

Here after we have to fill in the details as required and hit the predict button,here's a glimpse how it looks after filling the details in the form

![.](images/6.PNG)

Once the form is filled,hit the predict button and it will take some time as the requests made are asynchronous,as the data is been passed from the "FORM" to the Heroku cloud,where i have hosted my machine learning model,the data from the form is passed in the form of a multidimenssional array,and once the model at heroku is done with the computation it returns the result in form of json,which we have to convert into python list and get the result and display it in the front end.

![.](images/5.PNG)

 The model predicts the price of the house,in (Lakh),well to be honest,as there was not much data given to the model,the predictions might not seem that good,but if more and more data was fetched we would expect better results,and that is true,as one fetches more data to the Machine Learning Model,the model will learn better insights and will perform better
 
 
 


### Technologies Used

<code><img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" title="python"></code>
<code><img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" title="javascript"></code>
<code><img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" title="html5"></code>
<code><img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" title="css3"></code>
<code><img height="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" title="git"></code>











