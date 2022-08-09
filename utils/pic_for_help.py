import requests

def get_info_pic():
    photo = 'https://static3.gamerantimages.com/wordpress/wp-content/uploads/2020/11/YouTube-Logo-Black-Header.jpg'
    response = requests.get(photo)
    return response.content