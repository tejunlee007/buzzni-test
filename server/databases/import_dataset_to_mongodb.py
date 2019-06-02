import os

import joblib
import pymongo

from server.common.config import Config

dump_data_dir = os.path.dirname(os.path.abspath(__file__))
timeline_goods_list = joblib.load(dump_data_dir + "/timeline_goods_dump.dat")

timeline_goods_list = [dict(_id=good['id'],
                            **good)
                       for good in timeline_goods_list]

print('')
print('============ raw dataset ==============')
print(timeline_goods_list)
print('COUNT: ', len(timeline_goods_list))
print('========================================')

test_mongo_client = pymongo.MongoClient(Config.MONGO_DB)


# test_mongo_client.admin.add_user('test', 'test', roles=[{'role': 'readWrite', 'db': 'mall'}])

mall_db = test_mongo_client['mall']

print('')
print('===== DROP timeline_goods COLLECTION =====')
timeline_goods_collection = mall_db["timeline_goods"]
timeline_goods_collection.drop()
print(timeline_goods_collection)
print('==========================================')

print('')
print('==== CREATE timeline_goods COLLECTION ====')
timeline_goods_collection = mall_db["timeline_goods"]

print('')
print('========== insert timeline_goods =========')
x = timeline_goods_collection.insert_many(timeline_goods_list)
print(x.inserted_ids)
print('COUNT: ', len(x.inserted_ids))
print('==========================================')

