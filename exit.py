import datetime
from selenium import webdriver
import time



class student_exit:
    def __init__(self):
        self.login_url = "http://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2Fxg.hit.edu.cn%2Fzhxy-xgzs%2Fcommon%2FcasLogin%3Fparams%3DL3hnX21vYmlsZS94c0hvbWU%3D" #hit登陆url
        self.exit_url = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsCxsq" #出校申请的url
        self.home_url = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsHome" #首页url
        self.registration_url = "http://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/yqxx"  # 上报的url
        self.date = "2028年12月16日"

        self.id = '' #输入学号
        self.sc = '' #输入密码
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }

    def request_url(self, url1, url2, url3, id, sc, date):   # 通过request_url来获取上报界面
        driver_path = r"" # 本地的chromedriver绝对路径
        options = webdriver.ChromeOptions()
        # ## 下面两行能让chrome在不弹出的情况下使用
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        ## 给seleniuim添加headers
        options.add_argument('User-Agent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"')

        driver = webdriver.Chrome(executable_path=driver_path,options=options)
        driver.get(url1) #登陆
        driver.find_element_by_id("username").send_keys(id) #填写学号
        driver.find_element_by_id("password").send_keys(sc) #填写密码
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.get(url2)
        driver.get(url3)
        driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsCxsq/editCxsq?id=&zt=')
        time.sleep(1) #调整等待时间 如果运行失败可以适当增大
        driver.find_element_by_xpath("//input[@id='cxlx01']/../..").click()

        driver.find_element_by_id("cxly").send_keys('吃饭')

        js = 'document.getElementById("rq").removeAttribute("readonly")';
        driver.execute_script(js)
        driver.find_element_by_xpath("//input[@id='rq']").send_keys(date)
        driver.find_element_by_xpath("//input[@id='checkbox1']").click()
        driver.find_element_by_xpath("//input[@id='checkbox2']").click()
        driver.find_element_by_xpath("//input[@id='checkbox3']").click()
        driver.find_element_by_xpath("//input[@id='checkbox4']").click()
        driver.find_element_by_xpath("//input[@id='checkbox5']").click()
        driver.find_element_by_xpath("//input[@id='checkbox6']").click()
        driver.find_element_by_xpath("//input[@id='checkbox8']").click()
        driver.find_element_by_xpath("//input[@id='checkbox9']").click()
        driver.find_element_by_class_name('right_btn').click()
        time.sleep(2) #调整等待时间 如果运行失败可以适当增大
        driver.find_element_by_xpath('//a[@class="weui-dialog__btn primary"]').click()

    def run(self):
        begin = datetime.date(2020, 1, 3) #输入起始日期
        end = datetime.date(2021, 1, 10) #输入终止日期
        d = begin
        delta = datetime.timedelta(days=1)
        while d <= end:
            self.date = d.strftime("%Y" + "年" + "%m" + "月" + "%d" + "日")
            reg = self.request_url(self.login_url, self.home_url, self.exit_url, self.id, self.sc, self.date)
            print(d.strftime("%Y" + "年" + "%m" + "月" + "%d" + "日" + "申请成功"))
            d += delta

if __name__ == '__main__':
    CS=student_exit()
    CS.run()
