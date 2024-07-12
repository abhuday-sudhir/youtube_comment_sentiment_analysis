# YouTube Comment Sentiment Analysis

This project aims to analyze the sentiment of YouTube comments using Flask as the web framework and leveraging TextBlob and VADER for sentiment analysis.

## Features

- Extract YouTube video ID from a given URL.
- Retrieve comments for the specified video.
- Perform sentiment analysis on the comments.
- Display the results in a tabular format.

## Prerequisites

- Python 3.x
- Pip (Python package installer)
- A valid YouTube Data API key (for fetching comments)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/abhuday-sudhir/youtube-comment-sentiment-analysis.git
    cd youtube-comment-sentiment-analysis
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your YouTube Data API key in the environment variable:
    ```sh
    export YOUTUBE_API_KEY='YOUR_API_KEY'  # On Windows use `set`
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

3. Enter a YouTube video URL and submit the form to analyze the comments.

## Project Structure

