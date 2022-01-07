import requests

def login():
    url = "http://xuegong.qfnu.edu.cn:8080/authentication/login"
    payload = "{\"username\":\"这里填写学号\",\"password\":\"这里填写密码\",\"type\":\"student\"}"
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'content-length': '62',
        'host': 'xuegong.qfnu.edu.cn:8080'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response

cookie = login().text.split('\"', 20)[5]
print(cookie)

def save(cookie):
    url = "http://xuegong.qfnu.edu.cn:8080/student/healthInfo/save"
    payload = "{\"home\":\"在家\",\"address\":\"\",\"keepInHome\":\"否\",\"keepInHomeDate\":null,\"keepInHomeReasonSite\":\"\",\"contact\":\"否\",\"contactType\":\"\",\"infect\":\"否\",\"infectType\":\"\",\"infectDate\":\"\",\"familyNCP\":\"否\",\"familyNCPType\":\"\",\"familyNCPDate\":\"\",\"familyNCPRelation\":\"\",\"cold\":\"否\",\"fever\":\"否\",\"feverValue\":\"\",\"cough\":\"否\",\"diarrhea\":\"否\",\"homeInHubei\":\"否\",\"arriveHubei\":\"无\",\"travel\":\"无\",\"remark\":\"无\",\"submitCount\":2,\"contactDetail\":\"\",\"location\":\"\",\"naDetection\":\"否\",\"areaInfect\":\"否\",\"areaInfectType\":\"请选择\",\"areaInfectDate\":\"\",\"areaInfectNumber\":\"请选择\",\"contactAH\":\"否\",\"contactAHDetail\":\"\",\"outProvinceBack14\":\"未出省\",\"naDetectionDate\":\"\",\"pharynxResult\":\"阴性\",\"anusResult\":\"阴性\",\"saDetection\":\"否\",\"lgMResult\":\"阴性\",\"lgGResult\":\"阴性\",\"saDetectionDate\":\"\",\"vaccinationStatus\":\"已接种_完成第2剂\"}"
    payload = payload.encode("utf-8").decode("latin1")
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'cookie': 'syt.sessionId=8ca12baa-2415-4c5b-8f8b-97b2eeda743b',
        'accept-encoding': 'gzip',
        'content-length': '836',
        'host': 'xuegong.qfnu.edu.cn:8080'
    }
    headers['cookie'] = 'syt.sessionId=' + cookie
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

save(cookie=cookie)
