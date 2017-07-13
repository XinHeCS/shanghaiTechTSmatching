import requests
from lxml import html

class TeacherInformationSpider:
    def __init__(self):
        self.teacher_info = [];


    def spider(self):
        self.url = "http://sist.shanghaitech.edu.cn/cn/Staff.asp?mid=22"
        r = requests.get(self.url)
        r.encoding = 'utf-8'
        tree = html.fromstring(r.text)
        for i in range(2, 37):
            teacher_info_single = {}
            base_xpath = '//*[@id="lim"]/div/div[1]/div[2]/div[2]/div[' + str(i) +']'
            print(base_xpath)
            teacher_info_single['name'] =  tree.xpath(base_xpath+'/div[1]/a/text()')
            teacher_info_single['tel'] = tree.xpath(base_xpath+'/div[2]/span/text()[2]')
            if i == 2 or i == 33:
                teacher_info_single['email'] = tree.xpath(base_xpath + '/div[2]/span/text()[3]')
            #elif i == 34:
            #    teacher_info_single['email'] = tree.xpath(base_xpath + '/div[2]/span/text()[2]')
            else:
                teacher_info_single['email'] = tree.xpath(base_xpath + '/div[2]/span/text()[4]')

            teacher_info_single['address'] = tree.xpath(base_xpath+'/div[2]/span/text()[6]')
            if i == 8:
                teacher_info_single['area'] = '下一代无线通信的关键理论和技术：异质网络、干扰协调、大规模MIMO、定位技术 等图上信号处理：大规模不规则网络（社交网络，无线传感网络等）中的信息分析与处理'

            if i >= 15 and i <= 16:
                teacher_info_single['area'] = ''.join(
                    tree.xpath(base_xpath + '/div[2]/span/ul/li[1]/span//text()')
                    + tree.xpath(base_xpath + '/div[2]/span/ul/li[2]/span/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/ul/li[3]/span/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/ul/li[4]/span/text()'))
            elif i == 14:
                teacher_info_single['area'] = ''.join(
                    tree.xpath(base_xpath + '/div[2]/span/div/ul/li[1]/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/div/ul/li[2]/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/div/ul/li[3]/text()'))
            else:
                teacher_info_single['area'] = ''.join(tree.xpath(base_xpath+'/div[2]/span/ul/li[1]/text()[1]')+tree.xpath(base_xpath
                +'/div[2]/span/ul/li[2]/text()[1]')+tree.xpath(base_xpath+'/div[2]/span/ul/li[3]/text()[1]')+tree.xpath(
                base_xpath+'/div[2]/span/ul/li[4]/text()'))


            self.teacher_info.append(teacher_info_single)
    def print_test(self):
        i = 2
        for each_teacher in self.teacher_info:
            print(i)
            i = i +1
            print(each_teacher)

    def save


spider = TeacherInformationSpider()
spider.spider()
spider.print_test()




