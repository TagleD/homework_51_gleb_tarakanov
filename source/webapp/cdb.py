import random


class CatDataBase:
    name = None
    age = random.randint(1, 15)
    happiness = 10
    satiety = 40
    image = 'https://i.pinimg.com/564x/8b/07/72/8b0772f321bca2198113500167252a02.jpg'
    status = 'active'

    @classmethod
    def play(cls):
        if cls.status == 'sleep':
            cls.happiness -= 5
            cls.status = 'active'
            return 'Кота разбудили и поиграли с ним'

        cls.happiness += 15
        cls.satiety -= 10

        if random.uniform(0, 1) <= 0.33:
            cls.happiness = 0

        return 'С котом поиграли'

    @classmethod
    def eat(cls):
        if cls.status == 'sleep':
            return 'Кот спит, сейчас его нельзя покормить'
        cls.satiety += 15
        cls.happiness += 5
        if cls.satiety >= 90:
            cls.happiness -= 30
        return 'Кота покормили'

    @classmethod
    def put_to_sleep(cls):
        if cls.status == 'sleep':
            return 'Кот уже спит'
        cls.status = 'sleep'
        return 'Кота уложили спать'

    @classmethod
    def set_image(cls):
        if cls.happiness <= 10:
            cls.image = 'https://i.pinimg.com/564x/ed/40/a8/ed40a854795702d1b7989ee5798e4e45.jpg'
        if cls.happiness > 10 and cls.happiness <= 40:
            cls.image = 'https://i.pinimg.com/564x/8b/07/72/8b0772f321bca2198113500167252a02.jpg'
        if cls.happiness > 40 and cls.happiness <= 70:
            cls.image = 'https://i.pinimg.com/236x/7e/ac/0f/7eac0ff9a61ed46979169cc3b43fc04c.jpg'
        if cls.happiness > 70:
            cls.image = 'https://i.pinimg.com/236x/52/8f/82/528f82f9996ce5c20a3d6ec2c5339422.jpg'

    @classmethod
    def action(cls, action_from_form):
        if action_from_form:
            if action_from_form == 'put_to_sleep':
                message = cls.put_to_sleep()
            elif action_from_form == 'eat':
                message = cls.eat()
            else:
                message = cls.play()
            cls.set_image()
            return message

    @classmethod
    def get_status(cls):
        if cls.satiety >= 0:
            return True
        else:
            return None






