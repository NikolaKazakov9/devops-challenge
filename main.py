"""
The main module which is the entrypoint of the script.
"""

import logging
import os
import boto3

from libs.search_criteria_parser.SearchCriteriaParser import (
    SearchCriteriaParser,
)

from libs.result_manager.ResultManager import ResultManager

from libs.s3_object_search.S3SubstringSearcher import (
    S3SubstringSearcher,
    S3ObjectSearcher,
)

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
logging.basicConfig(level=LOGLEVEL)

def main():
    """
    The main function which runs the whole script. It uses ArgumentParser
    to parse and create SearchCriteria object. It then searches for all files
    in a bucket which contain the substring based on the SearchCriteria.
    """
    search_criteria_parser = SearchCriteriaParser()
    search_criteria = search_criteria_parser.parse_search_criteria()

    s3_client = boto3.client("s3")
    object_searcher: S3ObjectSearcher = S3SubstringSearcher(s3_client=s3_client)
    result = object_searcher.search_bucket(search_criteria=search_criteria)

    result_manager = ResultManager()
    if search_criteria.result_output_file_path:
        result_manager.output_result_to_file(
            result, search_criteria.result_output_file_path
        )
    else:
        result_manager.print_result(result)

if __name__ == "__main__":
    main()
