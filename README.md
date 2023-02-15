# reality_scrape
My first web-scraping code

Command for creting table in Postgrsql database called "reality1":

CREATE TABLE reality_store(id serial PRIMARY KEY, name text, img_url text); 

Other database parameters:

        hostname = 'localhost'
        port = '5432'
        username = 'postgres'
        password = 'RealityScrape'
        database = 'reality1'


Html output is saved in folder called "HttpServer".

