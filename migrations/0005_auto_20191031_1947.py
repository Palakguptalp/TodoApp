
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20191031_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.CharField(max_length=50),
        ),
    ]
