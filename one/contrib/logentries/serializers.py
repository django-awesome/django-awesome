from rest_framework.serializers import ModelSerializer


def serializer_data(instance):
    InstanceModel = instance.__class__

    class Serializer(ModelSerializer):
        class Meta:
            model = InstanceModel
            fields = "__all__"

    serializer = Serializer(instance)

    return serializer.data
