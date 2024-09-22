from django.utils.timezone import now
from blog.models import Post, User  # Adicione a importação de User
import factory
from faker import Faker

# Inicializa o Faker
faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super()._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
    
class PostFactory(factory.django.DjangoModelFactory):  # Corrigido aqui
    class Meta:
        model = Post  # Não esqueça de definir o modelo

    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0





