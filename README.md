
# Modern School Result: Talk to a Database  
This project aims to create an end-to-end system utilizing Google Palm LLM and Langchain framework to enable natural language interaction with a MySQL database storing student, teacher and marks data for a modern school. The system allows school administrators or teachers to ask questions in natural language, which are then converted into SQL queries to retrieve relevant information from the database.

# Project Highlights
Database Schema: Utilizes MySQL to store data for students, teachers and marks.

Natural Language Interaction: Implements Google Palm LLM and Hugging Face embeddings to process natural language queries from users.

User Interface: Utilizes Streamlit to provide an intuitive user interface where school administrators or teachers can input questions in natural language.

Langchain Framework: Incorporates the Langchain framework for seamless integration and execution of SQL queries generated from natural language input.

Chromadb Integration: Utilizes Chromadb as a vector store for efficient storage and retrieval of embeddings and other data representations.

Few-Shot Learning: Employs few-shot learning techniques to enhance the system's ability to understand and respond accurately to a wide range of user queries.

# Usage
1) Access the Streamlit user interface.
2) Input questions in natural language regarding student information, teacher details, or marks data.
3) The system will process the query using Google Palm LLM and Langchain, generate the corresponding SQL query, and execute it on the MySQL database.
4) Display the results or relevant information corresponding to the user's query on the user interface.


The web app will open in your browser where you can ask questions

# Sample Questions
1) Find the first three rankers of class 7th.
This question will generate an SQL query to retrieve the top three highest-scoring students from class 7th based on their marks.

2) Retrieve the name of the student who got an 'A' grade in computer for class 6th.
This question will generate an SQL query to identify the student(s) from class 6th who obtained an 'A' grade in the subject of computer.

3) Calculate the average marks obtained by students in each subject for class 7th.
This question will generate an SQL query to calculate the average marks obtained by students in each subject specifically for class 7th.
  

# Project Structure
- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- few_shots.py: Contains few shot prompts
- .env: Configuration file for storing your Google API key.