from django.shortcuts import render
from django.http import Http404

# Create your views here.
def home(request):
    context = {
        'title' : 'Home',
        'features' : ['DJango', 'Templates', 'Static Files'],
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title' : 'About'})

def announcements(request):
    return render(request, 'announcements.html', {'title' : 'Announcements'})

ANNOUNCEMENTS = {
    "docs": {
        "title": "📚 New Documentation",
        "content": "Updated user guide and developer API docs are now available, providing everything you need to get started and master our platform. The new documentation includes detailed setup instructions, configuration guides, and real-world usage examples to help both beginners and advanced users. We’ve added advanced tutorials that walk through complex workflows step by step, as well as troubleshooting tips to quickly resolve common issues. For developers, the API section now features expanded endpoints, sample requests, and integration guidelines with third-party services. Best practices for deploying in production environments, optimizing performance, and maintaining security are also included. A powerful search function makes finding information faster, and a brand-new FAQ section addresses the most common questions from our community. With this update, learning and building with our platform has never been easier.",
        "date": "Sept 18, 2025",
    },
    "event": {
        "title": "🎉 Special Event",
        "content": "Join our virtual anniversary celebration this October 1st! This milestone marks an incredible journey of growth, innovation, and community support, and we want to celebrate it with you. The event will feature inspiring keynote sessions from our founders and guest speakers, interactive Q&A panels, and exciting product demonstrations showcasing upcoming features. Attendees will have the chance to participate in live polls, community games, and trivia contests with exclusive prizes and giveaways. We’re also hosting a special ‘User Spotlight’ segment to highlight stories and projects from our amazing community. To wrap things up, we’ll unveil our roadmap for the upcoming year, including highly requested features such as dark mode, performance improvements, and new integration options. Don’t miss this opportunity to learn, connect, and celebrate with us—it’s going to be an unforgettable event!",
        "date": "Sept 15, 2025",
    },
}

def details(request, slug):
    announcement = ANNOUNCEMENTS.get(slug)
    if not announcement:
        raise Http404("Announcement not found")
    return render(request, "announcement_detail.html", {"announcement": announcement})

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)