from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(
        username='superadmin',
        email='admin@example.com',
        password='123dev0987zxc'  # Замініть на реальний пароль
    )

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_auto_20201001_2315'),  # Залежність від останньої міграції auth
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
