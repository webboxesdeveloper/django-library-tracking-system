from django.db import connection
from library.models import Member
from django.db.models import Count, Q

connection.queries.clear()

top_members = Member.objects.annotate(
    active_loans_count=Count('loans', filter=Q(loans__is_returned=False))
).order_by('-active_loans_count')[:5]

print(f"Queries: {len(connection.queries)}") # should be 1