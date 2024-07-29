import logging
from abc import ABC, abstractmethod
from typing import Any


from libs.search_criteria_parser.SearchCriteriaParser import (
    SearchCriteria,
)


class S3ObjectSearcher(ABC):
    """
    Class which searches an S3 bucket based on a passed search criteria.
    """

    def __init__(self, s3_client: Any) -> None:
        self._s3_client = s3_client

    def search_bucket(self, search_criteria: SearchCriteria) -> list[str]:
        """
        Searches the bucket based on the search criteria and returns a list
        containing the paths of all bucket objects which match the criteria.
        """
        paginator = self._s3_client.get_paginator("list_objects_v2")
        response_iterator = paginator.paginate(
            Bucket=search_criteria.s3_bucket_name,
            Prefix=search_criteria.s3_object_prefix,
            # Delimiter="/",
        )

        result = []

        for response in response_iterator:
            for obj in response["Contents"]:
                object_key = obj["Key"]

                if self.object_matches_criteria(
                    object_key=object_key, search_criteria=search_criteria
                ):
                    logging.debug(
                        "Object key %s matches search criteria. Adding it to the result...",
                        object_key,
                    )
                    result.append(object_key)
                else:
                    logging.debug(
                        "Object key %s does not match the search criteria. Not adding it to the result..."
                    )

        return result

    @abstractmethod
    def object_matches_criteria(
        self, object_key: str, search_criteria: SearchCriteria
    ) -> bool:
        """
        Check if the object matches the search criteria.
        """
