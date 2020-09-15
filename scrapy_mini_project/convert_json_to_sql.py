import sqlite3
import json
import datetime

quotes_file = 'quotes.json'
author_file = 'author.json'
db_file = 'scrapy_mini_project.db'

conn = sqlite3.connect(db_file)
c = conn.cursor()

data_quotes = json.load(open(quotes_file))
c.execute('CREATE TABLE quotes (quote TEXT NOT NULL, author_name TEXT NOT NULL, tags TEXT)')

for quote in data_quotes:
    tags_list = quote['tags']
    tags = ','.join(tags_list)
    data = [quote['text'], quote['author'], tags]
    c.execute('INSERT INTO quotes values (?,?,?)', data)

data_authors = json.load(open(author_file))
format_sql = '%B %d, %Y'
c.execute('CREATE TABLE authors (author_name TEXT NOT NULL, birth_date DATE NOT NULL, bio TEXT NOT NULL)')

for author in data_authors:
    birth_date = datetime.datetime.strptime(author['birthdate'], format_sql).date()
    data = [author['name'], birth_date, author['bio']]
    c.execute('INSERT INTO authors values (?,?,?)', data)

conn.commit()
