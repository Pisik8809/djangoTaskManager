from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(
        username='superadmin',
        email='admin@example.com',
        password='123dev0987zxc'  # ������ �� �������� ������
    )

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_auto_20201001_2315'),  # ��������� �� �������� ������� auth
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
