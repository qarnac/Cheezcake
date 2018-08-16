
class getItem():
    def getStr():
        q = DataItem.query(DataItem.category == 'music')
        q = q.order(DataItem.ranking)
        string += "<li>" + str(p.ranking) + ": " + p.title + " by " + p.info + "</li>\n"
