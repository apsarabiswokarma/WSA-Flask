# Web services API and Documentation

### Endpoint 1: Get All Users

- **Description:** Retrieve details of all users.
- **URL:** `/get-all-user`
- **Method:** GET
- **Parameters:** None
- **Status Code:** 200 OK
- **Example Request:**
  `curl -X GET http://localhost:5000/get-all-user`

  **Response:**

  ```json
  {
    "1": { "name": "Ram", "age": 21 },
    "2": { "name": "kushal", "age": 23 },
    "3": { "name": "Rupesh", "age": 22 },
    "4": { "name": "Sam", "age": 20 }
  }
  ```

### Endpoint 2: Get User by ID

- **Description:** Retrieve details of a specific user by ID.
- **URL:** `/user/{id}`
- **Method:** GET
- **Parameters:**
  - `{id}`: User ID (integer)
- **Status Code:** 200 OK if user found, 404 Not Found if user not found
- **Example Request:**
  `curl -X GET http://localhost:5000/user/1`

  **Response:**

  ```json
  { "name": "Ram", "age": 21 }
  ```

### Endpoint 3: Add User

- **Description:** Add a new user.
- **URL:** `/add-user`
- **Method:** POST
- **Parameters:**
  - JSON payload with "name" and "age" fields
- **Status Code:** 200 OK
- **Example Request:**

  bashCopy code

  `curl -X POST -H "Content-Type: application/json" -d '{"name": "NewUser", "age": 25}' http://localhost:5000/add-user`

  **Response:**

  jsonCopy code

  ```json
  {
    "1": { "name": "Ram", "age": 21 },
    "2": { "name": "kushal", "age": 23 },
    "3": { "name": "Rupesh", "age": 22 },
    "4": { "name": "Sam", "age": 20 },
    "5": { "name": "NewUser", "age": 25 }
  }
  ```

### Endpoint 4: Add User from Form

- **Description:** Add a new user from an HTML form.
- **URL:** `/add-user-from-form`
- **Method:** POST
- **Parameters:**
  - Form data with "name" and "age" fields
- **Status Code:** 200 OK
- **Example Request:**
  `curl -X POST -d 'name=NewUser&age=25' http://localhost:5000/add-user-from-form`

  **Response:**

  ```json
  {
    "1": { "name": "Ram", "age": 21 },
    "2": { "name": "kushal", "age": 23 },
    "3": { "name": "Rupesh", "age": 22 },
    "4": { "name": "Sam", "age": 20 },
    "5": { "name": "NewUser", "age": 25 }
  }
  ```

### Endpoint 5: Delete User by ID

- **Description:** Delete a user by ID.
- **URL:** `/user/{id}`
- **Method:** DELETE
- **Parameters:**
  - `{id}`: User ID (integer)
- **Status Code:** 200 OK if user found and deleted, 404 Not Found if user not found
- **Example Request:**
  `curl -X DELETE http://localhost:5000/user/1`

  **Response:**

  ```json
  {
    "2": { "name": "kushal", "age": 23 },
    "3": { "name": "Rupesh", "age": 22 },
    "4": { "name": "Sam", "age": 20 },
    "5": { "name": "NewUser", "age": 25 }
  }
  ```

### Endpoint 6: Update User by ID

- **Description:** Update a user's age by ID.
- **URL:** `/user/{id}`
- **Method:** PUT
- **Parameters:**
  - `{id}`: User ID (integer)
  - JSON payload with "age" field
- **Status Code:** 200 OK if user found and updated, 404 Not Found if user not found
- **Example Request:**
  `curl -X PUT -H "Content-Type: application/json" -d '{"age": 26}' http://localhost:5000/user/5`

  **Response:**

  ```json
  {
    "2": { "name": "kushal", "age": 23 },
    "3": { "name": "Rupesh", "age": 22 },
    "4": { "name": "Sam", "age": 20 },
    "5": { "name": "NewUser", "age": 26 }
  }
  ```

### Endpoint 7: Render Form Page

- **Description:** Render an HTML form page.
- **URL:** `/form`
- **Method:** GET
- **Parameters:** None
- **Status Code:** 200 OK
- **Example Request:**

  `curl -X GET http://localhost:5000/form`

  **Response:** HTML page rendering a form.

### Endpoint 8: Render JSON Page

- **Description:** Render an HTML page for JSON content.
- **URL:** `/json`
- **Method:** GET
- **Parameters:** None
- **Status Code:** 200 OK
- **Example Request:**

  `curl -X GET http://localhost:5000/json`

  **Response:** HTML page rendering a form.
