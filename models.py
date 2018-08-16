from google.appengine.ext import ndb

class DataItem(ndb.Model):
    category = ndb.StringProperty(required=True)
    ranking = ndb.IntegerProperty(required=True, default=0)
    title = ndb.StringProperty(required=True)
    info = ndb.StringProperty(required=True)
    imgsrc = ndb.StringProperty(required=False)

    def save_entity(item):
        item_key = item.put()
        return item_key

    def get_entity(item_key):
        item = item_key.get()
        return item
