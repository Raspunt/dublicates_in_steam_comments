from dbCon import DublicateDb,reviewsDb

db = DublicateDb()
revDv = reviewsDb()

counts = {}
db.create_table()

for comment in revDv.get_all_column():


    text_review = comment[4]

    words = text_review.split()
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    


for count in counts:
    db.insert_dublicate(count,counts[count])
