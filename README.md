# recruitment
项目实训，招聘网站数据爬取
1. 本项目主要爬取58同城，智联招聘数据网站
2. 主要爬取数据包括下面内容  <br>
   1. 公司名称
   2. 职位名称
   3. 招聘人数
   4. 职位月薪
   5. 公司地点
   6. 学历要求
   7. 经验要求
   8. 职位描述
   9. 职位类别
   10. 信息来源 <br>
3. 数据爬取完成后放到本项目目录下的excel表格中。
4. 同时封装了mongdb连接代码，可以直接将数据连接到mongodb数据库中。
5. 通过一定的措施进行了防止ip被禁止的数据[庆文驿站—【python】scrapy 爬虫 防止ip被禁措施 总结](http://118.89.138.205/wordpress/index.php/2017/07/12/deal-scrapy-ip-ban/)
6. 后期可以进行分布式爬取。
