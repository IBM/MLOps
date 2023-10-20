**Mission**<br>
Convert APAC MLOps Accelerator from CP4DaaS to CP4DS

### Info
---
- Awaiting tensorflow-data-validation update for compatibility w/ py3.10


### Todo
---
- [x] Cut out all use of Cloud Object Storage ✅ 2023-10-04
- [x] Reduce use of /utils to a minimum ✅ 2023-10-04
- [x] Remove use of *seaborn/sns* ✅ 2023-10-04
- [x] **Use WML .from_token instead of api_key ✅ 2023-10-04
- [ ]
- [ ]


### Save for later
---

#### Work w/ WML on CP4DS
```python
CPD_URL = '<CPD PLATFORM URL>'
from ibm_watson_studio_lib import access_project_or_space
wslib = access_project_or_space()
wml_credentials = {
    "url": CPD_URL,
    "token": wslib.auth.get_current_token(),
    "instance_id": "wml_local",
    "version" : "4.6"
}
from ibm_watson_machine_learning import APIClient
client = APIClient(wml_credentials)
client.spaces.list()
```

#### Use Pipelines on CP4DS

```python
token = os.environ['USER_ACCESS_TOKEN']
```

[WSPipelines On-Prem Tutorial](https://github.ibm.com/Lucas-Baier/ws-pipelines-guide)