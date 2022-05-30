# ProyectoFinalViaggio


This projects was made by Matias Viaggio as a FinalProject for CoderHouse's python course.
In this project you will find a webite made for an artist.
This website conteins the following urls:
    • admin/
    • appBlog/ [name='index']
    • appBlog/ home [name='home']
    • appBlog/ adminPage [name='adminPage']
    • appBlog/ aboutDeveloper [name='aboutDeveloper']
    • appBlog/ aboutMe [name='aboutMe']
    • appBlog/ beStudent [name='beStudent']
    • appBlog/ courseAdmin [name='courseAdmin']
    • appBlog/ search/
    • appBlog/ resultadoBusqueda [name='resultadoBusqueda']
    • appBlog/ projects/ [name='projects']
    • appBlog/ apply/ [name='apply']
    • appBlog/ unauthorized [name='unauthorized']
    • appBlog/ course/list [name='courseList']
    • appBlog/ ^courseDetail(?P<pk>\d+)$ [name='CourseDetail']
    • appBlog/ ^newCourse$ [name='NewCourse']
    • appBlog/ ^courseEdit/(?P<pk>\d+)$ [name='CourseEdit']
    • appBlog/ ^courseDelete/(?P<pk>\d+)$ [name='CourseDelete']
    • appBlog/ book/list [name='bookList']
    • appBlog/ ^bookDetail/(?P<pk>\d+)$ [name='BookDetail']
    • appBlog/ ^bookEdit/(?P<pk>\d+)$ [name='BookEdit']
    • appBlog/ ^bookDelete/(?P<pk>\d+)$ [name='BookDelete']
    • appBlog/ students/list [name='studentList']
    • appBlog/ ^studentDetails/(?P<pk>\d+)$ [name='StudentDetail']
    • appBlog/ ^studentDelete/(?P<pk>\d+)$ [name='StudentDelete']
    • appBlog/ login [name='login']
    • appBlog/ register/ [name='register']
    • appBlog/ logout [name='logout']
    • appBlog/ userEdit/ [name='userEdit']

Admin:
    At this url you can access the admin panel, where you can administrate all user whit their profile images, couses, reservations, students. To access this information you will need superuser profile, the default profile is the following:

        username: admin
        password: admin

    However i strongly recomend to change this in order to create one safer.


appBlog:
    This is the default home page for those who are NOT logged in.

appBlog/home:
    This is the home page for all users who already have an account.

appBlog/adminPage:
    This page is only for superusers, here you can access the information without leaving the website, such as:
    • appBlog/ courseAdmin [name='courseAdmin']
    • appBlog/ search/
    • appBlog/ resultadoBusqueda [name='resultadoBusqueda']
    • appBlog/ course/list [name='courseList']
    • appBlog/ ^courseDetail(?P<pk>\d+)$ [name='CourseDetail']
    • appBlog/ ^newCourse$ [name='NewCourse']
    • appBlog/ ^courseEdit/(?P<pk>\d+)$ [name='CourseEdit']
    • appBlog/ ^courseDelete/(?P<pk>\d+)$ [name='CourseDelete']
    • appBlog/ book/list [name='bookList']
    • appBlog/ ^bookDetail/(?P<pk>\d+)$ [name='BookDetail']
    • appBlog/ ^bookEdit/(?P<pk>\d+)$ [name='BookEdit']
    • appBlog/ ^bookDelete/(?P<pk>\d+)$ [name='BookDelete']
    • appBlog/ students/list [name='studentList']
    • appBlog/ ^studentDetails/(?P<pk>\d+)$ [name='StudentDetail']
    • appBlog/ ^studentDelete/(?P<pk>\d+)$ [name='StudentDelete']

appBlog/about_developer:
    Here you will find the information about me (devloper).

appBlog/about_me:
    Here you will find the information about the owner of the website.

appBlog/beStudent:
    Here is where future students will aply in order to get access to some classes

appBlog/unauthorized:
    This is the view that will be display when an unauthorized user try to access appBlog/adminPage.


############################################################################################################
                                                IMPORTANT
############################################################################################################

In case you didn't read all of these, here's again the superuser username and password:

u: admin
p: admin






