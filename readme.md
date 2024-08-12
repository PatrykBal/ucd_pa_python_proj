## My Python / Flask Project

### My python project is based on a personal portfolio web app that also hosts a blog.

* Github repo link : https://github.com/PatrykBal/ucd_pa_python_proj
* Render link: https://ucd-pa-python-proj.onrender.com

## Overview of each page

### Base / base.html

#### On this page you can find the navigation bar and footer. This was used to later tranfer into all the other pages using jinja templating. The only href link working on the navbar are the Jake Robinson for index.html and Blog for blog.html.

### Home Page / index.html

#### On this you can find the navbar and footer from base.html but also hero section with welcome message and below it a video slider. Slider was made using owl carousel.

### Blog / blog.html 

#### On this page you can find section 1 with welcome message to the blog. You can also find a button which brings you to the login page. You should also be able to see blog posts which were stored in the posts.csv file but I couldnt get  it working .

### Login / login.html

#### On this page you can find the login form. This login form validates the input and gives a message for invalid password or username. To log in use username - 'Patryk' and password '123' other users are found in app.py database section.

### Logout / logout.html

####  After login you are brought to logout.html and welcomed with a message using your login username. here you can find the logout button or create new post button.

### Create post / create.html

#### Here you can find a create post form which is connected to posts.csv which then stores the input from the form.

#### All the python code can be found in app.py and blog.py

#### Everything else isn't really functioning. 