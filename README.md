# CampusCompass

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Team
<a href="">Jon Tiong Jun Wei</a>

<a href="">Chang Yu Ern Matthew</a>

<a href="">Darren Chan Kai Jie</a>

<a href="">Valdez Francis Gabriel Manalo</a>

<a href="">Chloe Koh</a>


## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Steps to deploy application locally
## Step 1: Frontend Setup

```sh
npm install
npm run dev
```

### Step 2: Backend Setup

## 

1. Run the School_Database.sql to create the schema singaporeschools. Ensure that your root username is "localhost:3306" and that root password is ''.
2. Method 1:, Run the webscraper file legit_webscraper.py by clicking on "Run without debugging". The process will take about 1 minute to fully scrape and load the data into the SQL files
3. Method 2: If "Run without debugging" returns an error, run the webscraper file on the terminal using the command python legit_webscraper.py. 
4. Once running, run the sql file Alter_tables.sql to populate the remaining data
5. Method 3: If both "Run without debugging" and "terminal" methods still do not work, attached in this repo is a folder with all 8 of the tables converted into csv files. Please import the csv files directly into mysql workbench. 
6. INSERT INSTRUCTIONS ON HOW TO IMPORT

### Step 3: Flask Setup
1. Open a new terminal
2. Run python app.py

### Step 4: Open Frontend Interface
Click on http://127.0.0.1:5173/ to access the UI.




### Compile and Minify for Production

```sh
npm run build
```
