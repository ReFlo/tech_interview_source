"""
COPYRIGHT © BSH HOME APPLIANCES GROUP  2021
ALLE RECHTE VORBEHALTEN. ALL RIGHTS RESERVED.
The reproduction, transmission or use of this document or its contents is not permitted without express
written authority. Offenders will be liable for damages. All rights, including rights created by  patent
grant or registration of a utility model or design, are reserved.
"""


class InterviewSessionHandler:

    def __init__(self):
        self.cache_raw = None
        self.cache_shaped = None

    def execute(self):
        """
        This method handles the complete interview session.
        The workflow is sequenced in the following order:

        1. Load cache
        2. Shape cache
        3. Write cache to file
        """
        self.load_cache()
        self.shape_cache()
        self.write_cache_to_file()

    def load_cache(self):
        """
        This method loads the external cache.json file into the cache_raw attribute.
        """
        raise NotImplementedError

    def shape_cache(self):
        """
        This method shapes the cache_raw attribute into the cache_shaped attribute.

        Shaped structure (abstract)
        [
            '%description%_%jira%',
            '%description%_%jira%'
        ]

        Shaped structure (example)
        [
            'test_1_done',
            'test_2_done'
        ]
        """
        raise NotImplementedError

    def write_cache_to_file(self):
        """
        This method writes the cache_shaped attribute to an external shaped.txt file.
        """
        raise NotImplementedError


if __name__ == '__main__':
    applicant = InterviewSessionHandler()
    applicant.execute()
