#!/usr/bin/env nix-shell
# ! nix-shell -p python39 --run python

import sqlite3
import urllib.request

con = sqlite3.connect("data.db")


def create_table():
    # При подключении к базе, автоматически создается realty.db
    #connection = sqlite3.connect('category.db')
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jsonfeed_raw(
    feed_url TEXT  PRIMARY KEY, 
    scrape_date  TEXT  NOT NULL  DEFAULT (DATE('now')), 
    raw          TEXT  NOT NULL
  );
    """)
    connection.close()

def get_feed(feed_url):
    req = urllib.request.Request(feed_url, headers={"User-Agent": "Xe/feedfetch"})
    with urllib.request.urlopen(req) as response:
        cur = con.cursor()
        body = response.read()
        cur.execute("""
           INSERT INTO jsonfeed_raw
             (feed_url, raw)
           VALUES
             (?, json(?))
        """, (feed_url, body))
        con.commit()
        print("got feed %s" % (feed_url))


#create_table()
get_feed("https://christine.website/blog.json")

# CREATE TABLE IF NOT EXISTS jsonfeed_raw
#   ( feed_url     TEXT  PRIMARY KEY
#   , scrape_date  TEXT  NOT NULL  DEFAULT (DATE('now'))
#   , raw          TEXT  NOT NULL
#   );
