from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
