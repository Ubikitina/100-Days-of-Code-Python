# Day 71 Goal

Today's objective is to deploy our blog web application. The following is a description of the steps done.

# Verify that all the requirements are met

- Our Pycharm project must have a proper .gitignore.
- Version Control Integration is enabled in PyCharm
  - We can do it by typing git init in the Terminal.
  - All files must be added and committed to git (refer to day 70 for further instructions about git).
- Use environment variables to store sensitive information
  - E.g. replace code such as app.config['SECRET\_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' with app.config['SECRET\_KEY'] = os.environ.get('FLASK\_KEY')
  - Import the os module to do so.
- Set the app.run(debug=True) to app.run(debug=False).

# Setup a WSGI server with gnicorn

WSGI stands for **Web Server Gateway Interface**. More information can be found here: [https://peps.python.org/pep-3333/](https://peps.python.org/pep-3333/).

Traditional web servers may not be equipped to handle Python applications, needing the use of a dedicated server type known as WSGI (Web Server Gateway Interface) for executing our Flask application. WSGI servers play a crucial role in standardizing language and protocols between the Python Flask application and the hosting server.

Among the various WSGI options available, we have opted for **gunicorn** ([https://docs.gunicorn.org/en/stable/](https://docs.gunicorn.org/en/stable/)), a widely recognized choice. This decision ensures that our hosting provider invokes gunicorn to execute our code efficiently.

## How to add gunicorn

- Include gunicorn package in the requirements.txt.
- Create a Procfile document. Procfile tells our hosting provider about our gunicorn server, what our app is called, and how to run our Flask app.
- Commit all the changes.

# Push the project to our remote on Github

- Link PyCharm with GitHub
- Push to your remote on GitHub by clicking right button above the project name, and selecting: Git -\> Push.
  - Set up an origin URL: it is a .git URL from GitHub, created for our project.
- Once pushed, verify that our project is shown in GitHub.

# Create our web service in a hosting provider

Select a hosting provider. Examples:

| **Provider** | **~Cost/Month** | **Name of Plan** |
| --- | --- | --- |
| Heroku | $5 | Eco & Basic |
| render | $0 | Individual |
| Cyclic | $0 | Free Forever |
| Glitch | $0 | Starter |
| Vercel | $0 | Hobby |
| PythonAnywhere | $0 | Beginner |

Follow the step-by-step process. We will use render:

1. Create an account with the hosting provider.
2. Link our GitHub repo with the host.
3. Create a new Web Service: New -\> Web Service. Choose your blog app that you've uploaded to GitHub and connect your repo. Edit the Start Command to gunicorn main:app.
4. Add our environment variables: Store the key-value pairs for our environment variables with our host.
5. Set up a PostgreSQL database with the host, instead of SQLite database. To do so, in render, create a new Postgres database from the website menu by selecting: New -\> PostgreSQL. Pick a name for de database and create it. Copy the internal database URL, replace postgres:// with postgresql://, and set it as the SQLALCHEMY\_DATABASE\_URI environment variable in our web service.

## Clarification on PostgreSQL database vs SQLite database

The process involves transitioning from SQLite to PostgreSQL due to the limitations associated with SQLite's file-based nature. While SQLite is advantageous during the coding and testing phases, allowing easy inspection of data using tools like DB Viewer, it becomes a potential drawback when deployed with hosting providers like Heroku or Render.

The critical issue stems from the fact that the file locations of SQLite databases are rearranged approximately every 24 hours when hosted with certain providers. This volatility poses a significant risk of data loss, as the database may be inadvertently wiped during these shifts. Such an occurrence could lead to a negative impact on user experience and satisfaction.

To mitigate this risk and enhance database robustness, the decision is made to upgrade to PostgreSQL. PostgreSQL is chosen for its ability to handle vast amounts of data entries and ensure consistent data delivery to users, making it a more reliable solution for production environments.

An important aspect to note is that the transition from SQLite to PostgreSQL is facilitated by the prior use of SQLAlchemy in creating the Flask application. SQLAlchemy, being a SQL toolkit and Object-Relational Mapping (ORM) library, abstracts away the underlying database details, allowing for a seamless switch between different database management systems without the need for extensive code modifications. In addition, we are using the psycopg package in combination with SQLAlchemy. The psycopg module is a popular PostgreSQL database adapter for Python.

In essence, the primary task involves setting up the PostgreSQL database, and since the Flask app is already designed with SQLAlchemy, there is minimal code adjustment required. This strategic migration ensures data integrity, scalability, and long-term stability when deploying the Flask application in a production environment.