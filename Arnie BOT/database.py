import sqlite3
conn = sqlite3.connect('database1.db')
c = conn.cursor()
def create_table():
  c.execute("CREATE TABLE IF NOT EXISTS TableName(normaltext TEXT, number INTEGER)")
create_table()
def insert(stl):
  c.execute(stl)
  conn.commit()
stl = "INSERT INTO TableName (column1, stuff, anotherone) VALUES ('" + use-this-if-it's-an-defined-value +"', use-this-if-not)
insert(stl)
def select(sel):
  c.execute(sel)
  conn.commit()
sel = "SELECT * FROM TableName"
sel = "SELECT stuff FROM TableName"
sel = "SELECT stuff FROM TableName WHERE user_id = '" + ctx.message.author.id + "'"
select(sel)
def delete(del):
  c.execute(del)
  conn.commit()
del = "DELETE * FROM TableName"
del = "DELETE stuff FROM TableName"
del = "DELETE stuff FROM TableName WHERE state = california"
def use(us):
  c.execute(us)
  conn.commit()

@bot.command()
async def test():
  us = "SELECT * FROM TableName"
  use(us)
  await bot.say(us)
