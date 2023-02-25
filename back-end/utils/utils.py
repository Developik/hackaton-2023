'''

    return data after running mongodb cmd

'''
from settings import db
from definitions import MongoDBStaticData

supported_commands = ["insert", "find", "update", "delete"]

def mongodb_cmd_cases(cmd, cmd_id, new_data, session=None):
    assert(new_data.get("_id") is not None)

    query = db.listingsAndReviews.find()

    query_data_indexed = []
    for item in query:
        item.pop('_id')
        query_data_indexed[item['_id']] = item
    match supported_commands:
        case "insert":
            new_data_adj = {new_data['_id']: new_data}
            new_data_adj[new_data['_id']].pop('_id')
            query_data_indexed.append(new_data_adj)
            return query_data_indexed
        case "find":
            return query_data_indexed
        case "update":
            query_data_indexed[cmd_id] = new_data
            return query_data_indexed
        case "delete":
            del query_data_indexed[cmd_id]
            return query_data_indexed

        # There is an error
        case _:
            raise Exception("None of the cases were matched")

def execute_command(command):
    # Extract the collection name and command from user input
    try:
        _, collection_name, command_name = command.split('.')
    except ValueError:
        return "Invalid command format: Please use the format 'db.collection.command'"

    # Check if the collection exists 
    if collection_name not in db.list_collection_names():
        return f"Collection '{collection_name}' does not exist in the database"

    # Get the collection object
    collection = db[collection_name]

     # Check if the command is valid for the collection
    if any(supported_command in command_name for supported_command in supported_commands):
        # Execute the command using PyMongo
        result = list(eval(f"collection.{command_name}"))

        # Return the result as a string
        return "\n".join([str(doc) for doc in result])
  
    return f"Unsupported command '{command_name}' for collection '{collection_name}'. Valid commands are: {valid_commands}"