import re,subprocess,os

class ApkInfo():

    def __init__(self,apkPath):
        self.apkPath =apkPath
    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        appKey = match.group(2)
        appVersion = match.group(3)
        return packagename, appKey, appVersion

    def getApkActivity(self):
        #p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
         #                    stderr=subprocess.PIPE,
          #                   stdin=subprocess.PIPE, shell=True)
        #(output, err) = p.communicate()
        #match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        #if match is not None:
            #return match.group(1)

        launchableActivity=".view.WelcomeActivityAlias"

        return  launchableActivity

    def getApkName(self):
        cmd = "aapt dump badging " + self.apkPath + " | grep application-label: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            # print(output)
            result = output.split()[0].decode()[19:-1]
        return result

    def getPhoneInfo(devices):
        '''获取设备的一些基本信息'''
        cmd = "adb -s " + devices + " shell cat /system/build.prop "
        phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).stdout.readlines()
        release = "ro.build.version.release="  # 版本
        model = "ro.product.model="  # 型号
        brand = "ro.product.brand="  # 品牌
        device = "ro.product.device="  # 设备名
        result = {"release": release, "model": model, "brand": brand, "device": device}
        for line in phone_info:
            for i in line.split():
                temp = i.decode()
                if temp.find(release) >= 0:
                    result["release"] = temp[len(release):]
                    break
                if temp.find(model) >= 0:
                    result["model"] = temp[len(model):]
                    break
                if temp.find(brand) >= 0:
                    result["brand"] = temp[len(brand):]
                    break
                if temp.find(device) >= 0:
                    result["device"] = temp[len(device):]
                    break
        #LOG.info(result)
        return result

    #获取连接设备

    @classmethod
    def attached_devices(cls):
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.readlines()

        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        return devices

if __name__=="__main__":
    gai = ApkInfo('/Users/xueqiu/PycharmProjects/uiPractice/img/xueqiu.apk')
    print(gai.getApkBaseInfo())
    print(gai.getApkActivity())
    print(gai.attached_devices())





