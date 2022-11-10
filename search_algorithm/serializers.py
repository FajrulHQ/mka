from rest_framework import serializers
from search_algorithm import locations


class ShortestPathSerializer(serializers.Serializer):
    CHOICES = []
    for loc in [x["location"] for x in locations]:
      CHOICES.append((loc, loc))
    METHOD_CHOICES = [('greedy', 'Greedy'), ('A*', 'A*')]
    city = serializers.ChoiceField(required=True, choices=CHOICES, help_text='starting city to bucharest')
    method = serializers.ChoiceField(required=True, choices=METHOD_CHOICES, help_text='search algorithm method between greedy or A*')

    class Meta:
        fields = '__all__'
