# NBA xP (Scoring Probability Estimation)
The goal of this project was to develop a method for estimating the scoring probability of NBA players in real-time, based on their position on the court and their position relative to their opponents.

### Data
The Dataset used was found on AWS, it is called “Stats Perform Basketball Research Dataset”. 


### Methodology
1) Implement different classification models to predict the shooting outcome based on the distance of the ball carrier to the basket and the distance to the closest defender. The logistic regression model was found to be the most accurate.

2) Create animations from our dataset containing sequences of player and ball tracking data from the 2019 NBA season. 

3) Measure in real-time carrier's distance to the hoop, and to the other players

4) Predict xP using the trained model

5) Run animation and plot xP curve 

### Results
The animations show successive sequences of the game and display the shooting success probability for the ball carrier and each player on the attacking team. These animations can be found in the "real-time animations" folder. Note that you may need to run the .py file twice before the animation appears.

### Further improvements
Players were unlabeled in the tracking data, so we were unable to include player performance in the model. 
