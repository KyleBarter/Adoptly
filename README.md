# Adoptly

<<<<<<< HEAD

Renad, Louise and Kyle's project 3
<<<<<<< HEAD

Aka Teeming Emu, Beloved Dolphin, Responsible Locust
=======
>>>>>>> a44aed4 (new change)

Description
The third project during my time with General Assembly, and first within a group and using a stack of Python, Django and PostgreSQL. 
Adoptly’s mission was to start offering an alternative to the transcational process of pets bred by breeders through websites such 
as pets4home and give a chance to homeless and unwanted animals. One thing we noticed was a lot of animals being bought based on their 
looks and influence on social media without any real understanding of the responsibilities that comes with that animal, particularly dogs. 
We wanted to create an opportunity for aspiring pet owners to be displayed pets based on their lifestyle, personality and needs; moving 
away from pet transactions and more towards forming relationships between human and pet.

Deployment link
Issues with deployment link at present

Getting Started/Code Installation
You can access the code through my repo here:
https://github.com/KyleBarter/Adoptly

Timeframe & Working Team
We were given just under a week as a group of three to produce the MVP of a CRUD app. Louise was given the role of scrum master where she 
took control of the Trello and wireframes, whilst Renad worked on the ERD, both playing a crucial role in producing the final product as 
it set us up perfectly for when we went into coding. I focused mainly on the backend and was Github manager, ensuring the team weren’t having 
any issues with merges, pushes and pulls. We did have issues with this frequently so it was a good test to be on standby to help troubleshoot with them.

Technologies Used
This CRUD app was built using Python, Django and PostgreSQL. Our app also heavily relied on packages like form wizard, as we wanted the pet profile 
and adopter preferences questionnaire to stay on one URL so the user isn’t redirected after each question and just to create a tidier UI, and cleaner backend. 

Brief
We were briefed to create a functioning CRUD application using a Django framework with Python. The project also required one data entity if consuming 
an API, or at least two if we weren’t as well as Django’s built-in authentication.

Planning
We started planning through Zoom calls organised on Slack. From there we used excalibur as we could all collaborate and edit that simultaneously. 
Quickly from there I think we realised what each of our strengths were and how we could use that to produce synergy between the three of us, to be as 
efficient as possible. We continue to have standups each day during planning to know where everyone was at..

You can find a link to our Trello board here
https://trello.com/b/L0S2o53I/adoptly-find-your-pawfect-match-project-3
From there, you can access our wireframes and ERD, but screenshots are attached below also.
![Adoptly trello 1](https://github.com/KyleBarter/Adoptly/assets/118014478/6d8a37cd-4337-4e48-a966-40b96cf47cca)

![Adoptly trello 2](https://github.com/KyleBarter/Adoptly/assets/118014478/d49f6a5a-25c5-4185-8b79-9fae8853f37b)


We were heavily inspired by Hinge’s UI and concept, as we were fleshing out the idea and goal of our app we realised what we wanted was similar functionality 
to dating apps. Whilst Hinge’s UI is very clean and minimalist, it was also the sort of human-to-pet connection focused theme we wanted. You can see this very 
clearly below through the pet profile, and the questionnaire we ask the adopter’s and pet owner’s.
 ![Adoptly wf 1](https://github.com/KyleBarter/Adoptly/assets/118014478/5885879b-61cb-4e5e-a29e-ebfe8ef08e7a)


We also liked the idea of sticking to one colour scheme, but using different shades, where we settled on yellow.
One of our stretch goals was to create a messaging service for adopter-to-owner, as the pet profiles and user’s are a many to many relationship it would be 
an easier way for the user’s to view and handle their matches.

We wanted the user to be able to scroll through all their matches, click on the match which would take you to the pet detail page seen above, but instead of 
the floating like and dislike buttons, a message button. 
![Adoptly wf 2](https://github.com/KyleBarter/Adoptly/assets/118014478/77f5cb50-9e7e-4440-8fb9-f697c371dc3c)


Please also see below ERD. We used one user model, but once signed up they select whether they’re a pet owner or adopter which would then take them to fill 
in a form, either for the PetTable model or the AdoptioinPreferences model. 
![Adoptly ERD](https://github.com/KyleBarter/Adoptly/assets/118014478/fd3f184d-fcf7-4aee-8bec-b66b829ac0dd)


Build/Code Process
From the project start, I worked on getting the database setup, views and urls. Two view functions I was particularly proud of was the potential match pile 
sorting algorithm and also just the redirect form, albeit quite simple with just 20 lines of code.

As we were so heavily influenced by existing dating apps, we wanted to improve the UX through keeping the user from swiping endlessly. We identified the key 
attributes of both the user and pet’s personality and lifestyle as activity level, sociability and size. Using a for loop to iterate through the unmatched pets, 
it checks through each conditional statement to compare the attributes for an exact match, where the ‘score’ increments by one. This score, in a one to one relationship 
with the user and pet, is then appended to the end of the matches pile if the score is less than or equal to 1. 
![Adoptly code 1](https://github.com/KyleBarter/Adoptly/assets/118014478/14309b55-a514-496e-b8b6-135e4aa8e37e)


As mentioned, although this function is quite simple with the fact it’s only 20 lines it was an error we noticed very late on, which was that the user wasn’t being 
redirected correctly to the right page when choosing if they were an owner or a pet. As this was merged quite late to the development branch, it was a race against 
time to try and figure it out but I managed to solve it through the following if statement. The issue was that the choice wasn’t being saved so using the save method 
after setting each adopter boolean value to the choice of the user. 
![Adoptly code 2](https://github.com/KyleBarter/Adoptly/assets/118014478/db22c78e-6231-407d-a541-37a2f53814bf)


After I worked primarily on the views and urls, the other members of the team looked at working on the forms for both the adopter and owner. I created a lot of the 
standard pages so they would be presentation ready. The one that took the most work would have been the home page as this was where we wanted the user’s who had 
selected adopter would see a list of all the pets available to match with.
Unfortunately I wasn’t able to create it as a ‘stack’ of pets for the user so they only see one at a time. This would be something I’d definitely like to come back to 
and figure out how to fix. Also the process of liking and disliking a pet hasn’t quite worked so this needs further testing.
![Adoptly code 3](https://github.com/KyleBarter/Adoptly/assets/118014478/f75cb3a6-9bb9-42a4-af12-32991eb33e82)
![Adoptly code 4](https://github.com/KyleBarter/Adoptly/assets/118014478/7dd2540a-4571-46c1-8806-46e09c3e2a53)



Challenges
As this was our first time working in a group this came with many new challenges. Most of these were to do with merging and branching as we were getting error’s we 
wouldn’t have come across before and figuring out work-arounds with these.

Another was not having the full project in order to test things working thoroughly, I realised this a couple days into the project as my homepage feature could only work 
once the user had completed the forms and selected that they were an adopter / owner. So after this I tried to stress that we merge together as often as possible just to 
know what we had built and could advise each other what wasn’t working with each area of the app they worked on, once testing it against what each other’s work.


Key Learnings/Takeaways
One reflection of myself was that I was hesitant to move away from my features for fear of treading on people’s toes and taking work off of others. Whilst I think this was 
coming from the right place I could have been more vocal about what I could and couldn’t work on so that we could work as efficiently as possible. I sort of cornered myself 
into just my features and that meant that when we did merge our feature’s together I noticed we were missing some elements, such as the field to select if you’re an adopter 
or owner. Going forward I think it would be key for us to merge more often than not, as well as not being afraid to ask more direct questions about what everyone is up to, 
what their features are looking like so far. In any aspect of life I have always said communication is key, and this is no different, a lesson learnt which I’ll carry forward 
into any role I have as a dev. 

Wins
I think our biggest win was how well we worked as a team in the planning phase, we all knew exactly what we wanted the app to do, to feel like and what to look like. We were 
all on the same page each morning and if anyone had any new ideas, or wanted to make any changes they were listened to and most ideas were then implemented which I think shows 
how great we were at communicating our ideas, listening to each other and coming to an understanding of how best to implement that feature or design idea.

One of the issues we were having was no pets appearing on the home page, and we realised, using the Django admin, this was due to it not correctly saving the detail of whether 
the user was an owner or adopter. Once we sorted out the one to one relationship between the user and this preference, we could correctly display what they should see and it was 
a very satisfying moment.

Further on from this, also creating it so each pet would appear on the home page was rewarding as that was my feature, however we found it difficult to display just one at a time.

It was really insightful to move away from the MERN stack we had been using and try what’s similar to the MVC model but for Python and Django, it felt much more efficient with routing. 
As well as this, I felt much more comfortable using a relational database with PostgreSQL, particularly when working out the relationships between entities.

Bugs
Currently we have an issue with deleting an account, whilst it will delete the account it does take you to an error page at the moment.

We’ve also got issues with the like and unlike buttons. Initially we have tried associate and disassociate functions for the pet profile to the user adoption preferences. But this 
also returns an error at the moment. I think we will need to have another review at which model the likes sit with. Unfortunately we were quite short on time with this project, and 
as this was a group project we experienced a lot more difficulties with things such as Git has meant that there’s a few more bugs than we’d have liked.

Future Improvements
I would like to be able to fully complete the home page so that we can only see one pet at a time to fit more with our mission of moving away from transaction based relationships and 
more personal ones. We also wanted to add messaging as a stretch goal and I think I’d really like to give that a try as to date I haven’t tried implementing a feature like that in any projects. 
The styling will also need to become more consistent across each page.

