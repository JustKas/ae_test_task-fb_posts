import config


class DataManager:

    @staticmethod
    def get_header_with_profile_data(header):
        new_header = header.copy()
        new_header['name'] = config.profile_name
        new_header['profile_picture_url'] = config.profile_picture_url
        return new_header

    @staticmethod
    def get_body_with_message(message_text):
        new_body = {
            'message': message_text
        }
        return new_body
