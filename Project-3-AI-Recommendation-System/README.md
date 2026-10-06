# AI Movie Recommendation System

## DecodeLabs Artificial Intelligence Internship - Project 3

An AI-based movie recommendation system that recommends movies based on the user's preferred genres. The system uses preference matching and similarity logic to identify movies that best match the user's interests.

---

## Project Overview

The AI Movie Recommendation System allows users to enter one or more movie genres they are interested in.

The system:

* Accepts multiple user preferences
* Compares user preferences with movie genres
* Calculates a match score
* Identifies matching genres
* Ranks movies based on their matching score
* Displays movie recommendations

The recommendation process uses simple and explainable similarity logic.

---

## Objective

The main objective of this project is to demonstrate how an AI-based recommendation system can use user preferences and similarity logic to provide personalized movie recommendations.

---

## Recommendation Logic

The system compares the genres selected by the user with the genres assigned to each movie.

The match score is calculated using:

**Match Score = (Matched Preferences / Total User Preferences) x 100**

For example, if the user selects:


Action, Sci-Fi


and a movie contains:

Action, Sci-Fi, Adventure


the movie receives:


Match Score: 100%


If a movie contains only `Action`, it receives:


Match Score: 50%


Movies are then ranked according to their matching scores.

---

## Available Genres

The system currently supports:

* Action
* Adventure
* Comedy
* Crime
* Drama
* Animation
* Family
* Sci-Fi
* Thriller

---

## Movie Dataset

The project uses a predefined movie dataset containing movies and their associated genres.

Example movies include:

* Inception
* Interstellar
* The Matrix
* The Dark Knight
* Avengers: Endgame
* Jurassic Park
* Toy Story

---

## Technologies Used

* Python 3
* Python Standard Library
* Preference Matching
* Similarity Logic
* Rule-Based Recommendation

No external Python libraries are required for the current version.

---

## System Workflow


User enters interests
        |
        v
Input is processed
        |
        v
User preferences are identified
        |
        v
Movie genres are compared
        |
        v
Matching genres are calculated
        |
        v
Match score is calculated
        |
        v
Movies are ranked
        |
        v
Top recommendations are displayed


---

## Project Structure


Project-3-AI-Recommendation-System/
|
+-- main.py
+-- README.md
+-- requirements.txt
|
+-- screenshots/
    |
    +-- project3-output.png


---

## How to Run

### 1. Open the Project Folder

Open PowerShell or the VS Code terminal and navigate to the project folder:

powershell
cd "C:\Users\HEALTHY MACHINES\Desktop\New folder\DecodeLabs-Internship\Project-3-AI-Recommendation-System"


### 2. Run the Program

powershell
python main.py


### 3. Enter Your Interests

Enter one or more genres separated by commas.

Example:

Action, Sci-Fi


---

The exact recommendations depend on the preferences entered by the user.

---

## Learning Outcomes

Through this project, I practiced:

* Understanding recommendation systems
* Processing user preferences
* Implementing similarity-based matching
* Calculating recommendation scores
* Ranking recommendation results
* Designing a user-friendly command-line interface
* Applying AI concepts to a practical problem
* Organizing and documenting an AI project

---

## Future Improvements

Possible future improvements include:

* Larger movie datasets
* More detailed user profiles
* Rating-based recommendations
* Genre weighting
* Machine learning-based recommendation
* User rating history
* Graphical user interface
* Database integration
* More advanced similarity algorithms

---

## Internship Information

**Program:** DecodeLabs Artificial Intelligence Internship

**Project:** Project 3 - AI Recommendation System

**Developed by:** Navodya Mihiranga

**Degree:** BSc in Information & Communication Technology

**University:** South Eastern University of Sri Lanka

---

## Project Status

**Status:** Completed

The current version successfully accepts user preferences, calculates similarity-based match scores, and displays ranked movie recommendations.
