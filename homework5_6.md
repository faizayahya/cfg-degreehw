Question 1
									
·  Product backlog refinement

Product backlog refinement main goal is to review and break down the Product Backlog items into smaller items. During this new details may be added, detailed and estimated in terms of priority. Both the product owner and development team are involved in this and the main purpose is to see that everything is on track. 
		
·  Sprint planning
 
This commences the Sprint by setting goals to be performed for the Sprint. During this, the Scrum Master, product owner and agile team collaborate. 
·  Daily scrum 	
This is usually held every morning with the development team, it is optional for the Scrum Master to be involved in the Daily scrum. The purpose of this is to inspect and check progress and see that everything is on track and redefine priorities and tasks.											

·  Sprint review 	

The Sprint review is one of the last few events of the Sprint, it comes second to last. During this, the Scrum team, the product owner and any key stakeholders will be present. The members of the Scrum team will present what has been completed or not in the product backlog and this is a great opportunity to discuss any changes that need to be made and what’s next. 					
			
·  Sprint retrospective 

 This takes place when the Sprint is done. During this the Scrum team will discuss what went well in the last sprint and ways to improve the next sprint in terms of effectiveness and quality. 
		 	 	 				
				
·  ScrumMaster

The Scrum Master is accountable for the Scrum and the efficiency of the Scrum Team and makes sure the scrum plan is executed well by improving practices, ensuring everyone is on track and providing guidance to teams.  
				
·  Product Owner

The Product Owner is responsible for the effective management of the Product Backlog, which also includes defining and expressing the product goal clearly. The Scrum Product Owner is responsible for increasing the value of the final product that the Scrum Team produces. It is possible for businesses, Scrum Teams, and individuals to implement this in very different ways.							
	
·  Development Team 

The Scrum Development team is a cross-functional team of people that are responsible for building the product increment. Their purpose is to meet the Sprint goal. 


Question 2 

TASK 1
 				
As a user I need to be able to (tasks that can be worked in parallel): 		
- Create an account
- Delete/deactivate an account 


As a user I need to be able to (tasks that will need to be worked on in particular order): 
- Have the ability to input my account email address and password once the account has been created
- Be able to create an account and delete the account 
- Be able to reset password


User Needs: 
- Have a protected password 
- Be able to see available classes - with details on times and who is leading classes
- Book the class
- View the prices of the class if the user does not have a membership
- Be able to cancel the class within a given timeframe 
- See the class capacity 
- See how many people will be attending the class
- Booking confirmations must be sent to the users email address


Many features such as creating, deleting and logging in and out will need to be created in both parallel and particular order. These include:

- Being able to log into an account and log in - therefore a login will need to be built before building a sign out. 
- Being able to reset the password of an account 
- Being able to create an account and deactivate/delete an account 
- The ability to view classes and then have the option to book those classes 

These tasks can be assigned to small teams to work on. There can be two teams assigned on the following tasks: 

Team 1: 

- Building the login system: this will include creating an account, inputting user information and the ability to delete an account. This can be worked on in that same order.

Team 2: 

- Can create the database that will hold all of this information. They can work in parallel with team 1 as the login system will provide them with the data that needs to be stored. 

SQL: 

- Tables will all be linked by ID 
- The database forms will need to be created to input all users 
- There will need to be a table for all user information which includes: name, email, password
- A table for all users who either have a membership (that is paid or unpaid), or pay as you go classes
- There will need to be a separate table for all class information (this one can be updated to show any bookings including ones that have been updated or cancelled)
- SQL will also be needed to store all class information where this information can be updated
- API will be connected to Python and to the database in order to display on the users screen 

Python:

- This will need be worked on in parallel to SQL 
- Python flask will need to be connected with all databases 
- Connect and redner APIs 

TASK 2 

Key Requirements: 

- The database will need to record all bookings 
- There will need to be initialise and process payments 
- Set reservation time for the tickets that are purchased (time limit of up to 10 minutes) 
- There will need to be a server that houses the database 
- API will need to connected with both SQL and Python 

Main considerations:

- Will the users need an account to purchase tickets, or can this also be done as a guest user
- How will the user inputs be captures and where will the data be stored 
- Payment options - including apple/googlepay
- Reservation time for all bookings (what will the time limit be?)
- How will the information be presented 
- Can users purchase different tickets for different movies at once 
- Will there be the ability to choose user seats online? 

Common or biggest problems:

- The time limit - tickets will be held for up to 5-10 minutes until they complete the purchase. This gives them enough time to complete the purchase, especially as they have selected seats. This also means there is enough of a time gap between each booking for the next user to purchase (this is important during times there are limited or the last ticket).
- Create an option for a guest check out, however there will need to be code to ensure that emails are necessary and check out cannot be completed without this. Guest check out will also give the option to create a password. 
- Payment verification with their bank - an API can be used for this. 
- Prices are all consistent throughout purchase, if there are any offers/discounts on the website this is also shown on the payment page to avoid any confusion. 
- One time payment - so if the user accidentally refreshes the page or clicks back all information is still there and purchase can be made. No second payments as it is possible to purchase twice by accident. Cache/cookies will need to be used for this.
- Some users may accidentally put in the wrong email address (typo’s in the email address), tickets should be displayed after purchase with booking reference so they can save and screenshot. Their information should also be automatically stored in the database so that the person at the ticket desk can retrieve their details in case they did not save their ticket details. 

Components and tools:

- SQL will be used to store all data
- Python and Flask (Flask and Sql will be connected)
- API’s 
- All front end development such as html and css. 
