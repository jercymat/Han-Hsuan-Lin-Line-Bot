# -*- coding: utf-8 -*-
from linebot.models import *


class Me(object):
    """ instance of me """

    def __init__(self):
        print("Me instance created")

    def map_keywords(self, keyword):
        try:
            return self.keywords[keyword](self)
        except KeyError:
            return 'keyword not mapped'


    def render_ques_sheet(self, direct_call=False):
        titles = ['你也可以從這裡問我一些問題！', '從這裡問我一些問題！']
        title = titles[0] if direct_call else titles[1]

        ques_sheet = TemplateSendMessage(
            alt_text='指令選單',
            template=ButtonsTemplate(
                # thumbnail_image_url='https://example.com/image.jpg',
                title=title,
                text='在下方點選問題',
                actions=[
                    MessageAction(
                        label='問個好吧！',
                        text='你好'
                    ),
                    MessageAction(
                        label='可以自我介紹嗎？',
                        text='自我介紹'
                    ),
                    MessageAction(
                        label='你的學歷是？',
                        text='學歷'
                    ),
                    MessageAction(
                        label='你的網站連結或作品集？',
                        text='網站連結'
                    )
                ]
            )
        )

        return ques_sheet


    def render_url_sheet(self, direct_call=False):

        url_sheet = TemplateSendMessage(
            alt_text='指令選單',
            template=ButtonsTemplate(
                title='這裡是我的一些網站連結！',
                text='在下方點選網站',
                actions=[
                    URIAction(
                        label="Gitlab",
                        uri="https://gitlab.com/jercymat"
                    ),
                    URIAction(
                        label="Github",
                        uri="https://github.com/jercymat"
                    ),
                    URIAction(
                        label="Linkedin",
                        uri="https://www.linkedin.com/in/han-hsuan-lin-8ab9aa158/"
                    ),
                    URIAction(
                        label="作品集",
                        uri="https://drive.google.com/open?id=0B_io3mJinw4LYzY0NWlld2tlVk0"
                    )
                ]
            )
        )

        return url_sheet


    def greeting(self, direct_call=False):
        text = '你好！我是林瀚軒，很高興認識你，儘管問我問題！'
        return text


    def about_me(self, direct_call=False):
        text = '我是來自政治大學資訊科學系的林瀚軒。擁有三年的程式設計經歷，熟悉 C, C++, Python，也熟稔前端開發，同時也專注於平面、UI/UX設計，我相信深厚的程式基礎，加上美學的知識，能夠創造出更多的可能。時時刻刻精進，成就更完美的自己。'
        return text


    def education(self, direct_call=False):
        text = '我來自國立政治大學資訊科學系，目前就讀三年級。'
        return text


    def experience(self, direct_call=False):
        bubble1 = BubbleContainer(
            body=BoxComponent(
                layout="vertical",
                spacing="lg",
                contents=[
                    TextComponent(text='EXPERIENCE', size='sm', weight='bold', color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            TextComponent(text='行動計算與\n網路通訊實驗室,\n政大資科', size='xl', weight='bold', wrap=True),
                            TextComponent(text='Jan. 2019 - 現在', size='lg', color='#888888', weight='bold')
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            TextComponent(text='專題實習生', size='lg', weight='bold'),
                            TextComponent(text='研究領域：', color='#888888')
                            ]
                        ),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(
                                        url="https://i.imgur.com/Vwyw5sI.png"
                                        ),
                                    TextComponent(text='軟體定義網路(SDN)', weight='bold')
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(
                                        url="https://i.imgur.com/Vwyw5sI.png"
                                        ),
                                    TextComponent(text='3GPP 行動通訊網路協定', weight='bold')
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(
                                        url="https://i.imgur.com/Vwyw5sI.png"
                                        ),
                                    TextComponent(text='5G 網路', weight='bold')
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            footer=BoxComponent(
                layout="vertical",
                contents=[
                    ButtonComponent(
                        style="primary",
                        color="#13ab67",
                        action=URIAction(
                            label="實驗室網站",
                            uri="https://www.cs.nccu.edu.tw/~jang/research.html"
                            )
                        )
                    ]
                )
            )

        bubble2 = BubbleContainer(
            body=BoxComponent(
                layout="vertical",
                spacing="lg",
                contents=[
                    TextComponent(text='EXPERIENCE', size='sm', weight='bold', color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            TextComponent(text='政大傳播學院\n整合實驗中心\n數位平台', size='xl', weight='bold', wrap=True),
                            TextComponent(text='Oct. 2017 - 現在', size='lg', color='#888888', weight='bold')
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            TextComponent(text='實習助理', size='lg', weight='bold')
                            ]
                        ),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(
                                        url="https://i.imgur.com/Vwyw5sI.png"
                                        ),
                                    TextComponent(text='數位創作與平面設計實習機構', weight='bold')
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(
                                        url="https://i.imgur.com/Vwyw5sI.png"
                                        ),
                                    TextComponent(text='每年舉辦各式小展與年度大展', weight='bold')
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(
                                        url="https://i.imgur.com/Vwyw5sI.png"
                                        ),
                                    TextComponent(text='2018年度大展《晚安，晚安》\n策展團隊', weight='bold', wrap=True)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            footer=BoxComponent(
                layout="vertical",
                contents=[
                    ButtonComponent(
                        style="primary",
                        color="#13ab67",
                        action=URIAction(
                            label="數位平台網站",
                            uri="http://www.itlab.nccu.edu.tw"
                            )
                        )
                    ]
                )
            )

        carousel = CarouselContainer(
            contents=[bubble1, bubble2]
            )
        return FlexSendMessage(alt_text="Experience 經歷", contents=carousel)


    def research(self, direct_call=False):
        bubble1 = BubbleContainer(
            body=BoxComponent(
                layout="vertical",
                spacing="lg",
                contents=[
                    TextComponent(text='RESEARCH', size='sm', weight='bold', color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        spacing="xs",
                        contents=[
                            TextComponent(text='An efficient solution for 4G to 5G transition period by SDN-based switch', weight='bold', size='lg', wrap=True),
                            TextComponent(text='計畫執行中', size='md', color='#888888')
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        contents=[
                            TextComponent(text='大學部專題研究計畫', size='lg', weight='bold')
                            ]
                        ),
                    BoxComponent(
                        layout="vertical",
                        spacing="sm",
                        contents=[
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(url="https://i.imgur.com/Vwyw5sI.png"),
                                    TextComponent(text='開發一個 SDN 交換器使 LTE 基站得以異質網路形式接入 5G 核心網路', weight='bold', wrap=True)
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(url="https://i.imgur.com/Vwyw5sI.png"),
                                    TextComponent(text='設計將 LTE 基站 request 分析並轉譯成 5G 核心網路格式之演算法', weight='bold', wrap=True)
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(url="https://i.imgur.com/Vwyw5sI.png"),
                                    TextComponent(text='預期在 4/5G 過渡期能為 4G 網路帶來顯著效率提升', weight='bold', wrap=True)
                                    ]
                                ),
                            BoxComponent(
                                layout="baseline",
                                contents=[
                                    IconComponent(url="https://i.imgur.com/Vwyw5sI.png"),
                                    TextComponent(text='申請科技部大專生專題研究補助計畫中', weight='bold', wrap=True)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
            footer=BoxComponent(
                layout="vertical",
                contents=[
                    ButtonComponent(
                        style="primary",
                        color="#13ab67",
                        action=URIAction(
                            label="研究計畫書",
                            uri="https://drive.google.com/open?id=1bo4-PXpVKTx7KzRTcjsttCrPJ5oCzfBb"
                            )
                        )
                    ]
                )
            )

        carousel = CarouselContainer(
            contents=[bubble1]
            )
        return FlexSendMessage(alt_text="Research 研究", contents=carousel)


    def skills(self, direct_call=False):
        bubble1 = BubbleContainer(
            body=BoxComponent(
                layout="vertical",
                spacing="md",
                contents=[
                    TextComponent(text='SKILLS', size='sm', weight='bold', color='#13ab67', align='center'),
                    BoxComponent(
                        layout="vertical",
                        spacing="xs",
                        contents=[
                            TextComponent(text='Programming', size='xxl', weight='bold', align="center"),
                            TextComponent(text='程式設計', size='lg', color='#888888', align="center")
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        spacing="md",
                        contents=[
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(text='C', size='xxl', weight='bold', align="center"),
                                    SeparatorComponent(color='#aaaaaa'),
                                    TextComponent(text='C++', size='xxl', weight='bold', align="center")
                                    ]
                                )
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        spacing="md",
                        contents=[
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(text='Python', size='xxl', weight='bold', align="center"),
                                    SeparatorComponent(color='#aaaaaa'),
                                    TextComponent(text='Swift', size='xxl', weight='bold', align="center")
                                    ]
                                )
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    TextComponent(text='JavaScript', size='xxl', weight='bold', align="center")
                    ]
                )
            )
        bubble2 = BubbleContainer(
            body=BoxComponent(
                layout="vertical",
                spacing="md",
                contents=[
                    TextComponent(text='SKILLS', size='sm', weight='bold', color='#13ab67', align='center'),
                    BoxComponent(
                        layout="vertical",
                        spacing="xs",
                        contents=[
                            TextComponent(text='UI/UX/Web', size='xxl', weight='bold', align="center"),
                            TextComponent(text='介面／網頁設計', size='lg', color='#888888', align="center")
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    BoxComponent(
                        layout="vertical",
                        spacing="md",
                        contents=[
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(text='Sketch', size='xxl', weight='bold', align="center"),
                                    SeparatorComponent(color='#aaaaaa'),
                                    TextComponent(text='Jquery', size='xxl', weight='bold', align="center")
                                    ]
                                )
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    TextComponent(text='Django', size='xxl', weight='bold', align="center"),
                    SeparatorComponent(color='#13ab67'),
                    TextComponent(text='BootStrap', size='xxl', weight='bold', align="center")
                    ]
                )
            )
        bubble3 = BubbleContainer(
            body=BoxComponent(
                layout="vertical",
                spacing="md",
                contents=[
                    TextComponent(text='SKILLS', size='sm', weight='bold', color='#13ab67', align='center'),
                    BoxComponent(
                        layout="vertical",
                        spacing="xs",
                        contents=[
                            TextComponent(text='Design', size='xxl', weight='bold', align="center"),
                            TextComponent(text='平面設計', size='lg', color='#888888', align="center")
                            ]
                        ),
                    SeparatorComponent(color='#13ab67'),
                    TextComponent(text='Illustrator', size='xxl', weight='bold', align="center"),
                    SeparatorComponent(color='#13ab67'),
                    TextComponent(text='Photoshop', size='xxl', weight='bold', align="center"),
                    SeparatorComponent(color='#13ab67'),
                    TextComponent(text='Lightroom', size='xxl', weight='bold', align="center")
                    ]
                )
            )

        carousel = CarouselContainer(
            contents=[bubble1, bubble2, bubble3]
            )
        return FlexSendMessage(alt_text="Skills 技術", contents=carousel)

    keywords = {'關於我': about_me,
                '自我介紹': about_me,
                '經歷': experience,
                '研究': research,
                '技巧': skills,
                '問問題': render_ques_sheet,
                '網站連結': render_url_sheet,
                '你好':greeting,
                '學歷': education}