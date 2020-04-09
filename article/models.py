from django.db import models

# Create your models here.
# 导入内建的user的模型
from django.contrib.auth.models import User
#timezone用于处理时间相关事务
from django.utils import timezone

# 博客文章的数据模型
class ArticlePost(models.Model):
	#文章作者。 参on_delete 用于指定数据删除方式
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	#文章标题。
	title = models.CharField(max_length=100)

	#文章正文
	body = models.TextField()

	#文章创建时间
	created = models.DateTimeField(default=timezone.now)

	#文章更新时间
	updated = models.DateTimeField(auto_now=True)

	#内部类class meta 用于给model定义元数据
	class Meta:
		#ordering 指定模型返回的数据的排列顺序
		# '-created'表明数据以倒序排列
		ordering = ('-created',)

	# 函数__str__定义当调用对象的str()方法时的返回值内容
	def __str__(self):
		#将文章的标题返回
		return self.title


