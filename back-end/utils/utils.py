'''

    return data after running mongodb cmd

'''
from settings import db
from definitions import MongoDBStaticData


def mongodb_cmd_cases(cmd, cmd_id, new_data, session=None):
    query = list(db.listingsAndReviews.find().limit(10))

    #print(query)

    print(cmd)

    query_data_indexed = {}
    for item in query:
        item_id = item['_id']
        item.pop('_id')
        query_data_indexed[item_id] = item



    match cmd:
        case "INSERT":
            assert (new_data.get("_id") is not None)
            new_data_adj = {new_data['_id']: new_data}
            new_data_adj[new_data['_id']].pop('_id')
            query_data_indexed.append(new_data_adj)
            return query_data_indexed
        case "FIND":
            return query_data_indexed
        case "UPDATE":
            assert (cmd_id is not None)
            query_data_indexed[cmd_id] = new_data
            return query_data_indexed
        case "DELETE":
            del query_data_indexed[cmd_id]
            return query_data_indexed

        # There is an error
        case _:
            raise Exception("None of the cases were matched")

