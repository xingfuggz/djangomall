# Generated by Django 3.2.7 on 2021-10-10 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DmallAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, help_text='删除标记', verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, help_text='是否显示', verbose_name='是否显示')),
                ('province', models.CharField(default='', max_length=100, verbose_name='省份')),
                ('city', models.CharField(default='', max_length=100, verbose_name='城市')),
                ('district', models.CharField(default='', max_length=100, verbose_name='区域')),
                ('address', models.CharField(default='', max_length=100, verbose_name='详细地址')),
                ('signer_name', models.CharField(default='', max_length=100, verbose_name='签收人')),
                ('signer_mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=30, verbose_name='电子邮箱')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否设为默认收货地址')),
                ('owner', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
                'db_table': 'd_user_address',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, help_text='删除标记', verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, help_text='是否显示', verbose_name='是否显示')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(blank=True, default='', max_length=23, verbose_name='昵称')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m', verbose_name='用户头像')),
                ('signature', models.CharField(blank=True, default='', max_length=100, verbose_name='个性签名')),
                ('default_address', models.ForeignKey(blank=True, help_text='默认地址', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.dmalladdress', verbose_name='默认地址')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'd_user_info',
            },
        ),
        migrations.CreateModel(
            name='DmallRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, help_text='删除标记', verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, help_text='是否显示', verbose_name='是否显示')),
                ('score', models.SmallIntegerField(choices=[(0, '0分'), (1, '1分'), (2, '2分'), (3, '3分'), (4, '4分'), (5, '5分')], default=5, verbose_name='满意度评分')),
                ('disabled', models.BooleanField(default=True, verbose_name='是否允许打分')),
                ('owner', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评分',
                'verbose_name_plural': '评分',
                'db_table': 'd_rate',
            },
        ),
        migrations.CreateModel(
            name='DmallHotSearchWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, help_text='删除标记', verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, help_text='是否显示', verbose_name='是否显示')),
                ('keywords', models.CharField(help_text='热搜词', max_length=20, verbose_name='热搜词')),
                ('sort', models.PositiveSmallIntegerField(default=0, help_text='排序', verbose_name='排序')),
                ('owner', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
                'db_table': 'd_hot_words',
            },
        ),
        migrations.CreateModel(
            name='DmallFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, help_text='删除标记', verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, help_text='是否显示', verbose_name='是否显示')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('owner', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
                'db_table': 'd_fav',
                'unique_together': {('owner', 'content_type', 'object_id')},
            },
        ),
    ]
