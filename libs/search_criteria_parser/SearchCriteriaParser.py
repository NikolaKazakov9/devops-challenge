import argparse
import logging

from .SearchCriteria import SearchCriteria


class SearchCriteriaParser:
    """
    Search criteria parser class which creates parser with
    specific configuration and parses a SearchCriteria from the
    passed args.
    """

    def get_parser(self) -> argparse.ArgumentParser:
        """
        Creates and configures argument parser.
        """
        parser = argparse.ArgumentParser(
            description="Search for a substring in text files in an S3 bucket."
        )
        parser.add_argument(
            "s3_bucket_name", type=str, help="The name of the S3 bucket"
        )
        parser.add_argument(
            "substring",
            type=str,
            help="The substring to search for in text files",
        )

        parser.add_argument(
            "--s3_object_prefix",
            type=str,
            required=False,
            default="",
            help="Optional S3 object prefix to search in.",
        )

        parser.add_argument(
            "--result_output_file_path",
            type=str,
            required=False,
            default="",
            help="The file path where the result will be stored.",
        )

        return parser

    def parse_search_criteria_from_args(
        self, args: argparse.Namespace
    ) -> SearchCriteria:
        """
        Returns search criteria from the passed args.
        """
        return SearchCriteria(
            s3_bucket_name=args.s3_bucket_name,
            substring=args.substring,
            result_output_file_path=args.result_output_file_path,
            s3_object_prefix=args.s3_object_prefix,
        )

    def parse_search_criteria(self) -> SearchCriteria:
        """
        Creates ArgumentParser and parses SearchCriteria object from
        the args. The SearchCriteria is then returned.
        """
        arg_parser = self.get_parser()
        args = arg_parser.parse_args()

        search_criteria = self.parse_search_criteria_from_args(args)

        logging.debug("Search criteria: %r", search_criteria)

        return search_criteria
