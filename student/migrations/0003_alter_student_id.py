from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
