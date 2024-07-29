from dataclasses import dataclass


@dataclass
class SearchCriteria:
    """
    Search criteria class containing all options parsed
    from the passed program arguments.
    """

    s3_bucket_name: str
    substring: str
    result_output_file_path: str
    s3_object_prefix: str = ""
