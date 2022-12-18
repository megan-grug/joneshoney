# Nature Adventure 

![examples of the project site shown on different sized screens]()

This is a website allowing people to browse and buy different honey and beekeping related products and experiences.

It is a mobile first, responsive design and the live website can be viewed []().

An example of how the homepage looks on various screensizes is included above.


## USER EXPERIENCE:

### Who will use the website?
The site will be used by anyone who is looking for a place to buy honey or by people who want to learn more about beekeeping.


### New Users (User A)
**Goals:**
- 
-
-

### Regular Users (User B)
**Goals:**
-
-
-
-



## STRATEGY PLANE:

**Project Purpose from the perspective of the site owners:**


- Provide a site which ....

    - **Strategy:** xxxx


- Allow ....

    - **Strategy:** I will do this by ....


- Allow ....

    - **Strategy:** I will ....


- Encourage .....

    - **Strategy:**
    I will include ....


**Viability of features:**
| Feature                                       | Importance  | Viability   |
| ----------------------------------------------|------------ |-------------|
|                                               |     5       |     5       |
|                                               |     5       |     5       |             
|                                               |     5       |     5       |             
|                                               |     5       |     5       |
|                                               |     4       |     4       |
|                                               |     3       |     3       |
|                                               |     4       |     4       |
|                                               |     3       |     3       |
|                                               |     3       |     1       |
|                                               |     1       |     2       |


**Changes from initial plan:**
After my initial research, I have decided ....


## SCOPE PLANE:

The website will include the following features: 

- TBC
-
-
-
-
-
-     
     

## STRUCTURE PLANE:

The following pages will be included in the project:

**Pages visible to everyone, whether or not they are logged in or not:**
- Home Page

- Products

- FAQ

**Pages only visible to logged in users:**

- My Account

- My Orders

- Log Out

**Pages only visible to users who are NOT logged in:**

- Register

- Log In


## SKELETON PLANE



Before starting to code the website I prepared wireframes showing the planned page structures for mobile and laptop sizes on each page. This helped me to identify the basic page structure I wanted to achieve, and the wireframes show that I was planning to have a consistent layout with the various lists of birds looking the same throughout the website so that users quickly became familiar with the site. 

The wireframes also show the plans for the full record details to be condensed into small repeated cards - this is to avoid the site becoming cluttered by vast amounts of information.

The navigation structure I chose to pursue was based on simplicity to help the users feel comfortable on the website straight away, wherever they are accessing it from.




## SURFACE PLANE

**Colour scheme:**
- I chose ...

**Typography:**
- For this project I have chosen...

**Themes:**
-   I chose to....


## DATABASE

The site is built on a MySQL database. 


## TECHNOLOGIES USED

### Languages:
-	HTML5
-	CSS3
-   JavaScript
-   Python


### Frameworks, Libraries, Websites and Programs:
-	**Materialize CSS:**
Used for consistent styling and responsiveness. 

-   **Flask:**
Used for creating and running a Python server side project.

-   **Jinja:**
Used to inject logic inside of HTML templates. 

-   **jQuery:**
Used to provide neat interactivity.

-	**Google Fonts:**
Used to import custom fonts as referred to above. 

-   **Google Maps Javascript API:**
Used to capture and display maps and location data as part of the bird records. 

-	**Font Awesome:**
Used to import icons to create custom buttons.

-	**Git:**
Used for version control between GitPod and GitHub.

-	**GitHub:**
Used to store and deploy the project. 

-   **Heroku:**
Used to deploy project externally.

-	**Balsamiq:**
Used to create initial wireframes as part of the planning and designing stage. 

-   **Cloudinary:**
Used to host images and favicons.

-   **Google Developer Tools:**
Used to inspect each page and function of the site and to check each element and function at a granular level to ensure it is working as planned.

-   **Google Maps JavaScript API:**
Used to provide the maps and location functionality to be used as part of the bird records.

-   **Google Developer Console:**
Used to manage the use of the Google Maps JavaScript API. 

-  **Firefox Developre Tools:**
Used to inspect each page and function of the site and to check each element and function at a granular level to ensure it is working as planned.

## PROBLEMS IN ADVANCE OF TESTING:



## TESTING:

### VALIDATOR SERVICES:
- **W3C HTML Validator:**
    
    - All pages through the W3C HTML Validator without raising any errors, save for the following warning which appears on all pages:

        - Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed.
        I have reviewed this and have not taken any further action, as the page does in fact have a H4 header inherited from line 65 of base.html, however it is not visible as it is between jinja tags. The section always has a h4 heading whenever it is displayed. 


    The code passes through the W3C CSS Validator without raising any errors. 

- **W3C CSS Validator:**
    
    The code passes through the W3C CSS Validator without raising any errors. 

- **PEP8 Python Validator:**

    The code passes through the PEP8 Python Validator without raising any errors. 

- **Lighthouse:**
    The site returns passing scores on all counts when passed through Lighthouse for both desktop and mobile. 

    *Desktop:*
    ![image of desktop Lighthouse results](/assets/img/lighthouseresult_desktop.JPG)

    *Mobile:*
    ![image of mobile Lighthouse results](/assets/img/lighthouseresult_mobile.JPG)


### MANUAL TESTING

I have manually tested the site by: 

- visiting each page;
- methodically checking that it looks right at every size;
- methodically checking that every feature works as intended at various sizes. 


Manual testing was undertaken on the following browsers with no noticable differences:
- Google Chrome;
- Mozilla Firefox;
- Microsoft Edge;
- Opera;
- Safari 


**Bugs Identified in Manual Testing**


- Accessibility issue: 
    
    When the navbar is compressed at smaller screen sizes, the burger menu used is a dark grey instead of black. This is due to an issue overriding the Bootstrap 4 colour schemes. If using a custom colour scheme, the burger menu becomes transparent no matter what attempts are made to override the colour to black. I have therefore had to stick with Bootstraps built in navbar-light, which has slightly less contrast than I would have liked. 

- Navbar layout:

    Bootstrap's standard dropdown menu for 'My Account' displays slightly off the page to the right.

- Google Chrome Dev Tools produced the following console issue on the 'edit_record.html' page:

    custom.js:11 Uncaught ReferenceError: google is not defined
    at customMarker (custom.js:11:23)
    at custom.js:25:1

    I have identified that this is an issue with the order in which the scripts are loading, and have tried several things to remedy this such changing the order of the scripts, and using async and defer attributes in the scripts to determine the order in which they will load, unfortunately nothing has consistently worked and occasionally the maps 'dip out' due to this issue. I was not able to identify any other possible solutions to this issue. 



### USER STORIES TESTING:

### Experienced Birders (User A)
**Goals:**
- Create a record of which birds they have seen;

    The fact that every page includes a navbar with a link to the 'Add New Record' page supports this user goal, as does the fact that there is a prominent button on the hero image of the home page inviting the user to add a record to their list. 

    The simplicity of the 'Add New Record' page also helps the user achieve this goal.


- Review their list;

    Clear navigation to the 'My Records' page supports the user in achieving this goal. I have purposely kept this page simple so as not to distract from the records. Using cards to represent the records makes it easier for the user to review their list as they can use a visual representation of the record without reading through the whole thing and every piece of information associated with it. The ability to expand the record to view the full details also assists the user in achieving this goal as they can view the information of the relevant record they wish to review without the clutter of all their other records. 


- Add notes to their bird records;

    Users can achieve this goal easily by using the prominent 'notes' section under 'Add A Record', and can also review or edit their notes by accessing their records. 


- A higher proportion of this group are likely to be older users and therefore:

    - They may be more likely to use a desktop version of the site. It is important that full functionality is available on the desktop version. 


    - They may be less experienced web users and it is therefore important that the site is user friendly and not over complicated. 

        This goal has been achieved by setting the site up with a familiar, traditional navigational system which is consistent throughout. I have also added icons to buttons, and tooltips to make the site as intuitive as possible to use. 

        This view of the all birds page as seen on desktop shows how this goal is met. 
        ![view of the 'all birds' page as seen on a desktop](https://res.cloudinary.com/megan-jones/image/upload/v1649069818/rsz_laptopviewallbirds_nbjkgq.jpg)


- This user group is more likely to want and appreciate more advanced features. 

    The ability to record and review location data as well as specific notes for each record satisfies this goal.


### New Birders (User B)
**Goals:**
- Create a record of which birds they have seen;

    See above. Furthermore, particularly in the case of new birders, the autocomplete functionality removes any stress that may be caused by misspelling the name of a bird - this may be more likely for inexperienced birders who are not yet familiar with all the bird names or for very young users. 

- Review their list;

    Clear navigation to the 'My Records' page supports the user in achieving this goal. I have purposely kept this page simple so as not to distract from the records. Using cards to represent the records makes it easier for the user to review their list as they can use a visual representation of the record without reading through the whole thing and every piece of information associated with it. The ability to expand the record to view the full details also assists the user in achieving this goal as they can view the information of the relevant record they wish to review without the clutter of all their other records. 

- Find information about birds;

    The inclusion of a straightforward section called 'All UK Birds' will help users to achieve this goal as it is clear to them that they can find out about all British birds on one page. I have also included a search function, so that users can easily either browse to see what takes their interest or search for a specific bird they would like to read about. The fact that these pages pull information directly from the MongoDB database makes it easy for the site to grow and change in future. 

- Get suggestions for what to look for when/where to see certain birds. 

    This goal is met by the inclusion of the 'What to See Now' page which clearly sets out which birds to look out for, when. Additionally, there is a sample of this function on the home page which will dynamically stay up to date and present the user with the birds to look out for in the month they are visiting the site.  

- A higher proportion of this group is likely to be younger and therefore:
    - They may be more likely to use the site on mobile at the time of the sighting, so it is important that the mobile version is clear and quick to use on site. 

        Manual testing has shown the mobile version of the site to be fully functional and easy to use with clear navigation.

                Testing has shown the site to be fully functional on desktop. This image of the homepage as viewed on mobile shows how clear and simple the layout is, satisfying this goal. 

        ![Image of the home page as viewed on mobile](https://res.cloudinary.com/megan-jones/image/upload/v1649069538/mobileview-homepage_f0hkhg.jpg)

    - This group may include children, so it is important to make the site intuitive and not over-complicate it.

        See similar goal above for User Group A. 



## DEPLOYMENT

**GITHUB**


*Forking the repository on GitHub*

This will allow you to make changes to the project without affecting the original by making a copy of the project and working from that. 

- Log in to GitHub;

- Navigate to the GitHub repository for this project;

- Click 'Settings' in the repository;

- Under 'Settings' select 'Fork';

- Under 'Source' select 'None' and then 'Master Branch'.

- This will create a copy of the original project repository.

- You will need to create your own env.py file including the following variables: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME, GOOGLE_API. 


*Cloning*

- Log in to GitHub;

- Navigate to the GitHub repository for this project;

- In the repository, click 'Clone or download';

- To use HTTPS, copy the link under 'Clone with HTTPS';

- Open GitBash;

- Change the working directory to the location where you want to put the cloned directory.

- Type 'git clone' and then paste the link you copied from 'Clone with HTTPS'.

- Press enter to complete the creation of the local clone. 

- - You will need to create your own env.py file including the following variables: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME, GOOGLE_API. 

**HEROKU**

The project was deployed to Heroku as it uses pages based on template inheritance which cannot be hosted on GitHub Pages. 

**How to Deploy to Heroku:**

- Ensure that the project meets the requirements for deployment to Heroku:

        - It must have a requirements.txt file:

                - This can be created using the terminal command of 'pip3 freeze--local > requirements.txt' in your coding environment

        - It must have a Procfile:

                - This can be created by using the terminal command of 'echo web: python app.py > Procfile
                - If there is a blank line at the end of the Procfile, this may cause problems and this should be deleted. 

        - Both these files must have been pushed to the GitHub repository. 

- Create / log into an account at [Heroku](https://www.heroku.com)

- Click on the 'New' button at the top right to create a new app. 

- Under 'App name' create a name for the app (the name must be unique and must use a dash or minus instead of spaces)

- Under 'Choose region' select the region which is closest to you. 

- Click 'Create App' button. 

- At the 'Deployment method' section around halfway down the page, select "GitHub".

- Under 'Connect to GitHub:
    
    - make sure your GitHub profile is shown; 
    
    - type in the exact name of your GitHub repository;

    - click 'Search';

    - when the repository is found, click 'Connect' to connect to the app. 

- Scroll back to the top and navigate to the 'Settings' tab for the app.

- Scroll down to 'Config Vars' - here you will store the hidden variables so that Heroku can access them, as it will not be able to access the env.py file. 

- Add the following variables:

    - IP
    - PORT
    - MONGODB_NAME (the name of your Mongo DB database)
    - MONGO_URI
    - SECRET_KEY
    - GOOGLE_API (this should be your own google maps api key)

- Scroll back up and return to the 'Deploy' tab. 

- Click 'Enable Automatic Deployment'. 

- Wait as the app is built. 

- When the app is built you will see the message 'Your app was successfully deployed'. 

- Click 'View' to view the deployed app.


## CREDITS

### Code Credits




### Media Credits


**Favicon:**    


**Images:**



**Icons:**

- All icons from FontAwesome and Materialize CSS. 

**Content:** 





### Acknowledgements

Thank you to Adam, for keeping me fed whilst I hid away at my computer and to Richard for helping me to believe I could actually become a competent developer.

## DISCLAIMER

This site is for educational purposes only and is not intended to be accessed, viewed or used by the general public.
