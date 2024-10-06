# team_managment_api
Team management API using Django and Postrgres
This is a simple REST API built with Django and Django REST Framework (DRF) for managing teams and people within those teams. The API allows you to create, retrieve, update, and delete (CRUD) both Teams and People, with relationships between them.

Features: 
1. Create, retrieve, update, and delete Teams.
2. Create, retrieve, update, and delete People.
3. Assign people to teams.
4. List all members of a specific team.


API Endpoints
The following are the available endpoints for managing teams and people:

Teams
1. GET /api/teams/ - Get a list of all teams.
2. POST /api/teams/ - Create a new team.
3. GET /api/teams/{id}/ - Retrieve a specific team by ID.
4. PUT /api/teams/{id}/ - Update a specific team.
5. DELETE /api/teams/{id}/ - Delete a specific team.

People
1. GET /api/people/ - Get a list of all people.
2. POST /api/people/ - Create a new person.
3. GET /api/people/{id}/ - Retrieve a specific person by ID.
4. PUT /api/people/{id}/ - Update a specific person.
5. DELETE /api/people/{id}/ - Delete a specific person.
