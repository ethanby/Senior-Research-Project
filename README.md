# Analyzing User Behavior and Dependency Patterns in Navigation Apps 

**By: Ethan Byers**

### Objective: Conduct a survey to measure behavioral patterns in users of navigation apps

There are three main components to my survey research. The first is the survey_results.csv file containing all survey questions and responses.
Questions 21-35 are formatted in such a way to calculate a dependency score based on what answers were given by respondents.
The first answer choice is the *dependent* option, the second choice demonstrates *moderate dependency*, while the third choice suggests *no dependency* toward navigation apps.

The second component is the seniorresearch.py short python program. It can run through the survey results to automatically determine each respondents dependency score based on their answers for the 15 questions (#21-35).
A score between 0 and 10 suggests no dependency, 11-20 suggests moderate dependency, and 21-30 indicates high dependency.

The third components is the scores_results.csv file which displays the individual question scores and overall scores for all survey participants.

I have deemed the rest of the questions outside of the 15 used for dependency score to be better for more general behavioral insights. They are less usable to objectively determine someones dependency level and were not included in calculating scores.
 
