class ListSerializer(serializers.HyperlinkedModelSerializer):
    lists= serializers.HyperlinkedRelatedField(
        view_name='other_list',
        many=True,
        read_only=True
    )
    class Meta:
        model = List
        fields = ('owner', 'listItem')