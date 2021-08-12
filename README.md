README for TASK AKVELON PYTHON SDE CANDIDATE
Readme will organize by step. 

First task
1. How I use Anaconda Prompt, first step is based on defining environment. 
>>conda create -n ex #where 'ex' is the name of your new conda environment
2. Afer we define environment, we need to activate them.
>>conda activate ex
3. Install django
>>conda instal -c conda-forge django 
4. Create project
>>django-admin createproject 'project'
5. Create app in project directory
>>python manage.py startapp 'app'
For this task I use visual code editor because I never use Swagger. 

Steps in Visual Code Editor
1. Add app in setings.py "INSTALED APPS". After that, we can change database, in PostgreSQL or MySQL. By Default is sqlite3.
2. Add path from app in urls.py of project.
3. Define new urls.py file in app folder.
4. Create models in models.py. We create models which are based on SQL tables.
5. After we make models, we apply function for creating tables in django
>>python manage.py makemigrations
>>python manage.py migrate
Now, we have table which we use in next steps.
In this task, we use function for ordinary operation. However, this operation we can perform using django admin site.
6. Create function in views.py for different operatons. 
For example we create function for create, update, edit, delete information and function for sorting and show all information about entity.
7. Define path from all function in urls.py file.
8. Create forms.py file in app and make class forms for our entity. 
We will use that forms class for performin function form view. 
9. On the end of first task, we need define templates. That templates will use html language.
10. I create just one template for add transaction like example applying this function. 

Second task
Implement function which will return n'th number of Fibonaci sequence.
1. Read about Fibonaci sequence
2. Define function using formula for fabonaci sequence.
3. Apply this on some example. (I was not do this step.)

Last step will set our task on github
1. Create repisotory
2. Clone our file
