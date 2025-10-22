import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from library.tasks import check_overdue_loans

result = check_overdue_loans()
print(result.get())