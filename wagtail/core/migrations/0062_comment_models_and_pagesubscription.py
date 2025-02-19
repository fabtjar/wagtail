# Generated by Django 3.0.3 on 2021-04-19 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


COMMENTS_RELATION_NAME = getattr(settings, 'WAGTAIL_COMMENTS_RELATION_NAME', 'wagtail_admin_comments')


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0061_change_promote_tab_helpt_text_and_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('contentpath', models.TextField()),
                ('position', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name=COMMENTS_RELATION_NAME, to='wagtailcore.Page')),
                ('resolved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_resolved', to=settings.AUTH_USER_MODEL)),
                ('revision_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_comments', to='wagtailcore.PageRevision')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name=COMMENTS_RELATION_NAME, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='wagtailcore.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment reply',
                'verbose_name_plural': 'comment replies',
            },
        ),
        migrations.CreateModel(
            name='PageSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_notifications', models.BooleanField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='wagtailcore.Page')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('page', 'user')},
            },
        ),
    ]
