#! python3
import json, time
lt = time.localtime()
formatted_time = time.strftime("%Y%m%d-%H%M%S")
result = {
    "time": formatted_time,
    "name": f"web-{formatted_time}"
}
print(json.dumps(result))
