from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    context = {
        'name': 'Zahran Musyaffa Ramadhan Mulya',
        'npm': '2406365401',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)

def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, news_id):
    data = News.objects.filter(pk=news_id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    try:
        news_items = News.objects.filter(pk=news_id)
        xml_data = serializers.serialize("xml", news_items)
        return HttpResponse(xml_data, content_type="application/xml")
    except News.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, news_id):
    data = News.objects.filter(pk=news_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    try:
        news_items = News.objects.filter(pk=news_id)
        json_data = serializers.serialize("json", news_items)
        return HttpResponse(json_data, content_type="application/json")
    except News.DoesNotExist:
        return HttpResponse(status=404)