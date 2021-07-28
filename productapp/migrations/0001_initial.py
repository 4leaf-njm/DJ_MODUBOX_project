# Generated by Django 3.2.5 on 2021-07-28 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('title', models.CharField(max_length=200, verbose_name='상품 타이틀')),
                ('type', models.CharField(choices=[('맞춤박스', '맞춤박스'), ('쇼핑백', '쇼핑백'), ('행택', '행택')], max_length=100, verbose_name='상품 유형')),
                ('content', models.TextField(verbose_name='상품 내용')),
                ('spec', models.TextField(blank=True, null=True, verbose_name='제작 사양')),
                ('sort', models.IntegerField(help_text='정렬 순서는 3자리 까지 입력 가능합니다.', max_length=3, verbose_name='정렬 순서')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='product/', verbose_name='상품 이미지')),
                ('sort', models.IntegerField(help_text='정렬 순서는 3자리 까지 입력 가능합니다.', max_length=3, verbose_name='정렬 순서')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='productapp.product')),
            ],
        ),
    ]
