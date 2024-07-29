import logging

from libs.search_criteria_parser.SearchCriteriaParser import (
    SearchCriteria,
)

from .S3ObjectSearcher import S3ObjectSearcher


class S3SubstringSearcher(S3ObjectSearcher):
    """
    Searches for objects containing substring.
    """

    def object_matches_criteria(
        self, object_key: str, search_criteria: SearchCriteria
    ) -> bool:
        """
        Check if the object matches the search criteria. In this case we check if the
        object contains the substring from the search criteria. If it does, we return True.
        If it does not, we return False.
        """

        object_content = self._read_s3_object(
            s3_bucket_name=search_criteria.s3_bucket_name, key=object_key
        )

        result = search_criteria.substring in object_content

        logging.debug(
            "Object key %s with content %s has substring %s: %r",
            object_key,
            object_content,
            search_criteria.substring,
            result,
        )

        return result

    def _read_s3_object(self, s3_bucket_name: str, key: str):
        obj = self._s3_client.get_object(
            Bucket=s3_bucket_name,
            Key=key,
        )

        with obj["Body"] as stream:
            return stream.read().decode("utf-8")
