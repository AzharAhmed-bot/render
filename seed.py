from models import session,User
from faker import Faker
import random


if __name__=="__main__":
    fake=Faker()
    for i in range(30):
        user=User(
        name=fake.name(),
        email=fake.email(),
        password=random.randint(111111111,999999999)
        )
        session.add(user)
        session.commit()
        session.close()
