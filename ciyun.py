import jieba
from scipy.misc import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt

seg_list = "苹果是美国一家高科技公司由史蒂夫·乔布斯、斯蒂夫·沃兹尼亚克和罗·韦恩等人于1976年4月1日创立并命名为美国苹果电脑公司2007年1月9日更名为苹果公司总部位于加利福尼亚州的库比蒂诺\
苹果公司1980年12月12日公开招股上市美元的市值记录苹果公司已经连续三年成为全球市值最大公司苹果公司在2016年世界500强排行榜中排名第9名在宏盟集团的全球最佳品牌报告中苹果公司超过可口可乐成为世界最有价值品牌苹果品牌超越谷歌成为世界最具价值品牌\
财富世界500强排行苹果公司名列第九名苹果秋季新品发布会在美国旧金山的比尔格雷厄姆市政礼堂举行10月苹果公司成为2016年全球100大最有价值品牌第一名整红色星期五促销活动在苹果官网正式上线瞬间大量用户涌入官网进行抢购仅两分钟所有参与活动的耳机便被抢光发布2017年度全球500强品牌榜单，苹果公司排名第二6月7日《财富》美国500强排行榜发布，苹果公司排名第3位年世界500强排名第9位\
晚间苹果盘中市值首次超过1万亿美元股价刷新历史最高位至美元当前涨幅超过"
def draw_wordcloud():
    cut_text = " ".join(jieba.cut(seg_list))
    color_mask = imread(r"C:\Users\Liu\Desktop\timg.jpg") # 读取背景图片
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path=r"C:\Windows\Fonts\simhei.ttf",
        # 设置背景色
        background_color='black',
        # 词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=80
    )
    word_cloud = cloud.generate(cut_text) # 产生词云
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()

if __name__  ==  '__main__':
    draw_wordcloud()