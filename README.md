# Shopify Infrastructure / Site Reliability Engineering Intern - Summer 2022 Challenge

[Instructions for Challenge](https://docs.google.com/document/d/1wir0XQuviR6p-uNEUPzsGvMFwqgMsY8sEjGUx74lNrg/edit)

### Installation:
1. In your local directory, create a python virtual environment using: ```python3 -m venv {name of your virtual environment}```
2. cd into the virtual environment once it is created
3. Activate the environment using: ```source bin/activate```
4. Clone this repository using: ```git clone git@github.com:karansuryadevra/shopify-infrastructure-challenge.git```
5. Install all the dependencies needed in the project using: ```pip3 install < requirements.txt```

### Run the App:
1. Ensure that your virtualenvironment is activated by running ```source bin/activate`` inside the virtual environment directory
2. Change your directory into the ```/app``` directory and run: ```python3 models.py```
3. Now run ```python3 app.py```
4. Open your browser and type in the following: ```localhost:5000```
   
### How it works:
1. This **CRUD** app has been made using Python's [Flask framework](https://flask.palletsprojects.com/en/2.0.x/) with [SQLAlchemy](https://www.sqlalchemy.org/) and [SQLite3](https://www.sqlite.org/index.html) as the backend database
2. It does **NOT** have any JS/Frontend frameworks used to beautify the website. The frontend is built using plain HTML and basically 1 line of CSS
3. The homepage will provide a list of items that are part of the inventory. This is the **Read** part of the challenge
4. If there are no items in the inventory, the user can click on the ```Insert New``` button to add some
5. Clicking on that button will allow the user to add items to the inventory. This is the **Create** part of the challenge
6. On the homepage, the user can click on the ```Details``` option next to any of the items to see further details of each individual object. This will show the Description, Count and Inventory_ID of the item
7. On the details page, the user also has the option to click on the ```Update``` option of the item
8. In this section, the user can update any of the fields belonging to the item. This is the **Update** part of the challenge
9. On the Details view of an item, the user also has the option to click on a ```Delete``` button
10. If the button is clicked, a confirmation page is displayed, and if the user clicks the ```Yes``` button, the item is deleted from the database. This is the **Delete** part of the challenge
11. There is also the option of exporting the entire list of items that is present on the homepage
12. On the homepage, the user can click on the ```Export``` button will take the user to the export page
13. When the user clicks on the ```Download!``` which will automatically download a **CSV** file containing all the items in the inventory. This is the **Push a button export product data to a CSV** part of the challenge
14. The CSV export was made possible by exporting the SQLite database and converting it into a [Pandas](https://pandas.pydata.org/) dataframe and then writing to the CSV module
15. To stop the app, the user can just press ```Ctrl+C```
16. The user can then run: ```deactivate``` to exit the virtual environment

### You can view the screnshots of the website [here](./screenshots)