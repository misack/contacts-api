from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact

        fields = ['id', 'first_name', 'last_name', 'contact_picture', 'country_code', 'phone_number',
                   'is_favorite'
                  ]
