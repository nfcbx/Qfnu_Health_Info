import requests
import time

payload = [
    "{\"username\":\"这里填学号\",\"password\":\"这里填密码\",\"type\":\"student\"}",
    "{\"username\":\"这里填学号\",\"password\":\"这里填密码\",\"type\":\"student\"}",
    "{\"username\":\"这里填学号\",\"password\":\"这里填密码\",\"type\":\"student\"}"]

def login(payload):
    url = "http://xuegong.qfnu.edu.cn:8080/authentication/login"
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        'content-length': '62',
        'host': 'xuegong.qfnu.edu.cn:8080'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


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
    return response

for i in payload:

    print("当前用户：" + i)

    login_text = login(i).text.split('\"')

    login_status = login_text[10]

    cookie = login_text[5]

    if(login_status == ':200,'):
        print("登陆成功！开始签到", end=" ")
        for _i in range(5):
            print("..", end="")

        response_text = save(cookie=cookie).text.split('\"')

        response_message = response_text[11]

        print(response_message)
        time.sleep(5)


        ###Debug
        print("-----login------")
        for k in range(len(login_text)) :
            print(login_text[k], end="") 
        print("\n-----response-----")
        for n in range(len(response_text)) :
            print(response_text[n], end="")
        print("\n\n")
    else:
        print("登录失败！", end="")
        login_message = login_text[11]
        print(login_message)
        time.sleep(10)
        continue
