# API Documentation

This documentation provides details about the REST API for managing person records.

## Endpoints

### Create a Person

- **URL:** `https://second-task-sa3c.onrender.com/api`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@gmail.com"
  }
-Response:
----Success (201 Created):
     {
        "id": 1,
        "name": "John Doe",
        "email": "john@gmail.com" 
     }
-Error (400 Bad Request):
    {
      "error":"Name and Email must be include"
    }




### Update a Person

URL: https://second-task-sa3c.onrender.com//api/{user_id_or_name}
Method: PUT
Request Body:
   {
       "name": "Updated Name"
   }
-Response:
----Success (200 OK):
     {
         "message": "Updated Successfully!"
     }

-Error (404 Not Found):
    {
        "error": "User Not Found"
    }




### Delete a Person

URL: https://second-task-sa3c.onrender.com//api/{user_id_or_name}
Method: DELETE
-Response:
----Success (200 OK):
   {
       "message": "User Deleted!"
   }

-Error (404 Not Found):
  {
     "error": "User Not Found"
  }



-----------------------------------Sample Usage-----------------------------------------

### Create a Person

curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email":"john@gmail.com"}' http://localhost:5000/api


### Retrieve a Person
curl https://second-task-sa3c.onrender.com//api/1


### Update a person
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' https://second-task-sa3c.onrender.com//api/1


### Delete a Person
curl -X DELETE https://second-task-sa3c.onrender.com//api/1




UML Diagram link: https://drive.google.com/file/d/1m33m9ChzVH7IL5CRdAciMEJ8bVwRUs3B/view?usp=sharing
