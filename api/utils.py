import random
import string
from .models import Key


def generate_random_key():
    return "".join(random.choices(string.ascii_letters + string.digits, k=4))


def create_random_key():
    new_key = generate_random_key()
    try:
        key = Key.objects.create(key=new_key)
    except Exception:
        create_random_key()
    return key