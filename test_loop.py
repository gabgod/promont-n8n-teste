import requests
import time


# url do webhoook
url = ""

payload = [
    {
        "device_id": "RS-CADEADO-01",
        "user_report": "Fechei o cadeado mas o app diz que está aberta.",
        "event_batch": [
            {
                "timestamp": "2026-02-19T10:05:00Z",
                "alarm_id": 32,
                "value": 0
            },
            {
                "timestamp": "2026-02-19T10:00:00Z",
                "alarm_id": 32,
                "value": 1
            }
        ]
    },
    {
        "device_id": "RS-CADEADO-02",
        "user_report": "Sai agora do local.",
        "event_batch": [
            {
                "timestamp": "2026-02-19T10:02:00Z",
                "alarm_id": 33,
                "value": 0
            }
        ]
    },
    {
        "device_id": "RS-CADEADO-01",
        "user_report": "Travei o cadeado mas o app diz que está destravado.",
        "event_batch": [
            {
                "timestamp": "2026-02-19T10:02:00Z",
                "alarm_id": 33,
                "value": 0
            }
        ]
    },
    {
        "device_id": "RS-CADEADO-02",
        "user_report": "Sai agora do local.",
        "event_batch": [
            {
                "timestamp": "2026-02-19T10:02:00Z",
                "alarm_id": 32,
                "value": 1
            }
        ]
    },
    {
        "device_id": "RS-CADEADO-03",
        "user_report": "Travei o cadeado mas o app diz que está destravado.",
        "event_batch": [
            {
                "timestamp": "2026-02-19T10:01:00Z",
                "alarm_id": 32,
                "value": 0
            },
            {
                "timestamp": "2026-02-19T10:05:00Z",
                "alarm_id": 33,
                "value": 1
            }
        ]
    }
]
headers = {"content-type": "application/json"}

while True:
    response = requests.post(url, json=payload, headers=headers)
    time.sleep(60)