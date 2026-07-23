# 🎬 Netflix Data Explorer

## Overview

Netflix Data Explorer is a Streamlit web application that allows users to explore the Netflix Movies and TV Shows dataset. The app provides an interactive interface to view, filter, and analyze Netflix content.

## Features

* View the Netflix dataset
* Display dataset shape and summary
* Filter content by country
* Visualize Movies vs TV Shows
* Simple and interactive user interface

## Dataset

The project uses the `netflix_titles.csv` dataset containing information such as:

* Show ID
* Type (Movie/TV Show)
* Title
* Director
* Cast
* Country
* Release Year
* Rating
* Duration
* Genre
* Description

## Project Structure

```text
Netflix-Streamlit-App/
│
├── app.py
├── netflix_titles.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vedantpachurkar/Netflix-Streamlit-App.git
```

2. Move to the project folder:

```bash
cd Netflix-Streamlit-App
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

## Technologies Used

* Python
* Streamlit
* Pandas

## Author

Vedant Pachurkar
