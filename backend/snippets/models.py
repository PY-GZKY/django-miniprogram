from django.core.cache import cache
from django.db import models
from django.utils.html import format_html
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)
        verbose_name = 'Snippet'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class Entitie(models.Model):
    id = models.IntegerField(primary_key=True)
    header = models.CharField(max_length=100, blank=True, default='')
    original_header = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    original_description = models.CharField(max_length=100, blank=True, default='')
    video = models.CharField(max_length=100, blank=True, default='')
    image = models.CharField(max_length=100, blank=True, default='')
    duration_raw = models.IntegerField()
    duration = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name = 'Entitie'
        verbose_name_plural = verbose_name


# 书籍信息模型
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')  # 图书名称
    bpub_date = models.DateField(verbose_name='发布日期')  # 发布日期
    bread = models.IntegerField(default=0, verbose_name='阅读量')  # 阅读量
    bcomment = models.IntegerField(default=0, verbose_name='评论量')  # 评论量
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除')  # 逻辑删除
    logo = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    def __str__(self):
        return self.btitle

    # 元类信息 : 修改表名
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name



class Site(models.Model):
    """
    站点基本配置信息
    """
    site_name = models.CharField(max_length=32, verbose_name='站点名称', default="CharmCode")
    site_year = models.CharField(max_length=16, verbose_name='年份', default="2020")

    site_title = models.CharField(max_length=64, verbose_name='站点标题', default="Just For Fun")
    type_chinese = models.CharField(max_length=64, verbose_name='中文座右铭', default="向着未来而生")
    type_english = models.CharField(max_length=64, verbose_name='英文左座右铭', default="Being toward future")
    home_title = models.CharField(max_length=64, verbose_name='主页站点', default="CharmCode.cn")

    my_mail = models.CharField(max_length=64, verbose_name='我的邮箱地址', default="wg_python@163.com")

    site_keywords = models.CharField(max_length=128, verbose_name='站点描述(meta显示)',
                                     default="charmcode.com,代码的魅力,web前端,Python后端,小程序,安卓逆向,Python爬虫,渗透测试")
    site_desc = models.CharField(max_length=128, verbose_name='站点描述(meta显示)',
                                 default="领略代码的魅力,分享web前端,html5,css3,Python后端代码分享,了解认知前沿技术")
    domain_url = models.CharField(max_length=128, verbose_name='站点地址', default="https://www.charmcode.cn")
    site_avatar = models.CharField(max_length=128, verbose_name='站点地址',
                                   default="https://image.3001.net/images/20200504/1588558613_5eaf7b159c8e9.jpeg")

    about_name = models.CharField(max_length=32, verbose_name='about名称', default="王小右")
    about_desc = models.CharField(max_length=128, verbose_name='about简介', default="兴趣使然的编程爱好者")

    def avatar_data(self):
        return format_html(
            '<img src="{}" width="156px" height="98px"/>',
            self.site_avatar,
        )

    avatar_data.short_description = 'about头像'

    @staticmethod
    def fetch_all_site_info():
        # 获取站点信息
        site_info = cache.get(f"site_info")
        if not site_info:
            # 查询最后一条站点信息
            site_info = Site.objects.last()
            # 保存站点信息存到缓存redis中 缓存60*2
            if site_info:
                # 如果查询到了站点信息就缓存
                cache.set("site_info", site_info, 120)
        return site_info

    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.home_title
