# NBA-Expected-Points
The goal of this project was to find a way to estimate the scoring probability of NBA Players, in real-time, depending on their position on the field and their position with respect to their opponents. 

The Dataset used was found on AWS, it is called “Stats Perform Basketball Research Dataset”. 

The first step in this analysis was to use different classification models to predict the shooting outcome given the distance of the ball carrier to the basket, and to the closest defender. The Model Selection is detailed under the “Choosing Model” folder. For that purpose, the Logistic Regression was the most accurate.

Giving this model, the next step was to create an animation using our Dataset that contained sequences of player and ball tracking data of games from the 2019 NBA season. Unfortunately, the players were unlabeled so the players’ performances could not be included into the model. The animation displays successive sequences of the game, and described above the shooting success probability for either:
-	The ball carrier
-	Each player of the attacking team
These animations are on the “real-time animations” folder, you might need to run the py file twice before the animation appears. 
