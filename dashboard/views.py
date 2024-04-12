from django.shortcuts import get_object_or_404, render

from .models import HealthRecord

def health_record_detail(request, pk):
    health_record = get_object_or_404(HealthRecord, pk=pk)
    return render(request, 'dashboard/health_record_detail.html', {'health_record': health_record})