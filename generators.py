from faker import Faker


fake = Faker()

def generate_user_email():
    return f"{fake.bothify(text='?????###')}@{fake.lexify(text='????')}.{fake.lexify(text='???')}"

def generate_user_password():
    return fake.bothify(text='?????###')

def generate_user_username():
    return fake.bothify(text='?????###')