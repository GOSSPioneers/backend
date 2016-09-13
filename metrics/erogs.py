# insert card metric
from elasticsearch_dsl import Search, Q
from elasticsearch import Elasticsearch
import json

def get_results(args):
    esclient = Elasticsearch()
    s = Search(using=esclient)
    stationcd = int(args.get('statcd', '0'))

    #END DELIVERY Received - Delivery Ended, Reason

    qq = Q("match", statcd=stationcd) & Q("match", body="END") & Q("match", body="DELIVERY") & Q("match", body="Received") & Q("match", body="Reason")
    q = s.query(qq)
    q.aggs.bucket('erog_over_time', 'date_histogram', field='timestamp', interval="hour")

    response = q.execute()
    docs = []
    for tag in response.aggregations.erog_over_time.buckets:
        docs.append({'key': tag.key, 'key_as_string': tag.key_as_string, 'count': tag.doc_count})
    return json.dumps(docs)
            
            

