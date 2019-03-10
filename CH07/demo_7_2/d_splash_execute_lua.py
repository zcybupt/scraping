import requests
from urllib.parse import quote

lua = """
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status = response.status
        }
end
"""

# 使用 quote() 方法将脚本进行 URL 转码
url = 'http://137.100.100.128:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
