# Fapro Challenge
### Author: Jorge Arredondo Esparza

### Email: jorge.arredondo.e@gmail.com

This challenge consists in the creation of an API that with a specific date can give you the value of the UF for that date. Instructions for the Challenge [HERE](https://gist.github.com/lhidalgo42/47c2c1ea4ddbfd50e4b0acd82c24bc23).

### To run this project:

Install python 3 😄

**Use the terminal:**

Clone this project:
```
  git clone [THISPROJECT]
```
Create virtual environment:
```
  python3 -m venv [venvName]
```
Activate venv:

- Windows: 
```
  [venvName]\Scripts\activate
```
- Mac or Linux:
```
  source [venvName]/bin/activate
```
Install requirements.txt libraries for python:
```
  pip3 install -r requirements.txt
```

Initiate django app
```
  cd UFTracker
  python3 manage.py runserver
```
Now that the app is running you can manually access the different endpoints available:

- API Root: `http://127.0.0.1:8000/`
- Uf List: `http://127.0.0.1:8000/uf/`
- Uf Detail Api: `http://127.0.0.1:8000/uf/DD-MM-YYYY/`

For the Uf Detail Api the date must be in the format `DD-MM-YYYY` to receive a `200` Response.
The Uf List will not show any data unless the Uf Detail Api endpoint is called first. This is because the scrapper (beautifulsoup4) will search and update the database with the whole year of UF data of the year that is requested.

For example:

I request `http://127.0.0.1:8000/uf/01-02-2022` and the scrapper will search for the data and update the django UF table with the whole year 2022. Now i can request `http://127.0.0.1:8000/uf/` and it will list the data of year 2022 (and the other data that already was stored in the table). If i do a request for the same year (`http://127.0.0.1:8000/uf/20-06-2022`) the scrapper will not search for the data again, because it already exists in the database.

Also I included a Postman Collection named `UF-Endpoints.postman_collection.json` that can be imported in Postman and used to request the API (Remember to run the app to try this examples).

Now Enjoy 😎


#### Unit Tests:
To run the Unit Tests you must be located in the `desafio-fapro\UFTracker` directory and run the following line in the terminal:
```
  python3 manage.py test
```
If everything is working OK the 8 tests should run without problem 👍


# IMPORTANT DON'T USE THIS PROJECT IN PRODUCTION
This code was made with the intention to run locally only, because the SECRET_KEY for the django project is public in this repository
