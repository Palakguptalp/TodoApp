
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_added_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
