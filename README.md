# Recommender System for Educational Guidance
A Web Base user-item Majors Recommendation Engine using Regression Analysis algorithm. It is produced for students to get a recommendation of the proper university majors that fulfill their needs and passions.
The recommendation based on the underlying idea that is if a major has high score then the user will introduced by it , along with a list of majors follow this idea.

#### The experimented models are:
- GradientBoostingRegressor
- MultiOutputRegressor
- Ridge
- KNeighboursClassifier
- xbg
- Logistic regression

 After testing the quality of each model using NDCG method, we decide to use the KNeighboursClassifier which has the highest quality.



## Documentation
A detailed description about the project, all the classes, functions, interfaces and the project structure you'll find in the documentation of the project.

You can open the documentation by <a href ="https://docs.google.com/document/d/1ujWh-o56jcvPxPrOqzMIJeIRJhbEofhs7oBZaYKhB54/edit?usp=sharing">EduGuide project Documentation .</a>



### Technologies Used

#### Web Technologies
Html , Css , JavaScript , Bootstrap , Flask

#### Machine Learning Library In Python3
Numpy , Pandas , pySpark



##### Requirements
```
python 3.6

pip3

virtualenv
```
## Installation
 `npm install Flask`

## How to use
* On Command :
  - you need go to path => `cd ....\application`
  - run app => `py app.py`
