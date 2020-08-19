# Travel Blogging Site with 3D Virtual Tour
---
## Description
This is my CS50 project Capstone Final Submission it is a travel blogging web app that also allows visitors to take Virtual Tour to that paticular place using three.js a popular JS library and custom js it renders equi-rectangular panorama images into 3D skybox which user can control with mouse to gain realistic 3d experience. It uses Django Image field and pillow 5 to store images as models in Django also it stores blog content date author comments and other thing as models. In it Comments are Also Moderated from Admin Portal every comment is only visible after being approved from admin portal. It has all the features that a Travel blog must have. In addition to all those HTML contents can also be posted in blogs as it uses safe. More over its mobile responsive since it uses bootsrap.
It is very Complex as per as the requirements of this project.
---
## YouTube Link
https://www.youtube.com/watch?v=-5GL0K8U1A
---
## File Contains
---
### Models.py
Contains Post Model which contains blog title slug for url foreign key author updated_on DateTimeField to show last updated date content TextField img ImageField to show blog images virtualtour ImageField for Rendering 3D skyybox from panorma images created_on DateTimeField To Show the date on Which Created and its odering is done by date created on.
---
Comments It contains post foriegn key for knowing on which blog post to be dispalayed name CharField for commentors name and email EmailField for commentors email body TextField for comment and active BooleanField with default value False so that commment will be only visible once approved by the admin portal created_on DateTimeField for date comment posted.Comments are also ordered by created_on.
---
It also contains status with draft or publish options only published blogs are displayed with boolean value 1.
---
### urls.py 
Both the urls.py contains address the project url.py(blog) also contains admin site title header and index title it also contains static media url for debug mode
---
### settings.py
Every thing is same as default when created except a few changes in installed app travel is added TEMPLATES_DIRS is defined added below base dir and is also used in Templates Dir added in list there. in dir key. Media Root and Media URL are defined at the last two lines.
---
### admin.py
Here Post and comments models are imported and both are registered. CommentAdmin and PostAdmin are two define how each model is to be displayed/edited/created in Admin Portal like populated fields in post admin defines that slug will be same as title without spaces and with hyphens instead in lower case. similary actions in comments which approves comment with approve comment option which updates its boolean value to true similary other models are also defined to be displaye din list format filter are also created using created_on and other attributes same goes with search field.
---
### views.py
Contains functions and templates to render pages. Home Page defined as PostList is designed using django template and is also paginated by django template which automatically pases post model as object there oredred by date created on and filtered by staus published which is 1. Rest Pages are rendered noramlly.
---
### templates/layout.html
Contains the default site layout designed with bootsrap and custom css. It is Mobile Responsive since it uses bootsrap.
---
### templates/sidebar.html
Contains sidebar created with a bootsrap card have details About Site and a Know more button which redirects to about us page.
---
### templates/index.html
Displays list of Blogs paginated by per page 3 blog with every blog card having read more button redirecting blog page and a virtual tour button redirecting to virtual tour page of that travel blog.
---
### templates/post.html
Displays blog and also sidebar also it has comments sections where viewers can read or post comments. It also has image at the top of post and html contents can be also displayed inside post it also shows date created/updated and the author of the post along with post title. It has a virtual tour button just below the post which redirects it to virtual tour page.
---
### templates/virtual.html
It uses three.module.js to render a virtual 3d skybox out of equi-rectangular panormal images.If post or panormal image does not exist 404 will displayed. It is rendered dynamically it loads image url in js using the post virtualtour url variable which is when rendered it displays url of image in js and then js renders the skybox. The width and height of canvas is generated / resized automatically henced its also mobile responsive.
---
### templates/about.html
It Contains About us content
---
### templates/policy.html
It contains policies of the site.
---
### static/three.module.js
Contains three.js js.
---
### media/images Folder
Contains the images stored in media files.
---
### Rest all files are same the same as generated on Django Project Creation and Start App.