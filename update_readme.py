import feedparser, time
from datetime import datetime, timedelta

URL = "http://dmomo.co.kr/rss"
URL2 = "https://blog.ai.dmomo.co.kr/feed"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5
RSS_FEED2 = feedparser.parse(URL2)

markdown_text = """
# 💻 Damho Lee

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdamho1104&count_bg=%233D9CC8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)  

[![LinkedIn](https://img.shields.io/badge/Linkedin-%230077B5.svg?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/damho1104/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:damho1104@gmail.com)
[![Instagram](https://img.shields.io/badge/Instargram-%23E4405F.svg?style=flat&logo=Instagram&logoColor=white)](https://www.instagram.com/damho1104/)
[![Blog](https://img.shields.io/badge/Blog-%23000000.svg?style=flat&logo=Tistory&logoColor=white)](https://dmomo.co.kr/)
[![Blog](https://img.shields.io/badge/Blog-%23000000.svg?style=flat&logo=WordPress&logoColor=white)](https://blog.ai.dmomo.co.kr/)

## 📃 My Jobs
- Static Analysis Developer
- Web Backend Developer
- Web Infra DevOps Developer

## 📰 CV
- [Click](https://resume.dmomo.net/damho.lee/resume)  

## 📘 Resume
- [Click](https://damho1104.notion.site/8af3191b9815406d95708d9a0cea5a9e)  

## 🌐 Blog
- [IT Blog](https://dmomo.co.kr/)
- [AI Blog](https://blog.ai.dmomo.co.kr/)

## 💪 Technical Skills
### Languages & Frameworks
![C](https://img.shields.io/badge/c-%2300599C.svg?style=flat&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=flat&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?&style=flat&logo=Python&logoColor=white)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=openjdk&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-%237F52FF.svg?style=flat&logo=Kotlin&logoColor=white)
![Shell Script](https://img.shields.io/badge/Shell_script-%23121011.svg?style=flat&logo=gnu-bash&logoColor=white)  
  
![LLVM](https://img.shields.io/badge/LLVM/Clang-000B1D.svg?&style=flat&logo=LLVM&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![Spring](https://img.shields.io/badge/Springboot-%236DB33F.svg?style=flat&logo=spring&logoColor=white)
  
  
### IDE(s)
![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=flat&logo=visual-studio&logoColor=white) 
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJIDEA-000000.svg?style=flat&logo=intellij-idea&logoColor=white) 
![PyCharm](https://img.shields.io/badge/PyCharm-143?style=flat&logo=pycharm&logoColor=black&color=black&labelColor=green) 


### Tools
![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=flat&logo=cmake&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=flat&logo=notion&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=flat&logo=Raspberry-Pi)
![Vagrant](https://img.shields.io/badge/Vagrant-%231563FF.svg?style=flat&logo=vagrant&logoColor=white)


### OS
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white)
![Cent OS](https://img.shields.io/badge/Cent%20OS-002260?style=flat&logo=centos&logoColor=F0F0F0)


## :computer: Stats
![damho1104 Stats](https://github-readme-stats.vercel.app/api?username=damho1104&hide=issues&show_icons=true&theme=dark)  
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=damho1104&layout=compact&theme=dark)


## My Infra
![infra](https://nextcloud.dmomo.net/apps/files_sharing/publicpreview/EtWDB9RaEXyf4FT?file=/&fileId=142416&x=6016&y=3384&a=true&etag=eee0bc0c4308201c786211582fdbc678)  


"""
# ## My Infra
# <div align="center">
#     <p>
#     <img src="imgs/infra.png" alt="infra" style="width: 1200px; height: 300px;">
#     </p>
# </div>
markdown_text += """


## 📣 My Service
- [로또 번호 추천 및 당첨 알림 서비스](https://lotto.dmomo.co.kr/)  


## ✅ Latest Blog Post

"""  # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        # feed_date = feed['published_parsed']
        feed_date = datetime.fromtimestamp(time.mktime(feed['published_parsed'])) + timedelta(hours=9)
        markdown_text += f"[{feed_date.strftime('%Y/%m/%d')} - {feed['title']}]({feed['link']}) <br/>\n"

markdown_text += """
## ✅ Latest AI Blog Post
"""
# list of blog posts will be appended here
for idx, feed in enumerate(RSS_FEED2['entries']):
    if idx > MAX_POST:
        break
    else:
        # feed_date = feed['published_parsed']
        feed_date = datetime.fromtimestamp(time.mktime(feed['published_parsed'])) + timedelta(hours=9)
        markdown_text += f"[{feed_date.strftime('%Y/%m/%d')} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
