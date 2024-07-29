import json
import logging


class ResultManager:
    """
    Helper class which manages the results.
    """

    def output_result_to_file(self, result: list[str], file_name: str):
        """
        Outputs the result to a file in json format.
        """
        logging.info("Writing the result to file %s ...", file_name)

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

    def print_result(self, result: list[str]):
        """
        Prints the result to stdout
        """
        print("The result is: ", result)
