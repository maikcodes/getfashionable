import hashlib
import datetime


class Hash:

    @staticmethod
    def generate(base_description: str, added_description: str) -> str:
        current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        new_image_name = f"{added_description}_{base_description}_{current_time}"

        image_name_hashed = f"{current_time}{hashlib.sha256(new_image_name.encode('utf-8')).hexdigest()}"

        return image_name_hashed
