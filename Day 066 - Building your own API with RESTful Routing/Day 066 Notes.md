# Goals of Day 66

- Create an API to interact with the SQLite database.
- Test de API by using Postman.
- Create the API documentation by using Postman and publish it.

## What is REST?

In this module, the focus is on building a RESTful API from scratch. **REST** stands for Representational State Transfer and is an architectural style used in client-server interactions, which is the basis of the entire Internet. The client, analogous to a customer in a restaurant, makes requests to the server using **HTTP requests** , with various verbs like **GET** , **POST** , **PUT** , **PATCH** , and **DELETE**.

It is important using the correct language (HTTP) for communication between the client and server. Additionally, HTTPS (HTTP Secure) is used for secure communication, to ensure privacy.

**Origins of REST** : attributing its development to Roy Fielding's Ph.D. research. Fielding proposed a set of rules for web developers to follow, aiming for a standardized structure across all web APIs. It compares REST to other architectural styles like **SOAP** and highlights **REST as the gold standard for web APIs**.

**Two crucial aspects of building a RESTful API** :

- Using HTTP request verbs (GET, POST, PUT, PATCH, DELETE)
- Following a specific pattern of routes and endpoints. Routes and URLs provide access to specific resources in the server.

## Postman

Postman is a popular collaboration platform for API development that simplifies the process of designing, testing, and managing APIs. It provides a user-friendly interface for developers to interact with APIs and perform various tasks related to API development.

In this exercise we will use Postman to:

- **Request Building** : Developers can easily create and customize HTTP requests using Postman. This includes specifying request headers, query parameters, request body, and authentication methods.
- **API Testing** : Postman allows developers to send HTTP requests (GET, POST, PUT, DELETE, etc.) to APIs and view the responses. This is particularly useful for testing different endpoints, parameters, and payload structures to ensure that the API behaves as expected.
- **Documentation** : Postman provides tools for generating and hosting API documentation. This documentation is interactive and allows developers to explore and understand the API endpoints, request/response structures, and available functionalities.

## HTTP PUT vs PATCH

The course provides an analogy to explain the difference between the HTTP PUT and PATCH methods. The author uses an analogy of ordering a bicycle from Amazon to illustrate the concept. In the analogy, the author receives a damaged bicycle and contacts Amazon for a solution.

- **The PUT method** is likened to the option of receiving an entirely new bike. This is comparable to updating a database by sending a complete entry to replace the existing one.
- **The PATCH method** is compared to the option of receiving only a new tire for the damaged bicycle. This represents sending a patch request to the server, where only the specific data that needs updating is sent, rather than the entire entry.

## Day 66 Project Tasks Summary

1. **Download Starting Project**
   - Download the .zip file from the lesson's resources.
   - Unzip and open the project in PyCharm.
   - Create a new virtual environment and install dependencies from `requirements.txt`.

2. **Troubleshooting Setup**
   - If not prompted to create a virtual environment, set it up manually via File -> Settings -> Project -> Python Interpreter.
   - If red underlines persist in `main.py`, install required packages manually using the terminal:
     - Windows: `python -m pip install -r requirements.txt`
     - MacOS: `pip3 install -r requirements.txt`

3. **Database Familiarization**
   - Locate `cafes.db` in the "instance" folder.
   - Use DB Viewer to inspect the database fields and records.

4. **Create API Routes: HTTP GET - Random Cafe**
   - Create a `/random` route in `main.py` to serve a random cafe.
   - Use Flask's `jsonify()` to serialize and return the cafe data as JSON.

5. **Create API Routes: HTTP GET - All Cafes**
   - Create a `/all` route to return all cafes in the database as JSON.
   - Combine `.execute()` and `.select()` methods with `.scalars()` to fetch and format the data.

6. **Create API Routes: HTTP GET - Find a Cafe**
   - Create a `/search` route to find cafes by location, passing `loc` as a URL parameter.
   - Use `.where()` to filter cafes by location.

7. **Testing with Postman: Postman Setup**
   - Download and install Postman from https://www.postman.com/downloads/.
   - Test API routes and create a collection named "Cafe & Wifi" for existing routes.

8. **Create API Routes: Add New Cafe Route**
   - Create a POST route to add a new cafe to the database.
   - Simulate form submission using Postman by entering key-value pairs in the Body tab.

9. **Create API Routes: Update Cafe Price Route**
   - Create a PATCH route `/update-price/<cafe_id>` to update the coffee price.
   - Use `.get_or_404()` to fetch the cafe by id and update the price using Postman.

10. **Create API Routes:  Delete Cafe Route**
    - Create a DELETE route `/report-closed/<cafe_id>` to delete a cafe.
    - Implement an API key check (`"TopSecretAPIKey"`) for authorization, returning 403 if unauthorized.

11. **Generate API Documentation**
    - Use Postman to save and document each request in the "Cafe & Wifi" collection.
    - Publish the documentation using Postman's "Publish Docs" feature.
    - Add a link to the generated documentation in `index.html`.
