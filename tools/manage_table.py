'''
Creates a DynamoDb table for the main data store.

This tool takes two optional command line arguments, an action
that defaults to 'create' and a table name that defaults to
'movie_reviews'. To run it, try something like this:
    `python -m tools.manage_table create movie_reviews_test`
'''
import logging
import sys

from tools.infra.database_manager import DatabaseManager

if __name__ == '__main__':
    command_line_args = sys.argv[1:]
    action = 'create'
    table_name = 'movie_reviews'
    if len(command_line_args) == 2:
        action = command_line_args[0]
        table_name = command_line_args[1]

    status = "UNKNOWN"
    if action == 'create':
        status = DatabaseManager(
            "http://localhost:8000").create_reviews_table(table_name)
    elif action == 'delete':
        DatabaseManager().delete_table(table_name)
        status = 'DELETED'

    logging.info("Table status:", status)
