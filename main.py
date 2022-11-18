from kubernetes import client, config
from kubernetes.stream import stream
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
config = client.Configuration()

config.api_key['authorization'] = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlZXRi0yc3VQa1Fjc3RHT3NUcFFIamN3ejlCQmpZclNqc21tTmtreWJhdUkifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tdzc3ZngiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjFjMDRkMjYwLTY4ZmYtNDVkMi05OGQ2LTQwYTc0NDU2MDc4YSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.PJNIDkzgHMq9Pf-1bCCRfWnPvFO-FSJ9VdzmL7rAk3ZDWb2OYxBFc3u6H78VJW6SgOILWygaWKW-12jwZVgArZlHxtJ8TXVGlc7HA1Q5g7l8ukohxqY69QAV8w-DQUC7kv6NFM4YQh355cP3LNkCihfK3Rv2UeD2DImhticb-p7t0TEElbWPVzFNpFl5wRcDfGiWMdb0IlNjySwtkwhV7XL4zPyQ5JQkNKU1YLCycwfLg23o-vQn84nc4Adg60HD7piNmw3dyDZhQJKafBL-yTtYEUQ0CFvS2ZO-AFhq2AvyU8WragVfgjk5C6SySRDKVtX-5wZAcPEGxinh0jgt2w"
config.api_key_prefix['authorization'] = 'Bearer'
config.host = 'https://192.168.50.21:6443'
config.verify_ssl=False

# api_client는 "2. 연결 정보 설정하기" 항목을 참고한다
api_client = client.CoreV1Api(client.ApiClient(config))

# 첫 번째 argument에 당신이 사용하는 namespace를 입력한다
ret = api_client.list_namespaced_pod("monitoring", watch=False)

print("Listing pods with their IPs:")

for i in ret.items:
    print(f"{i.status.pod_ip}\t{i.metadata.name}")    