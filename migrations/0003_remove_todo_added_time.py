 
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20191027_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='added_time',
        ),
    ]
