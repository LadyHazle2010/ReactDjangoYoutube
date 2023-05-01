 # As a developer, I want to make 10 good, consistent commits.


 # As a developer, I want to create an ERD for my project that shows all models, fields, and relationships between models for the backend.


 # As a developer, I want to set up the Django + React starter code and connect the backend (Django API) to my MySQL database, closely following the setup guide for instructions. 


 # As a developer, I want to create a Comment model in a ‘comments’ app: 


            Property names must be in snake_case and match the following exactly!  


            user – ForeignKey 

            video_id – CharField 

            text – CharField 

            likes – IntegerField 

            dislikes – IntegerField 


 # As a developer, I want to create a Reply model in a ‘replies’ app: 


            Property names must be in snake_case and match the following exactly!  


            user – ForeignKey 

            comment – ForeignKey 

            text – CharField 


 # As a developer, I want to create a GET endpoint that does the following things: 


            Accepts a value from the request’s URL (The YouTube video id I am trying to get comments for). 

            Returns a 200 status code. 

            Responds with all comments from the database that are related to the video id sent in the URL. 


 # As a developer, I want to create a POST endpoint that does the following things: 


            Requires JWT authorization (Protected route). 

            Accepts a body object from the request in the form of a Comment model. 

            Adds the new comment to the database associated with the user who sent the JWT in the request. 

            Returns a 201 status code.  

            Responds with the newly created comment object.  


 # As a developer, I want to use  Postman to test all of my endpoints and save them to a collection, and then export it as a JSON from Postman.  



 # As a developer, I want to create a PUT endpoint that does the following things: 


            Requires JWT authorization (Protected route). 

            Accepts a value from the request’s URL (The id of the comment to be updated).  

            Accepts a body object from the request in the form of a Comment model.  

            Finds the comment in the Comments table and updates that comment with the properties that were sent in the request’s body.  

            Returns a 200 status code.  

            Responds with the newly updated comment object.  


 


 # As a developer, I want to create a GET endpoint that does the following things: 


            Requires JWT authorization (Protected route). 

            Accepts a value from the request’s URL (The id of the comment I am trying to get replies for).  

            Returns a 200 status code. 

            Responds with all replies from the database that are related to the comment id sent in the URL. 



 # As a developer, I want to create a POST endpoint that does the following things: 


            Requires JWT authorization (Protected route). 

            Accepts a value from the request’s URL (The id of the comment the reply will be connected to).  

            Accepts a body object from the request in the form of a Reply model.  

            Adds the new reply to the database associated with the comment id sent in the URL and the user who sent the JWT in the request. 

            Returns a 201 status code.  

            Responds with the newly created reply object.  

