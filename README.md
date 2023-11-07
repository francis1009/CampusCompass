# CampusCompass

Github Repository Public Link: https://github.com/francis1009/CampusCompass


## Team
<a href="https://github.com/aredtomato">Jon Tiong Jun Wei</a>

<a href="https://github.com/mchangye">Chang Yu Ern Matthew</a>

<a href="https://github.com/XDarner">Darren Chan Kai Jie</a>

<a href="https://github.com/francis1009">Valdez Francis Gabriel Manalo</a>

<a href="https://github.com/chloekoh2003">Chloe Koh</a>

## Technologies
Python
Flask
BeautifulSoup4
MySQL
HTML
CSS
JavaScript
Vue.Js Framework

## Steps to deploy application locally

### Step 1: Database Setup

## 
There are 3 Methods of setting up the database:
    Method 1: calling the database through the webscraper with the "Run without debugging" button
    Method 2: calling the database through the webscraper through the terminal
    Method 3: importing the csv files directly (only used in a worst case scenario)

1. Run the School_Database.sql to create the schema singaporeschools and the Database Tables. Ensure that your root username is "localhost:3306" and that root password is ''. If not, please run this SQL statement on your SQL server: SET PASSWORD FOR root@localhost='';
2. Method 1:, Run the webscraper file legit_webscraper.py by clicking on "Run without debugging". The process will take about 1 minute to fully scrape and load the data into the SQL files
3. Method 2: If "Run without debugging" returns an error, run the webscraper file on the terminal using the command python legit_webscraper.py. 
4. Once running, run the sql file Alter_tables.sql to populate the remaining data
5. Method 3: If both "Run without debugging" and "terminal" methods still do not work, attached in this repo is a zipped folder with all 8 of the tables converted into csv files. They are located in the folder called "Database Data". Please extract the csv files and import the csv files directly into mysql workbench. 
6. INSERT INSTRUCTIONS ON HOW TO IMPORT

### Step 2: Flask API Setup
1. Open a new terminal
2. Run python app.py

## Step 3: Frontend Setup

```sh
npm install
npm run dev
```

### Step 4: Open Frontend Interface
Click on http://127.0.0.1:5173/ to access the UI.


## To use the OneMap API
To enjoy the full functionalities of our Application, the OneMap API has to be enabled
The OneMap Routing function requires the use of an API token to access

To gain access to the API Token:
1. Go to OneMap API's website: https://www.onemap.gov.sg/apidocs/
2. Register for an Account: https://www.onemap.gov.sg/apidocs/register
3. Upon registering, go to the 'Verify Confirmation Page' and enter your details along with your confirmation code
4. Upon successfully confirming your account, you will be redirected to your API Key.
5. The API key is only valid for 3 days and has to be renewed beyond the 3 days
