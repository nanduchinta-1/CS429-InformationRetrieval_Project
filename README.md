# CS429-InformationRetrieval

# Project Report

## Abstract

This project aims to develop a search engine for querying quotes and their authors. The primary objective is to create a scalable, efficient, and user-friendly system that allows users to search for quotes and get relevant results. The next steps involve enhancing the search capabilities, improving the user interface, and incorporating advanced features like sentiment analysis and user recommendations.

## Overview

### Solution Outline

The solution involves a web scraping component that collects quotes and authors from various sources, an indexing component that creates an inverted index using TF-IDF scores, and a query processing component that handles user queries and returns relevant results.

### Relevant Literature

- "Information Retrieval" by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze
- "Scrapy Documentation" for web scraping
- "Scikit-Learn Documentation" for TF-IDF and cosine similarity calculations

### Proposed System

The proposed system includes:

- Web scraping module using Scrapy
- Indexing module using Scikit-Learn
- Query processing module using Flask

## Design

### System Capabilities

- Web scraping of quotes and authors
- TF-IDF based indexing
- Cosine similarity based query processing
- RESTful API for querying

### Interactions

- User interacts with the web interface to input queries
- The query is processed by the backend, and relevant quotes are fetched from the index
- Results are displayed to the user

### Integration

- Scrapy for web scraping
- Scikit-Learn for TF-IDF and cosine similarity calculations
- Flask for web server and API

## Architecture

### Software Components

- **Web Scraping Module**: `quotes_spider.py`
- **Indexing Module**: `indexer.py`
- **Query Processing Module**: `app.py`

### Interfaces

- Web Interface
- RESTful API

### Implementation

- Python for backend development
- Scrapy for web scraping
- Scikit-Learn for TF-IDF calculations
- Flask for web server and API

## Operation

### Software Commands

- `scrapy crawl quotes_spider`: Run the web scraping module
- `python indexer.py`: Run the indexing module
- `python app.py`: Run the query processing module and start the Flask server

### Inputs

- User queries via the web interface

### Installation

Refer to the `requirements.txt` file for installation instructions.

## Conclusion

The project successfully developed a basic search engine for quotes. While the system performs well for simple queries, there is room for improvement in terms of scalability and search accuracy. Future work includes integrating more advanced search algorithms, enhancing the user interface, and optimizing performance.

## Data Sources

- Goodreads Quotes: [Link](https://www.goodreads.com/quotes)

## Test Cases

- Test case files are located in the `tests` directory
- To run tests: `pytest`

## Source Code

- All source code files are available in the project repository
- Documentation is included in the `README.md` file
- Open-source dependencies are listed in `requirements.txt`

## Bibliography

- Manning, C. D., Raghavan, P., & Schütze, H. "Information Retrieval."
- Scrapy Documentation. Available at: [Link](https://docs.scrapy.org/en/latest/)
- Scikit-Learn Documentation. Available at: [Link](https://scikit-learn.org/stable/documentation.html)