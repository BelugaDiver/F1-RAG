# Project: F1 Data RAG

## Description

This project leverages the power of AI and LangChain's SQLDatabaseToolkit to provide a robust question-answering system over an F1 SQLite database. Users can pose natural language queries related to F1 data, and the system will process the query, interact with the database, and provide relevant responses.

## Technologies

**Python:** The backend is built using Python for its versatility and extensive libraries.
**FastAPI:** A modern, high-performance web framework for building APIs.
**LangChain:** A powerful framework for building and deploying language models.
**SQLDatabaseToolkit:** A LangChain tool specifically designed for interacting with SQL databases.
**SQLite:** A lightweight, serverless database management system.
**React:** A JavaScript library for building user interfaces.

## Project Structure

```
├── backend
│   ├── app.py
│   ├── models.py
│   └── utils.py
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── components
│   │   └── styles
│   └── public
│       └── index.html
├── requirements.txt
├── README.md
└── .gitignore
```

### How to Run

1. **Install dependencies:**

```Bash
cd f1-data-rag
pip install -r requirements.txt
```

1. **Run the backend:**

```Bash
cd backend
uvicorn app:app --reload
```

1. **Run the frontend:**

```Bash
cd frontend
npm start
```

## Usage

- **Access the frontend:** Open your web browser and navigate to <http://localhost:3000>.
- **Ask a question:** Enter your natural language question related to F1 data into the provided field.
- **Get a response:** The system will process the query, interact with the database, and display the relevant response.

## Customization

- **Database:** Modify the database connection details in the backend/utils.py file.
- **Language model:** Experiment with different language models and their parameters.
- **Prompt engineering:** Refine the prompts used to interact with the language model for better results.

## Future Enhancements

- **Vector databases:** Explore using vector databases for more efficient semantic search.
- **Natural language generation:** Generate more human-like responses using advanced NLP techniques.
- **Integration with other tools:** Connect the system with other tools like data visualization or machine learning.

This project provides a solid foundation for building a powerful question-answering system over F1 data. Feel free to customize and extend it based on your specific needs and requirements.
