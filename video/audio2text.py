import json
import time
import urllib.parse
import urllib.request


# curl "https://app.xunjiepdf.com/api/v4/uploadpar" ^
# -H "Connection: keep-alive" ^
# -H "sec-ch-ua: ^\^" Not;A Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"91^\^", ^\^"Chromium^\^";v=^\^"91^\^"" ^
# -H "Accept: application/json, text/javascript, */*; q=0.01" ^
# -H "X-Requested-With: XMLHttpRequest" ^
# -H "sec-ch-ua-mobile: ?1" ^
# -H "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36" ^
# -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" ^
# -H "Origin: https://app.xunjiepdf.com" ^
# -H "Sec-Fetch-Site: same-origin" ^
# -H "Sec-Fetch-Mode: cors" ^
# -H "Sec-Fetch-Dest: empty" ^
# -H "Referer: https://app.xunjiepdf.com/voice2text/" ^
# -H "Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7" ^
# -H "Cookie: xunjieUserTag=98F0CBB05248B0FB6ED5B487D49F4752; site_redirect_loginuri=https^%^3A//app.xunjiepdf.com/voice2text/; _ga=GA1.2.1632791774.1624503980; _gid=GA1.2.2015745962.1624503980; OUTFOX_SEARCH_USER_ID_NCOO=1563871560.1974661; appdownhide=1; xunjieTempFileList=7e96eef5ccb3448cbf2d85044b2f1e13^%^7c0ce8ca7c41de474ea9ac387e99c653f5; Hm_lvt_6c985cbff8f72b9fad12191c6d53668d=1624503980,1624505334; _gat_gtag_UA_117273948_9=1; Hm_lpvt_6c985cbff8f72b9fad12191c6d53668d=1624508905" ^
# --data-raw "tasktype=voice2text&limitsize=20480&filename=346304426-1-208.mp3&filecount=1&isshare=1&timestamp=1624508905&softname=pdfonlineconverter&softversion=V4.1.9.0&machineid=98F0CBB05248B0FB6ED5B487D49F4752&productid=146&validpagescount=20&filesrotate=0&filesequence=0&fanyi_from=zh-CHS&datasign=d8096e1b5813d086591bd61befdaae3b" ^
# --compressed


# curl "https://app.xunjiepdf.com/api/v4/uploadfile?tasktag=0bd2b06ce2bb4b0b937e51ef1850d09c&timestamp=1624514705&tasktoken=124e90699336e726ee37d9a8515e1f20&fileindex=0&chunks=2&chunk=0&id=WU_FILE_0&name=audio.mp3&type=audio^%^2Fmpeg&lastModifiedDate=Thu+Jun+24+2021+11^%^3A08^%^3A48+GMT^%^2B0800+(^%^E4^%^B8^%^AD^%^E5^%^9B^%^BD^%^E6^%^A0^%^87^%^E5^%^87^%^86^%^E6^%^97^%^B6^%^E9^%^97^%^B4)&size=4863564" ^
# -H "Connection: keep-alive" ^
# -H "sec-ch-ua: ^\^" Not;A Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"91^\^", ^\^"Chromium^\^";v=^\^"91^\^"" ^
# -H "sec-ch-ua-mobile: ?1" ^
# -H "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36" ^
# -H "Accept: */*" ^
# -H "Origin: https://app.xunjiepdf.com" ^
# -H "Sec-Fetch-Site: same-origin" ^
# -H "Sec-Fetch-Mode: cors" ^
# -H "Sec-Fetch-Dest: empty" ^
# -H "Referer: https://app.xunjiepdf.com/voice2text/" ^
# -H "Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7" ^
# -H "Cookie: xunjieUserTag=98F0CBB05248B0FB6ED5B487D49F4752; site_redirect_loginuri=https^%^3A//app.xunjiepdf.com/voice2text/; _ga=GA1.2.1632791774.1624503980; _gid=GA1.2.2015745962.1624503980; OUTFOX_SEARCH_USER_ID_NCOO=1563871560.1974661; appdownhide=1; Hm_lvt_6c985cbff8f72b9fad12191c6d53668d=1624503980,1624505334; xunjieTempFileList=87fbc4af9f7141da8a70001f675ffd0c^%^7cf87142a187244fb89428e56b81d1e573^%^7c7e96eef5ccb3448cbf2d85044b2f1e13^%^7c0ce8ca7c41de474ea9ac387e99c653f5; Hm_lpvt_6c985cbff8f72b9fad12191c6d53668d=1624514697; _gat_gtag_UA_117273948_9=1" ^
# --data-raw ^"ID3^^


# curl "https://app.xunjiepdf.com/api/v4/taskstate" ^
# -H "Connection: keep-alive" ^
# -H "sec-ch-ua: ^\^" Not;A Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"91^\^", ^\^"Chromium^\^";v=^\^"91^\^"" ^
# -H "Accept: application/json, text/javascript, */*; q=0.01" ^
# -H "X-Requested-With: XMLHttpRequest" ^
# -H "sec-ch-ua-mobile: ?1" ^
# -H "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36" ^
# -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" ^
# -H "Origin: https://app.xunjiepdf.com" ^
# -H "Sec-Fetch-Site: same-origin" ^
# -H "Sec-Fetch-Mode: cors" ^
# -H "Sec-Fetch-Dest: empty" ^
# -H "Referer: https://app.xunjiepdf.com/voice2text/" ^
# -H "Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7" ^
# -H "Cookie: xunjieUserTag=98F0CBB05248B0FB6ED5B487D49F4752; site_redirect_loginuri=https^%^3A//app.xunjiepdf.com/voice2text/; _ga=GA1.2.1632791774.1624503980; _gid=GA1.2.2015745962.1624503980; OUTFOX_SEARCH_USER_ID_NCOO=1563871560.1974661; appdownhide=1; Hm_lvt_6c985cbff8f72b9fad12191c6d53668d=1624503980,1624505334; Hm_lpvt_6c985cbff8f72b9fad12191c6d53668d=1624514697; _gat_gtag_UA_117273948_9=1; xunjieTempFileList=0bd2b06ce2bb4b0b937e51ef1850d09c^%^7c87fbc4af9f7141da8a70001f675ffd0c^%^7cf87142a187244fb89428e56b81d1e573^%^7c7e96eef5ccb3448cbf2d85044b2f1e13^%^7c0ce8ca7c41de474ea9ac387e99c653f5" ^
# --data-raw "deviceid=6D9C203026C052962969BE673946197F&productinfo=1245A2A101F776005F2E909C29CC8F7369FAA0BED21AE0A9F9ADBD8D49EE3783&timestamp=1624514709&tasktag=0bd2b06ce2bb4b0b937e51ef1850d09c&datasign=5bce766c5579e969ec59e51363a54c26" ^
# --compressed




# curl "https://app.xunjiepdf.com/api/v4/taskdown" ^
# -H "Connection: keep-alive" ^
# -H "sec-ch-ua: ^\^" Not;A Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"91^\^", ^\^"Chromium^\^";v=^\^"91^\^"" ^
# -H "Accept: application/json, text/javascript, */*; q=0.01" ^
# -H "X-Requested-With: XMLHttpRequest" ^
# -H "sec-ch-ua-mobile: ?1" ^
# -H "User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36" ^
# -H "Content-Type: application/json; charset=UTF-8" ^
# -H "Origin: https://app.xunjiepdf.com" ^
# -H "Sec-Fetch-Site: same-origin" ^
# -H "Sec-Fetch-Mode: cors" ^
# -H "Sec-Fetch-Dest: empty" ^
# -H "Referer: https://app.xunjiepdf.com/voice2text/" ^
# -H "Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7" ^
# -H "Cookie: xunjieUserTag=98F0CBB05248B0FB6ED5B487D49F4752; site_redirect_loginuri=https^%^3A//app.xunjiepdf.com/voice2text/; _ga=GA1.2.1632791774.1624503980; _gid=GA1.2.2015745962.1624503980; OUTFOX_SEARCH_USER_ID_NCOO=1563871560.1974661; appdownhide=1; Hm_lvt_6c985cbff8f72b9fad12191c6d53668d=1624503980,1624505334; Hm_lpvt_6c985cbff8f72b9fad12191c6d53668d=1624514697; xunjieTempFileList=0bd2b06ce2bb4b0b937e51ef1850d09c^%^7c87fbc4af9f7141da8a70001f675ffd0c^%^7cf87142a187244fb89428e56b81d1e573^%^7c7e96eef5ccb3448cbf2d85044b2f1e13^%^7c0ce8ca7c41de474ea9ac387e99c653f5" ^
# --data-raw "^{^\^"productinfo^\^":^\^"1245A2A101F776005F2E909C29CC8F7369FAA0BED21AE0A9F9ADBD8D49EE3783^\^",^\^"deviceid^\^":^\^"98F0CBB05248B0FB6ED5B487D49F4752^\^",^\^"timestamp^\^":1624516637,^\^"tasktag^\^":^\^"0bd2b06ce2bb4b0b937e51ef1850d09c^\^",^\^"downtype^\^":2,^\^"brandname^\^":^\^"-^迅^捷PDF^转^换^器^\^",^\^"datasign^\^":^\^"fac20a7fdca978b618b8d13ea5661884^\^"^}" ^
# --compressed


def pre_upload():
    data = {
        "tasktype": "voice2text",
        "limitsize": 20480,
        "filename": "audio.mp3",
        "filecount": 1,
        "isshare": 1,
        "timestamp": 1624554697,
        "softname": "pdfonlineconverter",
        "softversion": "V4.1.9.0",
        "machineid": "98F0CBB05248B0FB6ED5B487D49F4752",
        "productid": 146,
        "validpagescount": 20,
        "filesrotate": 0,
        "filesequence": 0,
        "fanyi_from": "zh-CHS",
        "datasign": "692faa64ac637bafcc6064b37c5d1bbc",
    }

    req = urllib.request.Request(url="https://app.xunjiepdf.com/api/v4/uploadpar",
                                 data=urllib.parse.urlencode(data).encode('utf-8'))
    resp = urllib.request.urlopen(req)
    body_str = resp.read().decode("utf-8")
    meta = json.loads(body_str)
    return meta


def upload_chunk(tasktag, timestamp, tasktoken, chunks, chunk, size, data):
    headers = {
        "Content-Length": size,
        "Cookie": "xunjieUserTag=98F0CBB05248B0FB6ED5B487D49F4752; site_redirect_loginuri=https%3A//app.xunjiepdf.com/voice2text/; _ga=GA1.2.1632791774.1624503980; _gid=GA1.2.2015745962.1624503980; OUTFOX_SEARCH_USER_ID_NCOO=1563871560.1974661; appdownhide=1; Hm_lvt_6c985cbff8f72b9fad12191c6d53668d=1624503980,1624505334; xunjieTempFileList=0bd2b06ce2bb4b0b937e51ef1850d09c%7c87fbc4af9f7141da8a70001f675ffd0c%7cf87142a187244fb89428e56b81d1e573%7c7e96eef5ccb3448cbf2d85044b2f1e13%7c0ce8ca7c41de474ea9ac387e99c653f5; Hm_lpvt_6c985cbff8f72b9fad12191c6d53668d=1624517381; _gat_gtag_UA_117273948_9=1"
    }
    req = urllib.request.Request(
        url=f"https://app.xunjiepdf.com/api/v4/uploadfile?tasktag={tasktag}&timestamp={timestamp}&tasktoken={tasktoken}&fileindex=0&chunks={chunks}&chunk={chunk}&id=WU_FILE_0&name=audio.mp3&type=audio^%^2Fmpeg&lastModifiedDate=Thu+Jun+24+2021+11^%^3A08^%^3A48+GMT^%^2B0800+(^%^E4^%^B8^%^AD^%^E5^%^9B^%^BD^%^E6^%^A0^%^87^%^E5^%^87^%^86^%^E6^%^97^%^B6^%^E9^%^97^%^B4)&size={size}",
        headers=headers,
        data=data)
    resp = urllib.request.urlopen(req)
    body_str = resp.read().decode("utf-8")
    upload_result = json.loads(body_str)
    return upload_result


def task_down(tasktag):
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    data = {"productinfo":"1245A2A101F776005F2E909C29CC8F7369FAA0BED21AE0A9F9ADBD8D49EE3783","deviceid":"98F0CBB05248B0FB6ED5B487D49F4752","timestamp":1624516637,"tasktag":tasktag,"downtype":2,"brandname":"-迅捷PDF转换器","datasign":"fac20a7fdca978b618b8d13ea5661884"}


    req = urllib.request.Request(url="https://app.xunjiepdf.com/api/v4/taskdown",
                                 headers=headers,
                                 data=urllib.parse.urlencode(data).encode('utf-8'))
    resp = urllib.request.urlopen(req)
    body_str = resp.read().decode("utf-8")
    down_result = json.loads(body_str)
    return down_result


# def task_state(tasktag, timestamp, tasktoken, chunks, chunk, size, data):
#     data = {
#         "deviceid": "6D9C203026C052962969BE673946197F",
#         "productinfo": "1245A2A101F776005F2E909C29CC8F7369FAA0BED21AE0A9F9ADBD8D49EE3783",
#         "timestamp": 1624514709,
#         "tasktag": "0bd2b06ce2bb4b0b937e51ef1850d09c",
#         "datasign": "5bce766c5579e969ec59e51363a54c26",
#     }
#
#     req = urllib.request.Request(url="https://app.xunjiepdf.com/api/v4/uploadpar",
#                                  data=urllib.parse.urlencode(data).encode('utf-8'))
#     resp = urllib.request.urlopen(req)
#     body_str = resp.read().decode("utf-8")
#     meta = json.loads(body_str)
#     return meta
#     }
#
#     req = urllib.request.Request(url="https://app.xunjiepdf.com/api/v4/uploadpar",
#     data = urllib.parse.urlencode(data).encode('utf-8'))
#     resp = urllib.request.urlopen(req)
#     body_str = resp.read().decode("utf-8")
#     meta = json.loads(body_str)
#
#
# return meta


def split_data(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    length = 3 * 1024 * 1024
    chunks = [data[i:i + length] for i in range(0, len(data), length)]
    return chunks


def audio2text(filepath):
    meta = pre_upload()

    if meta["code"] != 10000:
        print(meta)
        return
    print(f"pre upload 成功 {meta}")

    chunks = split_data(filepath)
    for i in range(0, len(chunks)):
        upload_result = upload_chunk(meta["tasktag"], meta["timestamp"], meta["tasktoken"], len(chunks), i,
                                     len(chunks[i]), chunks[i])
        if upload_result["code"] != 10000:
            print(f"上传chunk {i} 失败 {upload_result}")
            return
        print(f"上传chunk {i} 成功 {upload_result}")

    time.sleep(30)

    down_result = task_down(meta["tasktag"])
    print(down_result)


if __name__ == '__main__':
    # meta = pre_upload("346304426-1-208.mp3")
    # print(meta)

    audio2text("I:\\素材\\audio.mp3")
