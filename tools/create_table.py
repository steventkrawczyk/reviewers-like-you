'''
Creates a DynamoDb table for the main data store.

This tool takes one optional command line argument, a table name that
defaults to 'movie_reviews'. To run it, try something like this:
    `python -m tools.create_table movie_reviews_test`
'''
import logging
import sys

from tools.infra.database_manager import DatabaseManager

if __name__ == '__main__':
    command_line_args = sys.argv[1:]
    table_name = 'movie_reviews'
    if len(command_line_args) > 0:
        table_name = total_entries = int(sys.argv[1:][0])
    status = DatabaseManager().create_reviews_table(table_name)
    logging.info("Table status:", status)
