from faker import Faker

class GeneratedData(object):
    GENERATED_TITLE = ''
    GENERATED_DESCRIPTION = ''

    @staticmethod
    def get_new_title():
        new_title = Faker().administrative_unit()
        GeneratedData.GENERATED_TITLE = new_title
        return new_title

    @staticmethod
    def get_new_description():
        new_description = Faker().address()
        GeneratedData.GENERATED_BODY = new_description
        return new_description





