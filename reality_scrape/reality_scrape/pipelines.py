# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class RealityScrapePipeline(object):


# setting connection to database, deleting all old data

    def __init__(self):
        self.create_connection()
        self.curr.execute(""" DELETE FROM reality_store""")

# setting connection to a postgresql database 

    def create_connection(self):

        hostname = 'localhost'
        port = '5432'
        username = 'postgres'
        password = 'SrealityScrape'
        database = 'reality1'

        # Connect to database
        
        self.conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)

        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    # inserting scraped data into database as name and img_url

    def store_in_db(self, item):
        try:
            self.curr.execute(""" insert into reality_store (name, img_url) values (%s,%s)""", (
                item["name"],
                str(item["img_url"])
            ))
        except BaseException as e:
                print(e)
        self.conn.commit()

    def close_spider(self, spider):
        
        # this part is converting all relevant data from database into HTML file

        self.curr.execute("SELECT name, img_url FROM reality_store")
        rows = self.curr.fetchall()

        with open("../../../HttpServer/realitos.html", "a", encoding="utf-8") as f:
            f.write("<html><meta charset=\"UTF-8\"><body><table>")
            for row in rows:
                f.write("<tr>")
                for column in row:
                    print(column)
                    if column.startswith("http"):
                        f.write("<td><img src='{}'></td>".format(column))
                    else:
                        f.write("<td>{}</td>".format(column))
                f.write("</tr>")
            f.write("</table></body></html>")


        # Close cursor and connection to database 
        self.curr.close()
        self.conn.close() 


