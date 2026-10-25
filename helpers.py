from generators import generate_user_data
from auth_methods import AuthMethods


def register_new_user():
    """
    Регистрация нового уникального пользователя.
    Возвращает словарь с данными и токеном.
    """
    payload = generate_user_data()
    response = AuthMethods.register_user(payload)
    
    if response.status_code != 200:
        raise Exception(f"Не удалось зарегистрировать пользователя: {response.status_code} {response.text}")
        
    payload['accessToken'] = response.json()['accessToken']
    return payload
