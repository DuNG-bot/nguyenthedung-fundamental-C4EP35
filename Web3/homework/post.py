import pymongo
client = pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.c4e

db.posts.insert_one({
    "title": "Dear Python :_(",
    "author":"Nguyễn Thế Dũng",
    "content": "Chót học tới buổi thứ 10 r thì đành tiến nốt vậy...\nNever not be afraid of Python"
})
