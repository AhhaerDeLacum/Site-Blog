from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "222.jpg",
        "author": "Vladislav",
        "date": date(2022, 10, 28),
        "title": "Mountain Hiking",
        "excerpt": """There`s nothing like the views you get when hiking in the mountains! And I wasn`t even prepared 
        for what happened whilst I was enjoying the view!""",
        "content": """
            1yhujikoiuhgushutghushgushutghaughuthguhhgsjgnsthghgsuhtgsuhgushtghsuthgsutgushughsghtuhg
            gushtsuighsuitghsliughsiutghsiutghsuighsiuthgsuhg
            
            2yhujikoiuhgushutghushgushutghaughuthguhhgsjgnsthghgsuhtgsuhgushtghsuthgsutgushughsghtuhg
            gushtsuighsuitghsliughsiutghsiutghsuighsiuthgsuhg
            
            3yhujikoiuhgushutghushgushutghaughuthguhhgsjgnsthghgsuhtgsuhgushtghsuthgsutgushughsghtuhg
            gushtsuighsuitghsliughsiutghsiutghsuighsiuthgsuhg
            
                   """,

    },
    {
        "slug": "Python",
        "image": "4.png",
        "author": "Vladislav",
        "date": date(2022, 10, 27),
        "title": "Programing On Python",
        "excerpt": """Love Python""",
        "content": """
            1214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654

            2214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654

            3214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654

                   """,

    },
    {
        "slug": "into-the-woods",
        "image": "3.jpg",
        "author": "Vladislav",
        "date": date(2022, 10, 26),
        "title": "Nature At Its Best",
        "excerpt": """Love Nature""",
        "content": """
            1214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654

            2214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654

            3214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654214142124214141414145678987654

                   """,

    }
]


def get_date(post):
    return post.get('date') # or return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post
    })