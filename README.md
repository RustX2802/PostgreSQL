# translation_API

Translation API using Deep Learning
Project Overview
This project involves the development of a translation API leveraging deep learning techniques. Through the use of FastAPI, we'll establish a web server with two main routes: /translate for receiving translation requests and /results for retrieving the translation outcomes. The translations will be stored in an SQLite database, and the backend will utilize asynchronous programming alongside a pre-trained deep learning language model to efficiently handle translation tasks.

Upon completion, the project will yield a responsive web server capable of swiftly executing translation jobs. Additionally, the server architecture is designed to facilitate easy expansion for translating more languages or incorporating additional options.

Project Steps
Build API Routes: Establish routes for translation requests and results.
Add Models for Database Storage: Implement models to store translation data in the database.
Create Tasks for Translation: Develop tasks to handle the translation process using the deep learning language model.
File Overview
requirements.txt: Lists the required packages for installation.
languages.txt: Enumerates the supported languages for translation.
main.py: Defines the web server routes.
models.py: Contains definitions for the database models.
tasks.py: Executes backend tasks, including the translation process.
Usage
To run the server locally, execute the following command:

bash
Copy code
uvicorn main:app --reload
Data
During the project, a pre-trained language model will be downloaded and employed for translation tasks.

Deploying
Deploy with Docker
Build Docker Image:

bash
Copy code
docker build -t dlapi .
If not on 64-bit Linux, use the following command instead:

bash
Copy code
docker buildx build --platform linux/amd64 -t dlapi .
Run Docker Container:

bash
Copy code
docker run -d --name dlapi -p 80:80 dlapi
View Container Information:

bash
Copy code
docker ps
Check Container Logs:

bash
Copy code
docker logs
Ensure that Uvicorn is running on http://0.0.0.0:80.

Access the API Server:

Visit 127.0.0.1 or localhost. API documentation is available at localhost/docs.

Stop the Container:

bash
Copy code
docker stop dlapi
