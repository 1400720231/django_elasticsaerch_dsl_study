from django_elasticsearch_dsl import DocType, Index
from .models import PraiseUser, students

# Name of the Elasticsearch index
praise = Index('praises')
# See Elasticsearch Indices API reference for available settings
praise.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@praise.doc_type
class CarDocument(DocType):
    class Meta:
        model = PraiseUser # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'nickname',
            'mobile',
            'sex',
            'birthday',
            'country',
            'province',
            'city',

        ]
        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000




# Name of the Elasticsearch index
student = Index('students')
# See Elasticsearch Indices API reference for available settings
student.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@student.doc_type
class CarDocument(DocType):
    class Meta:
        model = students # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'nickname',
            'mobile',
            

        ]