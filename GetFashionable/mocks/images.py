from random import randint

api_url = 'https://picsum.photos'


def get_mock_image_url(width=250, height=700):
    return f'{api_url}/{width}/{height}.jpg'


def get_mocked_images(num_images=30):
    images = [0] * num_images
    for i in range(num_images):
        width, height = randint(100, 400), randint(200, 500)
        images[i] = {
            'width': width,
            'height': height,
            'url': get_mock_image_url(width, height)
        }

    return images
